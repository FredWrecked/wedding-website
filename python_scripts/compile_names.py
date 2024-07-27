import pandas as pd

df = pd.read_excel('RSVP for Wedding.xlsx')

def get_name_element(name):
    return f"<a href=\"#{name}\" onclick=\"setInputValue('{name}')\">{name}</a> \n"

names = ""
for name in df['Full Name'].dropna():
    names += get_name_element(name)

with open("name-elements.txt", 'w') as file:
    file.write(names)