![CI](https://github.com/herbertmoses/Data-Pipeline-Automation/actions/workflows/ci.yml/badge.svg)
# 🚀 End-to-End ETL Automation Pipeline (PostgreSQL + Python)

## 📌 Overview

This project implements a **fully automated, event-driven ETL pipeline** using:

- PostgreSQL (data source)
- Python (ETL + analytics)
- File-based pipeline (CSV)
- Watchdog (event detection)
- APScheduler (job scheduling)
- Email notification system

---

## 🏗 Architecture
PostgreSQL Tables
↓
ETL Scheduler (APScheduler)
↓
CSV Output (automation_input)
↓
Folder Watcher (Watchdog)
↓
Data Cleaning & Analytics (Pandas)
↓
CSV Output (automation_output)
↓
Email Notification


---

## ⚙️ Features

- ✅ Automated ETL job (runs every minute / configurable)
- ✅ Event-driven file processing
- ✅ Data cleaning & aggregation
- ✅ Email alerts on completion
- ✅ Fault-tolerant (polling + event detection)
- ✅ CI/CD pipeline (GitHub Actions)

---

## 🧰 Tech Stack

- Python 3.13
- PostgreSQL
- Pandas
- APScheduler
- Watchdog
- SMTP (Email)
- GitHub Actions

---

## 📁 Project Structure
automation_pipeline/
├── main.py
├── join_tables_etl.py
├── etl_scheduler.py
├── folder_watcher.py
├── email_sender.py
├── requirements.txt
├── .env.example
├── .gitignore
└── .github/workflows/ci.yml


---

## 🔐 Environment Setup

Create `.env` file:

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=your_lhost
DB_PORT=your_port

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com


---

## ▶️ Run the Application

```bash
python main.py

🔄 Workflow
Scheduler triggers ETL job
Data extracted from PostgreSQL
CSV written to input folder
Watcher detects new file
Data cleaned and processed
Output written to output folder
Email notification sent

## Sample Output
Starting ETL job...
ETL completed...

EVENT DETECTED...
Processing file...
Cleaned file saved...
Email sent successfully!

🚀 Future Enhancements
Apache Airflow DAG integration
Docker containerization
REST API (FastAPI)
Kafka-based streaming pipeline
Cloud deployment (AWS/GCP)

---

# 🚀 7. Push to GitHub

```bash
git init
git add .
git commit -m "Initial ETL automation pipeline"
git branch -M main
git remote add origin <your_repo_url>
git push -u origin main
