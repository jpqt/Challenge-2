# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(output_path, header, data):
    '''Saves CSV file into qualifying loans folder'''

    header = ['bank_data', 'credit_score', 'debt', 'income', 'loan_amount', 'home_value']
    with open (output_path, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile, delimiter=",")
        # csvwriter.writerow(header)
        csvwriter.writerows(data)