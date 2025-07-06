# Python Generator - SQL Streaming

## Objective

Create a script to set up a MySQL database and stream data row-by-row using a generator pattern.

## Features

- Connects to MySQL server
- Creates `ALX_prodev` database and `user_data` table
- Populates data from `user_data.csv`
- Prepares for generator-based streaming

## Usage

Make sure MySQL is running and accessible.

1. Update `seed.py` with your MySQL credentials.
2. Place `user_data.csv` in the same directory.
3. Run the driver script (e.g., `0-main.py`).

```bash
./0-main.py