from beautify_table.libs.squeeze import squeeze_headers, merge_coumns
from beautify_table.libs.string_manipulations import is_empty, is_number, is_string


def _identification_mask(pdf):
    def substitute(e):
        if is_empty(e):
            return None
        if is_number(e):
            return "n"
        if is_string(e):
            return "s"
    return pdf.applymap(substitute)


def _identify_number_area(c):
    ic = _identification_mask(c)
    dc = ic.copy()

    max_i, max_j = ic.shape
    index_sum = float('inf')
    for i in range(ic.shape[0]):
        for j in range(ic.shape[1]):
            if 0 == (ic.iloc[i:, j:] == "s").sum().sum() and i + j < index_sum:
                index_sum = i + j
                max_i, max_j = i, j

    return max_i, max_j


def process_table(table):
    na = _identify_number_area(table)
    sc = squeeze_headers(table, na)
    final = merge_coumns(sc)
    return final

