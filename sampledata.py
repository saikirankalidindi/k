import csv

# Path to your CSV file
csv_file_path = 'similar_skills_scores.csv'

# Initialize an empty list to store the values
values_list = []

# Open the CSV file and read the values from the first column
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Assuming the first column is at index 0
        if row:  # Check if the row is not empty
            values_list.append(row[0])

sample_skills = values_list[1:]
