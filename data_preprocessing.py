import sklearn as skl
from sklearn import preprocessing
import numpy as np


def data_spilt(input_x, label_y, proportion=0.8, random_seed=0):
    np.random.seed(random_seed)
    np.random.shuffle(input_x)
    np.random.seed(random_seed)
    np.random.shuffle(label_y)
    train_length = int(len(label_y) * proportion)
    train_data = {'x': input_x[:train_length], 'y': label_y[:train_length]}
    test_data = {'x': input_x[train_length:], 'y': label_y[train_length:]}
    return train_data, test_data


def data_scale(train_data, test_data=None, method='auto'):
    
    pass


if __name__ == '__main__':
    pass