# Importing all the required libraries
import streamlit as st
from api_calls import offers_activation


st.set_page_config(
    page_title="Offers Display APIs ",
    page_icon="🚀",
    layout="wide"
)

st.markdown(
    """
    ## Select the Offers Activation Operation
    - Activate an offer by offer_id
    """
)
st.divider()

response = {}

with st.expander("Activate an Offer by ID", expanded=False):
    with st.form("Activate an Offer by ID"):
        card_account_input = st.text_input("Card Account ID", placeholder="the card account ID")
        offer_id_input = st.text_input("Offer ID", placeholder="the offer ID")
        put_activate_offers_button = st.form_submit_button("Activate")
    if put_activate_offers_button:
        response = offers_activation.put_offer_activation(card_account_input, offer_id_input)

st.write("")
st.json(response)

