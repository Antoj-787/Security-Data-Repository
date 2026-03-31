README 4 — Phishing-Based Infection Chain: XWorm RAT (2025‑11‑19)
Overview
This dataset captures a phishing email leading to an XWorm RAT infection. XWorm is a remote‑access trojan capable of keylogging, credential theft, remote command execution, and persistence.

Key Behaviors Observed
Malicious email attachment execution

XWorm establishing C2 communication

Encrypted RAT traffic

Remote command channel setup

Beaconing intervals and persistence attempts

Why This Dataset Matters
This PCAP replaces the older 2016 phishing dataset and provides a modern phishing‑to‑malware infection chain, including:

User interaction (opening attachment)

Malware execution

RAT communication

C2 callbacks

Useful Wireshark Filters
Code
tcp.port == 4444
frame contains "POST"
ip.addr == <infected-host-ip>
File Included
Code
2025-11-19-worm-infection-traffic.pcap