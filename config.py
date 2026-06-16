import os

from dotenv import load_dotenv

load_dotenv()


def env_int(name: str) -> int:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    return int(value)

APPLICATION_ID = env_int("APPLICATION_ID")
BOT_TOKEN_ID = os.getenv("BOT_TOKEN_ID")
CHANNEL_ID = env_int("CHANNEL_ID")
