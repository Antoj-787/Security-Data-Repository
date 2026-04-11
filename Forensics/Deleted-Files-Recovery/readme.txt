Deleted File Recovery Dataset (Lostfolder.e01)
Overview
This dataset contains a forensic disk image created from a USB drive used to simulate a deleted‑file recovery scenario. The purpose of this dataset is to demonstrate how digital forensic tools identify, recover, and analyze deleted files, metadata, and file system artifacts.

The image was created using FTK Imager and saved in E01 (EWF) format, which preserves file system structure, unallocated space, and deleted file remnants.

Dataset Contents
The dataset includes:

Lostfolder.e01 — A full forensic image of a USB drive

Deleted files originally stored in:

misc/

File types included:

.txt

.pdf

.csv

.jpg

.png

.mp3

sample code files (sample-c++, sample-react-native, etc.)

This variety ensures strong coverage for file carving, metadata analysis, and timestamp reconstruction.

How the Dataset Was Created
1. Folder Preparation
A folder named lost-folder was created with three subdirectories:

Code
Lostfolder/
   misc/
Each subfolder contained a mix of documents, images, videos, and text/code samples.

2. Deletion Process
All files inside the folder were:

Deleted normally

Removed from the Recycle Bin

This ensured the files became logically deleted but still recoverable at the disk level.

3. Imaging the USB Drive
A USB drive was used to store the folder. After deletion, the entire USB drive was imaged using FTK Imager:

File → Create Disk Image

Physical Drive selected (USB)

Image Type: E01 (EWF)

Output: lost-folder.e01

This captured:

Deleted file entries

File system metadata

Unallocated space

Carvable data

Timestamps

Tools Used
FTK Imager
Used to create the forensic image of the USB drive.

Autopsy (Recommended for Analysis)
Autopsy can be used to:

View deleted files

Recover file content

Analyze timestamps

Inspect folder structure

Perform file carving

Examine metadata

Learning Objectives
This dataset is designed to help students and analysts practice:

Deleted file recovery

File system analysis

Metadata interpretation

Timeline reconstruction

Carving files from unallocated space

Understanding E01 forensic images

Using FTK Imager and Autopsy in a workflow

Expected Findings in Autopsy
When loaded into Autopsy, you should see:

Deleted files marked with red “X” icons

Recoverable content from:

documents

images

videos

text/code samples

File metadata (MAC times)

Folder structure reconstruction

Carved files from unallocated space

Use Cases
This dataset is ideal for:

Digital forensics coursework

Lab exercises

Demonstrating deleted file recovery

Teaching forensic imaging

Practicing Autopsy workflows

Creating timeline analysis examples