# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:18:41 2023

@author: admin
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json
import math
import base64

result = None


final_model = pickle.load(open('model.pkl', 'rb'))


def main():
    global result
    html_temp= """
    
        <div style="background-color:#130F49;padding:10px">
        <h2 style="color:white;margin-left:10rem;">Heart Failure Prediction</h2>
        </div>
       
        """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.markdown(
       
        """
        Fill this details to check your Heart Failure Prediction . 
    """
    )
    #['time','ejection_fraction','serum_creatinine','high_blood_pressure','serum_sodium']

    high_blood_pressure=float(st.number_input("High Blood Pressure (yes=1 or No=0)"))    
    time=int(st.number_input("Time (days)"))
    serum_creatinine=float(st.number_input("Serum Creatinine (mg/dL)"))
    serum_sodium=float(st.number_input("Serum Sodium (mEq/L)"))
    ejection_fraction=float(st.number_input("Ejection Fraction (percentage)"))      
    diabetes = float(st.number_input("Diabetes (yes=1 or No=0)"))

    if st.button("Predict"):
        pred = (final_model.predict(np.array([[high_blood_pressure,time,serum_creatinine,serum_sodium,ejection_fraction,diabetes]])))
        x=pred[0]
        if x==0:
            result="The Patient Survived "
        elif x==1:
            result="The Patient Not Survived"
        else:
            result="model can't predict the status"
        st.success('Output :  {}'.format(result))

    #st.success(f"Price = {result}")


if __name__ == "__main__":
    main()