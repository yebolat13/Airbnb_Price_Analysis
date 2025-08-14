# Airbnb Price Prediction in Major European Cities

## Project Overview

This project is a data science case study focused on predicting Airbnb rental prices in three major European cities: **Berlin, Istanbul, and Munich**. The goal is to build a baseline machine learning model for each city and analyze its performance. The project demonstrates a complete data science workflow, from data cleaning and exploratory data analysis to model building and critical evaluation.

## Project Structure

The repository is organized into a modular and easy-to-follow structure:

-   `data/`: Contains the raw and processed Airbnb datasets for each city.
-   `notebooks/`: Contains Jupyter Notebooks that document the project's entire workflow:
    -   `1_Data_Exploration.ipynb`: Initial inspection and understanding of the raw data.
    -   `2_Data_Cleaning_and_EDA.ipynb`: Data cleaning, preprocessing, and exploratory data analysis with visualizations.
    -   `3_Berlin_Price_Prediction.ipynb`: Building and evaluating a price prediction model for Berlin.
    -   `4_Istanbul_Price_Prediction.ipynb`: Applying the same model pipeline to Istanbul.
    -   `5_Munich_Price_Prediction.ipynb`: Applying the same model pipeline to Munich.
    -   `6_Summary_and_Conclusion.ipynb`: Final analysis, model comparison, and discussion of results.
-   `utils/`: A folder containing reusable Python functions for data loading, cleaning, and model evaluation, ensuring the codebase is modular and clean.

## Methodology

The project follows a standard data science methodology:

1.  **Data Preparation:** Datasets were loaded and cleaned using a custom, reusable function. This step involved handling missing values, cleaning the `price` column, and dropping irrelevant features.
2.  **Exploratory Data Analysis (EDA):** Visualizations were used to understand price distributions and the relationship between price and other key features like `room_type`.
3.  **Machine Learning Modeling:** A simple **Linear Regression** model was chosen as the baseline for price prediction. The data was preprocessed (one-hot encoding for categorical variables) and split into training and testing sets.
4.  **Model Evaluation:** The models were evaluated using **Root Mean Squared Error (RMSE)** and **R-squared (R²)** metrics to assess their performance on each city's test data.

## Key Findings & Conclusions

The baseline Linear Regression models provided the following performance metrics:

| City     | RMSE        | R²          |
|----------|-------------|-------------|
| Berlin   | 93.31       | 0.008       |
| Istanbul | 211.71      | 0.022       |
| Munich   | 142.19      | -0.002      |

The R² values for all models are very close to zero, indicating that the simple Linear Regression model is not well-suited for predicting Airbnb prices, as it fails to capture the complex, non-linear relationships within the data. This highlights a crucial learning point: the choice of model is highly dependent on the nature of the data.

## Future Work

This project provides a strong foundation for future enhancements. Potential next steps include:
* **Exploring Advanced Models:** Training and evaluating more powerful algorithms like **Random Forest** or **Gradient Boosting** models.
* **Advanced Feature Engineering:** Creating new features (e.g., `price_per_person`) to improve model performance.
* **Hyperparameter Tuning:** Optimizing model parameters to achieve better results.

## Technologies Used

-   Python
-   Pandas
-   Scikit-learn
-   Jupyter Notebook
-   Matplotlib & Seaborn