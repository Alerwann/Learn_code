from enum import Enum


class ThemeEnum(str, Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"
    SETUP = "setup"
    CLI = "CLI"


class DifficulteEnum(str, Enum):
    FACILE = "facile"
    MOYEN = "moyen"
    DIFFICILE = "difficile"
    EXPERT = "expert"
