# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:00:02 2022

@author: Tamer_Saleh
"""

import pandas as pd, numpy as np
from collections import Counter

### G-Sheet Online Link

'''
https://docs.google.com/spreadsheets/d/1u0rZWrmc--iKCJ9AYHDZNHBaFzjR7CZewjJNDE9ex6E/edit#gid=0
'''
## get data 

gsheet_id = "1u0rZWrmc--iKCJ9AYHDZNHBaFzjR7CZewjJNDE9ex6E"
slide_name = "Sheet1"

sheet_url = f"https://docs.google.com/spreadsheets/d/{gsheet_id}/gviz/tq?tqx=out:csv&sheet={slide_name}"

df = pd.read_csv(sheet_url)

# Data cleaning and formatting

df.rename(columns = {df.columns[0]:"topic", df.columns[1]: "status", df.columns[2]: "contributor_name", df.columns[3]:"md_link", df.columns[4]:"contributor_notes", df.columns[5]:"revised_status", df.columns[6]:"revised_link"}, inplace=True)
df = df[1:]
df.reset_index(inplace=True, drop=True)

df[["contributor_name"]] = df[["contributor_name"]].fillna("Not_Assigned")

df["contributor_name"] = list(map(lambda x: str(x.strip()), list(df["contributor_name"])))
df["contributor_name"] = list(map(lambda x: x.title(), list(df["contributor_name"])))

contributions_qty = dict(Counter(list(df.contributor_name)))
idx_contributor = df.columns.get_loc("contributor_name")
df["contributions_per_person"] = 0
idx_cont_per_person = df.columns.get_loc("contributions_per_person")

# Contributions count per translator

for idx in range(len(df.index)):
    if df.iloc[idx, idx_contributor] in contributions_qty.keys():
        df.iloc[idx, idx_cont_per_person] = contributions_qty[df.iloc[idx, idx_contributor]]

# Completion rate per translator

idx_status = df.columns.get_loc("status")
df["Completion_Rate"] = 0
idx_com_rate = df.columns.get_loc("Completion_Rate")
aux = df.loc[df.status == "Completed"] 
completed_per_person = dict(Counter(list(aux.contributor_name)))
df["completed_to_total"] = 0
idx_com_to_total = df.columns.get_loc("completed_to_total")
for idx in range(len(df.index)):
    if df.iloc[idx, idx_contributor] in completed_per_person.keys():
        df.iloc[idx, idx_com_rate] = round(completed_per_person[df.iloc[idx, idx_contributor]] / df.iloc[idx, idx_cont_per_person],2)*100
        df.iloc[idx, idx_com_to_total] = round(completed_per_person[df.iloc[idx, idx_contributor]] / sum(completed_per_person.values()), 2)*100

overall = {"Articles_Qty": len(df.index), "Completed": sum(completed_per_person.values()), "completion_pct": round(sum(completed_per_person.values())/len(df.index),2)}
print(df)

##### final_df >> "Contributor Name" - "Contribution_per_person" - "Completion_Rate" - "completed_to_total"

trimmed_df = df.copy()
trimmed_df = trimmed_df[["contributor_name", "contributions_per_person", "Completion_Rate", "completed_to_total"]]
trimmed_df = trimmed_df.sort_values(["contributor_name"])
trimmed_df.reset_index(inplace=True, drop=True)
idx_cont_name = trimmed_df.columns.get_loc("contributor_name")


trimmed_df["contributor_name"] = np.where(trimmed_df.iloc[:, idx_cont_name] != trimmed_df.iloc[:, idx_cont_name].shift(-1), trimmed_df.iloc[:, idx_cont_name], "to_del")


final_df = trimmed_df.loc[trimmed_df["contributor_name"] != "to_del"]
final_df.reset_index(inplace=True, drop=True)

print(final_df,"\n",overall)
