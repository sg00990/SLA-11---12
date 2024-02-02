import streamlit as st 

st.set_page_config(
    page_title="Tier 2 SLA Questionnaire",
    page_icon="💻",
    layout="wide"
)

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


st.write("**Date**")
survey_date = st.date_input("survey_date", format="MM/DD/YYYY", label_visibility="collapsed")
st.write("**Additional Comments**")
survey_text = st.text_area("survey_text", label_visibility="collapsed")

col1, col2, col3 = st.columns(3)

with col3:
    if st.button("Submit", use_container_width=True):
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


