from app.weapon_processing.weapons_loader import load_weapons_data
from utils.cleaner import Cleaner

def get_clean_weapons() -> str:
    weapons = " ".join(load_weapons_data("data/weapon_list.txt"))

    cleaner = Cleaner(weapons)
    cleaner.manager_cleaner()
    return cleaner.clean_data