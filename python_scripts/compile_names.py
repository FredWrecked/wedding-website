import pandas as pd

df = pd.read_excel('RSVP for Wedding.xlsx')

def get_name_element(name):
    return f"<a href=\"#{name}\" onclick=\"setInputValue('{name}')\">{name}</a> \n"

def get_attend_case(name, has_plus_one):
    if has_plus_one:
        return f"if (guest === '{name}') return true\n"
    return ""


names = ""
for name in df['Full Name'].dropna():
    names += get_name_element(name)

fun = ""
for name,has_plus_one in zip(df['Full Name'].dropna(), df['Has Plus One'].dropna()):
    fun += get_attend_case(name, has_plus_one)

with open("name-elements.txt", 'w') as file:
    file.write(names)

with open("plus-one-map.txt", 'w') as file:
    file.write(fun)