# YouTube Auto Uploader

A Python project to automatically upload videos from a folder to YouTube with scheduled uploads and AI-generated titles and descriptions.

---

## Features

- Automatically scans a folder for new `.mp4` videos.
- Uploads videos one by one to YouTube.
- Logs upload status, including successes and failures.
- 1-hour delay between uploads to avoid hitting YouTube limits.
- Fully automated title and description generation using ChatGPT (optional).
- Tracks uploaded videos to avoid duplicates.
- Scheduled folder check using a configurable interval.

---

## Project Structure

yt-auto-uploader/
│
├── .venv/ # Python virtual environment (ignored in Git)
├── uploads/ # Folder containing videos to upload
├── main.py # Main scheduler script
├── upload.py # Upload functions
├── requirements.txt # Python dependencies
├── .gitignore # Ignore .venv, .env, and other temp files
├── README.md # Project description
└── .env # Stores API keys and sensitive info (ignored in Git)
