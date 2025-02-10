import cv2
import sqlite3
import pytesseract
from picamera2 import Picamera2
from PIL import Image
import time
from mtgsdk import Card

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

def capture_card_image():
    """Captures an image of the card and saves it."""
    image_path = "card.jpg"
    picam2.capture_file(image_path)
    return image_path

def process_card(image_path):
    """Extracts text from the card image."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh)
    return text.strip()

def get_card_info(card_text):
    """Fetches card details from MTGSDK."""
    cards = Card.where(name=card_text).all()
    if cards:
        card = cards[0]  # Assuming the first match is correct
        return {
            "name": card.name,
            "set": card.set,
            "type": card.type,
            "mana_cost": card.mana_cost
        }
    return None

def store_card_info(card_info):
    """Stores the structured card info in an SQLite database."""
    conn = sqlite3.connect("cards.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            set_code TEXT,
            type TEXT,
            mana_cost TEXT
        )
    """
    )
    cursor.execute("INSERT INTO cards (name, set_code, type, mana_cost) VALUES (?, ?, ?, ?)",
                   (card_info["name"], card_info["set"], card_info["type"], card_info["mana_cost"]))
    conn.commit()
    conn.close()

def main():
    print("Capturing card image...")
    image_path = capture_card_image()
    time.sleep(2)  # Wait for the image to be saved
    
    print("Processing card...")
    card_text = process_card(image_path)
    print("Extracted text:", card_text)
    
    print("Searching MTGSDK for card info...")
    card_info = get_card_info(card_text)
    
    if card_info:
        print("Card found:", card_info)
        print("Saving to database...")
        store_card_info(card_info)
        print("Card saved successfully!")
    else:
        print("Card not found in MTGSDK.")

if __name__ == "__main__":
    main()
