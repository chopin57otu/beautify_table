def is_empty(e):
    if e is None:
        return True
    if isinstance(e, str) and not e:
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
        return (e
                .replace("\t", "")
                .replace("\n", "")
                .replace(" ", "")
                .replace("-", "")
                .replace("%", "")
                .replace(",", ".")
                .isdigit()
               )
    return False
