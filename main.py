from PyPDF2 import PdfReader
import re
import spacy
from utils.skill_set import skills_list 

reader =  PdfReader("agriculture_resume.pdf")

number_of_pages = len(reader.pages)

page = reader.pages[0]
text = page.extract_text()

# print(text)


'''Extract emails from the pdf string using regular expression'''

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

emails =  re.findall(email_pattern,text)

# print(emails)

phone_pattern = r'(\+?\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?\d{3,4}[\s-]?\d{4}'

phones = re.findall(phone_pattern, text)

phones = [''.join(phone) for phone in phones if ''.join(phone).strip() != '']
# print(phones)

lines = text.split('\n')
# print(lines)
for line in lines:
    if line.strip():  # Skip empty lines
        name_candidate = line.strip()
        break
# print("Possible Name:", name_candidate)

'''Extract Address using spacy  , Spacy is good for extracting entities'''



npl =  spacy.load("en_core_web_sm")

doc =  npl(text)

# for ent in doc.ents:
#     if ent.label_  in ["GPE","LOC"]:
#        print("Possible Address Part:", ent.text)

# print(doc)

'''Extract skills sections'''


def extract_skills(text,skill_list):
    skills = []
    for skill in skill_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match =  re.search(pattern,text, re.IGNORECASE)
        if match:
            skills.append(skill)
    return skills



# output_skills =  extract_skills(text,skills_list)

# print(output_skills)


'''Extract Educations'''

def extract_education(text):
    educations = []
    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches =  re.findall(pattern,text)
    for match in matches:
        educations.append(match.strip())
    return educations

print(extract_education(text))