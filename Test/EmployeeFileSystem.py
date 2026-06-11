import os

with open("employees.txt", "w") as f:
    f.write("Alok - Developer\n")
    f.write("Atul   - Designer\n")
    f.write("Chotu - Manager\n")

print("--- employees.txt created ---")

print("\nOriginal employees:")
with open("employees.txt", "r") as f:
    print(f.read())

with open("employees.txt", "a") as f:
    f.write("Rashu - Tester\n")
    f.write("Aryan   - DevOps\n")

print("2 employees appended.")

print("\nUpdated employees:")
with open("employees.txt", "r") as f:
    print(f.read())

os.remove("employees.txt")

if os.path.exists("employees.txt"):
    print("File still exists.")
else:
    print("employees.txt deleted successfully. File no longer exists.")