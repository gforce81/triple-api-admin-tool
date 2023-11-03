# Importing all the required libraries
import streamlit as st
import pandas as pd
import json
from pandas import json_normalize
from datetime import datetime, timezone
from api_calls import cards_transactions

st.set_page_config(
    page_title="Offers Display APIs ",
    page_icon="💵",
    layout="wide"
)

st.markdown(
    """
    ## Select the Transactions Operation
    - Get a list of transactions for the authenticated account
    - Create a transaction
    - Get a specific transaction by ID
    """
)
st.divider()

response = {}
view_as_dataframe = False


def check_string_len(data_string):
    if len(data_string) <= 0:
        data_string = None
        return data_string
    else:
        return data_string


def check_string_none(data_string):
    if data_string is "NONE":
        data_string = None
        return data_string
    else:
        return data_string


with st.expander("Get a List of Transactions", expanded=False):
    with st.form("Get a List of Transactions"):
        publisher_external_id_input = st.text_input("Publisher External ID [optional]",
                                                    placeholder="the publisher external ID")
        card_program_external_id_input = st.text_input("Card Program External ID [optional]",
                                                       placeholder="the card program external ID")
        card_account_external_id_input = st.text_input("Card Account External ID [optional]",
                                                       placeholder="the card account external ID")
        transaction_external_id_input = st.text_input("Transaction External ID [optional]",
                                                      placeholder="the transaction external ID")
        start_date_input = st.date_input("Start Date [optional]", value=None)
        end_date_input = st.date_input("End Date [optional]", value=None)
        matched_input = st.selectbox("Matched Transactions Only [optional]", ["NONE", True, False])
        df_view = st.radio("View Rewards Only", ["Yes", "No"])
        get_list_transactions_button = st.form_submit_button("Retrieve")
    if get_list_transactions_button:
        if df_view == "Yes":
            view_as_dataframe = True
        else:
            view_as_dataframe = False
        if len(publisher_external_id_input) <= 0:
            publisher_external_id_input = None
        if len(card_program_external_id_input) <= 0:
            card_program_external_id_input = None
        if len(card_account_external_id_input) <= 0:
            card_account_external_id_input = None
        if len(transaction_external_id_input) <= 0:
            transaction_external_id_input = None
        if matched_input == "NONE":
            matched_input = None

        data = {
            "publisher_external_id": publisher_external_id_input,
            "card_program_external_id": card_program_external_id_input,
            "card_account_external_id": card_account_external_id_input,
            "transaction_external_id": transaction_external_id_input,
            "start_date": start_date_input,
            "end_date": end_date_input,
            "matched": matched_input
        }

        response = cards_transactions.get_list_transactions(data)

with st.expander("Create a Transaction", expanded=False):
    with st.form("Create a Transaction"):
        amount_input = st.text_input("Amount", placeholder="amount")
        card_account_external_id_input = st.text_input("Card Account External ID",
                                                       placeholder="the card account external ID")
        card_bin_input = st.text_input("Card BIN [optional]", placeholder="card bin")
        card_last4_input = st.text_input("Card Last 4 Digits [optional]", placeholder="card last 4 digits")
        card_program_external_id_input = st.text_input("Card Program External ID",
                                                       placeholder="the card program external ID")
        currency_code_input = st.text_input("Currency Code [optional]", placeholder="USD")
        debit_input = st.selectbox("Debit", [True, False])
        description_input = st.text_input("Description", placeholder="transaction description")
        external_id_input = st.text_input("External ID", placeholder="the external ID of the transaction")
        merchant_category_code_input = st.text_input("Merchant Category Code [optional]", placeholder="5812")
        processor_mid_input = st.text_input("Processor MID [optional]", placeholder="the processor MID")
        processor_midtype_input = st.selectbox("Processor MID Type [optional]",
                                               ["NONE", "AMEX_SE_NUMBER", "DISCOVER_MID",
                                                "MC_AUTH_LOC_ID", "MC_AUTH_ACQ_ID",
                                                "MC_AUTH_ICA", "MC_CLEARING_LOC_ID",
                                                "MC_CLEARING_ACQ_ID", "MC_CLEARING_ICA",
                                                "MERCHANT_PROCESSOR", "NCR",
                                                "VISA_VMID", "VISA_VSID"])
        timestamp_input = datetime.now(timezone.utc).isoformat()
        transaction_type_input = st.selectbox("PURCHASE", ["CHECK", "DEPOSIT", "FEE", "PAYMENT", "PURCHASE", "REFUND",
                                                           "TRANSFER", "WITHDRAWAL"])
        st.markdown("### Merchant Address [optional]")
        city_input = st.text_input("City", placeholder="merchant city")
        street_address_input = st.text_input("Street Address", placeholder="street address")
        country_subdivision_input = st.text_input("Province/State", placeholder="MA")
        postal_code_input = st.text_input("Postal Code", placeholder="90210")
        country_code_input = st.text_input("Country Code", placeholder="US")
        complete_address_input = st.text_input("Complete Address", placeholder="the complete address")
        latitude_input = st.text_input("Latitude", placeholder="40.440624")
        longitude_input = st.text_input("Longitude", placeholder="-79.995888")

        create_transaction_button = st.form_submit_button("Create")

    if create_transaction_button:
        data = {
            "amount": amount_input,
            "card_account_external_id": card_account_external_id_input,
            "card_bin": check_string_len(card_bin_input),
            "card_last_4": check_string_len(card_last4_input),
            "card_program_external_id": card_program_external_id_input,
            "currency_code": check_string_len(currency_code_input),
            "debit": debit_input,
            "description": description_input,
            "external_id": external_id_input,
            "merchant_category_code": check_string_len(merchant_category_code_input),
            "merchant_address": {
                "city": check_string_len(city_input),
                "complete": check_string_len(complete_address_input),
                "country_code": check_string_len(country_code_input),
                "country_subdivision_code": check_string_len(country_subdivision_input),
                "latitude": latitude_input,
                "longitude": longitude_input,
                "postal_code": check_string_len(postal_code_input),
                "street_address": check_string_len(street_address_input)
            },
            "processor_mid": check_string_len(processor_mid_input),
            "processor_mid_type": check_string_none(processor_midtype_input),
            "timestamp": timestamp_input,
            "transaction_type": transaction_type_input
        }
        response = cards_transactions.create_transaction(data)

with st.expander("Get a Transactions", expanded=False):
    with st.form("Get a Transaction"):
        transaction_id_input = st.text_input("Transaction ID", placeholder="the transaction ID")
        get_transaction_button = st.form_submit_button("Retrieve")
        if get_transaction_button:
            response = cards_transactions.get_transaction(transaction_id_input)

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['transactions'], record_path='reward_details',
                           meta=['amount', 'card_account_id', 'card_account_external_id', 'created_at', 'currency_code',
                                 'debit', 'description', 'external_id', 'matching_status', 'transaction_type',
                                 ['merchant_address', 'complete'], ['merchant_category', 'description']],
                           meta_prefix='tx_',
                           errors='ignore')
    # df = pd.DataFrame(response["transactions"])
    st.dataframe(df)
else:
    st.json(response)
