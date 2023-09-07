from data import skills_list


# Define a function to remove unwanted characters from a string
def clean_string(s):
    return s.replace('.', '').replace('(', ' ').replace(')', '').replace('-', ' ').replace(',', ' ').replace('-', ' ').replace('   ', ' ')


# Apply the function to each element in the nested lists
cleaned_skills_list = [[clean_string(skill) for skill in sub_list] for sub_list in skills_list]
# print(cleaned_skills_list)
