"""
Functions for preprocessing data for ML tasks
"""

import pandas as pd
import numpy as np

def scale_min_max(data):
    """
    scale between 0 and 1: x_ = (x - x_min) / (x_max - x_min)
    :param data: list, pd.Series or np.ndarray
    :return: scaled list, pd.Series or np.ndarray
    """

    # try except block is used to check and return the datatype. If a TypeError occurs, the function breaks up
    try:
        data, output_format = check_return_datatype(data)
    except TypeError as e:
        return print(e)

    # Scale the data between 0 and 1
    scaled_data = (data - np.min(data)) / (np.max(data) - np.min(data))

    if output_format == list:
        scaled_data = scaled_data.tolist()
    elif output_format == pd.Series:
        scaled_data = pd.Series(scaled_data)

    return scaled_data

def invert_scale_min_max(scaled_data, original_min, original_max):
    """
    invert scaling operation and rescale to original
    :param scaled_data: list, pd.Series or np.ndarray
    :param original_min: float or int value
    :param original_max: float or int value
    :return: list, pd.Series or np.ndarray
    """

    # try except block is used to check and return the datatype. If a TypeError occurs, the function breaks up
    try:
        scaled_data, output_format = check_return_datatype(scaled_data)
    except TypeError as e:
        return print(e)

    # Invert the min-max scaling to get the original data range
    inverted_data = (scaled_data - np.min(scaled_data)) / \
                    (np.max(scaled_data) - np.min(scaled_data)) * (original_max - original_min) + original_min

    if output_format == list:
        inverted_data = inverted_data.tolist()
    elif output_format == pd.Series:
        inverted_data = pd.Series(inverted_data)

    return inverted_data

def check_return_datatype(data):
    """
    function to check datatype and convert to np.ndarray if input is list or pd.Series
    :param data:
    :return:
    """
    if isinstance(data, list):
        output = np.array(data)
        output_format = list
    elif isinstance(data, pd.Series):
        output = data.values
        output_format = pd.Series
    elif isinstance(data, np.ndarray):
        output_format = np.ndarray
        output = data
    else:
        raise TypeError("Input data type not supported. Please provide a list, a pd.Series, or a np.ndarray.")

    return data, output_format


if __name__ == '__main__':

    print('test scenario to perform scale transformation and inverse scale transformation of '
          'a list, a np.ndarray and one column of a pd.Dataframe \n')

    # scale and invert scaling
    data_list = [1, 2, 3, 4, 5]
    scaled_data_list = scale_min_max(data_list)
    inverse_data_list = invert_scale_min_max(scaled_data_list, min(data_list), max(data_list))
    print(f'list: {data_list}')
    print(f'scaled list: {scaled_data_list}')
    print(f'inverse operation list: {inverse_data_list} \n')

    df = pd.DataFrame({'A': data_list})
    scaled_data_df = pd.DataFrame()  # create the df first
    inverse_data_df = pd.DataFrame()  # create the df first
    scaled_data_df['A'] = scale_min_max(df['A'])  # add the scaled data as new series
    inverse_data_df['A'] = invert_scale_min_max(scaled_data_list, min(df['A']), max(df['A']))
    print(f'pd.Dataframe: {df}')
    print(f'scaled pd.Dataframe: {scaled_data_df}')
    print(f'inverse operation df: {inverse_data_df} \n')

    data_array = np.array(data_list)
    scaled_data_array = scale_min_max(data_array)
    inverse_data_array = invert_scale_min_max(scaled_data_list, min(data_array), max(data_array))
    print(f'list: {data_array}')
    print(f'scaled list:: {scaled_data_array}')
    print(f'inverse operation array: {inverse_data_array} \n')

    # test TypeError
    print('scenario with wrong data type:')
    data_tupel = (1, 2, 3, 4, 5)  # tupel type raises an error
    scaled_data_tupel = scale_min_max(data_tupel)
    scaled_data_tupel = (0, 0.25, 0.5, 0.75, 1)
    inverse_data_tupel = invert_scale_min_max(scaled_data_tupel, 0, 5)

