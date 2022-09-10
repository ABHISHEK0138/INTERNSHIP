# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:13:48 2022

@author: ABHISHEK
"""
'''ANALYSIS OF DATA SCIENCCE JOB SALARIES'''

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
'''import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))'''
df = pd.read_csv("ds_salaries.csv")
#finding company information
df.info()

df.head(10)

df.describe()
df.shape

df['Unnamed: 0']

df = df.drop(['Unnamed: 0'], axis=1)
df.nunique()

df.describe().T

df.corr()

#data preprocessing
df.isnull().sum()

x1=df["job_title"].unique()
df1=df["job_title"].value_counts()
df1
#company size
df.groupby("company_size").mean()['salary_in_usd'].sort_values(ascending=False)

median_salaries = df[['job_title', 'salary_in_usd']].groupby('job_title').median()
median_salaries

df['experience_level'].unique()

df['experience_level'].value_counts()

#job title in different year
print(df.loc[df['work_year']==2020,'job_title'].value_counts()[:5])
print(df.loc[df['work_year']==2021,'job_title'].value_counts()[:5])
print(df.loc[df['work_year']==2022,'job_title'].value_counts()[:5])

#number of jobs
df2=df1.iloc[:5]
plt.rcParams["figure.figsize"] = (10, 5)
plt.title('Number of Jobs', fontsize=18)
df["job_title"].value_counts().plot(kind='bar',width = 0.9, color = "red")
plt.xlabel('Job Titles')
plt.ylabel('Count')
plt.show()

#percentage of job titles
plt.rcParams["figure.figsize"] = (7,7)
plt.title('Percentage of job titles', fontsize=18)
df2.plot(kind='pie',autopct='%0.2f%%',shadow=True)
plt.legend(loc="lower left")
plt.figure(figsize=(20, 100))
plt.show()

#number of jobs in all country
df3=df["company_location"].value_counts()
df4=df3.iloc[:6]
plt.rcParams["figure.figsize"] = (8, 5)
plt.title('Number of Jobs', fontsize=18)
df4.plot(kind='bar',width = 0.9)
plt.xlabel('Country')
plt.ylabel('Count')

#Bargraph to represent Median salaries of each job
plt.rcParams["figure.figsize"] = (12, 5)
median_salaries.plot(kind='bar',width = 0.9)
plt.legend()
plt.xlabel('Jobs')
plt.ylabel('Salary')

df['experience_level'].value_counts().plot(kind='pie',autopct='%1.1f%%', figsize=(7,7), wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'dashed', 'antialiased': True},explode=(0.01,0.01,0.01,0.1))

print(df['job_title'].value_counts()[:4].plot(kind='bar', title='Top 4 Job profiles(according to numbers of employess)', xlabel='Job Profiles', ylabel='Number of Employees', figsize=(10,7), color=['#dcecc9', '#aadacc', '#78c6d0', '#48b3d3', '#3e94c0', '#3474ac', '#2a5599', '#203686']))

print(df['salary_currency'].unique())
print(df['salary_currency'].nunique())
print(df['salary_currency'].value_counts())
print(df['salary_currency'].value_counts().plot(kind='bar'))

df.value_counts().plot(kind='bar', xlabel='Remote Ratio', ylabel='Number of employees', title='Number of employees remotely located', color=['maroon','red','orange'])

print(df['company_size'].unique())
print(df['company_size'].value_counts())
print(df['company_size'].value_counts().plot(kind='pie',autopct='%1.1f%%', figsize=(7,7), wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'dashed', 'antialiased': True},explode=(0.01,0.01,0.1),))

#Companies in US in different years
print(df.loc[df['company_location']=='US','work_year'].value_counts())
print(df.loc[df['company_location']=='US','work_year'].value_counts().plot(kind='pie',figsize=(10,8),autopct='%1.1f%%',explode=(0.01,0.01,0.1)))

#Numbers of companies in INDIA in different years
print(df.loc[df['employee_residence']=='IN','work_year'].value_counts())
print(df.loc[df['employee_residence']=='IN','work_year'].value_counts().plot(kind='bar',figsize=(10,8),color=['violet','pink','orange'], ylabel='Numbers of company', xlabel='years', title='Number of companies in INDIA in different years').set_facecolor("black"))

#number of data scientists in india
print(df.loc[(df['company_location']=='IN') & (df['job_title']=='Data Scientist'),'work_year'].value_counts())
print(df.loc[(df['company_location']=='IN') & (df['job_title']=='Data Scientist'),'work_year'].value_counts().plot(kind='bar', figsize=(10,8), color=['red','orange','yellow'],xlabel='Years',ylabel='Number of Data scientist jon in India', title='Number of Data scientist in INDIA').set_facecolor('black'))

#Experience v/s salary
print(df.groupby("experience_level").mean()['salary_in_usd'].sort_values(ascending=False))
df.groupby("experience_level").mean()['salary_in_usd'].sort_values(ascending=False).plot(kind='bar',figsize=(10,8),color=['purple','blue','green','cyan'],ylabel='Average salary', xlabel='Experience level', title='Experience v/s Average salary').set_facecolor("black")

#Employment type of Data scientist
df.loc[df['job_title']=='Data Scientist','employment_type'].value_counts()
df.loc[df['job_title']=='Data Scientist','employment_type'].value_counts().plot(kind='pie',autopct='%1.1f%%', figsize=(10,8), title="Data scientist employees type")

