import csv
from getsheet import similar_skills_dict
import time

start = time.time()
data_dict = similar_skills_dict

# Prepare the data in a tabular format
rows = []
for skill, similar_skills in data_dict.items():
    row = [skill] + similar_skills
    rows.append(row)

# Write the data to a CSV file
csv_filename = 'similar_skills_scores.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Sample Skill'] + ['Similar Skills'])
    csv_writer.writerows(rows)
end = time.time()
# Calculate the execution time in seconds
execution_time_seconds = end - start

# Calculate the execution time in minutes
execution_time_minutes = execution_time_seconds / 60

print(f"Execution time: {execution_time_minutes:.4f} minutes")
