import streamlit as st
import pandas as pd
import joblib

# Load Models

kmeans = joblib.load("customer_segmentation_model.pkl")
scaler = joblib.load("rfm_scaler.pkl")
similarity_df = joblib.load("product_similarity.pkl")

# Title

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Product Recommendation",
        "Customer Segmentation"
    ]
)



# -------------------------------------------------
# Product Recommendation
# -------------------------------------------------

if menu == "Product Recommendation":

    st.header("🎯 Product Recommendation System")

    product_name = st.text_input(
        "Enter Product Name"
    )

    if st.button("Get Recommendations"):

        if product_name in similarity_df.index:

            recommendations = (
                similarity_df[product_name]
                .sort_values(ascending=False)
                .drop(product_name)
                .head(5)
            )

            st.success("Top 5 Recommendations")

            for product in recommendations.index:
                st.write("✅", product)

        else:
            st.error("Product Not Found")


# -------------------------------------------------
# Customer Segmentation
# -------------------------------------------------

elif menu == "Customer Segmentation":

    st.header("📊 Customer Segmentation")

    recency = st.number_input(
        "Recency",
        min_value=0
    )

    frequency = st.number_input(
        "Frequency",
        min_value=0
    )

    monetary = st.number_input(
        "Monetary",
        min_value=0.0
    )

    if st.button("Predict Cluster"):

        data = pd.DataFrame(
            [[recency, frequency, monetary]],
            columns=[
                "Recency",
                "Frequency",
                "Monetary"
            ]
        )

        scaled_data = scaler.transform(data)

        cluster = kmeans.predict(
            scaled_data
        )[0]

        cluster_labels = {
            0: "High-Value",
            1: "Regular",
            2: "Occasional",
            3: "At-Risk"
        }

        st.success(
            f"Customer Segment: {cluster_labels.get(cluster,'Unknown')}"
        )