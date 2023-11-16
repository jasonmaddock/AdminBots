import csv
from datetime import date

def read_input(filename):
    output = []
    with open(filename, newline="", encoding="utf-8-sig") as csvfile:
        lines = csv.DictReader(csvfile)
        output = [row for row in lines]
        return(output)

def archive_write(filename, user_dict):
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["Date", "FirstName", "LastName", "Email", "UserType", "Country", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        [writer.writerow(row) for row in user_dict]


if __name__ == "__main__":
    user_dicts = read_input(filename = "CPQUserBot/test_input.csv")
    for user_dict in user_dicts:
        user_dict["Date"] = date.today()
        user_dict["Status"] = "Test"
    archive_write("CPQUserBot/test_archive.csv", user_dicts)