import joblib
import features_extraction
import sys
import numpy as np
import os

from features_extraction import WORKING_PATH


def get_prediction_from_url(test_url,html):
    features_test = features_extraction.main(test_url,html)
    features_test = np.array(features_test).reshape((1, -1))
    #localPath = os.getcwd()
    clf = joblib.load(WORKING_PATH  + '/classifier/random_forest1.pkl')

    pred = clf.predict(features_test)
    return int(pred[0])

if __name__ == "__main__":
    main()
