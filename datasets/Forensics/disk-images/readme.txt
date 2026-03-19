Dataset Name
NPS‑2009‑Canon2 (Generation 1) – FAT32 SD Card Image

Source
Digital Corpora – NPS Test Disk Images
Public domain dataset created by the Naval Postgraduate School (NPS).

Download Link
https://drive.google.com/file/d/1lRq-XdS5W7NCHSaz9G-bS_nNuDeah2ve/view?usp=sharing

Description
This dataset is a 32MB FAT32 SD card image captured from a Canon PowerShot SD800IS digital camera.
The image represents the first generation of a multi‑stage forensic test scenario where photos were taken, deleted, and the card was repeatedly re‑imaged.

The dataset contains:

JPEG images numbered 1–36

Additional images labeled G2–G6, some of which are fragmented

A mix of:

Fully intact JPEGs

Deleted but recoverable files

Files with no filesystem metadata (carvable only)

Fragmented JPEGs requiring advanced carving techniques

This makes the dataset ideal for demonstrating:

File carving

Fragmentation analysis

Deleted file recovery

FAT32 filesystem behavior

File Format
E01 or RAW (depending on download)

Size: ~31 MB

Filesystem: FAT32

Suggested Tools for Analysis
Autopsy / Sleuth Kit

Bulk Extractor

PhotoRec / Scalpel (file carving)

Hex editors (fragmentation analysis)

Learning Objectives
Understand how digital cameras store and delete images

Explore FAT32 allocation behavior

Practice recovering deleted and fragmented JPEGs

Compare filesystem metadata vs. raw data carving

Why This Dataset Is Included
This dataset provides a simple, controlled environment for learning core disk forensics concepts. Its small size and predictable structure make it ideal for teaching and documentation.

Safety Notes
This dataset is public, legal, and contains no sensitive or personal information.
 