# Importing all the required libraries
import streamlit as st
import pandas as pd
from datetime import datetime

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
dataframe_property = ''

with st.expander("Initiate Session", expanded=False):
    with st.form("Initiate Session"):
        init_session_cardholder_input = st.text_input("Card Account ID", placeholder="card_account_id")
        init_session_button = st.form_submit_button("Start")
    if init_session_button:
        data = {
            "card_account_id": init_session_cardholder_input
        }
        response = ui_api.initiate_session(data)

with st.expander("Initiate Session Using a Cardholder External ID", expanded=False):
    with st.form("Initiate Session Using a Cardholder External ID"):
        init_session_cardholder_ext_input = st.text_input("Card Account External ID", placeholder="card_account_external_id")
        init_session_card_program_ext_input = st.text_input("Card Program External ID", placeholder="card_program_external_id")
        init_session_ext_button = st.form_submit_button("Start")
    if init_session_ext_button:
        data = {
            "card_account_external_id": init_session_cardholder_ext_input,
            "card_program_external_id": init_session_card_program_ext_input
        }
        response = ui_api.initiate_session(data)

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response[dataframe_property])
    st.dataframe(df)
else:
    st.json(response)
