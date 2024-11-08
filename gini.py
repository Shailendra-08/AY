
import csv
from math import log2


class Data:
    def __init__(self, attrs):
        self.attrs = attrs


def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  

        for row in reader:
            data.append(Data(dict(zip(headers, row))))
    return data

def calc_entropy(data, target):
    freq = {}
    entropy = 0.0

    for item in data:
        value = item.attrs[target]
        freq[value] = freq.get(value, 0) + 1

    for count in freq.values():
        prob = count / len(data)
        entropy += -prob * log2(prob) if prob else 0

    return entropy


def calc_gini(data, target):
    freq = {}
    gini = 1.0

    for item in data:
        value = item.attrs[target]
        freq[value] = freq.get(value, 0) + 1

    for count in freq.values():
        prob = count / len(data)
        gini -= prob * prob

    return gini


def main():
    file_name = "gini.csv"
    data = read_csv(file_name)

    if not data:
        print("invalid data")
        return 1

    print("attributes: ", ", ".join(data[0].attrs.keys()))

    target = input("enter target attribute: ")
    print(data[1].attrs)
    for attr in data[0].attrs:
        if attr != target:
            gini = calc_gini(data, attr)
            print(f"gini index for {attr}: {gini}")

    try:
        with open("output.txt", "w") as out_file:
            for attr in data[0].attrs:
                if attr != target:
                    gini = calc_gini(data, attr)
                    out_file.write(f"gini index for {attr}: {gini}\n")
    except IOError:
        print("error writing the outputt")


if __name__ == "__main__":
    main()