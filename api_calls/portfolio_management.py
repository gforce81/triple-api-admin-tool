# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


config = authentication.config


# create a publisher
def create_publisher(data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['portfolio_createPublishers']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# list publishers
def list_publishers():
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['portfolio_listPublishers']
    response = core_requests.get_request(request_url)
    return response


# get a publisher
def get_card_program(card_program_id):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['cardPrograms_getCardProgram']
    request_url = request_url.replace('{card_program_id}', card_program_id)
    response = core_requests.get_request(request_url)
    return response


# update a publisher
def update_card_program(card_program_id, name, card_bins):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['cardPrograms_updateCardProgram']
    request_url = request_url.replace('{card_program_id}', card_program_id)
    data = {
        "name": name,
        "card_bins": card_bins
    }
    response = core_requests.patch_request(request_url, data)
    return response