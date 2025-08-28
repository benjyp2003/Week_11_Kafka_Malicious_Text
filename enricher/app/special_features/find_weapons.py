def check_for_weapons_in_text(txt: str, weapons: list[str]) -> list:
    """Check if the given field contains weapons"""
    try:
        found_weapons_list = []
        for weapon in weapons:
            if weapon in txt:
                found_weapons_list.append(weapon)

        return found_weapons_list

    except Exception as e:
        raise Exception(f"An error occurred while checking for weapons in text: {e}")
