import pandas as pd
from sqlalchemy import create_engine
import os

# --- 1. CONFIGURATION ---

input_file = 'INC-5000-Companies-2019.csv'
output_csv_file = 'cleaned_inc5000_for_sql.csv' 

# Database Credentials
db_user = 'root'
db_password = 'YOUR_PASSWORD_HERE'
db_host = 'localhost' 
db_name = 'inc_5000_db'

# --- 2. LOAD DATA ---
print(f"Loading data from: {input_file}...")
# Using sep=None and engine='python' to handle potential separator issues automatically
df = pd.read_csv(input_file, sep=None, engine='python')

# --- 3. TRANSFORM (CLEANING) ---
def clean_revenue(value):
    """
    Parses revenue strings containing 'Million' or 'Billion' 
    and converts them to numeric float values.
    """
    text_value = str(value)
    
    if 'Billion' in text_value:
        return float(text_value.replace(' Billion', '')) * 1_000_000_000
    elif 'Million' in text_value:
        return float(text_value.replace(' Million', '')) * 1_000_000
        
    return value

print("Cleaning revenue column...")
df['revenue'] = df['revenue'].apply(clean_revenue)

# --- 4. SAVE TO CSV  ---
# This creates the file on your disk
df.to_csv(output_csv_file, index=False)
print(f"✅ Backup saved locally as: {output_csv_file}")

# --- 5. UPLOAD TO SQL ---
print("Connecting to Database...")
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')

try:
    # Changed 'fail' to 'replace' so you can run the script multiple times without error
    df.to_sql(name='inc_5000_2019', con=engine, if_exists='replace', index=False)
    print("🚀 Success! Data sent to MySQL database.")
except Exception as e:
    print(f"❌ Database Error: {e}")

# Check the results
print("\nFirst 5 rows of cleaned revenue:")
print(df['revenue'].head())