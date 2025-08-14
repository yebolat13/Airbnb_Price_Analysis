# utils/data_loader.py

import pandas as pd
import os
import re

def load_and_clean_data(city_name):
    """
    Loads a specific city's Airbnb dataset, cleans it, and returns the cleaned DataFrame.
    
    Args:
        city_name (str): The name of the city (e.g., 'berlin', 'istanbul', 'munich').
        
    Returns:
        pd.DataFrame: The cleaned and processed DataFrame.
    """
    # Dynamically find the project root from the current file's location.
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.abspath(os.path.join(current_file_path, '..', '..'))

    raw_path = os.path.join(project_root, 'data', city_name, 'raw', f'{city_name}_listings.csv.gz')
    processed_path = os.path.join(project_root, 'data', city_name, 'processed', f'{city_name}_cleaned.csv')
    
    # Check if a cleaned version already exists
    if os.path.exists(processed_path):
        print(f"Loading cleaned data for {city_name.capitalize()} from processed directory...")
        return pd.read_csv(processed_path)
    
    print(f"Loading and cleaning raw data for {city_name.capitalize()}...")
    
    # Load the raw dataset
    try:
        # We need to tell pandas that 'price' column might contain mixed types, so we read it as a string initially.
        df = pd.read_csv(raw_path, compression='gzip')
    except FileNotFoundError:
        print(f"Error: Raw data file not found at {raw_path}")
        return None  
    
    # --- Data Cleaning Steps ---
    
    # 1. Handle Missing Values: Drop columns with more than 50% missing values.
    missing_threshold = len(df) * 0.5
    cols_to_drop = [col for col in df.columns if df[col].isnull().sum() > missing_threshold]
    df.drop(columns=cols_to_drop, inplace=True)
    
    # 2. Clean the 'price' column: Remove '$' and ',' and convert to a numeric type.
    if 'price' in df.columns:
        # First, replace any potential NaN values with a string 'nan' to avoid type errors.
        df['price'] = df['price'].astype(str).replace('nan', '', regex=False)
        # Then, remove '$' and ',' characters.
        df['price'] = df['price'].apply(lambda x: re.sub(r'[$,]', '', x))
        # Finally, convert to numeric. errors='coerce' will turn any parsing failures into NaN.
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # 3. Remove Irrelevant Columns: Drop columns that are not useful for our prediction model.
    irrelevant_cols = ['listing_url', 'scrape_id', 'last_scraped', 'source', 'name', 'description', 
                       'neighborhood_overview', 'picture_url', 'host_url', 'host_name', 
                       'host_about', 'host_thumbnail_url', 'host_picture_url']
    df.drop(columns=[col for col in irrelevant_cols if col in df.columns], inplace=True)
    
    # 4. Handle Outliers: Remove listings with a price higher than a reasonable threshold (e.g., $1000).
    df = df[df['price'] <= 1000].copy()
    
    # Save the cleaned DataFrame for future use
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Cleaned data for {city_name.capitalize()} saved to: {processed_path}")
    
    return df