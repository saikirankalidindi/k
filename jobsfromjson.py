import json
from itertools import chain
# import timeit
with open('jobs.json', 'r') as file:
    data = json.load(file)

jobs_list = data


def clean_string(s):
    s = s.replace('.', '').replace('(', ' ').replace(')', '').replace('-', ' ').replace(',', ' ').replace('-',
                                                                                                          ' ').replace(
        '   ', ' ').replace('                                                             ', '')
    return s.split('/')


# List of job roles

# Apply the function to each element in the nested lists
cleaned_jobs_list = [[job for role in sublist for job in clean_string(role)] for sublist in jobs_list]

input_list = cleaned_jobs_list
cleaned_list = [[item.strip() for item in sublist if item.strip()] for sublist in input_list]

# print(cleaned_list)
flat_jobs = list(chain.from_iterable(cleaned_list))

flat_jobs_list = flat_jobs
unique_jobTitles = []

for jobs_flat in flat_jobs_list:
    if jobs_flat not in unique_jobTitles:
        if jobs_flat != '                                                               ':
            if jobs_flat != '':
                unique_jobTitles.append(jobs_flat)

print(len(unique_jobTitles))
