from itertools import chain
from clean import cleaned_list

flat_jobs = list(chain.from_iterable(cleaned_list))

flat_jobs_list = flat_jobs
unique_jobTitles = []

for jobs_flat in flat_jobs_list:
    if jobs_flat not in unique_jobTitles and jobs_flat != '                                                             ':
        if jobs_flat != '                                                               ':
            if jobs_flat != '':
                unique_jobTitles.append(jobs_flat)

print(len(unique_jobTitles))
# print(unique_jobTitles)
