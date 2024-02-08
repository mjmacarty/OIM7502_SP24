# user class
import datetime as dt
from dateutil.parser import parse
import dateutil


class User:

    def __init__(self, username, password, email, birthday):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"Username: {self.username}\npassword: {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def __eq__(self, other):
        return self.username == other.username

    def get_age(self):
        """ Calculates user age based on birthdate"""
        b_day = parse(self.birthday)
        today = dt.datetime.now()
        return (today - b_day).days // 365


if __name__ == "__main__":
    user = User(username='Fred', password="password", email="fred@some.com", birthday="2/7/1999")
    print(user.username)
    print(user)
    print(repr(user))
    other = User("Fred", "1234", "freddie@some.com", "2/8/00")
    print(user.get_age())
