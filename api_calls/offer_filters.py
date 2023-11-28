# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


config = authentication.config


# create a filter
def create_offer_filters(data):
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['filters_createOfferFilters']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# list filters
def list_offer_filters():
    request_url = streamlit.session_state.config['base_url'] + streamlit.session_state.config['filters_listOfferFilters']
    response = core_requests.get_request(request_url)
    return response


# patch a filter
def patch_offer_filters(filter_id, data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['filters_patchOfferFilters'])
    request_url = request_url.replace('{filter_id}', filter_id)
    data = data
    response = core_requests.patch_request(request_url, data)
    return response
