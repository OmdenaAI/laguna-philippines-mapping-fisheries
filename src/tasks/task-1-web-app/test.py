import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.sidebar.title("About")

st.title("Marker Cluster")


with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[16.879721, 121.774017], zoom=8)
        cities = r'C:\Users\patrick\Documents\Omdena\Challenges\Laguna Local Chapter\laguna-philippines-mapping-fisheries\src\data\Cities\ph_cities.csv'
        regions = r"C:\Users\patrick\Documents\Omdena\Challenges\Laguna Local Chapter\laguna-philippines-mapping-fisheries\src\data\Results\region_2_results.geojson"

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