# Importing all the required libraries
import requests
import streamlit
from api_calls import authentication


config = authentication.config


# default POST REQUEST
def post_request(request_url, data):
    r = requests.post(
        request_url,
        headers={"Authorization": "Bearer " + streamlit.session_state.config['auth_token'], "Content-Type": "application/json"},
        json=data
    )
    response = r.json()
    return response


# default GET REQUEST
def get_request(request_url):
    r = requests.get(
        request_url,
        headers={"Authorization": "Bearer " + streamlit.session_state.config['auth_token']}
    )
    response = r.json()
    return response


# default PATCH request
def patch_request(request_url, data):
    r = requests.patch(
        request_url,
        headers={"Authorization": "Bearer " + streamlit.session_state.config['auth_token'], "Content-Type": "application/json"},
        json=data
    )
    response = r.json()
    return response


# default DEL request
def del_request(request_url):
    r = requests.post(
        request_url,
        headers={"Authorization": "Bearer " + streamlit.session_state.config['auth_token']},
    )
    response = r.json()
    return response


# default PUT request
def put_request(request_url):
    r = requests.put(
        request_url,
        headers={"Authorization": "Bearer " + streamlit.session_state.config['auth_token']},
    )
    response = r.json()
    return response
