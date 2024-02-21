import streamlit as st 
import datetime
import json

st.set_page_config(
    page_title="SLA 11 & 12 Questionnaire",
    page_icon="💻",
    layout="wide"
)

conn = st.connection("snowflake")

st.markdown('<p style="font-family:sans-serif; color:#324a62; font-size: 28px; font-weight: bold">Tier 2 SLA Questionnaire</p>', unsafe_allow_html=True)
st.write("###")

st.markdown('<p style="font-family:sans-serif; color:#87c440; font-size: 20px; font-weight: bold">SLA 11 & 12</p>', unsafe_allow_html=True)

st.write("**Agenda Date**")
agenda_date = st.date_input(
    "agenda_date",
    format="MM/DD/YYYY",
    label_visibility="collapsed"
)

st.write("**Minutes Date**")
minutes_date = st.date_input(
    "minutes_date",
    format="MM/DD/YYYY",
    label_visibility="collapsed"
)


st.write("**Additional Comments**")
survey_text = st.text_area("survey_text", label_visibility="collapsed")
survey_text = survey_text.replace("\n", "  ").replace("'", "''").replace('"', r'\"')

col1, col2, col3 = st.columns(3)

with col3:
    if st.button("Submit", use_container_width=True):
        data = {
            "sla_11_12_agenda_date": agenda_date,
            "sla_11_12_minutes_date": minutes_date,
            "sla_11_12_comments": survey_text
        }

        json_data = json.dumps(data, indent=4, sort_keys=True, default=str)

        date_submitted = datetime.datetime.now()

        try:
            conn.query(f""" INSERT INTO sla_tier_2_questionnaire (type, date_submitted, json_data) SELECT 'SLA 11 & 12', '{date_submitted}', (parse_json('{json_data}'))""")
        except:
            st.success("Thank you for your responses!")


col4, col5, col6 = st.columns([1, .5, 1])

with col4:
    st.write("##")
    st.image("img/blue_bar.png")
    
with col5:
    col17, col18, col19 = st.columns(3)
    with col18:
        st.write("######")
        st.image("img/moser_logo.png")
with col6:
    st.write("##")
    st.image("img/blue_bar.png")



