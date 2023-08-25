import numpy as numpy
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/computer/OneDrive/Desktop/trained_model.sav",'rb'))
def churn_pred(input_data):
    as_numpy=np.asarray(input_data)
    as_reshape=as_numpy.reshape(1,-1)
    prediction=model.predict(as_reshape)
    print(prediction)
    if(prediction[0]==0):
       print("No customer churn")
    else:
        print("Customer churn")
def main():
    st.title("Customer Churn Prediction Web App")
    Age=st.text_input("Enter the age")
    Gender=st.text_input("Enter your gender(Male:0 and Female:1)")
    Location=st.text_input("Enter your location(Los Angeles:0,New York:1,Miami:2,Houston:3,Chicago:4)")
    Subscription_Length_Months=st.text_input("Enter the month")
    Monthly_Bill=st.text_input("Enter the monthly bill")
    Total_Usage_GB=st.text_input("Enter the usagein GB")
    find_churn=''
    if st.button("Find the churn"):
        find_churn=churn_pred([Age,Gender,Location,Subscription_Length_Months,Monthly_Bill])
    st.success(find_churn)
if __name__=='__main__':
    main()
