import random
import library_data
from library_data import save_data
from library_data import save_book
from library_data import save_history
from library_data import load_book
from library_data import load_data
from library_data import load_history

def value():
    print("Enter Numbers Only ❗\n")

def key():
    print("Keyboard Interrupted ❗\n")

def admin_menu(admin_name):
    import main
    from main import main_menu
    data = load_data()
    admins = data.get("admins", [])
    admin = next((s for s in admins if s["admin"] == admin_name), None)
    while True:
        print(f"\nWelcome Admin: {admin["admin"]}")
        print(f"1. Book Management 📖")
        print(f"2. User Management 👥")
        print(f"3. History and Report 🧾")
        print(f"4. LogOut 🚪")
        choose = input("Enter a number (1-4): ")
        if choose == "1":
            book_menu(admin_name)
        elif choose == "2":
            usermangement_menu(admin_name)
        elif choose == "3":
            history_report_menu()
        elif choose == "4":
            main_menu()
            break
def gen_book():
    return  'B'+ str(random.randint(100,199))

def book_menu(admin_name):
    books = load_book()
    total_books = len(books)
    borrowed_books = sum(
        (book["copies_total"] - book["copies_avail"]) for book in books
    )
    while True:
        print("===========================================")
        print("             📖 BOOK MANAGEMENT            ")
        print("===========================================")
        print("1️⃣  📘  View All Books  ")
        print("2️⃣  ➕  Add New Book")
        print("3️⃣  ✏️  Edit Book Details  ")
        print("4️⃣  🗑️  Delete a Book ")
        print("5️⃣  ↩️  Back to Admin Menu\n")
        print("-------------------------------------------")
        print(f"       Total Books: {total_books}   |   Borrowed: {borrowed_books}  ")
        print("-------------------------------------------")
        choose = input("Enter a number(1-5): ")
        if choose == "1":
            adview_book()
        elif choose == "2":
            add_book()
        elif choose == "3":
            edit_book()
        elif choose == "4":
            delete_book()
        elif choose == "5":
            gadmin_menu(admin_name)
        else:
            print("Enter (1-5)")


def adview_book():
    books = load_book()
    print(f"      Title       |   Book Id  | Category |  Available ")
    print("----------------------------------------------------------")
    for b in books:
        print(f"{b["title"]} | {b["book_id"]} | {b["category"]}    {b["copies_avail"]}/{b["copies_total"]}")

def add_book():
    book_data = load_book()
    print("\nAdd A Book New Book")
    try:
        book_id = gen_book()
        book_title = input("Enter Book Title: ").strip().title()
        book_author = input("Enter Book Author: ").strip().title()
        book_category = input("Enter Book Category: ").strip().title()
        book_summary = input("Enter Book Summary: ").strip().title()
        book_copies = int(input("Enter number of book copies: ").strip())
        confirm = input("Do you want to add book (y/n): ")
        if confirm == "y":
            new_book = {
                "book_id": book_id,
                "title": book_title,
                "author": book_author,
                "category": book_category,
                "summary": book_summary,
                "copies_total": book_copies,
                "copies_avail": book_copies,
            }
            book_data.append(new_book)
            save_book(book_data)
        elif confirm == "n":
            print("Cancelled❌")
        else:
            print("Enter (y/n)")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()

def edit_book():
    while True:
        print("\nEdit Book Info 📘\n")
        print("1. Edit Book Title")
        print("2. Edit Author")
        print("3. Edit Category")
        print("4. Edit Summary")
        print("5. Edit Total Copies")
        print("6. Back")
        choose = input("Enter a number(1-6): ")
        if choose == "1":
            edit_title()
        elif choose == "2":
            edit_author()
        elif choose == "3":
            edit_category()
        elif choose == "4":
            edit_summary()
        elif choose == "5":
            edit_copies()
        elif choose == "6":
            gbook_menu()
        else:
            print("Enter (1-6)")


def edit_title():
    books = load_book()
    print("\nEdit Book Title")
    try:
        book_id = input("Enter Book Id: ")
        book = next((s for s in books if s["book_id"] == book_id), None)
        if book:
            print(f"Current Book Title: {book["title"]}")
            new_title = input("Enter a new title: ").strip().title()
            if book["title"] != new_title:
                confirm = input("Do you want to save changes(y/n): ")
                if confirm == "y":
                    book["title"] = new_title
                    print("Changes Saved✅")
                    save_book(books)
                elif confirm == "n":
                    print("Changes Cancelled❌")
                else:
                    print("Enter (y/n) ❗")
            else:
                print("New title cant be the same a previous one")
        else:
            print("Book Not Found ❗")
    except KeyboardInterrupt:
        key()
def edit_author():
    books = load_book()
    print("\nEdit Book Author")
    try:
        book_id = input("Enter Book Id: ")
        book = next((s for s in books if s["book_id"] == book_id), None)
        if book:
            print(f"Current Book Author: {book["author"]}")
            new_author = input("Enter new book author: ").strip().title()
            if book["author"] != new_author:
                confirm = input("Do you want to save changes(y/n): ")
                if confirm == "y":
                    book["author"] = new_author
                    save_book(books)
                    print("Changes Saved✅")
                elif confirm == "n":
                    print("Changes Cancelled❌")
                else:
                    print("Enter(y/n)")
            else:
                print("New Author cant be the same a previous one")
        else:
            print("Book Not Found ❗")
    except KeyboardInterrupt:
        key() 

def edit_category():
    books = load_book()
    print("\nEdit Book Category")
    try:
        book_id = input("Enter Book Id: ")
        book = next((s for s in books if s["book_id"] == book_id), None)
        if book:
            print(f"Current Book Category: {book["category"]}")
            new_category = input("Enter new book category: ").strip().title()
            if book["category"] != new_category:
                confirm = input("Do you want to save changes(y/n): ")
                if confirm == "y":
                    book["category"] = new_category
                    save_book(books)
                    print("Changes Saved✅")
                elif confirm == "n":
                    print("Changes Cancelled❌")
                else:
                    print("Enter(y/n)")
            else:
                print("New Category cant be the same a previous one")
        else:
            print("Book Not Found ❗")
    except KeyboardInterrupt:
        key() 
    
def edit_summary():
    books = load_book()
    print("\nEdit Book Summary")
    try:
        book_id = input("Enter Book Id: ")
        book = next((s for s in books if s["book_id"] == book_id), None)
        if book:
            print(f"Current Book Summary: {book["summary"]}")
            new_summary = input("Enter new book Summary: ").strip().title()
            if book["summary"] != new_summary:
                confirm = input("Do you want to save changes(y/n): ")
                if confirm == "y":
                    book["summary"] = new_summary
                    save_book(books)
                    print("Changes Saved✅")
                elif confirm == "n":
                    print("Changes Cancelled❌")
                else:
                    print("Enter(y/n)")
            else:
                print("New Category cant be the same a previous one")
        else:
            print("Book Not Found ❗")
    except KeyboardInterrupt:
        key()

def edit_copies():
    books = load_book()
    print("\nEdit Book Total Copies")
    try:
        book_id = input("Enter Book Id: ")
        book = next((s for s in books if s["book_id"] == book_id), None)
        if book:
            print(f"Current Book Total Copies: {book["copies_total"]}")
            new_total = int(input("Enter new book copies: "))
            if book["copies_avail"] != new_total:
                confirm = input("Do you want to save changes(y/n): ")
                if confirm == "y":
                    book["copies_total"] = new_total
                    save_book(books)
                    print("Changes Saved✅")
                elif confirm == "n":
                    print("Changes Cancelled❌")
                else:
                    print("Enter(y/n)")
            else:
                print("New Total Copies cant be the same a previous one")
        else:
            print("Book Not Found ❗")
    except KeyboardInterrupt:
        key() 
    except ValueError:
        value()

def gbook_menu(admin_name):
    book_menu(admin_name)

def delete_book():
    books = load_book()
    check_id = input("Enter Book Id: ")
    book = next((s for s in books if s["book_id"] == check_id), None)
    if book:
        print(f"Book Title: {book["title"]}")
        confirm = input("Do you want to remove this book(y/n): ")
        if confirm == "y":
            books.remove(book)
            save_book(books)
            print("Changes Saved✅")
        elif confirm == "n":
            print("Cancelled ❌")
        else:
            print("Enter (y/n)")
    else:
        print("Book Not Found❌")

def gadmin_menu(admin_name):
    admin_menu(admin_name)

def usermangement_menu(admin_name):
    data = load_data()
    users_data = data.get("users", [])
    while True:
        check_activesta = sum(1 for s in users_data if s.get("status") == "Active") 
        check_sussta = sum(1 for s in users_data if s.get("status") == "Suspended")

        print("===========================================")
        print("       🧑‍💼 USER MANAGEMENT MENU           ")
        print("===========================================")
        print("1. 👥 View All Users")
        print("2. 🔍 Search User by ID")
        print("3. ⚙️ Suspend / Reactivate User Account")
        print("4. ♻️ Reset User Borrow Limit")
        print("5. 🧾 View User History")
        print("6. ❌ Delete User Account")
        print("7. ↩️ Return to Admin Menu")
        print("-------------------------------------------")
        print(f"    Active Users: {check_activesta}   |   Suspended: {check_sussta}   ")
        print("-------------------------------------------")
        try:
            choose = input("Enter a number(1-7): ")
            if choose == "1":
                adview_users()
            elif choose == "2":
                adsearch()
            elif choose == "3":
                adsus_user()
            elif choose == "4":
                reset_borrow()
            elif choose == "5":
                user_history()
            elif choose == "6":
                delete_user()
            elif choose == "7":
                admin_menu(admin_name)

        except KeyboardInterrupt:
            key()

def adview_users():
    data = load_data()
    users = data.get("users", [])
    print("\n👥 View Users")
    for s in users:
        print(f"UserName: {s["username"]} | UserId: {s["user_id"]} | UserStatus: {s["status"]}")

def adsearch():
    data = load_data()
    users = data.get("users", [])
    print("\nSearch User 🔍")
    try:
        check_id = int(input("Enter User Id: "))
        user = next((s for s in users if s["user_id"] == check_id), None)
        if user:
                print(f"UserName: {user["username"]} | UserId: {user["user_id"]} | UserStatus: {user["status"]}")
        else:
            print("User Not Found ❌")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()
    
def adsus_user():
    while True:
        print("\n⚙️ Suspend / Reactivate User Account")
        print("1.💥 Suspend User Account")
        print("2. 🔁 Reactivate User Account")
        print("3. ↩ Back\n")
        try:
            choose = input("Enter a number: ")
            if choose == "1":
                suspend()
            elif choose == "2":
                reactivate()
            elif choose == "3":
                usermangement_menu()
            else:
                print("Enter (1-3)")
        except KeyboardInterrupt:
            key()


def suspend():
    data = load_data()
    users = data.get("users", [])
    print("\n💥 Suspend User Account")
    try:
        check_id = int(input("Enter User Id: "))
        user = next((s for s in users if s["user_id"] == check_id), None)
        if user:
            if user["status"] == "Active":
                print(f"UserName: {user["username"]}")
                confirm = input("Do you want to suspend user account(y/n): ")
                if confirm == "y":
                    user["status"] = "Suspended"
                    print(f"User: {user["username"]} Suspended")
                    save_data(data)
                elif confirm == "n":
                    print("Cancelled❌")
                else:
                    print("Enter (y/n)")
            else:
                print("User Already Suspended ❗")
        else:
            print("User Not Found ❌")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()

def reactivate():
    data = load_data()
    users = data.get("users", [])
    print("\n🔁 Reactivate User Account")
    try:
        check_id = int(input("Enter User Id: "))
        user = next((s for s in users if s["user_id"] == check_id), None)
        if user:
            if user["status"] == "Suspended":
                print(f"\nUserName: {user["username"]}")
                confirm = input("Do you want to reactivate user account(y/n): ")
                if confirm == "y":
                    user["status"] = "Active"
                    save_data(data)
                    print("User Account Reactivate ✅")
                elif confirm == "n":
                    print("Cancelled ❌")
                else:
                    print("Enter (y/n)")
            else:
                print("User Account Is Active 👀")
        else:
            print("User Not Found❗")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()

def reset_borrow():
    data = load_data()
    users = data.get("users", [])
    print("\n♻️ Reset User Borrow Limit")
    try:
        check_id = int(input("Enter User Id: "))
        user = next((s for s in users if s["user_id"] == check_id))
        if user:
            print(f"User: {user["username"]}")
            con = input("Do you want reset user borrow limit(y/n): ")
            if con == "y":
                user["borrow"] = 3
                print(f"User: {user["username"]} reset")
                save_data(data)
            elif con == "no":
                print("Cancelled ❌")
            else:
                print("Enter (y/n)")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()

def user_history():
    data = load_data()
    users_data = data.get("users", [])
    history = load_history()
    try:
        check_id = int(input("Enter user id: "))
        user = next((s for s in users_data if s["user_id"] == check_id), None)
        if user:
            print("User History 🧾")
            for his in history:
                if his["user_id"] == user["user_id"]:
                    print(f"\nUsername: {user["username"]}")
                    print(f"Book Id: {his["book_id"]}")
                    print(f"Action {his["action"]}")
                    print(f"Date: {his["date"]}\n")
                else:
                    print("User Has No History ❗")
        else:
            print("User Not Found ❌")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()
    
def delete_user():
    data = load_data()
    history = load_history()
    books = load_book()
    users = data.get("users", [])

    try:
        check_id = int(input("Enter User Id: "))
        user = next((s for s in users if s["user_id"] == check_id), None)

        if user:
            print(f"User Name: {user['username']}")
            con = input("Do you want to delete user (y/n): ").strip().lower()

            if con == "y":
                users.remove(user)
                history = [h for h in history if h["user_id"] != check_id]

                for b in books:
                    b["borrowed_by"] = [
                        entry for entry in b["borrowed_by"] 
                        if entry["user_id"] != check_id
                    ]

                save_data(data)
                save_book(books)
                save_history(history)

                print("✅ User deleted successfully.")
            elif con == "n":
                print("❌ Cancelled.")
            else:
                print("⚠️ Enter (y/n)")

        else:
            print("❗ User Not Found.")

    except Exception as e:
        print(f"⚠️ Error: {e}")
import collections
from collections import Counter
import datetime
from datetime import datetime
def history_report_menu():
    while True:
        print("\n📊 HISTORY & REPORT MENU 🧾")
        print("──────────────────────────────────────")
        print(" 1️⃣  📜 View Borrow / Return History")
        print(" 2️⃣  📚 View Most Borrowed Books")
        print(" 3️⃣  👤 View User Activity Report")
        print(" 4️⃣  🧮 Summary Statistics")
        print(" 5️⃣  📅 Generate Monthly Report")
        print(" 6️⃣  🔙 Back to Admin Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_borrow_return_history()
        elif choice == "2":
            view_most_borrowed_books()
        elif choice == "3":
            view_user_activity()
        elif choice == "4":
            view_summary_stats()
        elif choice == "5":
            generate_monthly_report()
        elif choice == "6":
            break
        else:
            print("❗ Invalid choice, please try again.")

def view_borrow_return_history():
    history = load_history()
    if not history:
        print("No history records found ❗")
        return

    print("\n📜 BORROW / RETURN HISTORY")
    print("─────────────────────────────")
    for record in history:
        print(f"👤 {record['username']} | Book ID: {record['book_id']} | Action: {record['action'].upper()} | Date: {record['date']}")
    print("─────────────────────────────")

def view_most_borrowed_books():
    history = load_history()
    if not history:
        print("No borrowing records found ❗")
        return

    borrow_counts = Counter([h["book_id"] for h in history if h["action"] == "borrow"])
    if not borrow_counts:
        print("No books have been borrowed yet ❗")
        return

    books = load_book()
    print("\n📚 MOST BORROWED BOOKS")
    print("─────────────────────────────")
    for book_id, count in borrow_counts.most_common(5):
        book = next((b for b in books if b["book_id"] == book_id), None)
        if book:
            print(f"{book['title']} ({book['book_id']}) — Borrowed {count} times")
    print("─────────────────────────────")

def view_user_activity():
    history = load_history()
    users_data = load_data()
    users = users_data.get("users", [])

    print("\n👤 USER ACTIVITY REPORT")
    print("─────────────────────────────")

    for user in users:
        user_id = user["user_id"]
        borrows = sum(1 for h in history if h["user_id"] == user_id and h["action"] == "borrow")
        returns = sum(1 for h in history if h["user_id"] == user_id and h["action"] == "return")

        print(f"Username: {user['username']} | Status: {user['status']} | Borrowed: {borrows} | Returned: {returns}")
    print("─────────────────────────────")

def view_summary_stats():
    books = load_book()
    users_data = load_data()
    users = users_data.get("users", [])
    history = load_history()

    total_books = sum(b["copies_total"] for b in books)
    total_copies_avail = sum(b["copies_avail"] for b in books)
    total_borrowed = total_books - total_copies_avail

    active_users = sum(1 for u in users if u["status"] == "Active")
    suspended_users = sum(1 for u in users if u["status"] == "Suspended")

    print("\n🧮 SUMMARY STATISTICS")
    print("─────────────────────────────")
    print(f"📘 Total Books in Library: {total_books}")
    print(f"📕 Total Borrowed Copies: {total_borrowed}")
    print(f"📗 Copies Currently Available: {total_copies_avail}")
    print(f"👤 Active Users: {active_users}")
    print(f"🚫 Suspended Users: {suspended_users}")
    print(f"🧾 Total Transactions Logged: {len(history)}")
    print("─────────────────────────────")

def generate_monthly_report():
    history = load_history()
    if not history:
        print("No history records found ❗")
        return

    month_input = input("Enter month and year (e.g., 10-2025): ").strip()
    try:
        month, year = month_input.split("-")
        filtered = [
            h for h in history
            if datetime.strptime(h["date"], "%Y-%m-%d %H:%M:%S").month == int(month)
            and datetime.strptime(h["date"], "%Y-%m-%d %H:%M:%S").year == int(year)
        ]
    except Exception:
        print("Invalid format. Use MM-YYYY ❗")
        return

    if not filtered:
        print("No records found for that month ❗")
        return

    print(f"\n📅 MONTHLY REPORT — {month_input}")
    print("─────────────────────────────")
    for record in filtered:
        print(f"👤 {record['username']} | Book ID: {record['book_id']} | Action: {record['action'].upper()} | Date: {record['date']}")
    print("─────────────────────────────")