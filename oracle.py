def oracle_linear_search(v, key):
    """
    Oracol independent pentru linear_search.
    Nu apeleaza functia testata.
    """

    try:
        return v.index(key)
    except ValueError:
        return -1