# Airbnb Price Prediction Case Study: Berlin, Istanbul & Munich

## Project Overview

This project is a comprehensive machine learning case study aimed at predicting Airbnb rental prices in three major European cities: Berlin, Istanbul, and Munich. The primary goal was to explore the factors influencing pricing in different markets and to develop a highly accurate predictive model through an iterative and rigorous data science workflow.

The entire project demonstrates the full lifecycle of a machine learning initiative, from initial data cleaning and exploratory analysis to advanced model development and final performance evaluation.

## Table of Contents

-   [Project Goal](#project-goal)
-   [Methodology](#methodology)
-   [Project Structure](#project-structure)
-   [Key Findings & Final Results](#key-findings--final-results)
-   [Future Work](#future-work)
-   [Technologies Used](#technologies-used)

## Project Goal

The main objective was to build a machine learning model capable of accurately predicting the price of Airbnb listings. I aimed to not only achieve high predictive performance but also to gain insights into which features drive pricing in diverse urban environments.

## Methodology

My approach was an iterative process of model refinement:

1.  **Data Collection & Cleaning:** I started with raw, publicly available Airbnb data for three cities. The data was cleaned to handle missing values, correct data types, and prepare it for analysis.
2.  **Exploratory Data Analysis (EDA):** I performed a detailed analysis to understand data distributions, identify key features, and uncover initial correlations between features and price.
3.  **Model Iterations:**
    -   **V1: Baseline Model:** A simple Linear Regression model was implemented to establish a performance baseline.
    -   **V2: Random Forest:** A more powerful Random Forest model was trained to improve upon the baseline.
    -   **V3: Optimized Random Forest:** I performed hyperparameter tuning to optimize the Random Forest model for peak performance.
    -   **Final Model: XGBoost:** Recognizing that the Random Forest model's performance had plateaued in some cities, I implemented XGBoost, a state-of-the-art gradient boosting algorithm, as the final solution.

## Key Findings & Final Results

My analysis and modeling efforts yielded several critical insights into Airbnb pricing and model performance.

**Final Model Performance Summary: The Ultimate Comparison**

| Model | City | R² Score | RMSE |
|---|---|---|---|
| **Linear Regression (V1)** | Berlin | 0.008 | 93.31 |
| | Istanbul | 0.022 | 211.71 |
| | Munich | -0.002 | 142.19 |
| **Random Forest (V2/V3)** | Berlin | 0.7133 | 50.17 |
| | Istanbul | 0.3140 | 177.27 |
| | Munich | 0.4684 | 103.57 |
| **XGBoost (Final Model)** | **Berlin** | **0.7264** | **49.01** |
| | **Istanbul** | **0.3368** | **174.30** |
| | **Munich** | **0.5598** | **94.24** |

### Insights

-   **Algorithmic Choice Matters:** The jump in performance from Linear Regression to the ensemble models was dramatic.
-   **Validation and Optimization:** My hyperparameter tuning showed that the initial Random Forest model was already performing near its peak.
-   **Knowing When to Iterate:** When the Random Forest model's performance plateaued, I implemented XGBoost, a superior algorithm for this type of data, which led to significant performance gains in Istanbul and Munich.
-   **Data-Driven Problem Solving:** I encountered and resolved technical challenges, such as `ValueError`s, demonstrating my ability to diagnose and fix real-world coding issues.
-   **Market-Specific Dynamics:** The lower R² scores in Istanbul and Munich, compared to Berlin, suggest that each city has unique market factors not captured by the current dataset, providing valuable business insight for future work.

## Future Work

-   **Hyperparameter Tuning:** Conduct a full `GridSearchCV` or `RandomizedSearchCV` on the final XGBoost models for each city to potentially achieve marginal gains in performance.
-   **Feature Engineering:** Explore more advanced feature engineering, such as creating new features from textual data in reviews or incorporating external data like local events and tourism statistics.
-   **Deployment:** Develop a simple web application using Flask or Streamlit to deploy the final model and allow users to get real-time price predictions.

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   XGBoost
-   Jupyter Notebook
-   Matplotlib
-   Seaborn