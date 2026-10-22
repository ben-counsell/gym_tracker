# This module takes user input and returns 
# a dictionary containing their choices

def choose_exercise_to_analyse(gym_dict, exercises):
    people = [person for person in gym_dict]
    exercise_keys = [exercise for exercise in exercises]
    exercise_values = [exercises[exercise] for exercise in exercises]
    
    if len(people) > 1:
        person = input(
            "Whose progress would you like to analyse?\n" \
            "%s" \
            "Please input a number to continue.\n" %iterate_options(people))
        person = check_for_bad_input(len(people), person)
    else:
        person = 1
    if len(exercise_keys) > 1:
        exercise = input(
            "Which exercise would you like to analyse?\n" \
            "%s" \
            "Please enter a number to continue.\n" %iterate_options(exercise_values)
        )
        exercise = check_for_bad_input(len(exercise_keys), exercise)
    else:
        exercise = 1
    
    return {
        "person" : people[person], 
        "exercise" : exercise_keys[exercise]
    }

def iterate_options(options):
    result = ""
    for i, option in enumerate(options):
        result += "%s. %s\n" %(i+1, option)
    return result

def check_for_bad_input(no_of_options, inp):
    options = [str(x+1) for x in range(no_of_options)]
    while not inp in options:
        inp = input("%s\n" %_print_numbers(options))
    return int(inp) - 1    

def _print_numbers(options):
    if len(options) == 2:
        return "Please enter 1 or 2"
    else:
        option_string = "Please enter "
        option_string += ", ".join([str(option+1) for option in range(len(options) - 2)])
        option_string += ", " + str(options[-2]) + " or " + str(options[-1])
    return option_string
