# 🗂️ Auto File Organizer

A simple Python script to automatically organize files in a folder based on file type, using a customizable YAML configuration.

## 📁 What It Does

This script scans a specified folder and automatically moves files into subfolders based on their extensions. For example, all `.pdf` files can be moved into a `Documents` folder, `.jpg` files into an `Images` folder, and so on.

## ✅ Features

- Organizes files based on extension
- Customizable config using YAML
- Automatically creates missing folders
- Logs actions to a file
- Cross-platform (Linux, macOS, Windows)

---

## ⚙️ How It Works

1. The script loads settings from a `config.yaml` file.
2. It checks the `source_folder` and scans all files inside it.
3. Based on the `file_types` mapping, files are moved into the appropriate subfolder.
4. A log of all moved and skipped files is saved in the `/log` directory.

---

## 📝 Example `config.yaml`

```yaml
source_folder: /path/to/your/source/folder

file_types:
  .pdf: Documents
  .docx: Documents
  .txt: Text
  .png: Images
  .jpg: Images
  .zip: Archives
  .mp3: Audio
  .xlsx: Spreadsheets

Change /path/to/your/source/folder to the directory you want to organize.
🚀 Getting Started
1. Clone the repo

git clone https://github.com/yourusername/auto-file-organizer.git
cd auto-file-organizer

2. Install requirements

pip install -r requirements.txt

3. Run the script

python organizer.py

📦 Requirements

    Python 3.6+

    PyYAML

Install with:

pip install pyyaml

📄 Logs

All activity is saved to a log file in the log/ directory:

log/run.log

💡 Tips

    Add or remove file types in the config.yaml to suit your needs.

    Schedule this script with Task Scheduler (Windows) or cron (Linux/macOS) for automatic cleanup.
