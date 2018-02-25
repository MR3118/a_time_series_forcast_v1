# import sklearn as skl
# import keras as ks
# from keras.layers import Dense,LSTM
import numpy as np
import copy


class Main:

    def __init__(self, data_set, predict_times, goal_accuracy):
        self.data = data_set
        self.predict_times = predict_times
        self.goal_accuracy = goal_accuracy

    @staticmethod
    def judge(predict_data, real_data, threshold):
        mape = sum(abs(predict_data - real_data)) / int(len(predict_data)) * 100
        if mape > threshold:
            return False
        else:
            return True


class DataProcess(Main):

    def __init__(self, data_set, predict_times, goal_accuracy, history_time):
        super(DataProcess, self).__init__(data_set, predict_times, goal_accuracy)
        self.history_time = history_time

    def data_dispose(self, split_portion=0.8, scale_method='standard'):
        history_time=self.history_time
        dt = np.array(self.data)
        x = np.array([dt[i:i + history_time] for i in range(len(dt) - history_time)])
        xs = copy.deepcopy(x[:-1])
        y = np.array([dt[i + history_time] for i in range(len(dt) - history_time)])
        ys = copy.deepcopy(y)
        np.random.seed(1)
        np.random.shuffle(xs)
        np.random.seed(1)
        np.random.shuffle(ys)

        train_x = xs[:int(len(xs) * split_portion)]
        train_y = ys[:int(len(xs) * split_portion)]
        test_x = xs[len(xs) * split_portion:]
        test_y = ys[len(xs) * split_portion:]

        if scale_method == 'no':
            return x[-1], train_x, train_y, test_x, test_y
        elif scale_method == 'minmax':
            v_max = max(np.append(train_y, train_x))
            v_min = min(np.append(train_y, train_x))

            def minmax(var):
                return (var - v_min) / (v_max - v_min)

            return minmax(x[-1]), minmax(train_x), minmax(train_y), minmax(test_x), minmax(test_y)
        elif scale_method == 'standard':
            pass
if __name__ == '__main__':
    data = np.arange(0, 20)
    # pre_dispose(data, 6)
