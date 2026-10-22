import os
import sys
import inputter

cwd = os.getcwd()
cwd_contents = os.listdir(cwd)

data_sources = []

def select_data_file():
    for file in cwd_contents:
        if '.txt' in file:
            data_sources.append(file)

    if data_sources == 0:
        sys.exit("Couldn't find \"gym.txt\" in current working directory.")
    
    else:
        inp = inputter.check_for_bad_input(len(data_sources), input(
            "Expected to find \"gym.txt\". " \
            "Is there another file you would like to try to process?\n" \
            "Please enter a number to choose your data source.\n" \
            "%s" %inputter.iterate_options(data_sources)
        ))
        data_source = data_sources[inp]

    return data_source