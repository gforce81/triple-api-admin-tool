# Importing all the required libraries
import streamlit
from urllib.parse import urlencode
from api_calls import core_requests


# offers.search
def constuct_url(base_url, params):
    valid_params = {k: v for k, v in params.items() if v is not None and v != ""}
    query_string = urlencode(valid_params)
    if query_string:
        return f"{base_url}?{query_string}"


def get_list_transactions(data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['transactions_getListTransactions'])
    url = constuct_url(request_url, data)

    response = core_requests.get_request(url)
    return response


def get_transaction(data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['transactions_getTransaction'])
    print(request_url)

    request_url = request_url.replace('{transaction_id}', data)

    response = core_requests.get_request(request_url)
    return response


def create_transaction(data):
    request_url = (streamlit.session_state.config['base_url'] +
                   streamlit.session_state.config['transactions_createTransaction'])

    response = core_requests.post_request(request_url, data)
    return response

