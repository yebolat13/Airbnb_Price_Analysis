# utils/model_utils.py

import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def prepare_features(df, target_column):
    """
    Prepares features (X) and target (y) for a machine learning model.
    Handles one-hot encoding for categorical features.

    Args:
        df (pd.DataFrame): The input DataFrame.
        target_column (str): The name of the target column (e.g., 'price').

    Returns:
        tuple: A tuple containing the features (X) and target (y).
    """
    # Create copies to avoid SettingWithCopyWarning
    df = df.copy()
    
    # Separate features and target
    y = df[target_column]
    X = df.drop(target_column, axis=1)

    # Identify categorical columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns

    # Apply one-hot encoding
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    print("Categorical features have been one-hot encoded.")
    print(f"Shape of features (X) after encoding: {X.shape}")

    return X, y


def evaluate_model(y_true, y_pred):
    """
    Calculates and prints key evaluation metrics for a regression model.

    Args:
        y_true (array-like): The true target values.
        y_pred (array-like): The predicted values.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print("\n--- Model Evaluation ---")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R-squared (R²): {r2:.2f}")

def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    """
    Trains a given model on training data and evaluates its performance on test data.

    Args:
        model: The machine learning model to be trained.
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.
        y_train (pd.Series): Training target.
        y_test (pd.Series): Testing target.

    Returns:
        tuple: A tuple containing predictions (y_pred) and evaluation metrics (rmse, r2).
    """
    print(f"\nTraining {type(model).__name__} model...")
    model.fit(X_train, y_train)
    print("Training complete.")
    
    y_pred = model.predict(X_test)
    
    evaluate_model(y_test, y_pred)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    return y_pred, rmse, r2