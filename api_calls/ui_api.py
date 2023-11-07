# Importing all the required libraries
import streamlit
from api_calls import authentication
from api_calls import core_requests


def initiate_session(data):
    request_url = streamlit.session_state.config['ui_url'] + streamlit.session_state.config['ui_initiate']
    data = data
    response = core_requests.post_request(request_url, data)
    return response

