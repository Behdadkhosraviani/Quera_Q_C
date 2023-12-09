import numpy as np


def moving_average(data_list, window_size):
    averages = list()
    for i in range(len(data_list) - window_size + 1):
        averages.append(np.average(data_list[i: i + window_size]))

    return np.array(averages)
