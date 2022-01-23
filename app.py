import streamlit as st
import pandas as pd 
st.title("Financial Management System")
dataset = pd.read_csv("AIML Dataset.csv")

nav = st.sidebar.selectbox("Navigate",["Account","Data Details","About"])

if nav == "Account":
    tr_id = st.text_input("Transaction ID")
    # st.button("Predict")
    if st.button("Predict"):
        pass    


if nav == "Data Details":
    st.write("## Data Exploration Details")
    st.text("")
    st.image("pic1.png")
    st.text("")
    st.write("Most of the Transactions are carried out by Payment and Cash Out Types")
    st.text("")
    st.text("")
    st.image("pic2.png")
    st.text("")
    st.write("Fraud: 8213")
    st.text("")
    st.write("Non-Fraud: 6354407")
    st.text("")
    st.text("")
    st.image("pic3.png")
    st.text("")
    st.write("The number of fraudulent TRANSFERs = 4097")
    st.text("")
    st.write("The number of fraudulent CASH_OUTs = 4116")
    st.text("")
    st.write("Therefore only CASH-OUT and TRANSFER transactions can be fraudulent.")
    st.text("")
    st.write("Also there is an almost equal likelihood that a fraudulent transaction can be CASH_OUT or TRANSFER.")



if nav == "About":
    st.write("Unscript-Rookies-Hackathon....")
    st.