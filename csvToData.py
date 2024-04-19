import csv

def read_csv_to_arrays(file_path):
    data_arrays = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Assuming the first row contains headers
        for header in headers:
            data_arrays[header] = []
        
        for row in reader:
            for idx, value in enumerate(row):
                header = headers[idx]
                data_arrays[header].append(value)
    
    return data_arrays

def main():
    file_path = 'wage1.csv'  # Update with the path to your CSV file
    data_arrays = read_csv_to_arrays(file_path)
    
    # Print the data arrays
    for header, values in data_arrays.items():
        print(header, ':', values)

if __name__ == "__main__":
    main()
