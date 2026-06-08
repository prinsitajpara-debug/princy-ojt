# Employee Management System

A Flask REST API for managing employees.

## Installation

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python run.py
```

## Run Tests

```bash
pytest -v
```

## API Endpoints

### Create Employee

POST /employees

### Get Employees

GET /employees

### Get Employee

GET /employees/{id}

### Update Employee

PUT /employees/{id}

### Delete Employee

DELETE /employees/{id}