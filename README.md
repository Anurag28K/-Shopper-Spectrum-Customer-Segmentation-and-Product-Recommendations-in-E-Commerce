# 🛒 Shopper Spectrum: Customer Segmentation and Product Recommendation System

## Overview

Shopper Spectrum is an end-to-end E-Commerce Analytics project designed to analyze customer purchasing behavior and deliver personalized product recommendations. By leveraging transaction data, the project identifies meaningful customer segments through RFM (Recency, Frequency, Monetary) analysis and applies machine learning techniques to generate relevant product recommendations.

The solution enables businesses to gain actionable insights into customer behavior, improve marketing effectiveness, enhance customer retention strategies, and create personalized shopping experiences.

---

## Objectives

* Analyze customer purchasing patterns using transactional data.
* Segment customers into meaningful groups based on RFM metrics.
* Identify high-value, regular, occasional, and at-risk customers.
* Develop an item-based recommendation engine using collaborative filtering.
* Provide real-time customer segmentation and product recommendations through an interactive Streamlit application.

---

## Key Features

### Customer Segmentation

* RFM (Recency, Frequency, Monetary) Analysis
* Customer Behavior Profiling
* KMeans Clustering
* Cluster Evaluation using Elbow Method and Silhouette Score
* Business-Oriented Customer Segments

### Product Recommendation System

* Item-Based Collaborative Filtering
* Cosine Similarity Analysis
* Top-N Product Recommendations
* Personalized Product Discovery

### Interactive Web Application

* Real-Time Product Recommendations
* Customer Segment Prediction
* User-Friendly Streamlit Interface

---

## Technology Stack

* **Programming Language:** Python
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn
* **Clustering Algorithm:** KMeans
* **Recommendation Engine:** Cosine Similarity
* **Model Serialization:** Joblib
* **Web Application:** Streamlit

---

## Project Workflow

1. Data Collection and Understanding
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. RFM Feature Engineering
5. Customer Segmentation using KMeans Clustering
6. Cluster Evaluation and Interpretation
7. Product Recommendation System Development
8. Model Saving and Deployment
9. Streamlit Application Development

---

## Business Applications

* Customer Segmentation for Targeted Marketing
* Personalized Product Recommendations
* Customer Retention and Re-engagement Strategies
* Sales and Revenue Optimization
* Inventory Planning and Demand Forecasting
* Customer Lifetime Value Analysis

---

## Project Structure

```text
CustomerSegmentationProject/

├── app.py
├── customer_segmentation_model.pkl
├── rfm_scaler.pkl
├── product_similarity.pkl
├── online_retail.csv
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

## Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Streamlit Application

```bash
streamlit run app.py
```

---

## Results

* Successfully segmented customers based on purchasing behavior using RFM analysis and KMeans Clustering.
* Developed an item-based recommendation system capable of generating relevant product suggestions.
* Built a fully functional Streamlit application for real-time customer segmentation and product recommendations.
* Delivered actionable business insights to support customer engagement and decision-making.

---

## Conclusion

This project demonstrates the practical application of machine learning in the e-commerce domain by combining customer segmentation and recommendation systems into a single solution. The developed framework helps organizations better understand customer behavior, improve personalization, and support data-driven business strategies.

---

## Author

**Anurag Ram**

Artificial Intelligence & Machine Learning Enthusiast
