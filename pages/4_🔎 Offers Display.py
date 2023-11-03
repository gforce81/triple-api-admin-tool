# Importing all the required libraries
import streamlit as st
from api_calls import offers_display


st.set_page_config(
    page_title="Offers Display APIs ",
    page_icon="🔎",
    layout="wide"
)

st.markdown(
    """
    ## Select the Offers Display Operation
    - Retrieve activated offers for a card account
    - Retrieve the offer categories for a card account
    - Retrieve the offer recommendations for a card account
    - Search all available offers for a card account
    - Get the details of an offer using a card_account_id
    - Get the details of an offer without a card_account_id (no proximity target)
    """
)
st.divider()

response = {}
label_select_offerDisplayOperation = ""

triple_categories_none = ["NONE", "AUTOMOTIVE", "CHILDREN_AND_FAMILY", "ELECTRONICS", "ENTERTAINMENT",
                          "FINANCIAL_SERVICES", "FOOD", "HEALTH_AND_BEAUTY", "HOME", "OFFICE_AND_BUSINESS", "RETAIL",
                          "SERVICES_AND_SUBSCRIPTIONS", "TRAVEL", "UTILITIES_AND_TELECOM"]
triple_categories = ["AUTOMOTIVE", "CHILDREN_AND_FAMILY", "ELECTRONICS", "ENTERTAINMENT",
                     "FINANCIAL_SERVICES", "FOOD", "HEALTH_AND_BEAUTY", "HOME", "OFFICE_AND_BUSINESS", "RETAIL",
                     "SERVICES_AND_SUBSCRIPTIONS", "TRAVEL", "UTILITIES_AND_TELECOM"]

triple_modes_none = ["NONE", "ONLINE", "IN_PERSON", "IN_PERSON_AND_ONLINE"]
triple_modes = ["ONLINE", "IN_PERSON", "IN_PERSON_AND_ONLINE"]

triple_types_none = ["NONE", "CARD_LINKED", "AFFILIATE", "CATEGORICAL"]
triple_types = ["CARD_LINKED", "AFFILIATE", "CATEGORICAL"]

with st.expander("Get Activated Offers for a Card Account", expanded=False):
    with st.form("Get Activated Offers"):
        card_account_input = st.text_input("Card Account ID", placeholder="the card account ID")
        expires_within_input = st.text_input("Activated Offers Expiring in... [optional]", placeholder="1 or 3 or 5 or 10")
        include_expired_input = st.selectbox("Included Expired Offers [optional]", [True, False])
        page_offset_input = st.text_input("Page Offset [optional]", placeholder="0...975")
        page_size_input = st.text_input("Page Size [optional]", placeholder="0...100")
        st.markdown("### Proximity Target [optional]")
        country_code_input = st.text_input("Country Code", placeholder="US")
        latitude_input = st.text_input("Latitude", placeholder="40.440624")
        longitude_input = st.text_input("Longitude", placeholder="-79.995888")
        postal_code_input = st.text_input("Postal Code", placeholder="90210")
        radius_input = st.text_input("Radius", placeholder="35000")
        get_activated_offers_button = st.form_submit_button("Display")
    if get_activated_offers_button:
        try:
            expires_within = int(expires_within_input)
        except:
            expires_within = None

        try:
            page_offset = int(page_offset_input)
        except:
            page_offset = 0

        try:
            page_size = int(page_size_input)
        except:
            page_size = 25

        if len(country_code_input) > 0:
            country_code = country_code_input
        else:
            country_code = None

        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        if len(postal_code_input) > 0:
            postal_code = postal_code_input
        else:
            postal_code = None

        if len(radius_input) > 0:
            radius = int(radius_input)
        else:
            radius = None

        data = {
            "expires_within": expires_within,
            "include_expired": include_expired_input,
            "page_offset": page_offset,
            "page_size": page_size,
            "proximity_target": {
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code,
                "radius": radius
            }
        }
        response = offers_display.get_offers_activated(card_account_input, data)

with st.expander("Get Available Offer Categories", expanded=False):
    cardAccountTriple_getBox = st.text_input("Card Account ID", key="get_card_accountTriple_box")
    if st.button("Display", key="get_card_accountTriple_button"):
        response = offers_display.get_offers_categories(cardAccountTriple_getBox)

with st.expander("Get Offers Recommendations", expanded=False):
    with st.form("Get Offers Recommendations"):
        card_account_input = st.text_input("Card Account ID", placeholder="the card account ID")
        include_categories_input = st.multiselect("Include Categories [optional]", triple_categories)
        include_modes_input = st.multiselect("Include Modes [optional]", triple_modes)
        page_size_input = st.text_input("Page Size [optional]", placeholder="0...100")
        st.markdown("### Apply Filter [optional]")
        filter_exclude_category_input = st.selectbox("Only in Category", triple_categories_none)
        filter_exclude_offer_ids_input = st.text_input("Exclude Offer IDs", placeholder="abc-123, def-345")
        filter_include_offer_ids_input = st.text_input("Include Offer IDs", placeholder="abc-123, def-345")
        filter_mode = st.selectbox("Only in Mode", triple_modes_none)
        filter_type = st.selectbox("Only in Type", triple_types_none)
        filter_activation_required = st.selectbox("Activation Required", ["NONE", True, False])
        st.markdown("### Proximity Target [optional]")
        country_code_input = st.text_input("Country Code", placeholder="US")
        latitude_input = st.text_input("Latitude", placeholder="40.440624")
        longitude_input = st.text_input("Longitude", placeholder="-79.995888")
        postal_code_input = st.text_input("Postal Code", placeholder="90210")
        radius_input = st.text_input("Radius", placeholder="35000")
        get_offers_recommendations_button = st.form_submit_button("Get Recommendations")

    if get_offers_recommendations_button:
        try:
            page_size = int(page_size_input)
        except:
            page_size = 25

        if len(country_code_input) > 0:
            country_code = country_code_input
        else:
            country_code = None

        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        if len(postal_code_input) > 0:
            postal_code = postal_code_input
        else:
            postal_code = None

        if len(radius_input) > 0:
            radius = int(radius_input)
        else:
            radius = None

        if len(include_categories_input) < 1:
            include_categories_input = triple_categories
        if len(include_modes_input) < 1:
            include_modes_input = triple_modes

        if filter_exclude_category_input == "NONE":
            filter_exclude_category_input = None
        else:
            include_categories_input = filter_exclude_category_input
        if filter_mode == "NONE":
            filter_mode = None
        else:
            include_modes_input = filter_mode
        if filter_type == "NONE":
            filter_type = None
        if filter_activation_required == "NONE":
            filter_activation_required = None
        if len(filter_exclude_offer_ids_input) > 0:
            filter_exclude_offer_ids_input = filter_exclude_offer_ids_input.split(",")
        else:
            filter_exclude_offer_ids_input = []
        if len(filter_include_offer_ids_input) > 0:
            filter_include_offer_ids_input = filter_include_offer_ids_input.split(",")
        else:
            filter_include_offer_ids_input = []

        data = {
            "page_size": page_size,
            "include_categories": include_categories_input,
            "include_modes": include_modes_input,
            "proximity_target": {
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code,
                "radius": radius
            },
            "apply_filter": {
                "category": filter_exclude_category_input,
                "exclude_offer_ids": filter_exclude_offer_ids_input,
                "include_offer_ids": filter_include_offer_ids_input,
                "mode": filter_mode,
                "type": filter_type,
                "activation_required": filter_activation_required
            }
        }
        response = offers_display.offers_recommendations(card_account_input, data)

with st.expander("Search Offers", expanded=False):
    with st.form("Search Offers"):
        card_account_input = st.text_input("Card Account ID", placeholder="the card account ID")
        text_query_input = st.text_input("Text Query", placeholder="*")
        page_size_input = st.text_input("Page Size", placeholder="0...100")
        page_offset_input = st.text_input("Page Offset", placeholder="0...975")
        st.markdown("### Apply Filter [optional]")
        filter_exclude_category_input = st.selectbox("Only in Category", triple_categories_none)
        filter_exclude_offer_ids_input = st.text_input("Exclude Offer IDs", placeholder="abc-123, def-345")
        filter_include_offer_ids_input = st.text_input("Include Offer IDs", placeholder="abc-123, def-345")
        filter_mode = st.selectbox("Mode", triple_modes_none)
        filter_type = st.selectbox("Type", triple_types_none)
        filter_activation_required = st.selectbox("Activation Required", ["NONE", True, False])
        st.markdown("### Proximity Target [optional]")
        country_code_input = st.text_input("Country Code", placeholder="US")
        latitude_input = st.text_input("Latitude", placeholder="40.440624")
        longitude_input = st.text_input("Longitude", placeholder="-79.995888")
        postal_code_input = st.text_input("Postal Code", placeholder="90210")
        radius_input = st.text_input("Radius", placeholder="35000")
        get_search_offers_button = st.form_submit_button("Search Offers")

    if get_search_offers_button:
        try:
            page_size = int(page_size_input)
        except:
            page_size = 25

        try:
            page_offset = int(page_offset_input)
        except:
            page_offset = 0

        if len(text_query_input) > 0:
            text_query = text_query_input
        else:
            text_query = "*"

        if len(country_code_input) > 0:
            country_code = country_code_input
        else:
            country_code = None

        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        if len(postal_code_input) > 0:
            postal_code = postal_code_input
        else:
            postal_code = None

        if len(radius_input) > 0:
            radius = int(radius_input)
        else:
            radius = None

        if len(include_categories_input) < 1:
            include_categories_input = triple_categories
        if len(include_modes_input) < 1:
            include_modes_input = triple_modes

        if filter_exclude_category_input == "NONE":
            filter_exclude_category_input = None

        if filter_mode == "NONE":
            filter_mode = None

        if filter_type == "NONE":
            filter_type = None
        if filter_activation_required == "NONE":
            filter_activation_required = None
        if len(filter_exclude_offer_ids_input) > 0:
            filter_exclude_offer_ids_input = filter_exclude_offer_ids_input.split(",")
        else:
            filter_exclude_offer_ids_input = []
        if len(filter_include_offer_ids_input) > 0:
            filter_include_offer_ids_input = filter_include_offer_ids_input.split(",")
        else:
            filter_include_offer_ids_input = []

        data = {
            "page_size": page_size,
            "page_offset": page_offset,
            "text_query": text_query,
            "proximity_target": {
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code,
                "radius": radius
            },
            "apply_filter": {
                "category": filter_exclude_category_input,
                "exclude_offer_ids": filter_exclude_offer_ids_input,
                "include_offer_ids": filter_include_offer_ids_input,
                "mode": filter_mode,
                "type": filter_type,
                "activation_required": filter_activation_required
            }
        }
        response = offers_display.offers_search(card_account_input, data)

with st.expander("Offer Details", expanded=False):
    with st.form("Offers Details"):
        card_account_input = st.text_input("Card Account ID", placeholder="the card account ID")
        offer_id_input = st.text_input("Offer ID", placeholder="triple-abc-123")
        st.markdown("### Proximity Target [optional]")
        country_code_input = st.text_input("Country Code", placeholder="US")
        latitude_input = st.text_input("Latitude", placeholder="40.440624")
        longitude_input = st.text_input("Longitude", placeholder="-79.995888")
        postal_code_input = st.text_input("Postal Code", placeholder="90210")
        radius_input = st.text_input("Radius", placeholder="35000")
        get_offer_details_button = st.form_submit_button("Get Details")

    if get_offer_details_button:
        if len(country_code_input) > 0:
            country_code = country_code_input
        else:
            country_code = None

        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        if len(postal_code_input) > 0:
            postal_code = postal_code_input
        else:
            postal_code = None

        if len(radius_input) > 0:
            radius = int(radius_input)
        else:
            radius = None

        data = {
            "proximity_target": {
                "country_code": country_code,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": postal_code,
                "radius": radius
            },
            "offer_id": offer_id_input
        }
        response = offers_display.get_offers_details_by_cardholder(card_account_input, data)

with st.expander("Offer Details - No card_account_id", expanded=False):
    with st.form("Offers Details - No card_account_id"):
        offer_id_input = st.text_input("Offer ID", placeholder="the offer ID")
        get_offer_details_button2 = st.form_submit_button("Get Details")
    if get_offer_details_button2:
        response = offers_display.get_offers_details(offer_id_input)


st.write("")
st.json(response)
