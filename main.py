"""
    Capstone Project
    Learn how to use Selenium and BeautifullSoap

    you need to create a new form in Google Forms.
    1. Go to https://docs.google.com/forms/ and create your own form:
    2. Add 3 questions to the form, make all questions "short-answer":
        What is the Location?
        What is the Price?
        What is the Link Property?
    3. Click send and copy the link address of the form. You will need to use this in your program.
"""

import WebScrapping
import EntryFormWithSelenium

webscrapping = WebScrapping.WebScraping()

for item in webscrapping.getListOfLink():
    print(item[0], item[1], item[2])
    entryForm = EntryFormWithSelenium.EntryForm()
    entryForm.entry(item[0], item[1], item[2])

