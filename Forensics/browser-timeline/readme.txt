# Chrome Browser Timeline Dataset (Fake Profile)

## Overview
This dataset contains browser activity artifacts generated from a controlled, fake Chrome profile created specifically for digital forensics training. The browsing activity includes Google searches, website visits, YouTube interactions, and general navigation patterns. No real personal data is included.

## Contents
The dataset includes the following Chrome artifact files:

- History
- History-journal
- Cookies
- Cookies-journal
- Favicons
- Downloads
- Visited Links (optional)
- Top Sites (optional)

These files contain:
- URL visit timestamps
- Search queries
- Download history
- Cookie metadata
- Favicon metadata
- Navigation patterns

## Purpose
This dataset is designed for:
- Browser timeline reconstruction
- Artifact extraction
- SQLite-based analysis
- Forensic tool testing (Autopsy, Browser History Viewer, DB Browser for SQLite)

## Tools for Analysis
- Autopsy (Logical File Ingest)
- DB Browser for SQLite
- Browser History Viewer
- Chainsaw (optional for timeline merging)

## Safety
This dataset contains **no real personal browsing history**. All activity was intentionally generated for educational use.

## Example Activities Included
- Google searches (templates, cars, music, cybersecurity)
- YouTube video visits
- Reddit browsing
- Shopping site visits
- AI tool usage
- News and informational sites

## Learning Objectives
- Understand Chrome artifact structure
- Extract timestamps from History and Downloads tables
- Reconstruct user activity timeline
- Analyze cookie and favicon metadata
