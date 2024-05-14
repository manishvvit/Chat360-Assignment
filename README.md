# Log Ingestor and Search System

This project is a log ingestor and search system implemented with Flask. It generates logs and allows for searching logs based on different criteria such as log level, message pattern, and date range.

## Project Structure

- `index.html`: The HTML file for the user interface.
- `style.css`: The CSS file for styling the user interface.
- `app.py`: The Flask application to handle log generation and searching.
- `log_generator.py`: A script to make API requests for searching logs from the command line.

## Features

- Generate logs with random messages, levels, and timestamps.
- Search logs based on log level, message pattern, start date, and end date.
- Simple and intuitive web interface.
- Command-line interface for searching logs with advanced filters.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Requests
- tqdm

You can install the required Python packages using:
```sh
pip install flask requests tqdm
