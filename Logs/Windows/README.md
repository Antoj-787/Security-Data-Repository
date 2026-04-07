# Windows Logs Dataset

## Dataset Name
Windows Event Logs (Failed Login & PowerShell Activity)

## Source
Generated in a controlled Windows environment and supplemented with public DFIR datasets.

## Description
This dataset contains Windows Event Logs that capture system and security-related activities. 
It includes failed login attempts and PowerShell command execution logs. These logs are commonly used in digital forensics and security monitoring.

## Files Included
- failed_login.evtx (Event ID 4625 – failed login attempts)
- powershell_logs.evtx (PowerShell activity logs)

## File Format
- Format: EVTX (Windows Event Log)
- Size: Small (1–10 MB per file)

## Suggested Tools for Analysis
- Event Viewer (Windows)
- Chainsaw (log analysis tool)
- Autopsy (digital forensics)
- PowerShell

## Learning Objectives
Students can learn:
- How to detect failed login attempts
- Identify brute-force attacks
- Analyze PowerShell activity
- Understand Windows Event IDs

## Example Investigation
1. Open `failed_login.evtx` in Event Viewer  
2. Filter Event ID 4625  
3. Identify repeated login attempts  
4. Analyze source IP addresses  

## Safety Notes
These logs are generated in a controlled environment or obtained from public datasets. 
No sensitive or personal data is included.