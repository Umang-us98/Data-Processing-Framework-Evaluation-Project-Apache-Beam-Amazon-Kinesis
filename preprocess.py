import pandas as pd
import time

# Load your data (replace 'your_data.csv' with your actual file name)
start_time = time.time()
df = pd.read_csv('london_weather.csv')

# Display the initial data
print("Initial Data:")
print(df.head())

# Drop null values only for 'max_temp' and 'min_temp' columns
df = df.dropna(subset=['max_temp', 'min_temp'])

# Drop duplicate values
df = df.drop_duplicates()

# Keep only the required columns
columns_to_keep = ['date', 'max_temp', 'min_temp']
df = df[columns_to_keep]

# Convert 'date' to int
#df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y%m%d').astype(int)

# Save the preprocessed data to a new CSV file (replace 'preprocessed_data.csv' with your desired file name)
df.to_csv('preprocessed_data.csv', index=False)

# Display the preprocessed data
print("\nPreprocessed Data:")
print(df.head())

# Calculate and print the time taken for preprocessing
end_time = time.time()
time_taken = end_time - start_time
print(f"\nTime taken for preprocessing: {time_taken} seconds")
