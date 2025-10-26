import library_data
import copy
from library_data import save_data
from library_data import save_history
from library_data import save_book
from library_data import  load_book
from library_data import load_data
from library_data import load_history
import datetime
from datetime import datetime
def value():
    print("Enter Numbers Only ❗\n")

def key():
    print("Keyboard Interrupted ❗\n")

def status_idicator(user_id):
        data = load_data()
        users = data.get("users", [])
        current_user = next((s for s in users if s["user_id"] == user_id), None)
        status = current_user.get("status", "Unknown")
        if current_user:
            if  status == "Active":
                symbol = "🟢"
                print(f"----------Account Status: {symbol} {current_user["status"]}")
            else:
                current_user["status"] = "Suspended"
                symbol = "🔴"
                message = (f"----------Account Status: {symbol} {current_user["status"]}")
                print(message)
                return message

def user_menu(user_id):
    data = load_data()
    users = data.get("users", [])
    current_user = next((s for s in users if s["user_id"] == user_id), None)
    while True:
        print("\n------------------- Babs Virtual Library 📚📚 --------------\n")
        print(f"----------🙋‍♂️ {current_user["username"]}")
        print(f"----------🆔: {current_user["user_id"]}")
        status_idicator(current_user["user_id"])
        print("1. View All Books📚")
        print("2. Search by Name/Book Id📗")
        print("3. Search Books by Category📘")
        print("4. Borrow Book📖")
        print("5. Return Book📖")
        print("6. View History🧾")
        print("7. LogOut🚪")
        try:
            choose = input("Enter a number(1-7): ")
            if choose == "1":
                view_book()
            elif choose == "2":
                search_name()
            elif choose == "3":
                search_category()
            elif choose == "4":
                borrow(user_id)
            elif choose == "5":
                return_book(user_id)
            elif choose == "6":
                view_history(user_id)
            elif choose == "7":
                logout()
            else:
                print("Enter (1-7)")
        except ValueError:
            value()
        except KeyboardInterrupt:
                key()

def view_book():
    data = load_book()
    for s in data :
        print(f"\nTitle: {s["title"]} | Book Id: {s["book_id"]}")
        print(f"Author: {s["author"]}")
        print(f"Category: {s["category"]}")
        print(f"Book Description: {s["summary"]}")
        print(f"Total Copies: {s["copies_total"]} | Copies Available: {s["copies_avail"]}\n")

def search_name():
    data = load_book()
    search = input("Enter Book Name/Id: ").strip().title()
    found = False
    try:
        for s in data:
            if s["title"] == search or s["book_id"] == search:
                print(f"\nTitle: {s["title"]} | Book Id: {s["book_id"]}")
                print(f"Author: {s["author"]}")
                print(f"Category: {s["category"]}")
                print(f"Book Description: {s["summary"]}")
                print(f"Total Copies: {s["copies_total"]} | Copies Available: {s["copies_avail"]}\n")
                found = True
                break
        if not found:
            print("Book Not Found ❗")
    except ValueError:
        print("Book Not Found ❗")
    except KeyboardInterrupt:
        key()
            
def search_category():
    data = load_book()
    print("\nCategories Of Book Available")
    try:
        categories = []
        for book in data:
            if not book["category"] in categories:
                categories.append(book["category"])
        for category in categories:
            print(f"- {category}")
        search = input("Enter a category: ").strip().title()
        found = False
        for s in data:
            if s["category"] == search:
                print(f"\nTitle: {s["title"]} | Book Id: {s["book_id"]}")
                print(f"Author: {s["author"]}")
                print(f"Category: {s["category"]}")
                print(f"Book Description: {s["summary"]}")
                print(f"Total Copies: {s["copies_total"]} | Copies Available: {s["copies_avail"]}\n")
                found = True
        if not found:
            print("Category Not Available ❗")
    except KeyboardInterrupt:
        key()

def borrow(user_id):
    books = load_book()
    user_history = load_history()
    user_data = load_data()
    user = user_data.get("users", [])
    c_user = next((s for s in user if s["user_id"] == user_id), None)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if c_user["status"] == "Active":
        print("Borrow Book From Library📚")
        search = input("Search Book By Name/Id📖: ").strip().title()
        found = False

        for s in books:
            if s["book_id"] == search or s["title"] == search:
                print(f"\nTitle: {s['title']} | Book Id: {s['book_id']}")
                print(f"Author: {s['author']}")
                print(f"Category: {s['category']}")
                print(f"Book Description: {s['summary']}")
                print(f"Total Copies: {s['copies_total']} | Copies Available: {s['copies_avail']}\n")
                found = True

                borrow = input("Do you want to borrow this book (y/n): ").lower()
                if borrow == "y":
                    if c_user["borrow"] > 0:
                        borrowed = any(
                            h["book_id"] == s["book_id"] and 
                            h["user_id"] == user_id and 
                            h["action"] == "borrow" and 
                            not any(r["book_id"] == s["book_id"] and r["user_id"] == user_id and r["action"] == "return" for r in user_history)
                            for h in user_history
                        )
                        if not borrowed:
                            if s["copies_avail"] > 0:
                                user_borrow = {
                                   "username": c_user["username"],
                                   "user_id": user_id
                                }
                                # ✅ Append instead of replacing
                                s["borrowed_by"].append(user_borrow)

                                s["copies_avail"] -= 1
                                c_user["borrow"] -= 1

                                history = {
                                    "user_id": c_user["user_id"],
                                    "username": c_user["username"],
                                    "book_id": s["book_id"],
                                    "action": "borrow",
                                    "borrow_remain": c_user["borrow"],
                                    "date": timestamp
                                }
                                user_history.append(history)
                                save_history(user_history)
                                save_book(books)
                                save_data(user_data)
                                print("✅ Book borrowed successfully!")
                            else:
                                print("❌ Book currently not available.")
                        else:
                            print("⚠️ You already borrowed this book.")
                    else:
                        print("⚠️ You’ve reached your borrowing limit. Please return a book first.")
                elif borrow == "n":
                    print("❌ Cancelled.")
                else:
                    print("⚠️ Enter (y/n).")

        if not found:
            print("❗ Book not found.")
    else:
        print("⚠️ Account suspended. Contact admin.")


def return_book(user_id):
    user_data = copy.deepcopy(load_data())
    users = copy.deepcopy(user_data.get("users", []))
    books = copy.deepcopy(load_book())
    user_history = load_history()
    c_user = next((s for s in users if s["user_id"] == user_id), None)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not c_user:
        print("User Not Found ❌")
        return

    print("\n📚 Your Borrowed Books:")
    borrowed_books = [
        s for s in user_history
        if s["action"] == "borrow"
        and s["user_id"] == c_user["user_id"]
        and not any(
            r["book_id"] == s["book_id"]
            and r["user_id"] == user_id
            and r["action"] == "return"
            for r in user_history
        )
    ]

    if not borrowed_books:
        print("You haven't borrowed any books ❗")
        return

    for s in borrowed_books:
        book = next((d for d in books if d["book_id"] == s["book_id"]), None)
        if book:
            print(f"Book Id: {book['book_id']} | Title: {book['title']}")
            print(f"Author: {book['author']} | Category: {book['category']}")
            print(f"Date Borrowed: {s['date']}\n")

    return_b = input("Enter Book Id To Return: ").strip().title()
    found = False

    for b in books:
        if b["book_id"] == return_b:
            borrowed_user = next(
                (f for f in b["borrowed_by"] if f["user_id"] == c_user["user_id"]),
                None
            )

            if borrowed_user:
                found = True
                confirm = input("Do you want to return this book (y/n): ").strip().lower()

                if confirm == "y":
                    b["borrowed_by"] = [
                        entry for entry in b["borrowed_by"]
                        if entry["user_id"] != c_user["user_id"]
                    ]
                    b["copies_avail"] += 1
                    c_user["borrow"] += 1  

                    for i, u in enumerate(user_data["users"]):
                        if u["user_id"] == c_user["user_id"]:
                            user_data["users"][i] = c_user
                            break

                    user_return = {
                        "username": c_user["username"],
                        "user_id": c_user["user_id"],
                        "action": "return",
                        "book_id": b["book_id"],
                        "date": timestamp
                    }

                    user_history.append(user_return)
                    save_book(books)
                    save_data(user_data)
                    save_history(user_history)
                    print("✅ Book Returned Successfully!")

                elif confirm == "n":
                    print("❌ Book Return Cancelled.")
                else:
                    print("⚠️ Enter (y/n)")
                break

    if not found:
        print("You didn’t borrow this book ❗")

def view_history(user_id):
    user_history = load_history()
    books = load_book()

    user_records = [b for b in user_history if b["user_id"] == user_id]

    print("\nUSER HISTORY🧾")
    if not user_records:
        print("No history found.")
        return

    for record in user_records:
        book_info = next((bk for bk in books if bk["book_id"] == record["book_id"]), None)
        if book_info:
            print(f"Book: {book_info['title']} | Action: {record['action']} | Date: {record['date']}")
        else:
            print(f"Book ID {record['book_id']} not found in current book list.")


def logout():
    import main
    from main import main_menu
    print("Logged Out✅")
    main_menu()