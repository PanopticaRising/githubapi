from functools import reduce


def dict_to_td(dict):
    # TODO: This could be much smarter and provide a better DX. We can truncate long strings, add hover text, and limit the number of rows generated.
    return reduce(lambda accum, tup: accum + f"<tr><td>{tup[0]}</td><td>{tup[1]}</td></tr>", dict.items(), "")
