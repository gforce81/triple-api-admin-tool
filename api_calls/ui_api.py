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

############


def test_amplifi(token):
    list_of_urls = [
        "https://1stmidamerica-cu.rewards.tripleup.dev",
        "https://affinityplus-fcu.rewards.tripleup.dev",
        "https://americu-business.rewards.tripleup.dev",
        "https://americu.rewards.tripleup.dev",
        "https://bank-fund-staff-fcu.rewards.tripleup.dev",
        "https://arlington-community-fcu.rewards.tripleup.dev",
        "https://bluestone-fcu.rewards.tripleup.dev",
        "https://brightview-cu.rewards.tripleup.dev",
        "https://credit-union-colorado.rewards.tripleup.dev",
        "https://eastman-cu-cash.rewards.tripleup.dev",
        "https://eastman-cu-rwd2.rewards.tripleup.dev",
        "https://eastman-cu-rwds.rewards.tripleup.dev",
        "https://texas-community-fcu.rewards.tripleup.dev",
        "https://sf-fire-cu.rewards.tripleup.dev",
        "https://sanmateo-cu.rewards.tripleup.dev",
        "https://redstone-fcu-consu.rewards.tripleup.dev",
        "https://redstone-fcu-business.rewards.tripleup.dev",
        "https://pacific-horizon-cu.rewards.tripleup.dev",
        "https://midamerican-cu.rewards.tripleup.dev",
        "https://langley-fcu.rewards.tripleup.dev",
        "https://idaho-central-cu.rewards.tripleup.dev",
        "https://gsb.rewards.tripleup.dev",
        "https://firstbank.rewards.tripleup.dev",
        "https://faa-fcu.rewards.tripleup.dev",
        "https://truwest-tsig-cu.rewards.tripleup.dev",
        "https://truwest-twst-cu.rewards.tripleup.dev",
        "https://we-cu.rewards.tripleup.dev",
        "https://wescom-ucla.rewards.tripleup.dev",
        "https://wescom.rewards.tripleup.dev",
    ]
    list_of_urls_with_token = []

    for url in list_of_urls:
        new_url = url + "?token=" + token
        list_of_urls_with_token.append(new_url)

    return {"urls": list_of_urls_with_token}
