import os
import csv
import json
import argparse
import Levenshtein

class INFO:
    id = 'entity_extraction'
    name = 'Entity Extraction from Train Ticket Images'

def get_reader(f):
    has_header = csv.Sniffer().has_header(f.read(256))
    f.seek(0)
    if has_header: next(f, None)
    return csv.reader(f)

def build_dict(gen):
    return {
        name: {
            'origin': origin,
            'dest': dest,
            'line': line,
            'company': company,
            'price': price,
            'issued_at': issued_at,
            'expire_at': expire_at
        }
        for name, origin, dest, line, company, price, issued_at, expire_at in gen
    }

def compute_similarity(pred_dict, true_dict):
    score_sum = 0
    for k, true in true_dict.items():
        true = true if true else ''
        pred = pred_dict[k] if k in pred_dict and pred_dict[k] else ''
        true, pred = true.decode('utf-8'), pred.decode('utf-8')
        score = float(Levenshtein.distance(pred, true)) / max(len(true), len(pred)) \
            if true or pred else 0
        score_sum += score
    return score_sum / len(true_dict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pred_path', type=str)
    parser.add_argument('true_path', type=str)
    flags = parser.parse_args()

    assert os.path.exists(flags.pred_path)
    assert os.path.exists(flags.true_path)

    with open(flags.pred_path, 'r') as pred_f, \
            open(flags.true_path, 'r') as true_f:
        pred_dict = build_dict(get_reader(pred_f))
        true_dict = build_dict(get_reader(true_f))
        files = true_dict.keys()

        score_sum = 0

        for key in files:
            score_sum += compute_similarity(pred_dict[key] if key in pred_dict else dict(),
                                            true_dict[key])

        score = 1 - score_sum / len(files)
        metrics = {'accuracy': score, 'score': score}

        print(json.dumps(metrics))

