import streamlit as st
import pandas as pd

# Sample data
data = {'Product': ["A", "B", "C"],
        'Sales' : [1200,850,950],
        'Customers' : [300, 400, 350]}
df = pd.DataFrame(data)

# Show data with Streamlit Elements

st.dataframe(df)          # Interactive Table  
st.data_editor(df)        # Editable Table 
st.table(df)              # Static Table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers' : '${:,.0f}'}))


