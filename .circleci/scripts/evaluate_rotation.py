import os
import csv
import argparse
import numpy as np
from keras import metrics, backend as K

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pred_path', type=str)
    parser.add_argument('true_path', type=str)
    flags = parser.parse_args()

    assert os.path.exists(flags.pred_path)
    assert os.path.exists(flags.true_path)

    with open(flags.pred_path, 'r', newline='') as pred_f, \
            open(flags.true_path, 'r', newline='') as true_f:
        pred_dict = {name: label for name, label in csv.reader(pred_f)}
        true_dict = {name: label for name, label in csv.reader(true_f)}
        files = true_dict.keys()

        y_pred, y_true = np.array([pred_dict.get(name) for name in files], dtype=int), \
            np.array([true_dict.get(name) for name in files], dtype=int)

        acc = metrics.accuracy(y_pred, y_true)
        print(K.eval(K.sum(acc)) / y_true.shape[0])
