import streamlit as st
import folium
import streamlit_folium as stf
import geopandas as gdf
import requests
import json

def formatter(geojson, features):
    for i in range(len(geojson['features'])):
        for j in features:
            geojson['features'][i]['properties'][j] = round(float(geojson['features'][i]['properties'][j]))
    return geojson

st.set_page_config(layout="wide")

st.sidebar.title("About")

st.sidebar.title("Contact")
with st.sidebar.expander("How to use this map "):
    st.markdown('''### Instructions:
    1. ''')
st.sidebar.info(
    '''
    This project is owned by:\n
    © Omdena Laguna, Philippines\n
    omdena.laguna@gmail.com
    '''
)

st.title("Map of Fishing Activity Recommendation")


m = folium.Map(location=[17.879721, 121.774017], zoom_start=7)

regions = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/results/region_2_results_with_recommendation.geojson'
response = requests.get(regions)
regions = json.loads(response.content)
features = ['Recommended Production Value (2022) - Forecasted', 'Recommended Production Volume (2022) - Forecasted']

regions = formatter(regions, features)


style_function = lambda feature: {
     "fillColor": "#0000ff"
     if "Increase Fishing Activity" == feature["properties"]['Recommendation']
     else '#0000ff' 
     if "Decrease Fishing Activity" == feature["properties"]['Recommendation']
     else '#0000ff'}

tooltip = folium.features.GeoJsonTooltip(fields=['index','Recommendation',"Recommended Production Value (2022) - Forecasted", "Recommended Production Volume (2022) - Forecasted"], 
                              aliases = ['Province','Action','Advised Production Value', 'Advised Production Volume'],
                              labels=True, localize=False)

folium.GeoJson(regions, name='Region 2 Map', control = False,
                tooltip=tooltip).add_to(m)


stf.st_folium(m, width=1000, height=410)
