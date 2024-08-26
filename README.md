# FastAPI User Authentication and Data Management API

This project is a FastAPI-based web application designed for user authentication and data management. It includes endpoints for user signup, login, fetching user information, and creating posts. The application also connects to a MongoDB database for user data storage and management.

## Features

- **User Authentication**: Allows users to sign up and log in using a username and password.
- **Data Management**: Supports creating and retrieving posts associated with users.
- **API Key Management**: Tracks API call counts and manages API keys for users.
- **Static File Serving**: Serves static files like `index.html`, `script.js`, and `styles.css`.

## Installation

To run this project, you'll need Python installed with the following dependencies:

- `FastAPI`: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- `Pydantic`: Data validation and settings management using Python type annotations.
- `uvicorn`: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.
- `pymongo`: A MongoDB driver for Python.

You can install these dependencies using pip:

```bash
pip install fastapi pydantic uvicorn pymongo
