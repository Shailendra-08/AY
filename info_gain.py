import csv
import math

def entropy(data, target_attribute_index):
    freq = {}
    for row in data:
        target_value = row[target_attribute_index]
        if target_value in freq:
            freq[target_value] += 1
        else:
            freq[target_value] = 1
    
    total = len(data)
    ent = 0
    for count in freq.values():
        prob = count / total
        ent -= prob * math.log2(prob)  
    
    print(f"Entropy of the current set: {ent:.4f}")
    return ent

def info_gain(data, attribute_index, target_attribute_index):
    print(f"\nCalculating Information Gain for attribute at index {attribute_index}...")
    original_entropy = entropy(data, target_attribute_index)
    
    subsets = {}
    for row in data:
        attribute_value = row[attribute_index]
        if attribute_value in subsets:
            subsets[attribute_value].append(row)
        else:
            subsets[attribute_value] = [row]
    
    total_rows = len(data)
    subset_entropy = 0
    for attribute_value, subset in subsets.items():
        prob_subset = len(subset) / total_rows
        print(f"\nSubset for {attribute_value}: {len(subset)} instances")
        entropy_subset = entropy(subset, target_attribute_index)
        subset_entropy += prob_subset * entropy_subset
    
    ig = original_entropy - subset_entropy
    print(f"\nInformation Gain: {ig:.4f}")
    return ig

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            data.append(row)
    return data, headers

def main():
    input_filename = "entropy.csv"  
    data, headers = read_csv(input_filename)

    target_attribute_index = len(data[0]) - 1
    
    print("\nAttributes:")
    for i, header in enumerate(headers):
        if i != target_attribute_index:
            print(f"{i}: {header}")
    
    attribute_index = int(input(f"\nEnter attribute index (0 to {target_attribute_index - 1}): "))
    
    print(f"\nSelected attribute: {headers[attribute_index]}")
    print("Attribute values and target values:")
    for row in data:
        print(f"{row[attribute_index]} -> {row[target_attribute_index]}")

    ig = info_gain(data, attribute_index, target_attribute_index)

if __name__ == "__main__":
    main()
