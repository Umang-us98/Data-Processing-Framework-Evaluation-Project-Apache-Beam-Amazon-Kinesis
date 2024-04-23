# Data-Processing-Framework-Evaluation-Project-Apache-Beam-Amazon-Kinesis
# Introduction
The project's objective is to systematically evaluate Apache Beam and Amazon Kinesis frameworks, specifically assessing their performance in terms of latency and scalability under varying workloads. The insights gained from this analysis will be of significant value to organizations seeking to make informed decisions regarding data analysis.

# Files Included
1. preprocess.py: A python file for loading the preprocess data from the dataset (londonweather.csv) to create a new CSV file (preprocessed_data.csv).
2. ApacheBeam.ipynb: Jupiter Notebook demonstrates data processing using Apache Beam framework. It reads data from a CSV file (preprocessed_data.csv), processes it using the ExtractAndProcess class, and writes the output to 4 different text files (output1000, output5000, output10000, output15000). The script calculates the average temperature from the maximum and minimum temperatures for different iterations/workloads.
