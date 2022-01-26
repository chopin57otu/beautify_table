import glob

import pandas as pd

if __name__ == "__main__":
    for f in glob.glob("../data/res/*.csv", recursive=True):
        print("parsing",f)
        c = pd.read_csv(f, sep=',', thousands=' ', header=None, encoding='UTF-8')
        print(c)
