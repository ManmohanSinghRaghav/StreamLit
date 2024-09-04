import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("customers.csv")
# st.line_chart(df[["Index", "Customer_id", "First_name", "Last_name", "Email"]])
columns = st.multiselect("Select columns to display", df.columns)

# Display selected columns
if columns:
    st.write("Selected Columns:", df[columns])