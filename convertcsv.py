import csv
from getsheet import similar_skills_dict

data_dict = similar_skills_dict

# Prepare the data in a tabular format
rows = []
for skill, similar_skills in data_dict.items():
    row = [skill] + similar_skills
    rows.append(row)

# Write the data to a CSV file
csv_filename = 'finetuned_skillsV1.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Sample Skill'] + ['Similar Skills'])
    csv_writer.writerows(rows)

print(f'Data has been written to {csv_filename}')
