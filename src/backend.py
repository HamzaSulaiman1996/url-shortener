from typing import Tuple

import requests


def check_liveliness(url: str) -> Tuple[bool, str]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return (True, "Website is accessible.")
        else:
            print(response.status_code)
            return (False, f"{response.status_code}")
    except requests.RequestException as e:
        return (False, f"Error accessing website: {str(e)}")
