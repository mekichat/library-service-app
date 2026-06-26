import os
from dotenv import load_dotenv

# ONLY load once here
ENV_FILE = os.getenv("ENV_FILE", ".env.docker")
load_dotenv(ENV_FILE)