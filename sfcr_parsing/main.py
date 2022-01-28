import glob

import numpy as np
import pandas as pd

if __name__ == "__main__":
    for f in glob.glob("../data/res/*.csv", recursive=True):
        print("parsing", f)
        c = pd.read_csv(f, sep=',', thousands=' ', header=None, encoding='UTF-8')
        print(c)


def squeeze_headers(c, number_area):
    sc = c.applymap(lambda x: " " if isinstance(x, float) and np.isnan(x) else x)
    ie, je = number_area

    l = sc.iloc[0, :]
    for i in range(1, ie):
        l = l.str.cat(sc.iloc[i], sep=' ')

    sc = pd.concat([l.to_frame().T, sc.drop(axis=0, index=range(0, ie))])

    l = sc.iloc[:, 0]
    for i in range(1, je):
        l = l.str.cat(sc.iloc[:, i], sep=' ')
    sc = pd.concat([l.to_frame(), sc.drop(axis=1, columns=range(0, je))], axis=1)
    sc = sc.set_index([0])
    return sc