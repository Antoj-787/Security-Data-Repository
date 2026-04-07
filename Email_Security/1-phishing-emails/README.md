# Dataset Name
Phishing Email Dataset - Multiple Sources (SpamAssassin Corpus)

## Source
Kaggle Datasets - https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset
Compiled by Nasera Abdullah Alam from multiple public sources

## Description
This comprehensive dataset contains 82,500+ email samples collected from SpamAssassin,
TREC2007, Enron, and Nazario phishing corpus. Each email is labeled as either
spam/phishing or legitimate. The dataset includes complete email metadata: sender,
receiver, date, subject line, and message body. This dataset is essential for
understanding real-world phishing tactics, building email classification models,
and analyzing patterns in malicious emails.

## File Format
- Format: CSV
- Size: 14.88 MB (SpamAssassin.csv)
- Columns: From, To, Date, Subject, Body, Label (spam/legitimate)
- Encoding: UTF-8
- Records: 82,500+ emails

## Suggested Tools for Analysis
- Python (pandas, scikit-learn)
- Jupyter Notebook
- Splunk or ELK Stack
- Excel/LibreOffice Calc
- grep/awk (pattern extraction)

## Learning Objectives
Students can learn:
- Common phishing patterns and tactics
- Email metadata analysis
- Feature engineering for classification
- Machine learning models for spam detection
- Sender spoofing and social engineering techniques

## Why This Dataset Is Included
Provides real-world phishing examples paired with legitimate messages, is publicly
available and legal, contains no sensitive information, offers sufficient scale for
ML training, demonstrates practical email threat detection.

## Testing Results (Week 3)
- [OK] CSV file successfully downloaded (14.88 MB)
- [OK] All 82,500+ records load in pandas
- [OK] Email labels verified (spam/legitimate)
- [OK] Special characters handled correctly (UTF-8)
- [OK] URLs extracted successfully
- [OK] No data corruption detected

## Safety Notes
Completely public, legal, and free of sensitive information. All emails from public
sources. No real credentials or PII exposed. Safe for all educational purposes.