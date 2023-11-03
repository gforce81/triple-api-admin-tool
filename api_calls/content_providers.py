# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


config = authentication.config


# create a merchant
def create_merchant(data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_createMerchants']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# list merchants
def list_merchants():
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_listMerchants']
    response = core_requests.get_request(request_url)
    return response


# get a merchant
def get_merchant(merchant_id):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_getMerchants']
    request_url = request_url.replace('{merchant_id}', merchant_id)
    response = core_requests.get_request(request_url)
    return response


# update a merchant
def update_merchant(merchant_id, data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_updateMerchants']
    request_url = request_url.replace('{merchant_id}', merchant_id)
    data = data
    response = core_requests.patch_request(request_url, data)
    return response


def create_offer(data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_createOffers']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# list offers
def list_offers():
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_listOffers']
    response = core_requests.get_request(request_url)
    return response


# create a location
def create_location(data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_createMerchantsLocations']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# list locations
def list_locations():
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['providers_listMerchantsLocations']
    response = core_requests.get_request(request_url)
    return response





# update a card program
def update_card_program(card_program_id, name, card_bins):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['cardPrograms_updateCardProgram']
    request_url = request_url.replace('{card_program_id}', card_program_id)
    data = {
        "name": name,
        "card_bins": card_bins
    }
    response = core_requests.patch_request(request_url, data)
    return response

