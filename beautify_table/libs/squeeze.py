import numpy as np
import pandas as pd


def squeeze_headers(pdf, number_area):
    def apply_transform(s):
        return s.apply(str).apply(lambda x: "" if x == "NaN" else x)

    sc = pdf.applymap(lambda x: "NaN" if isinstance(x, float) and np.isnan(x) else x)
    ie, je = number_area

    l1 = None
    for i in range(0, ie):
        if l1 is None:
            l1 = apply_transform(sc.iloc[0, :])
        else:
            l1 = l1.str.cat(apply_transform(sc.iloc[i]), sep=' ')
    if l1 is not None:
        sc = pd.concat([l1.to_frame().T, sc.drop(axis=0, index=range(0, ie))])

    l2 = None
    for i in range(0, je):
        if l2 is None:
            l2 = apply_transform(sc.iloc[:, 0])
        else:
            l2 = l2.str.cat(apply_transform(sc.iloc[:, i]), sep=' ')
    if l2 is not None:
        sc = pd.concat([l2.to_frame(), sc.drop(axis=1, columns=range(0, je))], axis=1)

    if l1 is not None:
        sc.iloc[0, :] = [f"*{i}" if x.strip() == "" else x for i, x in enumerate(sc.iloc[0, :])]
        sc.columns = sc.iloc[0, :]
        sc = sc.drop(axis=0, index=[0])

    sc = sc.set_index(sc.columns[0])

    return sc


def merge_columns(pdf):
    columns_to_drop = []
    for c1, c2 in zip(pdf.columns, pdf.columns[1:]):
        c1s, c2s = str(c1), str(c2)
        all_is_nan = (pdf[c1] == "NaN").all()
        if not isinstance(all_is_nan, pd.Series) and all_is_nan and c2s[0] == "*":
            pdf[c1] = pdf[c2]
            columns_to_drop.append(c2)

    return pdf.drop(columns=columns_to_drop)
