# Expense Project

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
│   │    └── csv_reader.py
│   ├── validation
│   │    └── expense_schema.py
│   ├──export
│   │    └── export_csv.py
│   └── db
│       ├── connection.py
│       ├── create_tables.py
│       ├── get_category_summary.py
│       ├── get_expenses_by_date.py
│       ├── get_expenses.py
│       ├── get_total.py
│       └── insert_expense.py
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



## Tech Stack

* Python
* PostgreSQL
* Docker
* Pytest
* Pydantic





