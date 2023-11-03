import streamlit as st
from streamlit.web import cli as stcli

st.set_page_config(
    page_title="Triple API Home",
    page_icon="🖥️",
)

st.write("# Welcome to Triple API's Testing Tool! 👋")

st.sidebar.success("Select an API call above.")

st.markdown(
    """
Triple is a Platform that enables Financial Institutions to provide a large catalog of merchant-funded card incentives 
to their customers. This guide aims to assist you in using the Triple API, which provides the necessary endpoints for 
interacting with the platform.  

Triple's content partners consist of established networks of offer providers, merchants/retailers, and loyalty programs.
Thanks to its relationships with numerous popular aggregation networks and individual merchants, Triple efficiently 
connects publishers and their cardholders with a large and constantly updated set of offers.

As a developer, you can utilize Triple's API to create engaging user experiences with the most relevant offers and 
incentives.

"""
)
