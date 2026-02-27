# Auto Organizer – Cross-Platform Desktop File Organizer

## Description

Auto Organizer is a tool that automatically organizes your desktop files by type  
(images, text files, Excel, PowerPoint, etc.) and moves them into categorized folders.  
It runs daily on **Windows, Linux, and macOS** and requires **no code editing**, just a simple configuration file.



## Features

- 🔹 **Cross-platform:** Works on Windows, Linux, and macOS  
- 🔹 **Configurable:** Change folders, file types, and schedule via `config.json`  
- 🔹 **Automatic scheduling:** Sets up Task Scheduler (Windows) or cron job (Linux/macOS)  
- 🔹 **Logging:** Tracks every moved file in `automation.log`  
- 🔹 **User-friendly:** Works for beginners and developers alike  

---

## Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/DIANEDWEIRI /auto-organizer.git

2️⃣ Install required package:

pip install schedule

1️⃣ Configure Settings

Edit the config.json file:

{
  "source_folder": "Desktop",
  "destination_folder": "Desktop/Organized",
  "schedule_time": "06:10",
  "file_types": {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "TextFiles": [".txt", ".pdf", ".docx"],
    "PowerPoint": [".pptx"],
    "Excel": [".xlsx", ".csv"]
  }
}
2️⃣ Automatic Scheduling

Run the scheduler script:

python scheduler.py

Windows → sets up Task Scheduler automatically

Linux/macOS → installs a cron job automatically

3️⃣ Manual Run (Optional)

python organizer.py
