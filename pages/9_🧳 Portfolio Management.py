# Importing all the required libraries
import streamlit as st
import pandas as pd
from pandas import json_normalize
from api_calls import portfolio_management

st.set_page_config(
    page_title="Portfolio Management APIs ",
    page_icon="🧳",
    layout="wide"
)

st.markdown(
    """
    ## Select the Portfolio Management Operation
    - Get a list of publishers
    - Create a publisher
    - Get a publisher by ID
    - Update an existing publisher
    """
)
st.divider()

response = {}
view_as_dataframe = False

with st.expander("List Publishers", expanded=False):
    df_view = st.radio("View as Dataframe", ["Yes", "No"])
    if st.button("Display", key="list_publishers", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        if df_view == "Yes":
            view_as_dataframe = True
        response = portfolio_management.list_publishers()

with st.expander("Create a Publisher", expanded=False):
    with st.form("Create a Publishert"):
        publisher_assumed_name_input = st.text_input("Publisher Name", placeholder="assumed_name")
        publisher_external_id_input = st.text_input("Publisher External ID", placeholder="external_id")
        revenue_share_input = st.text_input("Revenue Share [optional]", placeholder="5")
        st.markdown("### Publisher Address")
        city_input = st.text_input("Publisher City [optional]", placeholder="city")
        complete_input = st.text_input("Publisher Complete Address [optional]", placeholder="complete")
        country_code_input = st.text_input("Publisher Country Code", placeholder="country_code")
        country_subdivision_code_input = st.text_input("Publisher State/Province [optional]",
                                                       placeholder="country_subdivision_code")
        latitude_input = st.text_input("Publisher Latitude [optional]", placeholder="latitude")
        longitude_input = st.text_input("Publisher Longitude [optional]", placeholder="longitude")
        postal_code_input = st.text_input("Publisher Postal Code", placeholder="postal_code")
        street_address_input = st.text_input("Publisher Street Address", placeholder="street_address")
        create_publisher_button = st.form_submit_button("Create")
    if create_publisher_button:
        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        if len(revenue_share_input) > 0:
            revenue_share = revenue_share_input
        else:
            revenue_share = None

        data = {
            "assumed_name": publisher_assumed_name_input,
            "external_id": publisher_external_id_input,
            "revenue_share": revenue_share,
            "address": {
                "country_code": country_code_input,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code_input,
                "city": city_input,
                "complete": complete_input,
                "country_subdivision_code": country_subdivision_code_input,
                "street_address": street_address_input
            }
        }
        response = portfolio_management.create_publisher(data)


st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['publishers'])
    st.dataframe(df)
else:
    st.json(response)
