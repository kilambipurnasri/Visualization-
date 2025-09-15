import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔻 Funnel Chart Visualizer")

# 1️⃣ Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # 2️⃣ Read the CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # 3️⃣ Choose columns
    cols = df.columns.tolist()
    stage_col = st.selectbox("Select column for Funnel Stages", cols)
    value_col = st.selectbox("Select numeric column for Values", df.select_dtypes(include=['int','float']).columns)

    # 4️⃣ Plot funnel chart
    st.subheader("Funnel Chart")
    fig = px.funnel(df, x=value_col, y=stage_col)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload a CSV file to visualize.")
