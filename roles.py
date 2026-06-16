from config import env_int

VERDANT_ROLE_ID = env_int("VERDANT_ROLE_ID")
CRIMSON_FLAME_ROLE_ID = env_int("CRIMSON_FLAME_ROLE_ID")
VOID_ROLE_ID = env_int("VOID_ROLE_ID")
CELESTIAL_ROLE_ID = env_int("CELESTIAL_ROLE_ID")

GOLF_GAMES_ROLE_ID = env_int("GOLF_GAMES_ROLE_ID")
MOVIES_ROLE_ID = env_int("MOVIES_ROLE_ID")
AQWORDLE_ROLE_ID = env_int("AQWORDLE_ROLE_ID")

ANNOUNCEMENTS_ROLE_ID = env_int("ANNOUNCEMENTS_ROLE_ID")
BADGES_ROLE_ID = env_int("BADGES_ROLE_ID")
EVENTS_ROLE_ID = env_int("EVENTS_ROLE_ID")
SELFIES_ROLE_ID = env_int("SELFIES_ROLE_ID")
BIRTHDAYS_ROLE_ID = env_int("BIRTHDAYS_ROLE_ID")
HELPER_ROLE_ID = env_int("HELPER_ROLE_ID")

COLOR_ROLE_DATA = [
    ("🌱 Verdant", VERDANT_ROLE_ID),
    ("🔥 Crimson Flame", CRIMSON_FLAME_ROLE_ID),
    ("🌌 Void", VOID_ROLE_ID),
    ("👼 Celestial", CELESTIAL_ROLE_ID),
]

SOCIAL_ROLE_DATA = [
    ("⛳ Golf Games", GOLF_GAMES_ROLE_ID),
    ("🎬 Movies", MOVIES_ROLE_ID),
    ("🧩 AQWordle", AQWORDLE_ROLE_ID),
]

NOTIFICATION_ROLE_DATA = [
    ("📢 Announcements", ANNOUNCEMENTS_ROLE_ID),
    ("🏆 Badges", BADGES_ROLE_ID),
    ("🎉 Events", EVENTS_ROLE_ID),
    ("🤳 Selfies", SELFIES_ROLE_ID),
    ("🎂 Birthdays", BIRTHDAYS_ROLE_ID),
    ("💬 Helper", HELPER_ROLE_ID),
]

ROLE_GROUPS = {
    "color": COLOR_ROLE_DATA,
    "social": SOCIAL_ROLE_DATA,
    "notification": NOTIFICATION_ROLE_DATA,
}