# Expense Data Pipeline Project

A simple **data engineering pipeline** built using **Python, PostgreSQL, and Docker**.
The pipeline ingests expense data from CSV files, validates it, stores it in a database, and allows querying through a CLI.

---

## Project Overview

This project demonstrates a basic **data pipeline architecture**:

* Read expense data from CSV files
* Validate records using **Pydantic**
* Store data in **PostgreSQL**
* Query and analyze data using CLI commands
* Export results in tabular format

---

## Architecture

```
CSV Files
   │
   ▼
CSV Reader
   │
   ▼
Validation Layer (Pydantic)
   │
   ▼
PostgreSQL Database
   │
   ▼
CLI Commands
   │
   ▼
Tabular Output / Export
```

---

## Project Structure

```
expense_project
│
├── app
│   ├── cli.py
│   ├── ingestion
│   ├── validation
│   └── db
│
├── data
│   └── expenses.csv
│
├── tests
│   ├── conftest.py
│   ├── test_csv_reader.py
│   └── test_validation.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── ARCHITECTURE.md
└── README.md
```

---

## Features

* CSV data ingestion
* Schema validation using **Pydantic**
* Storage in **PostgreSQL**
* CLI-based analytics queries
* Tabular output using **tabulate**
* Containerized with **Docker**
* Unit testing using **pytest**

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run ingestion

```bash
python main.py ingest
```

### Run analytics

```bash
python main.py analytics
```

### Run tests

```bash
pytest
```

---

## Tech Stack

* Python
* PostgreSQL
* Docker
* Pytest
* Pydantic
