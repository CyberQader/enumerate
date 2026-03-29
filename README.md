A sleek Python script that iterates through a list of skills, providing a custom starting counter for professional indexing.

💻 The Code
Python
myskills = ['js', 'python', 'css', 'mysql']
myskillwithcounter = enumerate(myskills, 10)

for counter, skill in myskillwithcounter:
    print(f'{counter}-{skill.upper()}')
