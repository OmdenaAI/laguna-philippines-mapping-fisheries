import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")

st.sidebar.title("Contact")
st.sidebar.info(
    '''
    This project is owned by:\n
    © Omdena Laguna, Philippines\n
    omdena.laguna@gmail.com
    '''
)

st.title("Map of Fishing Activity Recommendation")

with st.expander("How to use this map "):
    st.markdown('''### Instructions:
    1. ''')

m = leafmap.Map(center=[17.879721, 121.774017], zoom=7)
# cities = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities.csv'
cities = "https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/ph_cities_filtered.csv"
regions = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/data/Cities/region_2_results_filtered.geojson'

m.add_geojson(regions, layer_name='Cluster Map', info_mode="on_click")
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