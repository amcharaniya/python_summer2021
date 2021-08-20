#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:01:17 2021

@author: amaancharaniya
"""

• Go to: https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addressesand-remarks
• Create a csv file with the following information for each spoken address given by President Biden since
he became president on 2021-01-20:
– Date of spoken address
– Title
– Full text of address or remarks
– Citation/footnote (if one exists)
• Remember, be polite and sleep after accessing each individual document page

os.chdir("/Users/amaancharaniya/Documents/python_summer2021/HW")

from bs4 import BeautifulSoup
import lxml
import html5lib
import urllib.request
import csv 
import os, time, random


with open("BidenSpeeches.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames= ("Date", "Title", "Full Text", "Footnote") )
    w.writeheader()
    speech = {}
    web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?items_per_page=60'
    web_page = urllib.request.urlopen(web_address)
    soup = BeautifulSoup(web_page.read(), features="lxml") 
    origin = soup.find_all(class_="pagination")    
    for x in origin[0:4]: 
        website = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?items_per_page=60' + x.find("a")["href"]
        new_webpage = new_page = urllib.request.urlopen(website)
        newest_soup = BeautifulSoup(new_webpage.read(), features="lxml") 
        s = soup.find_all(class_="field-title")  
        for i in s:
            webpage = "https://www.presidency.ucsb.edu/" +  i.find("a")["href"]
            new_page = urllib.request.urlopen(webpage)
            new_soup = BeautifulSoup(new_page.read(), features = "lxml")
            try:
                speech["Date"] = new_soup.find(class_="date-display-single").text
            except:
                speech["Date"] = "N/A"
            try:
                speech["Title"] = new_soup.find(class_="field-ds-doc-title").text
            except:
                speech["Title"] = "N/A"
            try:
                speech["Full Text"] = new_soup.find(class_="field-docs-content").text
                speech["Full Text"] = new_soup.find(class_="field-docs-content").text
            except:
                speech["Full Text"] = "N/A"
            try:
                speech["Footnote"] = new_soup.find(class_="field-docs-footnote").text
            except:
                speech["Footnote"] = "N/A"
            w.writerow(speech)
            time.sleep(random.uniform(1, 5))



