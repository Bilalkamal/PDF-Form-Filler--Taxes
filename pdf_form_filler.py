#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from PyPDF2.generic import NameObject
from PyPDF2 import PdfReader, PdfWriter


df = pd.read_excel('SampleFile.xlsx', sheet_name='Sheet1', skiprows=3)
df = df.drop(df.columns[0], axis=1)
df = df.astype(str)
df = df.replace('nan', np.nan)
df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.columns = ['Employee ID', 'Individual Name (First)', 'Individual Name (Last)',
       'Country of Citizenship', 'Permanent residence address (Street)',
       'Permanent residence address (No.)', 'City/Town', 'State/Province',
       'Postal Code', 'Country',
       'Mailing address', 'City/Town (Mailing address)',
       'State/ Province', 'Postal Code.1', 'Country.1',
       'U.S. Taxpayer ID Number', 'Foreign Tax Identifying Number',
       'Reference Number', 'Date of Birth', 'Unnamed: 20',
       'Resident Country', 'Treaty Article ', 'Withholding Tax Rate',
       'Type of Income',
       'Reasons Beneficial Owner meets Treaty Article Terms']




def combine_inputs(*args):
    return ''.join(arg if arg == args[-1] else f'{arg}, ' for arg in args if isinstance(arg, str))


new_df = pd.DataFrame()
new_df["f_1[0]"] = df["Individual Name (First)"] + ' ' + df["Individual Name (Last)"]
new_df["f_2[0]"] = df["Country of Citizenship"]
new_df["f_3[0]"] = df.apply(lambda x: combine_inputs(x['Permanent residence address (Street)'], x['Permanent residence address (No.)']), axis=1)
new_df["f_4[0]"] = df.apply(lambda x: combine_inputs(x['City/Town'], x['State/Province'], x['Postal Code']), axis=1)
new_df["f_5[0]"] = df["Country"]
new_df["f_6[0]"] = df.apply(lambda x: combine_inputs(x['Mailing address']), axis=1)
new_df["f_7[0]"] = df.apply(lambda x: combine_inputs(x['City/Town (Mailing address)'], x['State/ Province'], x['Postal Code.1']), axis=1)
new_df["f_8[0]"] = df["Country.1"]
new_df["f_9[0]"] = df["U.S. Taxpayer ID Number"]
new_df["f_10[0]"] = df["Foreign Tax Identifying Number"]
new_df["f_11[0]"] = df["Reference Number"]
new_df["f_12[0]"] = df["Date of Birth"]
new_df["f_12[0]"] = new_df["f_12[0]"].str.replace('/', '-')
new_df["f_13[0]"] = df["Resident Country"]
new_df["f_14[0]"] = df["Treaty Article "]
new_df["f_15[0]"] = df["Withholding Tax Rate"]
new_df["f_16[0]"] = df["Type of Income"]
new_df["f_17[0]"] = df["Reasons Beneficial Owner meets Treaty Article Terms"]

new_df.head()


og_pdf = "fw8ben.pdf"
reader = PdfReader(og_pdf)
fields = reader.get_form_text_fields()


for index, row in new_df.iterrows():
    writer = PdfWriter()
    page = reader.pages[0]
    fields = reader.get_fields()
    writer.add_page(page)

    for key in fields:
        if key in row:
            writer.update_page_form_field_values(
                writer.pages[0], {key: row[key]}
            )
    for i in range(len(page["/Annots"])): 
        if (page["/Annots"][i].get_object())['/FT']=="/Btn" and (page["/Annots"][i].get_object())['/T']=='topmostSubform[0].Page1[0].c1_02[0]': 
            writer_annot = page["/Annots"][i].get_object() 
            writer_annot.update(
            {
                NameObject("/V"): NameObject(
                    "/Yes"), 
                NameObject("/AS"): NameObject(
                    "/Yes" 
                )
            }
        )
    name = row["f_1[0]"]
    last_name = name.split(' ')[-1]
    filename = name[0] + last_name + og_pdf
    with open(filename, "wb") as output_stream:
        writer.write(output_stream)






