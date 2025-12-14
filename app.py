import streamlit as st
import json

with open('maincode', 'r') as f:
    data = json.load(f)

st.write(data)
