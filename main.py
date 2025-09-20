from multi_table import print_multi_table
import pandas as pd
import streamlit as st

data = pd.read_csv("product.csv")
print(data)

st.title("Dashboard")
st.write("This App is about displaying product sales")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sales","1,200","12%")
with col2:
    st.metric("Revenue","$3B","20%")
with col3:
    st.metric("Users","1.2B",'50%')
    
name = st.text_input("name")
st.write(name)


st.line_chart(data['sales'])

if st.button("show table"):
    st.header("Sales Table")
    st.subheader("This is a sales table")
    st.write(data)

