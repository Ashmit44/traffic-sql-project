# Traffic Chalan Management System

![Screenshot 2025-03-23 004227](https://github.com/user-attachments/assets/4677d969-fdfd-465d-a0a7-24366d9b465e)


Real-time dashboard for tracking traffic violations and fines.

## Features
- Interactive Dash visualizations
- MySQL database integration
- Payment status tracking
- Violation type analysis

## Setup
1. Install MySQL and create database:
   ```sql
   CREATE DATABASE violations_db;
   ```

2. Import schema and data:
   ```bash
   mysql -u root -p violations_db < database/schema.sql
   mysql -u root -p violations_db < database/sample_data.sql
   ```

3. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file with your credentials

5. Run the dashboard:
   ```bash
   python src/dashboard.py
   ```

## Tech Stack
- Python 3.11+
- MySQL 8.0+
- Dash/Plotly
- SQLAlchemy
