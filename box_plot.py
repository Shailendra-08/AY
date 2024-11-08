import csv

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return (arr_sorted[n//2 - 1] + arr_sorted[n//2]) / 2
    else:
        return arr_sorted[n//2]

def getQ1(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return median(arr_sorted[:n//2])
    else:
        return median(arr_sorted[:n//2 + 1])

def getQ2(arr):
    return median(arr)

def getQ3(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return median(arr_sorted[n//2:])
    else:
        return median(arr_sorted[n//2 + 1:])

def five_number_summary(arr):
    Q1 = getQ1(arr)
    Q2 = getQ2(arr)
    Q3 = getQ3(arr)
    IQR = Q3 - Q1
    mini = Q1 - 1.5 * IQR
    maxi = Q3 + 1.5 * IQR
    outliers = [x for x in arr if x < mini or x > maxi]
    return Q1, Q2, Q3, IQR, mini, maxi, outliers

# Updated code to match the simplified CSV file format
path = 'cropcultivation.csv'
with open(path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    data = [float(row[0]) for row in reader]  # Read values from the first column

Q1, Q2, Q3, IQR, low, high, outliers = five_number_summary(data)

print("Five Number Summary:")
print("Data (sorted):", sorted(data))
print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("IQR:", IQR)
print("Outliers:", outliers)
