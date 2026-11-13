import streamlit as st
import pandas as pd
DATA = "data/heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(DATA)
st.title("데이터")
st.dataframe(df, width="stretch")

