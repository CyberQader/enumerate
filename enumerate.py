myskills = ['js','python','css','mysql']
myskillwithcounter = enumerate(myskills,10)

for counter,skill in myskillwithcounter:
    print(f'{counter}-{skill.upper()}')