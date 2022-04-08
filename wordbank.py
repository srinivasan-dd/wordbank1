#importing the ibraries
from operator import index
import pandas as pd
import numpy as np
import altair as at
import streamlit as st
#decaring the title
st.title('word bank data of - india')
#read csv fie
india=pd.read_csv('World_Bank_India.csv',skiprows=4)
st.write(india)
st.write(india.index)