# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


config = authentication.config


def list_card_accounts():
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['cardAccounts_listCardAccounts'])
    response = core_requests.get_request(request_url)
    return response


# get a card account internal
def get_card_account(card_holder_id):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['cardAccounts_getCardAccount'])
    request_url = request_url.replace('{cardholder_id}', card_holder_id)
    response = core_requests.get_request(request_url)
    return response


# get a card account external
def get_card_account_external(card_holder_external_id):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['cardAccounts_getCardAccountExternal'])
    data = {
        "card_account_external_id": card_holder_external_id
    }
    response = core_requests.post_request(request_url, data)
    return response


# create a card account
def create_card_account(data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['cardAccounts_createCardAccount'])
    response = core_requests.post_request(request_url, data)
    return response


# update a card account
def update_card_account(card_holder_id, status):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['cardAccounts_updateCardAccount'])
    request_url = request_url.replace('{cardholder_id}', card_holder_id)
    data = {
        "status": status
    }
    response = core_requests.patch_request(request_url, data)
    return response
