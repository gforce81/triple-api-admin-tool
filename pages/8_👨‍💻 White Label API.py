# Importing all the required libraries
import streamlit as st
import pandas as pd
import json

import api_calls.ui_api
from api_calls import ui_api

st.set_page_config(
    page_title="White Label API ",
    page_icon="👨‍💻",
    layout="wide"
)

st.markdown(
    """
    ## Select the UI API related operation
    - Initiate Session
    - Initiate Session Using a Cardholder External ID
    - Offers Search
    - Offer Details
    - Activated Offers
    - Offers Home
    - Affiliate Link
    - Transactions
    """
)

st.divider()

response = {}
view_as_dataframe = False
display_images = False
show_test_amplifi = False
dataframe_property = ''

with st.expander("Initiate Session", expanded=False):
    with st.form("Initiate Session"):
        init_session_cardholder_input = st.text_input("Card Account ID", placeholder="card_account_id")
        init_session_amplifi = st.checkbox("Generate ampliFI Test URLs")
        init_session_button = st.form_submit_button("Start")
    if init_session_button:
        if init_session_amplifi:
            show_test_amplifi = True
        data = {
            "card_account_id": init_session_cardholder_input
        }
        response = ui_api.initiate_session(data)

with st.expander("Initiate Session Using a Cardholder External ID", expanded=False):
    with st.form("Initiate Session Using a Cardholder External ID"):
        init_session_cardholder_ext_input = st.text_input("Card Account External ID",
                                                          placeholder="card_account_external_id")
        init_session_card_program_ext_input = st.text_input("Card Program External ID",
                                                            placeholder="card_program_external_id")
        init_session_ext_button = st.form_submit_button("Start")
    if init_session_ext_button:
        data = {
            "card_account_external_id": init_session_cardholder_ext_input,
            "card_program_external_id": init_session_card_program_ext_input
        }
        response = ui_api.initiate_session(data)

with st.expander("Offers Home", expanded=False):
    with st.form("Offers Home"):
        offers_home_cardholder_input = st.text_input("Card Account ID", placeholder="card_account_id")
        offers_home_country_code = st.text_input("Country Code", placeholder="US")
        offers_home_latitude = st.text_input("Latitude", placeholder="40.440624")
        offers_home_longitude = st.text_input("Longitude", placeholder="-79.995888")
        offers_home_postal_code = st.text_input("Postal Code", placeholder="15206")
        offers_home_sections = st.text_area("Sections",
                                            """[{},{"include_modes": ["ONLINE"]},{"include_modes": ["IN_PERSON"], 
                                            "include_categories": ["FOOD"]}]""")
        offers_home_radius = st.text_input("Radius", placeholder="25000")

        offers_home_button = st.form_submit_button("Display")

    if offers_home_button:
        if len(offers_home_country_code) > 0:
            country_code = offers_home_country_code
        else:
            country_code = None

        if len(offers_home_latitude) > 0:
            latitude = float(offers_home_latitude)
        else:
            latitude = None

        if len(offers_home_longitude) > 0:
            longitude = float(offers_home_longitude)
        else:
            longitude = None

        if len(offers_home_postal_code) > 0:
            postal_code = offers_home_postal_code
        else:
            postal_code = None

        if len(offers_home_radius) > 0:
            radius = int(offers_home_radius)
        else:
            radius = None

        if latitude is None:
            data = {
                "card_account_id": offers_home_cardholder_input,
                "country_code": country_code,
                "postal_code": postal_code,
                "radius": radius,
                "sections": json.loads(offers_home_sections)
            }
        else:
            data = {
                "card_account_id": offers_home_cardholder_input,
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code,
                "radius": radius,
                "sections": json.loads(offers_home_sections)
            }
        response = ui_api.offers_home(data)
        display_images = True

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response[dataframe_property])
    st.dataframe(df)
else:
    st.json(response, expanded=False)
    if show_test_amplifi:
        amplifi_response = ui_api.test_amplifi(response['token'])
        for url in amplifi_response['urls']:
            st.markdown("- [" + url + "](" + url + ")")

if display_images:
    for idx, section in enumerate(response['sections']):
        list_of_images = []
        list_of_captions = []
        ncol = len(response['sections'][idx]['offers'])
        cols = st.columns(ncol, gap="medium")
        for offer in response['sections'][idx]['offers']:
            list_of_images.append(offer['merchant_logo_url'])
            list_of_captions.append(offer['headline'])
        for i in range(ncol):
            with cols[i]:
                st.image(list_of_images[i], caption=list_of_captions[i], width=80)
        st.divider()
