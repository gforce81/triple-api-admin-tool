# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


def initiate_session(data):
    request_url = streamlit.session_state.config['ui_url'] + streamlit.session_state.config['ui_initiate']
    data = data
    response = core_requests.post_request(request_url, data)
    return response


def offers_home(data):
    request_url_token = streamlit.session_state.config['ui_url'] + streamlit.session_state.config['ui_initiate']
    request_url_offers_home = streamlit.session_state.config['ui_url'] + streamlit.session_state.config['ui_offersHome']
    token_data = {
        "card_account_id": data['card_account_id']
    }

    try:
        offers_data = {
                "proximity_target": {
                    "country_code": data['country_code'],
                    "latitude": data['latitude'],
                    "longitude": data['longitude'],
                    "postal_code": data['postal_code'],
                    "radius": data['radius']
                },
                "sections": data['sections']
        }
    except Exception as e:
        offers_data = {
            "proximity_target": {
                "country_code": data['country_code'],
                "postal_code": data['postal_code'],
                "radius": data['radius']
            },
            "sections": data['sections']
        }
        print(e)

    response_token = core_requests.post_request(request_url_token, token_data)
    response_token = response_token['token']

    response_offers_home = core_requests.post_request_ui(request_url_offers_home, offers_data, response_token)

    return response_offers_home
