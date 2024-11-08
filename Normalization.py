import csv
import math

# Functions for Z-score normalization
def getMean(arr):
    return sum(arr) / len(arr)

def getSD(arr):
    mean = getMean(arr)
    variance = sum((x - mean) ** 2 for x in arr) / (len(arr) - 1)
    return math.sqrt(variance)

def zscore(arr):
    mean = getMean(arr)
    sd = getSD(arr)
    return [(x - mean) / sd for x in arr]

# Function for Min-Max normalization
def minmax(arr, rmin, rmax):
    min_val = min(arr)
    max_val = max(arr)
    return [(x - min_val) / (max_val - min_val) * (rmax - rmin) + rmin for x in arr]

# Ask user to select normalization method
print("Please select the normalization method:")
print("1 --> Min-Max")
print("2 --> Z-score")

choice = int(input("Enter your choice (1 or 2): "))

# Path to the external CSV file
path = 'input.csv'

# Read data from CSV
with open(path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

# Show headers for the user to select a column for normalization
print("\nAvailable columns:", headers)
col_index = int(input("Enter the column index to normalize (e.g., 3 for 'Weight'): "))

# Extract selected column data as a list of floats
selected_column_data = [float(row[col_index]) for row in data]
print(f"\nSelected column data for normalization: {selected_column_data}")

# Perform the chosen normalization and print the results
if choice == 1:
    # Perform Min-Max normalization
    rmin, rmax = map(int, input("Enter min and max values for Min-Max normalization (e.g., 0 1): ").split())
    normalized_data = minmax(selected_column_data, rmin, rmax)
    print(f"Min-Max Normalized Values: {normalized_data}")

elif choice == 2:
    # Perform Z-score normalization
    normalized_data = zscore(selected_column_data)
    print(f"Z-score Normalized Values: {normalized_data}")

else:
    print("Invalid choice. Please enter 1 or 2.")
