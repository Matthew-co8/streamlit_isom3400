st.title("Retail Business Dashboard")

st.header("Manager Input Section")
st.write("Please enter the monthly stage target and select the region.")

st.number_input("Enter the Monthly Sales Target (in USD)", min_value = 0, value = 50000)

st.selectbox("Select Region:",["North", "South", "East", "West"])

if st.button("Submit"):
    st.success("Form Submitted Successfully!")
