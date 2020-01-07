import os
import csv
import argparse
import numpy as np
from keras import metrics, backend as K

import common

is_pr = 'CIRCLE_PR_NUMBER' in os.environ

class INFO:
    name = 'Document Image Rotation Correction'

def compute_accuracy(y_pred=[], y_true=[]):
    y_pred, y_true = np.array(y_pred, dtype=int), \
        np.array(y_true, dtype=int)

    acc = metrics.accuracy(y_pred, y_true)
    return K.eval(K.sum(acc)) / y_true.shape[0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pred_path', type=str)
    parser.add_argument('true_path', type=str)
    flags = parser.parse_args()

    assert os.path.exists(flags.pred_path)
    assert os.path.exists(flags.true_path)

    with open(flags.pred_path, 'r') as pred_f, \
            open(flags.true_path, 'r') as true_f:
        pred_dict = {name: label for name, label in csv.reader(pred_f)}
        true_dict = {name: label for name, label in csv.reader(true_f)}
        files = true_dict.keys()

        score = compute_accuracy(y_pred=[pred_dict.get(name) for name in files],
                                 y_true=[true_dict.get(name) for name in files])

        if is_pr:
            common.comment_result(INFO, {'Accuracy': score})

        print(score)
