import re
from datetime import datetime


def find_relevant_time_stamp(text: str) -> str:
    """
    Find the most relevant time stamp in the given text.
    """
    # find all YYYY-MM-DD patterns
    matches = re.findall(r"\d{4}-\d{2}-\d{2}", text)

    if matches:
        dates = [datetime.strptime(m, "%Y-%m-%d") for m in matches]
        latest = max(dates)
        return latest.strftime("%Y-%m-%d")

    else:
        return ""