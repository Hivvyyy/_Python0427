
#使累計計數
#利用session_state的寫法


import streamlit as st

st.title("COUNTER")
if "count" not in st.session_state:
    st.session_state.count = 0


#利用session_state的寫法
increment = st.button("Increment",key="Increment")
st.session_state
if increment:
    st.session_state.count += 1


st.write("Count=", st.session_state.count)