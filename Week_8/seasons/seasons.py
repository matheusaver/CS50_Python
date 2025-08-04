from datetime import date
import sys
import inflect


def main():
    user_date = input("Birth date: ")
    convert(user_date)


def convert(user_date):
    try:
        user = date.fromisoformat(user_date)
    except:
        return sys.exit(1)
    else:
        p = inflect.engine()
        today = date.today()
        diference = today - user
        days = diference.days
        minutes = days * 1440
        result = p.number_to_words(minutes, andword = '')
        print(result.capitalize(), "minutes")
        return result.capitalize() + " minutes"

if __name__ == "__main__":
    main()
