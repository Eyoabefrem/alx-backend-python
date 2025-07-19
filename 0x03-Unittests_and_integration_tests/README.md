# ALX Backend Python - Unit and Integration Tests

## 📌 Project Description
This project is part of the **ALX Backend Specialization** focusing on mastering **unit testing**, **mocking**, **patching**, **parameterization**, and **integration testing** in Python.

Through this project, we create comprehensive tests for utility functions, HTTP client methods, memoization, and simulate real-world API interactions by mocking external calls.

---

## 🛠️ Technologies Used
- Python 3
- `unittest` for testing framework
- `parameterized` for parameterized tests
- `unittest.mock` for mocking and patching
- `requests` for HTTP calls
- `pytest` (optional, for enhanced test runs)

---

## 📁 Project Structure
0x03-Unittests_and_integration_tests/
│
├── utils.py # Utility functions (e.g., access_nested_map, get_json, memoize)
├── client.py # GithubOrgClient for interacting with GitHub API
├── fixtures.py # Test data (fixtures) for integration tests
│
├── test_utils.py # Unit tests for utils.py
├── test_client.py # Unit and integration tests for client.py
│
├── README.md # Project documentation
└── ...


---

## ✅ Learning Objectives
- Write **unit tests** using the `unittest` module.
- Apply **parameterized tests** to cover multiple input scenarios.
- Use **mocking and patching** to isolate dependencies.
- Test **memoization** (caching of method results).
- Perform **integration testing** with controlled fixtures.
- Understand how to simulate external API calls without actual network dependency.

---

## 📚 Key Features Tested
1. **Utils Module**
   - `access_nested_map`
   - `get_json`
   - `memoize` decorator

2. **GithubOrgClient**
   - `org`
   - `_public_repos_url`
   - `public_repos`
   - `has_license`

3. **Integration Tests**
   - End-to-end testing of `GithubOrgClient.public_repos`
   - Filters for specific licenses (e.g. Apache 2.0)

---

## 🚀 How to Run the Tests
To run **all tests**:
```bash
python3 -m unittest discover
python3 -m unittest test_utils.py
python3 -m unittest test_client.py

```

## 👨‍💻 Author
Developed with 💻 by Eyoab Efrem as part of the ALX Software Engineering Program.