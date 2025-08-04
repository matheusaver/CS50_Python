def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.translate({ord(c): None for c in '$'}))

def percent_to_float(p):
    new = float(p.translate({ord(c): None for c in '%'}))
    return float(new*0.01)

main()
