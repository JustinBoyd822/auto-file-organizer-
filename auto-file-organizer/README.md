Auto File Organizer
A simple Python script that automatically organizes files in your Downloads folder by creating subfolders based on file types.
Features

Organizes files by extension into categorized folders
Configurable file type mappings via YAML
Detailed logging of all file operations
Works directly within your Downloads folder (in-place organization)

Installation

Clone or download this repository
Install the required dependencies:
bash
Configuration
Edit the config.yaml file to customize:

source_folder: The folder to organize (e.g., your Downloads folder)
file_types: Mapping of file extensions to folder names

Example configuration:
source_folder: C:/Users/YourName/Downloads

file_types:
  .pdf: Documents
  .docx: Documents
  .txt: Text
  .png: Images
  .jpg: Images
  .zip: Archives
  .mp3: Audio
  .xlsx: Spreadsheets
