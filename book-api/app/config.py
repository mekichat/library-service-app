import os
from typing import cast

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

DATABASE_URL = cast(str, DATABASE_URL)
print("Using DATABASE_URL:", DATABASE_URL)