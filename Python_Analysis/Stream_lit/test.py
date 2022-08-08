import streamlit as st

# text and title
st.title("Stream Tutorial")
st.header('Data Analysis')
st.success('Success')
st.info('Information')
location = [i for i in range(1, 10)]
location_2 = st.multiselect("Where do you work", location)
st.write('Numbers selected:', len(location_2))
#st.balloons()
st.sidebar.header('About')
