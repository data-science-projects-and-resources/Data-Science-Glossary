alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# function to get words and their meanings from their respective alphabet file
def get_word(file):
    with open(file, "r") as f:
        data = f.read()
        ls = data.strip().split("\n")
        return sorted(ls)
    

# function to convert the words into dictionary keys and their meanings into dictionary values
def write_dictionary(file):        
    ls = get_word(file)
    for i in range(len(ls)):
        dictionary_words = ls[i].split(":")
        dictionary = {dictionary_words[0]:dictionary_words[1]}
        for key, val in dictionary.items():
            f.write(f"**{key}**: {val}\n\n")



with open("ReadMe.md", "w") as f:
    f.write("""[![update-readme-script](https://github.com/sharmas1ddharth/data_science_glossary/actions/workflows/update-readme.yml/badge.svg)](https://github.com/sharmas1ddharth/data_science_dictionary/actions/workflows/update-readme.yml)
            
            
This repository is a glossary of common Data Science, Machine Learning and Statistics terms commonly used in the industry. In the coming days, we will add more terms. In the meanwhile, if you want to contribute to the glossary please read the [contribution guidelines](#contributionguidelines) provided below
            
            
            
## Table of Contents:\n""")
    for alphabet in alphabets:
        f.write(f"- [{alphabet}](#{alphabet.lower()})\n")
    
    f.write("\n<br>\n<br>\n\n")
    for alphabet in alphabets:
        f.write(f"- ## {alphabet}\n")
        try:
            write_dictionary(f"dictfiles/{alphabet}.txt")
            
        except:
            pass
    
    f.write("""# Contribution
If you want to contribute to this repository please follow the instructions below:
- Fork the repository.

- Run `git pull` to fetch all the recent changes otherwise your commits will clash with the main branch commits.

- Add the glossary words in their respective alphabet text file inside the dictfiles folder.

- Commit the changes as 'alphabet.txt file updated' where alphabet.txt is the file where you are going to insert words.

- Finally push the changes and the github action will update the readme file.

**NOTE:** 

- Please don't change anything inside python script if you have anything to add or to improve in the script please raise an issue first.
- Please format the glossary as 'word: meaning' because the script is going to split the word with ':'
    
            """)
