import streamlit as st
import json

with open('NatGeo Story Performance Analyzer .json', 'r') as f:
    data = json.load(f)

st.write(data)
