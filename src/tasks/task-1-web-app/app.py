import streamlit as st
import leafmap.foliumap as leafmap
import json
import requests
import geopandas as gpd
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("About")

st.title("Marker Cluster")

provinces_url = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Shape%20File/provinces-region2.json'
response = requests.get(provinces_url)
provinces = response.json()

coordinates = []
for feature in provinces["features"]:
    for geometry in feature["geometry"]["coordinates"]:
        for coordinate in geometry:
            coordinates.append(coordinate)
flat_coordinates = [coord for coords in coordinates for coord in coords if type(coord) == list]
# Convert the coordinates into a format that add_points_from_xy() can use
coordinates_df = pd.DataFrame(flat_coordinates, columns=["lng", "lat"])

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[16.879721, 121.774017], zoom=8)
        # cities = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities.csv'
        cities = r"C:\Users\patrick\Documents\Omdena\Challenges\Laguna Local Chapter\laguna-philippines-mapping-fisheries\src\tasks\task-1-web-app\ph_cities_filtered.csv"
        regions = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/tasks/task-1-web-app/region_2_results_filtered.geojson'

        m.add_geojson(regions, layer_name='Cluster Map')
        m.add_points_from_xy(
            cities,
            x="lng",
            y="lat",
            # color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
m.to_streamlit(height=700)