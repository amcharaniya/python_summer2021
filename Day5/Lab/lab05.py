import re

import os
os.chdir('/Users/amaancharaniya/Documents/python_summer2021/Day5/Lab/')

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

keyword = re.compile("the ")
for i, line in enumerate(obama):
  if not keyword.search(line):   
      print(i)
      print(line) 
    
## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

# TODO: print lines that contain a word of any length starting with s and ending with e
pattern = re.compile(r'(\s*)\s(\e*)')

test = 'saturdaye\nhappinesse\Swednesdaye'

re.findall(r"\d", obama)

pattern = re.compile(r'\b[sS]\w*e\b', re.MULTILINE)
for i, line in enumerate(obama):
    if pattern.findall(line):
        print(line)
        


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'

pattern = re.compile(r'(\d*)\.(\d*)\.(\d*)')
pattern = re.compile(r"\d{2}.\d{2}.\d{2}")
pattern.search(date).groups()

 
print("Month: {}\nDay: {}\nYear: {}".format(pattern.search(date).group(1),pattern.search(date).group(2),pattern.search(date).group(3)))
