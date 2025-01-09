# Importing all the required libraries
import streamlit as st
import pandas as pd
from pandas import json_normalize
from api_calls import card_programs

st.set_page_config(
    page_title="Card Programs APIs ",
    page_icon="📂",
    layout="wide"
)

st.markdown(
    """
    ## Select the Card Program Operation
    - List all card programs for the authenticated Triple account
    - Get the details for a specific card program using a triple_id
    - Create a new card program
    - Update an existing card program
    """
)
st.divider()

response = {}
label_select_cardProgramOperation = ""
view_as_dataframe = False

with st.expander("List Card Programs", expanded=False):
    df_view = st.radio("View as Dataframe", ["Yes", "No"])
    if st.button("Display", key="list_card_programs_button", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        if df_view == "Yes":
            view_as_dataframe = True
        response = card_programs.list_card_programs()

with st.expander("Get a Card Program", expanded=False):
    cardProgram_getBox = st.text_input("Card Program ID", key="get_card_program_box")
    if st.button("Display", key="get_card_program_button"):
        response = card_programs.get_card_program(cardProgram_getBox)


with st.expander("Create Card Program", expanded=False):
    with st.form("Create Card Program"):
        card_bins_input = st.text_input("Card Program BINs", placeholder="123456,789012")
        default_country_code_input = st.text_input("Default Country Code", placeholder="US")
        default_postal_code_input = st.text_input("Default Postal Code", placeholder="90210")
        external_id_input = st.text_input("External ID", placeholder="external ID as string")
        name_input = st.text_input("Name", placeholder="display name as string")
        description_input = st.text_input("Description", placeholder="program description as string")
        program_currency_input = st.text_input("Currency", placeholder="USD")
        loyalty_unit_input = st.text_input("Loyalty Unit [optional]", placeholder="MILES or POINTS")
        loyalty_conversion_input = st.text_input("Loyalty Conversion Rate [optional]", placeholder="0")
        publisher_external_id_input = st.text_input("Publisher External ID [optional]", placeholder="publisher_external_id")
        hosted_ui_subdomain_input = st.text_input("Hosted UI Subdomain [optional]", placeholder="hosted_ui_subdomain")
        create_program_button = st.form_submit_button("Create")
    if create_program_button:
        try:
            converted_loyalty_rate = float(loyalty_conversion_input)
        except Exception as e:
            converted_loyalty_rate = None

        if loyalty_unit_input not in ['POINTS', 'MILES']:
            loyalty_unit_input = None

        if len(publisher_external_id_input) > 0:
            publisher = publisher_external_id_input
        else:
            publisher = None

        data = {
            "card_bins": card_bins_input.split(","),
            "default_country_code": default_country_code_input,
            "default_postal_code": default_postal_code_input,
            "external_id": external_id_input,
            "name": name_input,
            "description": description_input,
            "program_currency": program_currency_input,
            "loyalty_unit": loyalty_unit_input,
            "loyalty_conversion_rate": converted_loyalty_rate,
            "publisher_external_id": publisher,
            "hosted_ui_subdomain": hosted_ui_subdomain_input
        }
        response = card_programs.create_card_program(data)

with st.expander("Update a Card Program", expanded=False):
    cardProgram_patchBoxID = st.text_input("Card Program ID", key="patch_card_program_box")
    cardProgram_patchBoxName = st.text_input("Card Program Name", key="patch_card_program_name_box")
    cardProgram_patchBoxBins = st.text_input("Card Program BINs", key="patch_card_program_bins_box",
                                             placeholder="""123456, 678901""")
    if st.button("Update", key="update_card_programs_button", help=None, on_click=None, args=None,
                 kwargs=None, type="primary", disabled=False, use_container_width=False):
        response = card_programs.update_card_program(cardProgram_patchBoxID, cardProgram_patchBoxName,
                                                     cardProgram_patchBoxBins.split(","))

st.write("")
if view_as_dataframe:
    df = pd.json_normalize(response['card_programs'])
    st.dataframe(df)
else:
    st.json(response)
