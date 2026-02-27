# Code Alpha Internship – Task 1
## Web Scraping Project: Job Market Analytics

### 📌 Project Overview
This project was developed as part of my **Code Alpha Internship – Task 1**.  
The objective of this project is to perform **web scraping using Python** to collect job market data from a website and convert unstructured web information into a structured dataset for analysis.

The project extracts job-related details such as job title, company name, and location, and performs basic job market analysis.

---

### 🛠️ Technologies Used
- Python
- Requests Library
- BeautifulSoup
- Pandas
- CSV File Handling

---

### ⚙️ Project Workflow

1. Sent an HTTP request to the website using the `requests` library.
2. Parsed the HTML content using `BeautifulSoup`.
3. Extracted job details including:
   - Job Title
   - Company Name
   - Location
4. Stored extracted data into a Pandas DataFrame.
5. Saved the structured data as a CSV file.
6. Performed basic job market analysis.

---

### 📊 Analysis Performed
- Identification of top job titles
- Top hiring companies
- Job distribution based on locations
- Count of unique companies and locations

---

### 📁 Project Files
- `scrape_jobs.py` → Python script for web scraping
- `jobs_dataset.csv` → Extracted job dataset
- `README.md` → Project documentation

---

### 📈 Output
The scraped job data is saved as:
jobs_dataset.csv


This dataset can be further used for data analysis and visualization projects.

---

### 🎯 Learning Outcomes
- Understanding Web Scraping concepts
- Extracting real-world data from websites
- HTML parsing using BeautifulSoup
- Data manipulation using Pandas
- Performing basic data analysis

---
