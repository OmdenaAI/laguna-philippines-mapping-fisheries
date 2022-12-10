import streamlit as st
import leafmap.foliumap as leafmap
import json
import requests

st.set_page_config(layout="wide")


st.sidebar.title("About")

st.title("Marker Cluster")


with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[16.879721, 121.774017], zoom=8)
        cities = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities.csv'
        regions = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Results/region_2_results.geojson'

        m.add_geojson(regions, layer_name='Thingy')
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

geojson_url = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Results/region_2_results.geojson'
response = requests.get(geojson_url)
geojson_data = response.json()

geojson_dict = json.loads(geojson_data)


def filter_properties(feature):
  if 'total_area' in feature['properties'] and 'mean_temperature' in feature['properties']:
    return True
  else:
    return False

print(geojson_dict)