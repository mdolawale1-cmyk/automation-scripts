
# ⚙️ Automation Scripts Repository

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Repo Size](https://img.shields.io/github/repo-size/mdolawale1-cmyk/automation-scripts)
![Last Commit](https://img.shields.io/github/last-commit/mdolawale1-cmyk/automation-scripts)
![Issues](https://img.shields.io/github/issues/mdolawale1-cmyk/automation-scripts)
![Stars](https://img.shields.io/github/stars/mdolawale1-cmyk/automation-scripts?style=social)

A collection of practical automation scripts for **incident management, monitoring, and system optimization**.  
This repository demonstrates skills in Python scripting, Linux administration, and proactive system reliability engineering.

---

## 📂 Repository Structure
```bash
automation-scripts/
│
├── dashboards/
│   └── system_health_dashboard.py
│
├── database/
│   └── check_db_connection.py
│
├── monitoring/
│   ├── disk_space_alert.py
│   ├── disk_usage.sh
│   ├── memory_usage.sh
│   ├── monitor_cpu.sh
│   ├── network_check.py
│   └── process_monitor.py
│
├── notifications/
│   └── alert_email.py
│
├── samples/
│   ├── disk_space_alert_example.log
│   ├── log_parser_summary_example.txt
│   ├── memory_alert_example.txt
│   ├── service_status_report_example.txt
│   └── system_health_dashboard_example.txt
│
├── utilities/
│   ├── .gitignore
│   ├── LICENSE
│   ├── README.md
│   └── requirements.txt

```
- **database/** → Database health checks  
- **monitoring/** → System monitoring scripts (CPU, memory, disk, processes, network)  
- **utilities/** → General automation tasks (cleanup, rotation, reporting, parsing logs)  
- **notifications/** → Alerting scripts (e.g., email notifications)  
- **dashboards/** → Consolidated system health reports  
- **samples/** → Example outputs from scripts (alerts, reports, dashboards)

---

## 🚀 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mdolawale1-cmyk/automation-scripts.git
   cd automation-scripts

## 🛠️ Script Categories

### Database
- `check_db_connection.py` → Verifies database connectivity

### Monitoring
- `monitor_cpu.sh` → Tracks CPU usage  
- `memory_usage.sh` → Monitors memory usage  
- `disk_usage.sh` → Checks disk usage  
- `disk_space_alert.py` → Alerts when disk usage exceeds threshold  
- `network_check.py` → Tests network connectivity  
- `process_monitor.py` → Ensures critical processes are running  

### Utilities
- `cleanup_temp_files.py` → Removes temporary files  
- `service_restart.py` → Restarts services automatically  
- `error_report.py` → Generates error reports  
- `backup_cleanup.py` → Cleans old backups  
- `log_rotation.sh` → Rotates logs  
- `service_status_report.py` → Summarizes service status  
- `log_parser.py` → Counts errors/warnings in logs  

### Notifications
- `alert_email.py` → Sends email alerts

### Dashboards
- `system_health_dashboard.py` → Generates consolidated Markdown/HTML system health report

   

## Install dependencies:
```bash
pip install -r requirements.txt

