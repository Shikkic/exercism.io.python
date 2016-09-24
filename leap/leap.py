# start with def func_name(args)


# Every year that is evenly divisble by 4

# except Every year that is evenly divisible by 100

# unless that year is also envenly divislbe by 400

def is_leap_year(year):
    if year < 0:
        return False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    return False
