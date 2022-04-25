from typing import Iterable

import numpy as np


def omit_symbols(s: str, symbols: Iterable[str]):
    for symbol in symbols:
        s.replace(symbol, "")
    return s


def omit_special_symbols(s: str):
    return (s.replace("\t", "")
            .replace("\n", "")
            .replace(" ", "")
            .replace("-", "")
            .replace("%", "")
            .replace(".", ""))


def is_empty(e):
    if e is None:
        return True
    if isinstance(e, str):
        if not e:
            return True
        if 0 == len(e.replace("\t", "")
                            .replace("\n", "")
                            .replace(" ", "")
                            .replace("-", "")
                            .replace("%", "")
                            .replace(",", ".")
                            .replace(".", "")
                    ):
            return True
    if isinstance(e, float) and np.isnan(e):
        return True
    if hasattr(e, '__len__') and len(e) == 0:
        return True
    return False


def is_string(e):
    if isinstance(e, str):
        if len(e.replace("\t", "")
                       .replace("\n", "")
                       .replace(" ", "")
               ) > 0:
            return True
    return False


def is_number(e):
    if isinstance(e, float) and not np.isnan(e):
        return True
    if isinstance(e, str) and e:
        return (
            e
                .replace("\t", "")
                .replace("\n", "")
                .replace(" ", "")
                .replace("-", "")
                .replace("%", "")
                .replace(",", ".")
                .replace(".", "")
                .isdigit()
        )
    return False
