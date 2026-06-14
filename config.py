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
VERDANT_ROLE_ID = env_int("VERDANT_ROLE_ID")
CRIMSON_FLAME_ROLE_ID = env_int("CRIMSON_FLAME_ROLE_ID")
VOID_ROLE_ID = env_int("VOID_ROLE_ID")
CELESTIAL_ROLE_ID = env_int("CELESTIAL_ROLE_ID")

COLOR_ROLES = frozenset({
    VERDANT_ROLE_ID,
    CRIMSON_FLAME_ROLE_ID,
    VOID_ROLE_ID,
    CELESTIAL_ROLE_ID,
})