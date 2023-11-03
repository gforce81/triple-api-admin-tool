# Importing all the required libraries
import streamlit as st
import pandas as pd
from datetime import datetime
from api_calls import content_providers

st.set_page_config(
    page_title="Offer Providers ",
    page_icon="🏷️",
    layout="wide"
)

st.markdown(
    """
    ## Select the Offer related operation
    - List Merchants
    - List Offers
    - List Locations
    - Create Merchant
    - Create Location
    - Create Offer
    - Update Merchant
    - Update Location
    - Update Offer
    """
)


def unflatten(dictionary):
    resultDict = {}
    for key, value in dictionary.items():
        parts = key.split('.')
        d = resultDict
        for part in parts[:-1]:  # iterate over all parts except the last one
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = value
    return resultDict


st.divider()

response = {}
view_as_dataframe = False
online_location = False
activation_required = False
dataframe_property = ''

with st.expander("Get a List of Merchants", expanded=False):
    with st.form("Get a List of Merchants"):
        df_view = st.radio("View As Dataframe", ["Yes", "No"])
        get_list_merchants_button = st.form_submit_button("Retrieve")
    if get_list_merchants_button:
        if df_view == "Yes":
            view_as_dataframe = True
            dataframe_property = 'merchants'
        else:
            view_as_dataframe = False
        response = content_providers.list_merchants()

with st.expander("Get a List of Offers", expanded=False):
    with st.form("Get a List of Offers"):
        df_view = st.radio("View As Dataframe", ["Yes", "No"])
        get_list_offers_button = st.form_submit_button("Retrieve")
    if get_list_offers_button:
        if df_view == "Yes":
            view_as_dataframe = True
            dataframe_property = 'offers'
        else:
            view_as_dataframe = False
        response = content_providers.list_offers()

with st.expander("Get a List of Locations", expanded=False):
    with st.form("Get a List of Locations"):
        df_view = st.radio("View As Dataframe", ["Yes", "No"])
        get_list_offers_button = st.form_submit_button("Retrieve")
    if get_list_offers_button:
        if df_view == "Yes":
            view_as_dataframe = True
            dataframe_property = 'locations'
        else:
            view_as_dataframe = False
        response = content_providers.list_locations()

with st.expander("Create a Merchant", expanded=False):
    with st.form("Create a Merchant"):
        assumed_name_input = st.text_input("Merchant Name", placeholder="assumed_name")
        external_id_input = st.text_input("Merchant External ID", placeholder="external_id")
        merchant_category_code_input = st.text_input("Merchant Category Code", placeholder="merchant_category_code")
        logo_url_input = st.text_input("Merchant Logo URL [optional]", placeholder="logo url")
        st.markdown("### Merchant Address")
        city_input = st.text_input("Merchant City [optional]", placeholder="city")
        complete_input = st.text_input("Merchant Complete Address [optional]", placeholder="complete")
        country_code_input = st.text_input("Merchant Country Code", placeholder="country_code")
        country_subdivision_code_input = st.text_input("Merchant State/Province [optional]",
                                                       placeholder="country_subdivision_code")
        latitude_input = st.text_input("Merchant Latitude [optional]", placeholder="latitude")
        longitude_input = st.text_input("Merchant Longitude [optional]", placeholder="longitude")
        postal_code_input = st.text_input("Merchant Postal Code", placeholder="postal_code")
        street_address_input = st.text_input("Merchant Street Address", placeholder="street_address")
        create_merchant_button = st.form_submit_button("Create")
    if create_merchant_button:
        if len(latitude_input) > 0:
            latitude = float(latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(longitude_input)
        else:
            longitude = None

        data = {
            "assumed_name": assumed_name_input,
            "external_id": external_id_input,
            "merchant_category_code": merchant_category_code_input,
            "logo_url": logo_url_input,
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
        response = content_providers.create_merchant(data)

with st.expander("Create a Merchant Location", expanded=False):
    with st.form("Create a Merchant Location"):
        location_email_input = st.text_input("Email [optional]", placeholder="email")
        location_external_id_input = st.text_input("Location External ID", placeholder="external_id")
        location_is_online_input = st.radio("Is Online", ["Yes", "No"])
        location_name_input = st.text_input("Location Name [optional]", placeholder="location_name")
        location_website_input = st.text_input("Location Website [optional]", placeholder="location_website")
        location_parent_merchant_input = st.text_input("Location Parent Merchant External ID",
                                                       placeholder="parent_merchant_external_id")
        location_phone_input = st.text_input("Location Phone Number [optional]", placeholder="phone_number")
        st.markdown("### Processor Merchant IDs")
        mid_input = st.text_input("MID", placeholder="mid")
        mid_type_input = st.selectbox("MID Type", ['AMEX_SE_NUMBER', 'DISCOVER_MID', 'MC_AUTH_LOC_ID', 'MC_AUTH_ACQ_ID',
                                                   'MC_AUTH_ICA', 'MC_CLEARING_LOC_ID', 'MC_CLEARING_ACQ_ID',
                                                   'MC_CLEARING_ICA', 'MERCHANT_PROCESSOR', 'NCR', 'VISA_VMID',
                                                   'VISA_VSID'])
        st.markdown("### Merchant Address")
        location_city_input = st.text_input("Location City [optional]", placeholder="city")
        location_complete_input = st.text_input("Location Complete Address [optional]", placeholder="complete")
        location_country_code_input = st.text_input("Location Country Code", placeholder="country_code")
        location_country_subdivision_code_input = st.text_input("Merchant State/Province [optional]",
                                                                placeholder="country_subdivision_code")
        location_latitude_input = st.text_input("Location Latitude [optional]", placeholder="latitude")
        location_longitude_input = st.text_input("Location Longitude [optional]", placeholder="longitude")
        location_postal_code_input = st.text_input("Location Postal Code", placeholder="postal_code")
        location_street_address_input = st.text_input("Location Street Address", placeholder="street_address")
        create_location_button = st.form_submit_button("Create")
    if create_location_button:
        if len(latitude_input) > 0:
            latitude = float(location_latitude_input)
        else:
            latitude = None

        if len(longitude_input) > 0:
            longitude = float(location_longitude_input)
        else:
            longitude = None
        if location_is_online_input == "True":
            online_location = True
        else:
            online_location = False

        data = {
            "email": location_email_input,
            "external_id": location_external_id_input,
            "is_online": online_location,
            "location_name": location_name_input,
            "location_website": location_website_input,
            "parent_merchant_external_id": location_parent_merchant_input,
            "phone_number": location_phone_input,
            "processor_merchant_ids": [
                {
                    "mid": mid_input,
                    "mid_type": mid_type_input
                }
            ],
            "address": {
                "country_code": location_country_code_input,
                "latitude": latitude,
                "longitude": longitude,
                "postal_code": location_postal_code_input,
                "city": location_city_input,
                "complete": location_complete_input,
                "country_subdivision_code": location_country_subdivision_code_input,
                "street_address": location_street_address_input
            }
        }
        response = content_providers.create_location(data)

with st.expander("Create an Offer", expanded=False):
    with st.form("Create an Offer"):
        offer_activation_required_input = st.radio("Is Online", ["Yes", "No"])
        offer_category_input = st.selectbox("Category",
                                            ['AUTOMOTIVE', 'CHILDREN_AND_FAMILY', 'ELECTRONICS', 'ENTERTAINMENT',
                                             'FINANCIAL_SERVICES', 'FOOD', 'HEALTH_AND_BEAUTY',
                                             'HOME', 'OFFICE_AND_BUSINESS', 'RETAIL', 'SERVICES_AND_SUBSCRIPTIONS',
                                             'TRAVEL', 'UTILITIES_AND_TELECOM'])
        offer_currency_input = st.text_input("Currency Code", placeholder="USD")
        offer_effective_date_input = st.date_input("Start Date", value=None)
        offer_expiration_date_input = st.date_input("End Date", value=None)
        offer_external_id_input = st.text_input("External ID", placeholder="external_id")
        offer_description_input = st.text_area("Description", placeholder="description")
        offer_headline_input = st.text_input("Headline", placeholder="headline")
        offer_marketing_fee_currency_code_input = st.text_input("Marketing Fee Currency", placeholder="USD")
        offer_marketing_fee_type_input = st.text_input("Marketing Fee Type", placeholder="FIXED")
        offer_marketing_fee_value_input = st.text_input("Marketing Fee Value", placeholder="0")
        offer_max_redemptions_input = st.text_input("Maximum Redemptions", value= "1/1Y", placeholder="1/1Y")
        offer_max_reward_cumulative_input = st.text_input("Maximum Reward Cumulative [optional]", placeholder="1")
        offer_max_reward_input = st.text_input("Maximum Reward Per Transaction [optional]", placeholder="1")
        offer_merchant_external_id_input = st.text_input("Merchant External ID", placeholder="merchant_external_id")
        offer_merchant_website_input = st.text_input("Merchant Website", placeholder="merchant_website")
        offer_minimum_spend_input = st.text_input("Minimum Spend", placeholder="minimum_spend")
        offer_mode_input = st.selectbox("Offer Mode", ['ONLINE', 'IN_PERSON', 'IN_PERSON_AND_ONLINE'])
        offer_type_input = st.selectbox("Offer Type", ['CARD_LINKED', 'AFFILIATE', 'CATEGORICAL'])
        offer_reward_type_input = st.selectbox("Reward Type", ['FIXED', 'PERCENTAGE'])
        offer_reward_value = st.text_input("Offer Reward Value (for FIXED)", placeholder="40")
        offer_reward_rate = st.text_input("Offer Reward Rate (for PERCENTAGE)", placeholder="5")
        offer_terms_input = st.text_area("Offer Terms", placeholder="terms")
        st.markdown("### Merchant Categories")
        offer_merchant_category_code_input = st.text_input("Merchant Category Code [optional]", placeholder="8912")
        offer_merchant_category_description = st.text_input("Category Description [optional]", placeholder="something")
        st.markdown("### Offer Budget")
        offer_budget_limit = st.text_input("Maximum Budget", placeholder="5000")
        create_offer_button = st.form_submit_button("Create")
    if create_offer_button:
        if offer_activation_required_input == "Yes":
            activation_required = True
        else:
            activation_required = False
        if offer_marketing_fee_value_input:
            offer_marketing_fee_value_input = float(offer_marketing_fee_value_input)
        if offer_max_reward_cumulative_input:
            offer_max_reward_cumulative_input = float(offer_max_reward_cumulative_input)
        if offer_max_reward_input:
            offer_max_reward_input = float(offer_max_reward_input)
        if offer_minimum_spend_input:
            offer_minimum_spend_input = float(offer_minimum_spend_input)
        if offer_reward_value:
            offer_reward_value = float(offer_reward_value)
        if offer_budget_limit:
            offer_budget_limit = float(offer_budget_limit)

        data = {
            "activation_required": activation_required,
            "category": offer_category_input,
            "currency_code": offer_currency_input,
            "effective_date": offer_effective_date_input.strftime('%Y-%m-%d'),
            "expiration_date": offer_expiration_date_input.strftime('%Y-%m-%d'),
            "external_id": offer_external_id_input,
            "description": offer_description_input,
            "headline": offer_headline_input,
            "marketing_fee_currency_code": offer_marketing_fee_currency_code_input,
            "marketing_fee_type": offer_marketing_fee_type_input,
            "marketing_fee_value": offer_marketing_fee_value_input,
            "max_redemptions": offer_max_redemptions_input,
            "maximum_reward_cumulative": offer_max_reward_cumulative_input,
            "maximum_reward_per_transaction": offer_max_reward_input,
            "merchant_categories": [
                {
                    "merchant_category_code": offer_merchant_category_code_input,
                    "description": offer_merchant_category_description
                }
            ],
            "merchant_external_id": offer_merchant_external_id_input,
            "merchant_website": offer_merchant_website_input,
            "minimum_spend": offer_minimum_spend_input,
            "mode": offer_mode_input,
            "offer_budget": {
                "limit": offer_budget_limit
            },
            "offer_type": offer_type_input,
            "reward_type": offer_reward_type_input,
            "reward_value": offer_reward_value,
            "reward_rate": offer_reward_rate,
            "terms": offer_terms_input
        }
        response = content_providers.create_offer(data)


# def update_merchant(dataframe):
#     data_pd = dataframe.to_dict(orient='records')
#     data = unflatten(data_pd[0])
#     response = content_providers.update_merchant(merchant_id_input, data)
#     return response


# def change_state(edited_df):
#     st.session_state['df_value'] = edited_df


# with st.expander("Update a Merchant", expanded=False):
#     with st.form("Update a Merchant"):
#         df_view = "Yes"
#         merchant_id_input = st.text_input("Merchant ID", placeholder="id")
#         updateget_merchants_button = st.form_submit_button("Retrieve")
#     if updateget_merchants_button:
#         response_dfeditor = content_providers.get_merchant(merchant_id_input)
#         df = pd.json_normalize(response_dfeditor)
#         if "df_value" not in st.session_state:
#             edited_df = st.session_state['df_value']
#             edited_df = st.data_editor(pd.json_normalize(response_dfeditor), on_change=change_state, args=(edited_df,))
#             update_merchant(edited_df)


st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response[dataframe_property])
    st.dataframe(df)
else:
    st.json(response)
