README 1 — Ursnif Malware Infection and Data Exfiltration (2018‑01‑03)
Overview
This dataset captures network traffic from a real-world Ursnif (Gozi) banking trojan infection. Ursnif is known for credential theft, form grabbing, and data exfiltration. The PCAP shows the full infection chain, including initial execution, C2 communication, and exfiltration behavior.

Key Behaviors Observed
HTTP POST requests to command‑and‑control servers

Encrypted data exfiltration

Multiple callback attempts

Persistence-related traffic

Indicators of credential harvesting

Why This Dataset Matters
Ursnif is one of the most widely analyzed banking trojans. This PCAP provides a clear example of:

Malware beaconing

Data theft

C2 infrastructure communication

Post‑infection activity

Useful Wireshark Filters
Code
http
tcp.port == 80
ip.addr == <infected-host-ip>
File Included
Code
2018-01-03-Ursnif-infection-traffic.pcap