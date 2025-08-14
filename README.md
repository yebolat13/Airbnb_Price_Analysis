# Airbnb Price Prediction in Major European Cities

## Project Overview

This project is a data science case study focused on predicting Airbnb rental prices in three major European cities: **Berlin, Istanbul, and Munich**. The primary goal is to demonstrate a complete data science workflow, starting with a simple baseline model and progressing to a more robust, advanced model to improve predictive performance.

The project showcases skills in data cleaning, exploratory data analysis (EDA), modular code design, and iterative machine learning model development and evaluation.

## Project Structure

The repository is organized into a modular and easy-to-follow structure:

-   `data/`: Contains the raw and processed Airbnb datasets for each city.
-   `notebooks/`: Contains Jupyter Notebooks that document the project's entire workflow:
    -   `1_Data_Exploration.ipynb`: Initial inspection and understanding of the raw data.
    -   `2_Data_Cleaning_and_EDA.ipynb`: Data cleaning, preprocessing, and exploratory data analysis.
    -   `3_Berlin_Price_Prediction.ipynb`: Baseline (V1) price prediction model for Berlin using Linear Regression.
    -   `4_Istanbul_Price_Prediction.ipynb`: Baseline (V1) price prediction model for Istanbul.
    -   `5_Munich_Price_Prediction.ipynb`: Baseline (V1) price prediction model for Munich.
    -   `6_Summary_and_Conclusion.ipynb`: Final analysis and summary of the baseline models.
    -   `7_Advanced_Modeling_RandomForest.ipynb`: Advanced (V2) price prediction model for Berlin using Random Forest.
    -   `8_Advanced_Modeling_RandomForest_Istanbul.ipynb`: Advanced (V2) price prediction model for Istanbul.
    -   `9_Advanced_Modeling_RandomForest_Munich.ipynb`: Advanced (V2) price prediction model for Munich.
    -   `10_Final_Analysis_and_V2_Summary.ipynb`: Comprehensive comparison and conclusion of all models.
-   `utils/`: A folder containing reusable Python functions for data loading, preprocessing, and model evaluation, ensuring the codebase is modular and clean.

## Methodology

The project follows a two-stage modeling approach:

1.  **V1 - Baseline Modeling:** A simple **Linear Regression** model was chosen as the initial baseline. This phase focused on establishing a robust data pipeline and providing a point of comparison for more advanced models.
2.  **V2 - Advanced Modeling:** Recognizing the limitations of the linear model, a **Random Forest Regressor** was implemented. This phase aimed to significantly improve predictive performance by using a more powerful algorithm capable of handling non-linear data.

## Key Findings & Conclusions

The project successfully demonstrated the importance of model selection in machine learning. The baseline Linear Regression model performed poorly, while the advanced Random Forest model delivered significant performance improvements across all cities.

### Model Performance Comparison

| Model                  | City     | RMSE        | R²          |
|------------------------|----------|-------------|-------------|
| Linear Regression (V1) | Berlin   | 93.31       | 0.008       |
| Linear Regression (V1) | Istanbul | 211.71      | 0.022       |
| Linear Regression (V1) | Munich   | 142.19      | -0.002      |
| **Random Forest (V2)** | **Berlin** | **48.90** | **0.73** |
| **Random Forest (V2)** | **Istanbul** | **177.69** | **0.31** |
| **Random Forest (V2)** | **Munich** | **103.06** | **0.47** |

The R² values for the Random Forest model show that it can explain a substantial portion of the price variance, particularly in Berlin. This validates the decision to move beyond the baseline model.

The following chart visually summarizes the performance comparison:

![Model Performance Comparison](https://i.imgur.com/k2B8xK6.png)

## Future Work

This project provides a strong foundation for further enhancements. Potential next steps include:
* **Hyperparameter Tuning:** Optimizing the Random Forest model's parameters to achieve even better performance.
* **Feature Engineering:** Creating more sophisticated features (e.g., interaction terms, time-based features) to provide the model with more information.
* **Exploring Other Advanced Models:** Testing other powerful algorithms like Gradient Boosting (XGBoost, LightGBM) to see if they can surpass the Random Forest model's performance.

## Technologies Used

-   Python
-   Pandas
-   Scikit-learn
-   Jupyter Notebook
-   Matplotlib & Seaborn