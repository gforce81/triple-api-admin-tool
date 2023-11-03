# Importing all the required libraries
import streamlit
from api_calls import core_requests


def put_offer_activation(cardholder_id, offer_id):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['offer_activation_activate_offer'])
    request_url = request_url.replace('{cardholder_id}', cardholder_id)
    request_url = request_url.replace('{offer_id}', offer_id)
    print(request_url)
    response = core_requests.put_request(request_url)
    return response

