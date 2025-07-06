# Python Generators: Memory-Efficient Data Streaming with MySQL

## 📚 Overview

This project demonstrates how Python **generators** can be used to efficiently process large datasets from a MySQL database. Instead of loading entire tables into memory, we use generators to stream, paginate, and process data in chunks or on-demand — making the code scalable and performant.

We simulate real backend behavior such as:
- Setting up a database and populating it from a CSV file
- Streaming user records one by one
- Fetching data in batches
- Paginating data lazily
- Calculating aggregate values (like average age) efficiently without SQL's aggregation functions

---

## ⚙️ Technologies Used

- **Python 3**
- **MySQL**
- **mysql-connector-python**
- **CSV file for dataset**
- **Generators and yield expressions**

---

## 🗃️ Database Schema

**Database Name:** `ALX_prodev`  
**Table:** `user_data`

| Column Name | Type         | Description                 |
|-------------|--------------|-----------------------------|
| user_id     | UUID (PK)    | Primary key, Indexed        |
| name        | VARCHAR      | User's full name            |
| email       | VARCHAR      | User's email address        |
| age         | DECIMAL      | User's age (can be float)   |

---

## 🔧 Project Setup

1. Ensure you have MySQL installed and running.
2. Install the MySQL connector:

```bash
pip install mysql-connector-python
