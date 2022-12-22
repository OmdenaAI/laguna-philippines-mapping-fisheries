import streamlit as st
import folium
import streamlit_folium as stf
import geopandas as gdf
import requests
import webbrowser
import json


#-----Functions------
def formatter(geojson, features):
    for i in range(len(geojson['features'])):
        for j in features:
            geojson['features'][i]['properties'][j] = round(float(geojson['features'][i]['properties'][j]))
    return geojson

def color_coding(row):
    if row.Recommendation == 'Increase Fishing Activity':
        return ['background-color:lightgreen'] * len(row)
    elif row.Recommendation == 'Decrease Fishing Activity':
        return ['background-color:salmon'] * len(row)
    else:
        return ['background-color:peachpuff'] * len(row)

    
#------Page and Element Configs----
st.title("Fishing Activity Recommender")
col1, col2 = st.columns(2)

#-----Map Components-----
regions_raw = 'https://raw.githubusercontent.com/OmdenaAI/laguna-philippines-mapping-fisheries/main/src/results/region_2_results_with_recommendation.geojson'
response = requests.get(regions_raw)
regions = json.loads(response.content)
data = gdf.read_file(regions_raw)
features = ['Recommended Production Value (2022) - Forecasted', 'Recommended Production Volume (2022) - Forecasted']
data = data[['index','Recommendation']+features]
data[features] = data[features].astype(float).astype(int)
data.rename({'Recommended Production Value (2022) - Forecasted':'Recomm Prod Value (per 1000 PhP)',
             'Recommended Production Volume (2022) - Forecasted':'Recomm Prod Volume (in metric tons)'},
            axis=1,
            inplace=True)
regions = formatter(regions, features)


m = folium.Map(location=[18.43959, 121.3991212], zoom_start=6.3, zoom_control=False)
tooltip = folium.features.GeoJsonTooltip(fields=['index','Recommendation',"Recommended Production Value (2022) - Forecasted", "Recommended Production Volume (2022) - Forecasted"], 
                              aliases = ['Province','Action','Production Value', 'Production Volume'],
                              labels=True, localize=True)

folium.GeoJson(regions, name='Region 2 Map', control = False,
                tooltip=tooltip).add_to(m)


#-----Page Building-----
st.sidebar.title("About")
st.sidebar.markdown("""This is an open source project created by Omdena Laguna Chapter. The aim being to help connect and encourage organizations to use AI tools to understand and plan how to better utilize the country’s aquatic resources. We also hope to encourage citizen science by open sourcing the dataset and code.""")

st.sidebar.empty()

st.sidebar.markdown(f"Watch the [Project Presentation]({st.secrets['slide_deck']})")
st.sidebar.markdown(f"Review the [Project Repository]({st.secrets['repo']})")

st.sidebar.empty()

st.sidebar.title("Contact")
st.sidebar.info(
    '''
    This project is owned by:\n
    © Omdena Laguna, Philippines\n
    omdena.laguna@gmail.com
    '''
)



with col1:
    stf.st_folium(m, width=500, height=330)
with col2:
    st.subheader('Recommendation Descriptions')
    with st.expander('Increase Fishing Activity'):
        st.success("The recommended production value and volume shows a significant increase. It is advised to increase the fishing activity to leverage higher production and higher valuation")
    with st.expander('Decrease Fishing Activity'):
        st.error('The recommended production value and volume shows a significant decrease. It is advised to decrease the fishing actvity to lower the production volume and lower valuation')
    with st.expander('Increase Fishing Activity (Lower Price)'):
        st.warning('The recommeded production value and volume shows a slight increase. It is advised to increase the fishing activity but to lower the valuation since the resources can support higher demand for lower valuation.')
    with st.expander('Increase Fishing Activity (Keep Price)'):
        st.warning('The recommeded production value and volume shows a slight increase. It is advised to increase the fishing activity but to retain the current valuation')
st.table(data.style.apply(color_coding, axis=1))
