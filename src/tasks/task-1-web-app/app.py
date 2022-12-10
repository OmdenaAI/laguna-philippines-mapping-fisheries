import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[17.879721, 121.774017], zoom=7)
        # cities = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities.csv'
        cities = "https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities_filtered.csv"
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