import pandas as pd
import numpy as np

def average_rate_of_progress(data, exercise, person="Ben"):
    # Calculates the mean difference in weight between
    # sessions, indicating overall rate of progress
    difference_total = 0
    counter = 0
    previous_amount = None

    for date in data[person]:
        if exercise in data[person][date]:
            current_amount = data[person][date][exercise]

            if previous_amount is not None:
                difference_total += current_amount - previous_amount
                counter += 1

            previous_amount = data[person][date][exercise]
    
    if counter == 0:
        return 0
    
    result = difference_total / counter

    assert verify_result(data, exercise, person, result)

    return round(result, 2)

def verify_result(data, exercise, person, result):
    dates = [date for date in data[person] if exercise in data[person][date]]
    weights = [data[person][date][exercise] for date in dates]
    
    series = pd.Series(weights)
    mean = np.mean(series.diff())

    return np.isclose(mean, result)
