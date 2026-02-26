# -------------------------------------------------------
# TASK 1: WEB SCRAPING PROJECT
# Project: Job Market Analytics
# -------------------------------------------------------

# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# -------------------------------------------------------
# Step 1: Website URL
# -------------------------------------------------------
url = "https://realpython.github.io/fake-jobs/"

# -------------------------------------------------------
# Step 2: Send request to website
# -------------------------------------------------------
response = requests.get(url)

# Check connection
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# -------------------------------------------------------
# Step 3: Parse HTML
# -------------------------------------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------------------------------
# Step 4: Find all job cards
# -------------------------------------------------------
jobs = soup.find_all("div", class_="card-content")

# -------------------------------------------------------
# Step 5: Extract job details
# -------------------------------------------------------
job_data = []

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_data.append([title, company, location])

# -------------------------------------------------------
# Step 6: Create DataFrame
# -------------------------------------------------------
df = pd.DataFrame(job_data, columns=[
    "Job Title",
    "Company",
    "Location"
])

# -------------------------------------------------------
# Step 7: Save dataset
# -------------------------------------------------------
file_name = "jobs_dataset.csv"
df.to_csv(file_name, index=False)

# -------------------------------------------------------
# Step 8: Display Results
# -------------------------------------------------------
print("\n✅ Data Scraped Successfully!")
print("\nFile saved at:", os.getcwd())

print("\nFirst 5 Records:\n")
print(df.head())

print("\nTotal Jobs Found:", len(df))

# -------------------------------------------------------
# Step 9: Basic Job Market Analysis
# -------------------------------------------------------
print("\n-----------------------------")
print(" JOB MARKET ANALYSIS REPORT ")
print("-----------------------------")

# Top job titles
print("\nTop Job Titles:")
print(df["Job Title"].value_counts().head(5))

# Top hiring companies
print("\nTop Hiring Companies:")
print(df["Company"].value_counts().head(5))

# Jobs by location
print("\nJobs by Location:")
print(df["Location"].value_counts().head(5))


print("\nTotal Unique Companies:", df["Company"].nunique())
print("Total Unique Locations:", df["Location"].nunique())


