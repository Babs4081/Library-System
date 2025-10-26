import json
import os

DATA_FILE = os.path.join(os.getcwd(), "data_store.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "admins":[
                {"admin": "Babs", "pin": 3016}
            ],
            "users": []
        }
        save_data(default_data)
        return default_data
    
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {
                "admins": [
                    {"admin": "Babs", "pin": 3016}
                ],
                "users": []
            }
            save_data(data)

    if not "users" in data or "admins" not in data:
        data = {
            "admins": [
                {"admin": "Babs", "pin": 3016}
            ],
            "users": []
        }
        save_data(data)
    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

BOOK_FILE = os.path.join(os.getcwd(), "book_store.json")

def load_book():
    if not os.path.exists(BOOK_FILE):
        default_books = [
            {
                "book_id": "B101",
                "title": "Babs Python Programming For Beginner Crash Course",
                "author": "Babs",
                "category": "Learning",
                "summary": "This Course Is For Python Beginners",
                "copies_total": 6,
                "copies_avail": 6,
                "borrowed_by": []
            },
            {
                "book_id": "B111",
                "title": "Starlight Paradox",
                "author": "Nova Ardent",
                "category": "Sci-Fi",
                "summary": "A daring pilot discovers a hidden galaxy that could change the fate of humanity.",
                "copies_total": 5,
                "copies_avail": 5,
                "borrowed_by": []
            },
            {
                "book_id": "B112",
                "title": "Love in the Mist",
                "author": "Clara Bennett",
                "category": "Romance",
                "summary": "Two strangers meet on a rainy night and discover that love can heal even the deepest scars.",
                "copies_total": 6,
                "copies_avail": 6,
                "borrowed_by": []
            }
        ]
        save_book(default_books)
        return default_books
    with open(BOOK_FILE, "r") as f:
        try:
            book_data = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Corrupted book file. Restoring defaults...")
            default_books = [
                {
                    "book_id": "B101",
                    "title": "Babs Python Programming For Beginner Crash Course",
                    "author": "Babs",
                    "category": "Learning",
                    "summary": "This Course Is For Python Beginners",
                    "copies_total": 6,
                    "copies_avail": 6,
                    "borrowed_by": []
                },
                {
                    "book_id": "B111",
                    "title": "Starlight Paradox",
                    "author": "Nova Ardent",
                    "category": "Sci-Fi",
                    "summary": "A daring pilot discovers a hidden galaxy that could change the fate of humanity.",
                    "copies_total": 5,
                    "copies_avail": 5,
                    "borrowed_by": []
                },
                {
                    "book_id": "B112",
                    "title": "Love in the Mist",
                    "author": "Clara Bennett",
                    "category": "Romance",
                    "summary": "Two strangers meet on a rainy night and discover that love can heal even the deepest scars.",
                    "copies_total": 6,
                    "copies_avail": 6,
                    "borrowed_by": []
                }
            ]
            save_book(default_books)
            return default_books       
    for book in book_data:
        if "borrowed_by" not in book:
            book["borrowed_by"] = []
        if "copies_total" not in book:
            book["copies_total"] = 1
        if "copies_avail" not in book:
            book["copies_avail"] = book["copies_total"]

    return book_data


def save_book(book_data):
    with open(BOOK_FILE, "w") as f:
        json.dump(book_data, f, indent=4)

HISTORY_FILE = os.path.join(os.getcwd(), "history.json")
def load_history():
    if not os.path.exists(HISTORY_FILE):
       history_data = []
       return history_data
    
    with open(HISTORY_FILE, "r") as f:
        try:
            history_dataa = json.load(f)
        except json.JSONDecodeError:
            history_dataa = []
            save_history(history_data)
        return history_dataa
    
def save_history(history_dataa):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history_dataa, f, indent=4)