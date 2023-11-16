from webhandler import startup, add_user
from csvhandler import read_input, archive_write
from datetime import date

TEST = False
file_dicts = {"Test": ["CPQUserBot/test_input.csv","CPQUserBot/test_archive.csv"], "Prod": ["CPQUserBot/input.csv","CPQUserBot/archive.csv"]}
input_file, archive_file = file_dicts["Test"] if TEST else file_dicts["Prod"]

if __name__ == "__main__":
    user_dicts = read_input(input_file)
    driver = startup()
    for user_dict in user_dicts:
        user_dict["Status"] = add_user(driver, user_dict)
        user_dict["Date"] = date.today()
    archive_write(archive_file, user_dicts)