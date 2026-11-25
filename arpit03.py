import csv
import os

script_folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_folder, "student.csv")
output_file = os.path.join(script_folder, "selected_student.csv")

if not os.path.exists(input_file):
    with open(input_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll Number", "Name", "Department", "Marks", "City"])
        writer.writerow(["101", "Alice", "Computer", "85", "Pune"])
        writer.writerow(["102", "Bob", "IT", "72", "Mumbai"])
        writer.writerow(["103", "Charlie", "Computer", "91", "Nashik"])
        writer.writerow(["104", "David", "ENTC", "65", "Pune"])
        writer.writerow(["105", "Emma", "IT", "88", "Mumbai"])
    print(f"Created sample file at: {input_file}")

columns_to_extract = ["Name", "Roll Number", "Marks"]

with (
    open(input_file, mode="r", encoding="utf-8", newline="") as infile,
    open(output_file, mode="w", encoding="utf-8", newline="") as outfile,
):
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)

    writer.writeheader()
    for row in reader:
        filtered_row = {col: row[col] for col in columns_to_extract}
        writer.writerow(filtered_row)

print(f"Done! Extracted columns saved to: {output_file}")
