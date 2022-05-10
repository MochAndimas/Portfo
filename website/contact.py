import csv
from flask import Blueprint, request, redirect, flash

contact = Blueprint("contact", __name__)


def user_data(data):
    """user data"""
    with open("data.csv", mode="a", newline="\n", encoding="utf-8") as file2:
        fieldnames = ["name", "email", "message"]
        writer = csv.DictWriter(file2, fieldnames=fieldnames, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)


@contact.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """submit form"""
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            user_data(data)
            flash('You were successfully logged in')
            return redirect("/index.html")
        except:
            return print("did not save to database")
    else:
        return print("something went wrong!!")
