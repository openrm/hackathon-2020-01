import os
import csv
import json
import argparse
import numpy as np
from keras import metrics, backend as K

class INFO:
    id = 'rotation_correction'
    name = 'Document Image Rotation Correction'

def compute_accuracy(y_pred=[], y_true=[]):
    y_pred, y_true = np.array([y if y else -1 for y in y_pred], dtype=int), \
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

        accuracy = compute_accuracy(y_pred=[pred_dict.get(name) for name in files],
                                    y_true=[true_dict.get(name) for name in files])

        metrics = {'accuracy': accuracy, 'score': accuracy}

        print(json.dumps(metrics))
