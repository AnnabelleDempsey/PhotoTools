# Step 2. Prep the Table

#Import Modules
import PySimpleGUI as sg
import pandas as pd
import openpyxl
import exifread
import os

# Define the Excel file and sheets
unclean_data = 'Data_Entry.xlsx'
clean_data = 'Data_Entry.xlsx'

df = pd.read_excel('Data_Entry.xlsx', sheet_name="Data Entry")
df2 = pd.read_excel('Data_Entry.xlsx', sheet_name="Clean Data")

#1. Define User Interface
Theme = 'Topanga'
sg.theme(Theme)
layout =

# Define path of images
imgpath = r'C:\Users\Annabelle\Pictures\EOS M6 Mark II\2022_05_20__CANON\Singular_Images\001.tif'


f = open(imgpath, 'rb')

# Return Exif tags
tags = exifread.process_file(f, details=False)
print(tags)