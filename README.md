# COMP3005 – Assignment 3  
**Student:** Mohamed Cherif Bah  
**Student ID:** 101292844

## Overview

This project implements a basic student management system using Python and PostgreSQL. It supports creating a student table, inserting sample data, and performing CRUD operations through a menu-driven interface.

## Technologies

- Python 3  
- PostgreSQL  
- psycopg2

## Structure
COMP3005_Assignment3/
├── db/
│   ├── connection.py       # Handles database connection setup
│   └── schema.py           # Creates tables and inserts initial data
│
├── models/
│   └── student.py          # CRUD operations for the students table
│
├── main.py                 # Menu-driven interface to interact with the system
└── README.md               # Project overview and setup instructions

## How to Run

1. Install dependencies:

pip install psycopg2

CREATE DATABASE your_database_name;

2. Update database credentials in `db/connection.py`.

3. Run the program:


## Features

- Create and initialize `students` table  
- Insert sample data  
- View, add, update, and delete student records via menu
