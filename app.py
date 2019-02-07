def time_converter(time):

    first_two = str(time[0:2])
    last_two = str(time[-2:])

    am_pm = "p.m"

    if 12 > int(first_two):
        am_pm = "a.m"
        if int(first_two) == 0:
            first_two = 12

    elif int(first_two) > 12:
        first_two = int(first_two) - 12

    return "{}:{} {}".format(int(first_two), last_two, am_pm)


# example - print(time_converter("12:30")
# output: 12:30 p.m 
