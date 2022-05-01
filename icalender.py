from icalendar import Calendar

lookForWork = ['game', 'steam', 'helium', 'web', '3D', 'implement', 'asset', 'fix', 'hesap', 'research', 'port']
lookForDnD = ['D&D']
g = open(r'S:\____\Veri\semihsolmazgul@gmail.com.ical\semihsolmazgul@gmail.com.ics', 'rb')
gcal = Calendar.from_ical(g.read())


def parse_that(title, look_for_list):
    totalTime = 0
    get_in = True
    first_day = None
    last_day = None

    for component in gcal.walk():
        if component.name == 'VEVENT':
            summary = component.get('summary')
            if first_substring(look_for_list, summary):
                start = component.get('dtstart').dt
                end = component.get('dtend').dt

                if get_in:
                    first_day = start
                    last_day = start
                    # print(first_day)

                if last_day < start:
                    last_day = start

                # print('----------------------')
                # print(start)
                # print(summary)
                # print(end)

                totalTime += (end - start).total_seconds() / 3600
                get_in = False

    # print(last_day)
    numberOfDay = (last_day - first_day).total_seconds() / (3600 * 24)
    print(title)
    print("Number of days: " + str(round(numberOfDay, 1)))
    print("Total work hours: " + str(round(totalTime, 1)))
    print("Average per day: " + str(round(totalTime / numberOfDay, 1)))
    print()


def first_substring(the_list, substring):
    for s in the_list:
        if s in substring:
            return substring
    return None


if __name__ == '__main__':
    parse_that('Work', lookForWork)
    parse_that('D&D', lookForDnD)
    g.close()
