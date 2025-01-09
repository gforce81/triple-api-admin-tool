# Importing all the required libraries
import streamlit as st
from api_calls import authentication

st.set_page_config(
    page_title="Triple Authentication",
    page_icon="🔑",
    layout="wide"
)

label_config_file = "Select a configuration file"
label_endpoints_file = "Select an endpoints configuration file"
label_select_env = "Select environment"
label_button = "Generate Token"
environments = ["sandbox", "prod", "dev", "qa"]
token_data = {}

st.markdown(
    """
    ## Configure the environment
    1. Select the Triple platform environment you would like to use (dev, sandbox, prod)
    2. Select the configuration file to use
    3. Click on the button below to generate an OAuth token.
    
    The token is required to exercise all the other API endpoints.
    """
)
st.divider()

uploaded_file_config = st.file_uploader(label_config_file, type=None, accept_multiple_files=False,
                                        key="config_file_input", help=None, on_change=None, args=None, kwargs=None,
                                        disabled=False, label_visibility="visible")
st.write("")

box_environment = st.selectbox(label_select_env, environments, index=0, key="env_list", help=None,
                               on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

st.write("")

st.divider()
response = {}
if st.button(label_button, key="token_button", help=None, on_click=None, args=None, kwargs=None,
             type="primary", disabled=False, use_container_width=False):
    if uploaded_file_config is not None:
        response = authentication.initialize(uploaded_file_config.getvalue(), box_environment)

st.write("")
st.json(response)
