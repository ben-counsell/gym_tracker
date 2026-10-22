import re
import datetime

# The parse() function iterates through the data line by line and 
# outputs a dictionary which contains all of the training dates, the
# exercises that were done, who they were done by, and what weight was 
# used, in that order. Dictionary[Person][Date][Exercise] = Weight

# I wanted to be able to account for some variations in input, so the parser has
# a degree of flexibility in what it can read. It expects input
# to follow roughly this repeating format:

# DD/MM
# exercise weight

def check_number_of_records(lines):
    # Verifies data has loaded correctly
    # by counting number of records
    date_counter = 0
    for line in lines:
        if _is_date(line):
            date_counter += 1
    return date_counter

def parse(lines, exercises, year=2025): 
    # Parses data, returning a dictionary 
    # with the following structure:
    # dictionary["person"]["date"]["exercise"] = weight

    result = {
        "Ben" : {},
        "Vale" : {}
    }

    # Keeps track of the previous date
    # in order to increment year at the 
    # appropriate time.
    previous_date = datetime.date(year, 1, 1)

    for i, line in enumerate(lines):

        # Iterates through the data to find the next date, then splits
        # the date into day, month, and year.
        if _is_date(line):
            date_list = line.split("/")

            # Checks if the current month is lower than the previous, indicating
            # that the year should be incremented. This part would break if there were 
            # a gap of greater than 11 months in the data.
            if previous_date.month > int(date_list[1]):
                year += 1

            date = datetime.date(year, int(date_list[1]), int(date_list[0]))

            result["Ben"][date] = {}

            _find_exercises_for_dates(result, lines, exercises, date, i)

            previous_date = date
        i += 1
    return result

def _is_date(line):
    # Returns True if a line contains text in date format (minimally D/MM)
    return re.match("\d*/\d\d", line)

def _find_exercises_for_dates(result, lines, exercises, date, i, j=1, person="Ben"):
    # Iterates over exercises performed on a given date. By default
    # this function attributes exercises to Ben.
    while i + j < len(lines):

        # Stops the loop when the next date is reached
        if _is_date(lines[i+j]):
            break

        # Also stops the loop if Valentina's name is reached. 
        # Recursively calls the function specifying that 
        # subsequent exercises were done by Valentina.
        if "VALENTINA" in lines[i+j]:
            result["Vale"][date] = {}
            j += 1
            _find_exercises_for_dates(result, lines, exercises, date, i, j, person="Vale")
            break

        _add_exercises_to_date(result, lines[i+j], exercises, date, person)
        j += 1

def _add_exercises_to_date(result, line, exercises, date, person):
    # Checks if any of the exercises are included in the line, and if
    # so adds the weight value to the appropriate section of the dictionary.
    for exercise in exercises:
        if exercise in line:
            weight = line.split(" ")[1]
            if "x" in weight:
                weight = weight.split("x")[0]
            weight = weight.strip("\n")
            weight = weight.strip("kg")
            result[person][date][exercise] = float(weight)