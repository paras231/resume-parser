from PyPDF2 import PdfReader
import re
import spacy

reader =  PdfReader("fullstackdev.pdf")

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


skills = []
for token in doc:
    if token.pos_ == "NOUN" or token.pos_ == "VERB": # Example: Nouns and verbs
        if token.text.lower() in ["Javscript", "HTML", "sql", "data analysis", "machine learning"]:
            skills.append(token.text)

print(skills)