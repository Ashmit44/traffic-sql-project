# Traffic Chalan Management System

![Screenshot 2025-03-23 004227](https://github.com/user-attachments/assets/4677d969-fdfd-465d-a0a7-24366d9b465e)


Real-time dashboard for tracking traffic violations and fines.

## Features
- Dash visualizations
- MySQL database integration
- Payment status tracking
- Violation type analysis

## Setup
1. Install MySQL and create database:
   ```sql
   CREATE DATABASE violations_db;
   ```

2. Execute sample dataset query file:
   

4. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

5. Create `.env` file with your credentials

6. Run the dashboard:
   ```bash
   python dashboard.py
   ```

## Tech Stack
- Python 3.11+
- MySQL 8.0+
- Dash/Plotly
- SQLAlchemy
