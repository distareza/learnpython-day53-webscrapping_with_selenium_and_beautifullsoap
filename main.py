"""
    Capstone Project
    Learn how to use Selenium and BeautifullSoap
"""

import WebScrapping
import EntryFormWithSelenium

rent_url = "https://www.mudah.my/kuala-lumpur/properties-for-rent"
webscrapping = WebScrapping.WebScraping(rent_url)

for item in webscrapping.getListOfLink():
    print(item[0], item[1], item[2])
    entryForm = EntryFormWithSelenium.EntryForm()
    entryForm.entry(item[0], item[1], item[2])

