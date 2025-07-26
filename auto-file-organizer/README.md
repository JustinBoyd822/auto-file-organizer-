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
The script will:

Create subfolders in your source folder for each file type
Move files into their appropriate folders
Log all operations to log/run.log

Example
Before running:
Downloads/
├── document.pdf
├── photo.jpg
├── music.mp3
└── spreadsheet.xlsx
After running:
Downloads/
├── Documents/
│   └── document.pdf
├── Images/
│   └── photo.jpg
├── Audio/
│   └── music.mp3
└── Spreadsheets/
    └── spreadsheet.xlsx
Logging
All file operations are logged in log/run.log with timestamps. Check this file to see what files were moved or if there were any issues.
Adding New File Types
To support additional file types, simply add them to the file_types section in config.yaml:
yamlfile_types:
  .pdf: Documents
  .mp4: Videos
  .py: Code
  # Add more as needed
Notes

Files with extensions not listed in the config will remain in the source folder
The script creates folders as needed - you don't need to create them manually
All operations are logged for your reference
