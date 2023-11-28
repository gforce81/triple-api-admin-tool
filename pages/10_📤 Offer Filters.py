# Importing all the required libraries
import streamlit as st
import pandas as pd
from pandas import json_normalize
from api_calls import offer_filters


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


with st.expander("List Filters", expanded=False):
    df_view = st.radio("View as Dataframe", ["Yes", "No"])
    if st.button("Display", key="list_filters", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        if df_view == "Yes":
            view_as_dataframe = True
        response = offer_filters.list_offer_filters()

with st.expander("Create a Filter", expanded=False):
    with st.form("Create a Filter"):
        patch_selection = st.toggle("Patch", value=False)
        if patch_selection:
            filter_id_input = st.text_input("Filter ID. All other fields are [optional]", placeholder="filter_id")
        filter_description_input = st.text_input("Filter Description", placeholder="readable description")
        filter_name_input = st.text_input("Filter Name", placeholder="name")
        filter_activated_input = st.checkbox("Activated", value=False)
        st.markdown("### Conditions")
        filter_categories = st.text_input("Categories [optional]", placeholder="AUTOMOTIVE,FOOD")
        filter_merchants = st.text_input("Merchant IDs [optional]", placeholder="1,2,3")
        filter_content_providers = st.text_input("Content Providers IDs [optional]", placeholder="1,2,3")
        filter_offers = st.text_input("Offer IDs [optional]", placeholder="1,2,3")
        create_filter_button = st.form_submit_button("Create")
    if create_filter_button:
        if len(filter_categories) > 0:
            categories = filter_categories.split(",")
        else:
            categories = None
        if len(filter_merchants) > 0:
            merchants = filter_merchants.split(",")
        else:
            merchants = None
        if len(filter_content_providers) > 0:
            providers = filter_content_providers.split(",")
        else:
            providers = None
        if len(filter_offers) > 0:
            offers = filter_offers.split(",")
        else:
            offers = None

        data = {
            "description": filter_description_input,
            "is_activated": filter_activated_input,
            "name": filter_name_input,
            "offer_condition": {
                "categories": categories,
                "content_provider_ids": providers,
                "merchant_ids": merchants,
                "offer_ids": offers
            }
        }
        if patch_selection == "Patch":
            response = offer_filters.patch_offer_filters(filter_id_input, data)
        else:
            response = offer_filters.create_offer_filters(data)


st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['filters'])
    st.dataframe(df)
else:
    st.json(response)
