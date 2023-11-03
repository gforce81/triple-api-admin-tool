# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


# offers.search
def offers_search(cardholder_id, data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_searchOffers'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    data = data
    print("OFFER SEARCH")
    print(data)
    response = core_requests.post_request(request_url, data)
    return response


# offers.recommendations
def offers_recommendations(cardholder_id, data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_getOffersRecommendations'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    data = data
    response = core_requests.post_request(request_url, data)
    return response


# get offers categories
def get_offers_categories(cardholder_id):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_offersCategories'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    response = core_requests.get_request(request_url)
    return response


# get offers details with carholder_id
def get_offers_details_by_cardholder(cardholder_id, data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_offersDetailsByCardholder'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    response = core_requests.post_request(request_url, data)
    return response


# get offers details without carholder_id
def get_offers_details(offer_id):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_offersDetails'])
    request_url = request_url.replace('{offer_id}', offer_id)
    print("OFFER DETAILS")
    print(request_url)
    response = core_requests.get_request(request_url)
    return response


# get offers activated
def get_offers_activated(cardholder_id, data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_display_activedOffers'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    response = core_requests.post_request(request_url, data)
    return response
