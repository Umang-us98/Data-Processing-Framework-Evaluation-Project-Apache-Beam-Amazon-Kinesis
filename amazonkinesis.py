#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install amazon_kclpy


# In[3]:


pip install psutil


# In[4]:


pip install memory-profiler


# In[2]:


import boto3
import csv
import time

# AWS credentials and region
aws_access_key_id = 'AKIAZUHXIJF6A6K3RU6I'
aws_secret_access_key = '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'
region_name = 'us-east-2'

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
stream_name = 'demo12'

# Kinesis client
kinesis_client = boto3.client(
    'kinesis',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Read CSV file and put records into Kinesis stream
start_time = time.time()  # Start the timer

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)

    # Skip header row if present
    header = next(reader, None)

    for row in reader:
        data = ','.join(row)  # Assuming CSV columns are comma-separated
        partition_key = 'default'  # Modify this based on your data

        # Put record into the Kinesis stream
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=data,
            PartitionKey=partition_key
        )

        print(f"Record sent to partition {response['ShardId']} with sequence number {response['SequenceNumber']}")

end_time = time.time()  # Stop the timer
total_time = end_time - start_time
print(f"Total time taken: {total_time} seconds")


# In[9]:


import csv
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data1000.txt"
max_entities = 1000  # Processing first 1000 entities 

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 1000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[11]:


import csv
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data5000.txt"
max_entities = 5000  # First 5000 entities to process

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            # average_temperature = sum(temps['temperatures']) / len(temps['temperatures'])
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 5000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[10]:


import csv
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data15000.txt"
max_entities = 15000  # Set the maximum number of entities to process

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            # average_temperature = sum(temps['temperatures']) / len(temps['temperatures'])
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 15000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[12]:


import csv
import time
import logging
import psutil  # Import the psutil library for CPU and memory monitoring

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data1000(CPU and memory monitoring).txt"
max_entities = 1000  # First 1000 entities to process

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            # average_temperature = sum(temps['temperatures']) / len(temps['temperatures'])
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def monitor_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage for the last 1 second
    memory_info = psutil.virtual_memory()

    logger.info(f"CPU Usage: {cpu_percent}%")
    logger.info(f"Memory Usage: {memory_info.percent}%")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            # Monitor system resources before data processing
            monitor_system_resources()

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

            # Monitor system resources after data processing
            monitor_system_resources()

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 1000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[13]:


import csv
import time
import logging
import psutil  # Import the psutil library for CPU and memory monitoring

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data5000(CPU and memory monitoring).txt"
max_entities = 5000  # Set the maximum number of entities to process

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            # average_temperature = sum(temps['temperatures']) / len(temps['temperatures'])
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def monitor_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage for the last 1 second
    memory_info = psutil.virtual_memory()

    logger.info(f"CPU Usage: {cpu_percent}%")
    logger.info(f"Memory Usage: {memory_info.percent}%")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            # Monitor system resources before data processing
            monitor_system_resources()

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

            # Monitor system resources after data processing
            monitor_system_resources()

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 5000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[14]:


import csv
import time
import logging
import psutil  # Import the psutil library for CPU and memory monitoring

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV file path (using raw string to handle backslashes)
csv_file_path = r"C:\Users\lidda\OneDrive\Desktop\Term Project\preprocessed_data.csv"
output_txt_file = r"C:\Users\lidda\OneDrive\Desktop\Term Project\output_data15000(CPU and memory monitoring).txt"
max_entities = 15000  # Set the maximum number of entities to process

def calculate_average_temperature(data):
    date_index = 0
    max_temp_index = 1
    min_temp_index = 2

    temperature_by_date = {}

    for row in data:
        date = row[date_index]
        max_temp = float(row[max_temp_index])
        min_temp = float(row[min_temp_index])

        average_temp = (max_temp + min_temp) / 2

        if date in temperature_by_date:
            temperature_by_date[date]['temperatures'].append(average_temp)
        else:
            temperature_by_date[date] = average_temp

    return temperature_by_date

def write_to_txt(temperature_by_date, output_txt_file):
    with open(output_txt_file, mode='w') as txt_file:
        for date, temps in temperature_by_date.items():
            # average_temperature = sum(temps['temperatures']) / len(temps['temperatures'])
            txt_file.write(f"{{'date': '{date}', 'avg_temp': {temperature_by_date[date]}}}\n")

def monitor_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage for the last 1 second
    memory_info = psutil.virtual_memory()

    logger.info(f"CPU Usage: {cpu_percent}%")
    logger.info(f"Memory Usage: {memory_info.percent}%")

def main():
    start_time = time.time()  # Start the timer

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)

            # Skip header row if present
            header = next(reader, None)

            # Limit data processing to the first 'max_entities' rows
            data = [next(reader) for _ in range(max_entities)]

            # Monitor system resources before data processing
            monitor_system_resources()

            temperature_by_date = calculate_average_temperature(data)

            # Write the results to a text file
            write_to_txt(temperature_by_date, output_txt_file)

            # Monitor system resources after data processing
            monitor_system_resources()

    finally:
        end_time = time.time()  # Stop the timer
        total_time = end_time - start_time
        logger.info(f"Total time taken for 15000 entities: {total_time} seconds")

if __name__ == "__main__":
    main()


# In[ ]:




