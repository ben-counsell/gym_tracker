import matplotlib.pyplot as plt
import os

def plot(dict, exercises, exercise, person):
    # Plots and saves a graph for the 
    # specified exercise and person
    x_values = [date for date in dict[person] if exercise in dict[person][date]]
    y_values = [dict[person][date][exercise] for date in x_values]
    plt.plot_date(x_values, y_values, linestyle="solid", ydate=False, label=exercises[exercise])
    plt.ylabel("Weight (kg)")
    plt.title("%s %s Chart" %(person, exercises[exercise]))
    filepath = generate_filepath(person, exercise)
    plt.savefig(filepath, format="pdf")
    plt.clf()
    print("Chart saved to \"output/%s_%s_chart.pdf\"" %(person.lower(), exercise))
            
def generate_filepath(person, exercise):
    # Checks if output folder exists,
    # makes one if it doesn't. 
    # Returns filepath.
    target_dir = "output"
    filename = person.lower() + "_" + exercise + "_chart.pdf"
    filepath = os.path.join(target_dir, filename)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    return filepath