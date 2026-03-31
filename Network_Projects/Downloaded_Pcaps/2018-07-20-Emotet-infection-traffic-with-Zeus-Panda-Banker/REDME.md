README 3 — Emotet Loader Delivering Zeus Panda Banker (2018‑07‑20)
Overview
This dataset captures an Emotet infection that delivers Zeus Panda, a credential‑stealing banking trojan. The PCAP includes loader activity, payload download, and Zeus Panda C2 communication.

Key Behaviors Observed
Emotet initial beaconing

Download of Zeus Panda payload

Zeus Panda HTTP POST exfiltration

Credential harvesting behavior

Multiple C2 endpoints contacted

Why This Dataset Matters
This PCAP highlights how Emotet acts as a malware delivery platform, distributing banking trojans like Zeus Panda. It demonstrates:

Loader → payload workflow

Financial malware behavior

Exfiltration patterns

Useful Wireshark Filters
Code
http
tcp.port == 80
frame contains "POST"
File Included
Code
2018-07-20-Emotet-infection-traffic-with-Zeus-Panda-Bank