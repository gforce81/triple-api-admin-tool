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
    ## Select the Offer Filters Operation
    - List Filters
    - Create a Filter
    - Patch a Filter
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
        categories = filter_categories.split(",") if len(filter_categories) > 0 else None
        print(f"Categories: {categories}")
        merchants = filter_merchants.split(",") if len(filter_merchants) > 0 else None
        print(f"Merchants: {merchants}")
        providers = filter_content_providers.split(",") if len(filter_content_providers) > 0 else None
        print(f"Content Providers: {providers}")
        offers = filter_offers.split(",") if len(filter_offers) > 0 else None
        print(f"Offers: {offers}")

        # Construct offer_condition dynamically
        offer_condition = {}
        if categories is not None:
            offer_condition["categories"] = categories
        else:
            offer_condition["categories"] = []
        if providers is not None:
            offer_condition["content_provider_ids"] = providers
        else:
            offer_condition["content_provider_ids"] = []
        if merchants is not None:
            offer_condition["merchant_ids"] = merchants
        else:
            offer_condition["merchant_ids"] = []
        if offers is not None:
            offer_condition["offer_ids"] = offers
        else:
            offer_condition["offer_ids"] = []

        # Construct the main data dictionary dynamically
        data = {}
        if filter_description_input is not None:
            data["description"] = filter_description_input
        if filter_activated_input is not None:
            data["is_activated"] = filter_activated_input
        if filter_name_input is not None:
            data["name"] = filter_name_input
        if offer_condition:  # Add offer_condition only if it's not empty
            data["offer_condition"] = offer_condition
        response = offer_filters.create_offer_filters(data)

with st.expander("Patch a Filter", expanded=False):
    with st.form("Patch a Filter"):
        filter_id_input = st.text_input("Filter ID. All other fields are [optional]", placeholder="filter ID")
        filter_description_input = st.text_input("Filter Description [optional]", placeholder="readable description")
        filter_name_input = st.text_input("Filter Name [optional]", placeholder="name")
        filter_activated_input = st.checkbox("Activated [optional]", value=False)
        st.markdown("### Conditions")
        filter_categories = st.text_input("Categories [optional]", placeholder="AUTOMOTIVE,FOOD")
        filter_merchants = st.text_input("Merchant IDs [optional]", placeholder="1,2,3")
        filter_content_providers = st.text_input("Content Providers IDs [optional]", placeholder="1,2,3")
        filter_offers = st.text_input("Offer IDs [optional]", placeholder="1,2,3")
        patch_filter_button = st.form_submit_button("Create")
    if patch_filter_button:
        categories = filter_categories.split(",") if len(filter_categories) > 0 else None
        print(f"Categories: {categories}")
        merchants = filter_merchants.split(",") if len(filter_merchants) > 0 else None
        print(f"Merchants: {merchants}")
        providers = filter_content_providers.split(",") if len(filter_content_providers) > 0 else None
        print(f"Content Providers: {providers}")
        offers = filter_offers.split(",") if len(filter_offers) > 0 else None
        print(f"Offers: {offers}")

        # Construct offer_condition dynamically
        offer_condition = {}
        if categories is not None:
            offer_condition["categories"] = categories
        if providers is not None:
            offer_condition["content_provider_ids"] = providers
        if merchants is not None:
            offer_condition["merchant_ids"] = merchants
        if offers is not None:
            offer_condition["offer_ids"] = offers

        # Construct the main data dictionary dynamically
        data = {}
        if filter_description_input is not None:
            data["description"] = filter_description_input
        if filter_activated_input is not None:
            data["is_activated"] = filter_activated_input
        if filter_name_input is not None:
            data["name"] = filter_name_input
        if offer_condition:  # Add offer_condition only if it's not empty
            data["offer_condition"] = offer_condition

        # Call the API with the populated data
        response = offer_filters.patch_offer_filters(filter_id_input, data)

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['filters'])
    st.dataframe(df)
else:
    st.json(response)
