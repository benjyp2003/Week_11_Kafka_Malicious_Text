def load_weapons_data(file_path):
    """Load weapons data from a file"""
    try:
        with open(file_path) as f:
            data = f.read().splitlines()
        return data
    except Exception as e:
        raise Exception(f"An error occurred while loading weapons data: {e}")