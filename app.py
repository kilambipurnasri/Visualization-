
import streamlit as st
import pandas as pd

st.title("📈 Simple Line Chart Visualizer")

# 1️⃣ Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # 2️⃣ Read the CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # 3️⃣ Let user choose columns for X and Y
    numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
    if len(numeric_cols) < 1:
        st.error("No numeric columns found for plotting.")
    else:
        x_axis = st.selectbox("Select column for X-axis", df.columns)
        y_axis = st.selectbox("Select numeric column for Y-axis", numeric_cols)

        # 4️⃣ Plot line chart
        st.subheader("Line Chart")
        st.line_chart(df.set_index(x_axis)[y_axis])
else:
    st.info("Please upload a CSV file to begin.")
  
