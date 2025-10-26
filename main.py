import library_data
import auth
from auth import create_account
from auth import login
from auth import admin_login
from library_data import load_data
from library_data import save_data

def main_menu():
    while True:
        try:
            print("\nWelcome To Babs Virtual Library📚📚")
            print("1. Create An Account")
            print("2. Login To Account ")
            print("3. Admin Login")
            print("4. Exit\n")
            choose = input("Enter a number(1-4): ")
            if choose == "1":
                create_account()
            elif choose == "2":
                login()
            elif choose == "3":
                admin_login()
            elif choose == "4":
                print("GoodBye 🙋‍♂️🙋‍♂️")
                break
            else:
                print("Enter (1-4)❗\n")
        except ValueError:
            print("Enter Numbers Only ❗\n")
        except KeyboardInterrupt:
            print("Keyboard Interrupted ❗\n")
        except Exception as e:
            print(e)
main_menu()

