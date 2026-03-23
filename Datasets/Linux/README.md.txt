# Linux Logs Dataset

## Dataset Name
Linux Authentication & System Logs

## Source
Public cybersecurity datasets (e.g., Stratosphere IPS) and simulated lab environments.

## Description
This dataset contains Linux system logs that record authentication attempts and system activity. 
These logs help in detecting unauthorized access, brute-force attacks, and suspicious command usage.

## Files Included
- auth.log (SSH login attempts)
- syslog (system activity logs)

## File Format
- Format: Plain text (.log)
- Encoding: UTF-8
- Size: Small (1–5 MB)

## Suggested Tools for Analysis
- Linux terminal (grep, awk, less)
- Splunk / ELK Stack
- Python scripts

## Learning Objectives
Students can learn:
- Detect SSH brute-force attacks
- Analyze login attempts
- Understand Linux logging systems
- Identify suspicious activity patterns

## Example Investigation
1. Open `auth.log`  
2. Search for "Failed password" using grep  
3. Identify repeated login attempts  
4. Analyze IP addresses  

## Safety Notes
All logs are from public or simulated sources. 
No sensitive information is included.