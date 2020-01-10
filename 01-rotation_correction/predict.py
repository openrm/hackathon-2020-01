import os
import sys
import csv
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

if __name__ == '__main__':
    # define command-line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path',
                        type=str)
    parser.add_argument('--image_dir',
                        type=str)
    parser.add_argument('-o', '--output',
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()

    # load trained weights
    model = load_model(args.model_path)

    image_paths = [
        os.path.join(args.image_dir, filename)
        for filename in os.listdir(args.image_dir)
        if os.path.splitext(filename)[-1].lower() in ['.jpg', '.jpeg', '.png']
    ]

    data_gen = (img_to_array(load_img(path)) for path in image_paths)

    preds = model.predict_generator(data_gen)

    writer = csv.writer(args.output)
    for i, pred in enumerate(preds):
        filename = os.path.basename(image_paths[i])
        label = np.argmax(pred)
        writer.writerow([filename, label * 90])
