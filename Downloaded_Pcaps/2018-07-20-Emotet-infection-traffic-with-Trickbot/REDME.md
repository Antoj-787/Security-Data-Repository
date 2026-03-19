🟩 README 2 — Emotet Initial Infection Followed by Trickbot (2018‑07‑20)
Overview
This dataset captures an Emotet infection that later downloads and executes Trickbot as a secondary payload. Emotet acts as a loader, spreading through malspam and enabling follow‑up malware deployment.

Key Behaviors Observed
Emotet HTTP-based C2 traffic

Download of Trickbot payload

Trickbot establishing persistence

Trickbot C2 communication

Modular malware behavior

Why This Dataset Matters
This PCAP demonstrates a classic multi‑stage infection chain:

Emotet loader

Payload retrieval

Trickbot execution

C2 communication

This mirrors real-world enterprise compromises.

Useful Wireshark Filters
Code
http.request
tcp.port == 447
ip.addr == <infected-host-ip>
File Included
Code
2018-07-20-Emotet-infection-traffic-with-Trickbot.pcap