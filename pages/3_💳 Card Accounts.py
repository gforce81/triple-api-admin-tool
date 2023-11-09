# Importing all the required libraries
import streamlit as st
import pandas as pd
from pandas import json_normalize
from api_calls import card_accounts

st.set_page_config(
    page_title="Card Accounts APIs ",
    page_icon="💳",
    layout="wide"
)

st.markdown(
    """
    ## Select the Card Account Operation
    - List all card accounts for the authenticated Triple account
    - Get the details for a specific card account using a triple_id
    - Get the details for a specific card account using an external_id
    - Create a new card account
    - Update an existing card account
    """
)
st.divider()

response = {}
label_select_cardAccountOperation = ""
view_as_dataframe = False

with st.expander("List Card Accounts", expanded=False):
    df_view = st.radio("View as Dataframe", ["Yes", "No"])
    if st.button("Display", key="list_card_accounts_button", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        if df_view == "Yes":
            view_as_dataframe = True
        response = card_accounts.list_card_accounts()


with st.expander("Get a Card Account by triple_id", expanded=False):
    cardAccountTriple_getBox = st.text_input("Card Account ID", key="get_card_accountTriple_box")
    if st.button("Display", key="get_card_accountTriple_button"):
        response = card_accounts.get_card_account(cardAccountTriple_getBox)


with st.expander("Get a Card Account by external_id", expanded=False):
    cardAccountExternal_getBox = st.text_input("Card Account External ID", key="get_card_accountExternal_box")
    if st.button("Display", key="get_card_accountExternal_button"):
        response = card_accounts.get_card_account_external(cardAccountExternal_getBox)


with st.expander("Create Card Account", expanded=False):
    with st.form("Create Card Account"):
        card_program_external_input = st.text_input("Card Program External ID", placeholder="the external ID of the card program")
        default_country_code_input = st.text_input("Default Country Code", placeholder="US")
        default_postal_code_input = st.text_input("Default Postal Code", placeholder="90210")
        external_id_input = st.text_input("External ID", placeholder="external ID as string")
        status_input = st.selectbox("Enrollment Status", ["ENROLLED", "NOT_ENROLLED", "CLOSED"])
        publisher_external_id_input = st.text_input("Publisher External ID [optional]",
                                                    placeholder="publisher_external_id")
        create_card_account_button = st.form_submit_button("Create")
    if create_card_account_button:
        if len(publisher_external_id_input) > 0:
            publisher = publisher_external_id_input
        else:
            publisher = None

        data = {
            "card_program_external_id": card_program_external_input,
            "default_country_code": default_country_code_input,
            "default_postal_code": default_postal_code_input,
            "external_id": external_id_input,
            "status": status_input,
            "publisher_external_id": publisher
        }
        response = card_accounts.create_card_account(data)

with st.expander("Update a Card Account", expanded=False):
    cardAccountTriple_getBox = st.text_input("Card Account ID")
    status_input = st.selectbox("Enrollment Status", ["ENROLLED", "NOT_ENROLLED", "CLOSED"])
    if st.button("Update", key="update_card_programs_button", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        response = card_accounts.update_card_account(cardAccountTriple_getBox, status_input)

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['card_accounts'])
    st.dataframe(df)
else:
    st.json(response)
