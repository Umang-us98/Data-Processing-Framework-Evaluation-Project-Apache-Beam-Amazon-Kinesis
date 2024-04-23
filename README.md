# Data-Processing-Framework-Evaluation-Project-Apache-Beam-Amazon-Kinesis
# Introduction
The project's objective is to systematically evaluate Apache Beam and Amazon Kinesis frameworks, specifically assessing their performance in terms of latency and scalability under varying workloads. The insights gained from this analysis will be of significant value to organizations seeking to make informed decisions regarding data analysis. For both ApacheBeam.ipynb amazonkinesis.py files reads data from a CSV file (preprocessed_data.csv) and write the output to 3 different text files (output1000, output5000, output15000). The script calculates the average temperature from the maximum and minimum temperatures for different iterations/workloads. Moreover, it showcases the Average processing time, CPU usage, and Memory usage.

# Files Included
1. preprocess.py: A python file for loading the preprocess data from the dataset (londonweather.csv) to create a new CSV file (preprocessed_data.csv).
2. ApacheBeam.ipynb: Jupiter Notebook demonstrates data processing using Apache Beam framework.
3. amazonkinesis.py: Python file for demonstrating data processing using the Amazon Kinesis framework.

# Required Libraries
1. ApacheBeam.ipynb: pip install apache-beam[gcp]
2. amazonkinesis.py: pip install amazon_kclpy psutil memory-profiler

# Steps to Simulate the Project
1. Download the repository or clone it using the following command: git clone (https://github.com/Umang-us98/Data-Processing-Framework-Evaluation-Project-Apache-Beam-Amazon-Kinesis)
2. Install the required Python libraries listed above
3. Run preprocess.py to preprocess the dataset and generate the preprocessed_data.csv file.
4. Open and run ApacheBeam.ipynb and amazonkinesis.py (order doesn't matter)

# Contributors
1. Manvesh Lidhar
2. Dhruvil Shah
3. Umang Sood
