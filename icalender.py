from icalendar import Calendar
import math


def parse_that():
    totalTime = 0
    get_in = True
    first_day = None
    last_day = None

    g = open('semih.ics', 'rb')
    gcal = Calendar.from_ical(g.read())

    for component in gcal.walk():
        if component.name == "VEVENT":
            sum = component.get('summary')
            if ("game" in sum) or ("steam" in sum) or ("hel" in sum) or ("web" in sum) or ("3D" in sum) \
                    or ("hot" in sum) or ("port" in sum) or ("input" in sum) or ("asset" in sum) \
                    or ("fix" in sum) or ("hesap" in sum):

                start = component.get('dtstart').dt
                end = component.get('dtend').dt

                if get_in:
                    first_day = start
                    last_day = start
                    # print(first_day)

                if last_day < start:
                    last_day = start

                # print(sum)
                # print(start)
                # print(end)

                totalTime += (end - start).total_seconds() / 3600
                get_in = False

    # print(last_day)
    numberOfDay = (last_day - first_day).total_seconds() / (3600 * 24)
    print("Number of days: " + str(math.ceil(numberOfDay)))
    print("Total work hours: " + str(math.ceil(totalTime)))
    print("Average per day: " + str(math.ceil(totalTime / numberOfDay)))
    g.close()


if __name__ == '__main__':
    parse_that()
