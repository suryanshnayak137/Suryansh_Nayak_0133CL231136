with open("report.txt", "w") as f:
    f.write("Rahul-85\n")
    f.write("Priya-90\n")
    f.write("Rohan-78\n")
    f.write("Sneha-92\n")
    f.write("Amit-65\n")

print("--- report.txt created ---")

try:
    with open("report.txt", "r") as f:
        lines = f.readlines()

    print("\nStudents with marks > 80:")
    for line in lines:
        name, marks = line.strip().split("-")
        if int(marks) > 80:
            print(f"  {name}: {marks}")

except FileNotFoundError:
    print("Error: report.txt not found!")

finally:
    print("\nFile operation complete (report.txt).")