import random
import user
from user import user_menu
import library_data
from library_data import load_data
from library_data import save_data
import admin
from admin import admin_menu
def value():
    print("Enter Numbers Only ❗\n")

def key():
    print("Keyboard Interrupted ❗\n")
def gen_id():
    return random.randint(71000,71999)
def create_account():
    data = load_data()
    users = data.get("users", [])
    print("\nCreate An Account🧾")
    acc_id = gen_id()
    try:
        username = input("Enter Your Name: ").strip().capitalize()
        while True:
            try:
                check_pin = int(input("Set a 4 digits Pin: "))
                if len(str(check_pin)) == 4:
                    pin = check_pin
                    print(f"Pin Set Successfully✅. Pin: {pin}\n")
                    break
                else:
                    print("Pin must be 4 digits ❗\n")
            except ValueError:
                print("Enter Only Numbers ❗\n")
        user_detail = {
            "username": username,
            "user_id" : acc_id,
            "pin": pin,
            "status": "Active",
            "borrow": 3
        }
        users.append(user_detail)
        save_data(data)
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()
    user_menu(acc_id)

def login():
    data = load_data()
    users = data.get("users", [])
    print("\n Login To Account 👥👥\n")
    try:
        check_id = int(input("Enter ID: "))
        user = next((s for s in users if s["user_id"] == check_id), None)
        if user:
            print(f"Welcome Back {user["username"]}")
            check_pin = int(input("Enter Pin:  "))
            if check_pin == user["pin"]:
                print("Logged In Successfully✅")
                user_menu(check_id)
                
            else:
                print("Invalid Pin❌")
        else:
            print("User Not Found ❗")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()

def admin_login():
    data = load_data()
    admins = data.get("admins", [])
    print("\nAdmin Login 👤👤\n")
    try:
        check_admin = input("Enter Name: ").strip().capitalize()
        admin = next((s for s in admins if s["admin"] == check_admin), None)
        if admin:
            print(f"Welcome {admin["admin"]}")
            check_pin = int(input("Enter Pin: "))
            if admin["pin"] == check_pin:
                print("Logged In Successfullly✅\n")
                admin_menu(check_admin)

            else:
                print("Invalid Pin❌")
        else:
            print("Admin Not Found ❗")
    except ValueError:
        value()
    except KeyboardInterrupt:
        key()