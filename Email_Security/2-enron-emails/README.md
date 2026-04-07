# Dataset Name
The Enron Email Dataset - Structured CSV Version

## Source
Kaggle Datasets - https://www.kaggle.com/datasets/rcmonteiro/structured-enron-dataset
Original Corpus: http://www.cs.cmu.edu/~enron/

## Description
This dataset contains 517,401 legitimate corporate emails from approximately 150
Enron employees (2001-2002). The structured CSV version organizes all email metadata
including sender, recipient, subject, date, and message body. Unlike phishing datasets,
these represent genuine corporate communications, making them valuable for understanding
normal email patterns, SMTP headers, and enterprise behavior. When paired with phishing
datasets, enables effective comparison of legitimate vs. malicious characteristics.

## File Format
- Format: CSV
- Size: 335 MB
- Columns: From, To, Date, Subject, Message, CC, BCC
- Encoding: UTF-8
- Records: 517,401 emails
- Date Range: 1998-2002

## Suggested Tools for Analysis
- Python (pandas, numpy)
- Jupyter Notebook
- Splunk/ELK Stack
- Excel/LibreOffice Calc
- Regular expressions
- Natural language processing tools

## Learning Objectives
Students can learn:
- Email header structure and SMTP metadata
- Legitimate vs. malicious email patterns
- Feature extraction from email data
- Data preprocessing for datasets
- Email traffic pattern analysis
- Statistical analysis of metadata

## Why This Dataset Is Included
Provides legitimate email baseline for comparison, contains real corporate SMTP headers,
is public and legal (bankruptcy record), offers massive scale (517K emails), teaches
critical skill of distinguishing legitimate from malicious emails.

## Testing Results (Week 3)
- [OK] CSV file successfully downloaded (335 MB)
- [OK] All 517,401 records load without errors
- [OK] Column structure verified
- [OK] Email addresses in valid format
- [OK] Dates convert correctly to datetime
- [OK] Message bodies parse with UTF-8
- [OK] No significant corruption detected

## Safety Notes
Completely public and legal. All emails from Enron bankruptcy proceedings (public
record). No active credentials or sensitive financial data. Safe for all academic
and training purposes.