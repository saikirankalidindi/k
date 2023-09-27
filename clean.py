from jobs import jobs_list


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
