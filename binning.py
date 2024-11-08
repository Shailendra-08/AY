def binning(data, num_bins, method):
    # Sort data for easier manipulation in bin by mean and bin by boundary
    data.sort()
    
    # Equal Partition Binning
    if method == 1:
        min_value = min(data)
        max_value = max(data)
        bin_width = (max_value - min_value) / num_bins
        bins = [[] for _ in range(num_bins)]
        
        for value in data:
            bin_index = int((value - min_value) / bin_width)
            if bin_index == num_bins:  # Edge case for max value
                bin_index -= 1
            bins[bin_index].append(value)
            
    # Bin by Mean
    elif method == 2:
        bins = []
        bin_size = len(data) // num_bins
        remainder = len(data) % num_bins  # Handle remainder if the data isn't evenly divisible

        start = 0
        for i in range(num_bins):
            # Distribute extra items (remainder) across the first few bins
            end = start + bin_size + (1 if i < remainder else 0)
            bin_data = data[start:end]
            bin_mean = sum(bin_data) / len(bin_data)
            bins.append([bin_mean] * len(bin_data))
            start = end

    # Bin by Boundary
    elif method == 3:
        bin_size = len(data) // num_bins
        bins = [data[i:i + bin_size] for i in range(0, len(data), bin_size)]
        
        for i in range(len(bins)):
            min_val = bins[i][0]
            max_val = bins[i][-1]
            bins[i] = [min_val if abs(val - min_val) < abs(val - max_val) else max_val for val in bins[i]]

    else:
        raise ValueError("Invalid method. Choose 1 for equal partition, 2 for bin by mean, or 3 for bin by boundary.")
    
    return bins

# Input data from user
data_input = input("Enter the data values separated by spaces: ")
data = [float(i) for i in data_input.split()]
num_bins = int(input("Enter the number of bins: "))
method = int(input("Choose binning method (1 for equal partition, 2 for bin by mean, 3 for bin by boundary): "))

# Get the binned data based on chosen method
binned_data = binning(data, num_bins, method)

# Display the binned data
for i, b in enumerate(binned_data):
    print(f"Bin {i + 1}: {b}")
