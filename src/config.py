import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DEBUG = True

DB_DRIVER = os.getenv("DB_DRIVER")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = "localhost" if DEBUG else os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
API_VERSION = os.getenv("API_VERSION")

# Test database params
DB_DRIVER_TEST = os.getenv("DB_DRIVER")
DB_USER_TEST = os.getenv("DB_USER")
DB_PASS_TEST = os.getenv("DB_PASS")
DB_HOST_TEST = "localhost" if DEBUG else os.getenv("DB_HOST")
DB_PORT_TEST = os.getenv("DB_PORT")
DB_NAME_TEST = os.getenv("DB_NAME")
API_VERSION_TEST = os.getenv("API_VERSION")
