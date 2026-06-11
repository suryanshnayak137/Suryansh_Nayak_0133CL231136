class AccountLockedError(Exception):
    pass
class LoginSystem:
    def __init__(self):
        self.__password = 'python@123'
        self.__attempts = 3
    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account is locked! Too many failed attempts.")

            if password != self.__password:
                self.__attempts -= 1
                if self.__attempts == 0:
                    raise AccountLockedError("Account is locked! Too many failed attempts.")
                print(f"Wrong password! Attempts remaining: {self.__attempts}")
            else:
                print("Login successful! Welcome.")

        except AccountLockedError as e:
            print(f"AccountLockedError: {e}")

        finally:
            print(f"Login attempt completed. Attempts left: {self.__attempts}\n")

obj = LoginSystem()
print("--- Attempt 1: Wrong password ---")
obj.login("wrongpass")
print("--- Attempt 2: Wrong password ---")
obj.login("hello123")
print("--- Attempt 3: Wrong password (locks account) ---")
obj.login("abc")
print("--- Attempt 4: Correct password (but locked) ---")
obj.login("python@123")