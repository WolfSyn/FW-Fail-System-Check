"""
Carlos Garcia
2/10/2025 Created @ 8AM
Last Updated: 2/10/2025 @ 11AM

This script is used to analyze a CSV file containing firmware version and failure description data.
The script will calculate the total number of failures per firmware version and display a bar chart & pie chart.

To run the script, provide the path to the CSV file as an argument when executing the script.

Example usage:
    python firmware_analysis.py firmware_data.csv
"""




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='script_log(Main).log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSV file
def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    df = pd.read_csv(file_path)
    logging.info("Data Loaded Successfully...")
    return df

# Total Failures per Firmware
def total_failures_by_fw(df):
    logging.info("Calculating total failures per firmware...")
    failure_counts = df['FW'].value_counts()
    plt.figure(figsize=(10,5))
    sns.barplot(x=failure_counts.index, y=failure_counts.values, hue=failure_counts.index,legend=False, palette='viridis')
    plt.xlabel("Firmware Version")
    plt.ylabel("Total Failures")
    plt.title("Total Failures per Firmware")
    plt.xticks(rotation=90)
    plt.show()
    logging.info("Total failures per firmware calculated successfully...")
    return failure_counts

# Most common failure description per firmware with percentage
def most_common_failure_desc(df):
    logging.info("Finding most common failure descriptions per firmware with percentage...")
    fail_counts = df.groupby('FW')['FAIL_DESC'].value_counts(normalize=True).unstack(fill_value=0)
    most_common = fail_counts.idxmax(axis=1)
    percentage = (fail_counts.max(axis=1) * 100).round(2)
    result = pd.DataFrame({'Most_Common_Fail': most_common, 'Percentage': percentage})
    logging.info("Most common failure descriptions found")
    return result

# Pie chart of failures per firmware
def failures_pie_chart(df):
    logging.info("Generating pie chart of failures per firmware")
    failure_counts = df['FW'].value_counts()
    plt.figure(figsize=(8,8))
    plt.pie(failure_counts, labels=failure_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title("Failure Distribution by Firmware")
    plt.show()
    logging.info("Pie chart generated...")

# Line graph of failures over time
def failures_over_time(df):
    logging.info("Generating failure tend line graph...")
    df['DATE_TESTED'] = pd.to_datetime(df['DATE_TESTED'], format='%m/%d/%Y %H:%M:%S', errors='ceorce') # make sure a timestamp column exists (before it crashes)
    df.set.index('DATE_TESTED', inplace=True)
    failure_trend = df.resample("D").size()
    plt.figure(figsize=(12,6))
    plt.plot(failure_trend, maker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Number of Failures")
    plt.title("Failure Trends Over Time")
    plt.xsticks(rotation=45)
    plt.show()
    logging.info("Failure trend graph generated.")

# Matrix visualization of SFP_TEMP vs SN
def sfp_temp_matrix(df):
    logging.info("Generating SFP_TEMP matrix visual")
    pivot_table = df.pivot_table(index='SN', columns='FW', values='SFP_TEMP', aggfunc=np.mean)
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot_table,cmap="coolwarm", annot=True, fmt='.1f')
    plt.xlable("Firmware Version")
    plt.ylable("Serial Number (SN)")
    plt.title("SFP_TEMP Matrix")
    plt.show()
    logging.info("SFP_TEMP matrix visual generated.")

# Main Functions
def main():
    file_path = r"C:\Users\cgarcia\Documents\CX Lab\CXLAB_FW_Monitoring\2025 LOGS\FEB 2025\02-03 to 02-10 -- 2025\Encore_RG_Monitoring.csv"
    logging.info("Script started...")
    df = load_data(file_path)

    logging.info("Processing data...")
    print("Total Failures Per firmware:\n", total_failures_by_fw(df))
    print("Most Common Failure Descriptions per Firmware:\n", most_common_failure_desc(df))

    failures_pie_chart(df)
    failures_over_time(df)
    sfp_temp_matrix(df)

    logging.info("Script excecution completed...")

if __name__ == "__main__":
    main()
