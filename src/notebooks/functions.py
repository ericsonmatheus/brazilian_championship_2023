from PIL import Image
import urllib
import logging

def get_shields(shield_id):
    fotmob_url = "https://images.fotmob.com/image_resources/logo/teamlogo/"
    try:
        url = f"{fotmob_url}{shield_id}.png"
        image = Image.open(urllib.request.urlopen(url))
        return image
    except Exception as err:
        logging.error(f"Error to load image from shield {shield_id}: {err}")
        return None
