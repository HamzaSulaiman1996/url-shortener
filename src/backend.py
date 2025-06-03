from pathlib import Path
from typing import Tuple
from urllib.parse import urlparse

import qrcode

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

def generate_qr(url: str, save_path: Path = Path('qr_code')) -> Path:

    file_name = get_website_name(url)
    img_path = save_path / f"{file_name}.png"
    save_path.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_path)  # type: ignore
    return img_path


def get_website_name(url: str) -> str:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    if domain.startswith("www."):
        domain = domain[4:]

    site_name = domain.split('.')[0]
    return site_name.capitalize()
