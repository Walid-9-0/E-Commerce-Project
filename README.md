# 🧠 Seen E-Commerce: Full Data Science & ML Project Suite

This document includes:

1. 📊 **Full BI Project Overview** – A complete business analysis of Seen E-Commerce using SQL, Power BI, and Streamlit.
2. 🎯 **Sentiment Analysis** – A machine learning model that classifies English reviews into positive or negative sentiment.
3. 🔄 **Return Status Prediction** – A predictive model for classifying return statuses of e-commerce orders.
4. 🌐 Web App and Presentation Access

---

## 📍 Project 1: Seen E-Commerce Full BI Analysis

### 📦 Table of Contents
1. [About the Company](#about-the-company)  
2. [Problem Overview & Stakeholders](#problem-overview--stakeholders)  
3. [Business Objectives](#business-objectives)  
4. [Data Structure & Storage](#data-structure--storage)  
5. [Project Flow & Tools Used](#project-flow--tools-used)  
6. [Executive Summary](#executive-summary)  
7. [Dashboard Insights](#dashboard-insights)  
8. [Recommendations Summary](#recommendations-summary)  

### 🏢 About the Company
Seen is a rapidly growing Egyptian e-commerce business operating for the last three years. With increasing competition and operational complexity, Seen is leveraging data analytics to guide smarter decision-making across sales, logistics, customer experience, and marketing.

### ❓ Problem Overview & Stakeholders
Seen possesses vast amounts of data but lacks a centralized and analytical approach to uncover meaningful, actionable insights for business growth and efficiency.

**Stakeholders:** CEO, Marketing Manager, Product Manager, Supply Chain Lead, Customer Experience Manager

**KPIs:** Total Revenue, Conversion Rate, AOV, Return Rate

### 🎯 Business Objectives
- Improve forecasting and planning
- Segment customers for better targeting
- Optimize stock and product performance
- Minimize avoidable returns
- Improve delivery
- Use sentiment analysis for improvement

### 🧱 Data Structure & Storage
- **Storage**: Azure Blob for raw data, SQL Server for processed views
- **ER Diagram**: [View ER Diagram](https://drive.google.com/uc?export=view&id=1q-tnZfYB3987NqKL1hUVc1lurzDVUQGB)

### 📈 Executive Summary Highlights
- January: highest sales & lowest returns
- BOX & NM: strong performance, no returns
- Devolved Apps: high sales, low stock


🔗 [Live Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjI5Y2ExYjItMjJlYS00MWUyLWFjNTUtYzMwYzY3MjM1YWZjIiwidCI6IjIxNzY5YTc2LTgxZTItNDcyNS1hODkzLWQ0MDQ5YjFhMDRlZSJ9)

### 📊 Dashboard Insights

#### 1. Overview
- January = peak month
- New categories launched
- Focus on cash payment convenience

#### 2. Sales Performance
- BOX & NM regions: top purchases, zero returns
- Suggest loyalty & marketing efforts here

#### 3. Product Performance
- Devolved apps: low stock & high demand
- Automate replenishment

#### 4. Logistics
- Avg delivery = 1 day, 3 reliable partners
- Setup delivery tracking

#### 5. Returns
- Feb highest return value
- Return rate = 1.31%
- Study invoice discounts & returns

#### 6. Customer Insights
- NM region: top revenue
- Run local events, reward referrals

#### 7. Sentiment Analysis
- Avg rating = 3/5, mostly neutral
- Investigate neutral & negative reviews

### ✅ Recommendations Summary
- Replicate January campaigns
- Focus on BOX & NM regions
- Restock key items automatically
- Enhance sentiment tracking via NLP
- Streamline logistics & return processes
---

## 📍 Project 2: Return Status Prediction (E-Commerce Orders)

### 🎯 Objective
Predict the **return status** of an e-commerce order based on structured order features. The return status is classified into one of **four categories**: 0, 1, 2, or 3.

### 🛠️ Project Steps

#### 1. Data Preparation
- Analyze and clean the dataset (handling missing values, encoding categorical variables, etc.).
- Select important features that affect return behavior.

#### 2. Features Used
- `state_code`: Location of the order.
- `carrier`: Shipping company.
- `status`: Order fulfillment status.
- `payment_method`: Payment type used.
- `total_sales`: Total revenue from the order.
- `quantity`: Quantity of items purchased.
- `is_active`: Whether the user is active.
- `percentage`: Discount rate.
- `return_days`: Number of days before a return request.
- `shipping_month`: Month when the order was shipped.

#### 3. Model Training and Evaluation
Train and compare multiple classification models:
- **K-Nearest Neighbors (KNN)**
- **Support Vector Classifier (SVC)**
- **Decision Tree**
- **XGBoost**
- **AdaBoost**

#### ✅ Accuracy
- The best-performing model achieved an accuracy score of **approximately 91%**.

---

## 📍 Project 3: Sentiment Analysis

### 🎯 Objective
Build a machine learning model that classifies English sentences or reviews into either **positive** or **negative** sentiment.

### 🛠️ Project Steps

#### 1. Text Preprocessing
- Convert all text to lowercase.
- Remove punctuation, numbers, and extra whitespaces.
- Remove stopwords.
- Tokenize the text into words.

#### 2. Feature Extraction
- Use **TF-IDF Vectorization** to convert preprocessed text into numerical vectors that capture term importance.

#### 3. Model Training
- Train a **Logistic Regression** model on the TF-IDF features.
- Evaluate the model using accuracy and classification metrics.

#### ✅ Accuracy
- The model achieved an accuracy score of **approximately 88%** on the test data.

---


## 📍 Project 4: 🌐 Web App Access

[Deployment Video](https://drive.google.com/file/d/18i_nAo5uPkrotnc0EaiiidUT6c_43oh9/view?usp=sharing)

[Deployment Link](https://ecommerce-project.streamlit.app/)

[Presentation](https://gamma.app/docs/Seen-9vty7hr3dos1a53)


## 🔁 Project Flow & Tools Used
| Phase               | Tools                   |
|--------------------|--------------------------|
| Data Storage       | Azure, SQL Server        |
| Data Cleaning      | SQL Server Views         |
| Dashboard & Viz    | Power BI                 |
| Sentiment Analysis | Python (NLP)             |
| Return Prediction  | Python                   |
| Deployment         | Streamlit                |

### 👥 Team Members
```
Mohamed Gamal, Amira Hegazy, Shimaa Mohamed, Mohamed Ashraf, Kareem Zaki, Walid AbdElhameed
