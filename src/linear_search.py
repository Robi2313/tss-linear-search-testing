def linear_search(v, key):
    """
    Cauta valoarea key intr-o lista de exact 5 numere intregi.

    Parametri:
        v: lista de numere intregi, cu lungimea 5
        key: valoarea cautata

    Returneaza:
        indicele primei aparitii a lui key in lista
        -1 daca key nu se afla in lista

    Ridica:
        TypeError daca v nu este lista
        ValueError daca lista nu are lungimea 5
        TypeError daca elementele listei sau key nu sunt intregi
    """

    if not isinstance(v, list):
        raise TypeError("v trebuie sa fie o lista")

    if len(v) != 5:
        raise ValueError("v trebuie sa aiba exact 5 elemente")

    if not isinstance(key, int):
        raise TypeError("key trebuie sa fie numar intreg")

    for element in v:
        if not isinstance(element, int):
            raise TypeError("toate elementele listei trebuie sa fie numere intregi")

    for i in range(len(v)):
        if v[i] == key:
            return i

    return -1