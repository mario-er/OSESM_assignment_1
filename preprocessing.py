"""
Functions for preprocessing data
"""

import pandas as pd
import numpy as np

def scale_min_max(data):
    """
    scale between 0 and 1: x_ = (x - x_min) / (x_max - x_min)
    :param data: list, pd.Series or np.ndarray
    :return: scaled list, pd.Series or np.ndarray
    """

    if isinstance(data, list):
        data = np.array(data)  # necessary for uniform min max operation
        output_format = list
    elif isinstance(data, pd.Series):
        data = data.values
        output_format = pd.Series
    elif isinstance(data, np.ndarray):
        output_format = np.ndarray
    else:
        raise ValueError("Input data type not supported. Please provide a list, a pd.Series, or a np.ndarray.")

    # Scale the data between 0 and 1
    scaled_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    # scaled_data = (data - data.min()) / (data.max() - data.min())

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
    if isinstance(scaled_data, list):
        scaled_data = np.array(scaled_data)
        output_format = list
    elif isinstance(scaled_data, pd.Series):
        scaled_data = scaled_data.values
        output_format = pd.Series
    elif isinstance(scaled_data, np.ndarray):
        output_format = np.ndarray
    else:
        raise ValueError("Input data type not supported. Please provide a list, a pd.Series, or a np.ndarray.")

    # Invert the min-max scaling to get the original data range
    inverted_data = (scaled_data - np.min(scaled_data)) / \
                    (np.max(scaled_data) - np.min(scaled_data)) * (original_max - original_min) + original_min

    if output_format == list:
        inverted_data = inverted_data.tolist()
    elif output_format == pd.Series:
        inverted_data = pd.Series(inverted_data)

    return inverted_data


if __name__ == '__main__':

    # scale and invert scaling
    data_list = [1, 2, 3, 4, 5]
    scaled_data_list = scale_min_max(data_list)
    inverse_data_list = invert_scale_min_max(scaled_data_list, min(data_list), max(data_list))
    print(f'list: {data_list}')
    print(f'scaled list:: {scaled_data_list}')
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

