# Importing all the required libraries
import json
import requests
import base64

import streamlit

from api_calls import endpoints


config = {}


# Reading & storing the selected configuration files
def read_configuration(configuration_object):
    created_vars = []

    data = json.loads(configuration_object)

    for key, value in data.items():
        globals()[key] = value
        created_vars.append(key)

#    endpoints_data = json.loads(endpoints_object)

#    for key, value in endpoints_data.items():
#        globals()[key] = value
#        created_vars.append(key)

    return created_vars


# Storing main the configuration
def store_config(environment):
    config['client_id'] = globals()['environment'][environment]['client_id']
    config['client_secret'] = globals()['environment'][environment]['client_secret']
    config['base_url'] = endpoints.endpoints['base_urls'][environment]['base_url']
    config['ui_url'] = endpoints.endpoints['base_urls'][environment]['ui_base_url']
    config['auth_url'] = endpoints.endpoints['base_urls'][environment]['auth_url']
    config['cardAccounts_listCardAccounts'] = endpoints.endpoints['card_accounts']['GET_listCardAccounts']
    config['cardAccounts_getCardAccount'] = endpoints.endpoints['card_accounts']['GET_getCardAccount']
    config['cardAccounts_getCardAccountExternal'] = endpoints.endpoints['card_accounts']['POST_getCardAccountExternal']
    config['cardAccounts_createCardAccount'] = endpoints.endpoints['card_accounts']['POST_createCardAccount']
    config['cardAccounts_updateCardAccount'] = endpoints.endpoints['card_accounts']['PATCH_updateCardAccount']
    config['cardPrograms_listCardPrograms'] = endpoints.endpoints['card_programs']['GET_listCardPrograms']
    config['cardPrograms_getCardProgram'] = endpoints.endpoints['card_programs']['GET_getCardProgram']
    config['cardPrograms_createCardProgram'] = endpoints.endpoints['card_programs']['POST_createCardProgram']
    config['cardPrograms_updateCardProgram'] = endpoints.endpoints['card_programs']['PATCH_updateCardProgram']
    config['offer_display_searchOffers'] = endpoints.endpoints['offer_display']['POST_searchOffers']
    config['offer_display_getOffersRecommendations'] = endpoints.endpoints['offer_display']['POST_getOffersRecommendations']
    config['offer_display_offersCategories'] = endpoints.endpoints['offer_display']['GET_offersCategories']
    config['offer_display_offersDetailsByCardholder'] = endpoints.endpoints['offer_display']['GET_offersDetailsByCardholder']
    config['offer_display_offersDetails'] = endpoints.endpoints['offer_display']['GET_offersDetails']
    config['offer_display_activedOffers'] = endpoints.endpoints['offer_display']['GET_activedOffers']
    config['offer_activation_activate_offer'] = endpoints.endpoints['offer_activation']['PUT_activateOffer']
    config['transactions_getListTransactions'] = endpoints.endpoints['transactions']['GET_listTransactions']
    config['transactions_getTransaction'] = endpoints.endpoints['transactions']['GET_getTransaction']
    config['transactions_createTransaction'] = endpoints.endpoints['transactions']['POST_createTransaction']
    config['providers_listMerchants'] = endpoints.endpoints['offer_providers']['GET_listMerchants']
    config['providers_createMerchants'] = endpoints.endpoints['offer_providers']['POST_createMerchant']
    config['providers_updateMerchants'] = endpoints.endpoints['offer_providers']['PATCH_updateMerchant']
    config['providers_getMerchants'] = endpoints.endpoints['offer_providers']['GET_getMerchant']
    config['providers_listMerchantsLocations'] = endpoints.endpoints['offer_providers']['GET_listMerchantLocations']
    config['providers_createMerchantsLocations'] = endpoints.endpoints['offer_providers']['POST_createMerchantLocation']
    config['providers_listOffers'] = endpoints.endpoints['offer_providers']['GET_listOffers']
    config['providers_createOffers'] = endpoints.endpoints['offer_providers']['POST_createOffers']
    config['providers_updateOffers'] = endpoints.endpoints['offer_providers']['PATCH_updateOffers']
    config['ui_initiate'] = endpoints.endpoints['ui-api']['POST_initiateSession']
    config['ui_offersHome'] = endpoints.endpoints['ui-api']['POST_offersHome']


# Creating a Triple Auth Token
def create_auth_token():
    grant_type = "client_credentials"

    # authorization key must be base64 encoded and concatenate triple_id:triple_secret

    byte_key = config['client_id'] + ":" + config['client_secret']
    byte_key = byte_key.encode("ascii")
    triple_authorization_key = base64.b64encode(byte_key)
    triple_authorization_key = triple_authorization_key.decode("ascii")

    # print(triple_authorization_key)
    # print(config['auth_url'])

    r = requests.post(
        config['auth_url'],
        data={"grant_type": grant_type},
        headers={"Authorization": "Basic " + triple_authorization_key,
                 "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    )

    response = r.json()
    # print(response["access_token"]
    return response["access_token"]


# Initializing (reading config, storing main config, getting auth token)
def initialize(configuration, environment):
    created_vars = read_configuration(configuration)
    store_config(environment)
    config['auth_token'] = create_auth_token()
    streamlit.session_state['config'] = config
    # print("NOW PRINTING THE SESSION STATE")
    # print(streamlit.session_state.config)
    response = {"token": config['auth_token']}
    return response

