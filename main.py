########### Ben  Counsell ###########
##### Fundamentals of Computing #####
### Graded Programming Assignment ###

# This program was designed to process data I have recorded
# over the last few months of mine and my wife's progress in strength 
# training. It takes a text file as input and parses it, then outputs two
# graphs demonstrating progress in different exercises
# over time, measured by weight lifted. 

import parser, analyser, inputter, finder, plotter

# This determines the exercises that the parser will
# search the dataset for later. Eventually I would like
# to make it possible to configure this by editing a 
# config file.
exercises = {
        "ohp":"Overhead Press",
        "bench":"Bench Press",
        "squat":"Squat",
        "deadlift":"Deadlift"
    }

# To verify that the file has loaded correctly:
# there should be 47 dates in the dataset
number_of_dates = 47

def read_file(file):
    lines = file.readlines()
    if parser.check_number_of_records(lines) == number_of_dates:
        global gym_dict 
        gym_dict = parser.parse(lines, exercises)
    else:
        raise Exception("Unable to parse chosen file. Please check that \"gym.txt\" is in current working directory and that it contains %s dates." %number_of_dates)

try:
    with open("gym.txt", "r") as file:
        # opens file, generates a list of the lines
        # contained in the file, checks the file 
        # has loaded correctly, then calls parse()
        # to parse the lines. Saves the result
        # to a dictionary.
        read_file(file)
except FileNotFoundError:
    alt_file = finder.select_data_file()
    with open(alt_file, "r") as file:
        read_file(file)
    
choice = inputter.choose_exercise_to_analyse(gym_dict, exercises)

result =  analyser.average_rate_of_progress(gym_dict, choice["exercise"], choice["person"])

print("Average rate of progress for %s for %s: %skg\n" 
        %(
    exercises[choice["exercise"]].lower(), 
    choice["person"], 
    result
    )
)

plotter.plot(gym_dict, exercises, choice["exercise"], choice["person"]) 