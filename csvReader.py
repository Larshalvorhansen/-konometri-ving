import csv

def calculate_row_average(file_path, row_index):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # Check if the row index is valid
        if row_index >= len(data):
            print("Error: Row index out of range.")
            return None
        
        # Get the row
        row = data[row_index]
        
        # Convert row values to floats and calculate average
        row_values = [float(value) for value in row]
        row_average = sum(row_values) / len(row_values)
        
        return row_average

file_path = 'wage1.csv'  # Replace 'data.csv' with your CSV file path
row_index = 5  # Specify the row index you want to calculate the average for

average = calculate_row_average(file_path, row_index)

if average is not None:
    print(f"The average of row {row_index} is: {average}")


# #,wage,educ,exper,tenure,nonwhite,female,married,numdep,smsa,northcen,south,west,construc,ndurman,trcommpu,trade,services,profserv,profocc,clerocc,servocc,lwage,expersq,tenursq
