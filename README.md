# TSS - Testare unitară în Python pentru funcția `linear_search`

![CI Status](https://github.com/Robi2313/tss-linear-search-testing/actions/workflows/ci.yml/badge.svg)

## Descriere proiect

Acest proiect a fost realizat pentru materia **Testarea sistemelor software**. Am ales să lucrez în Python, deoarece mi s-a părut varianta cea mai potrivită pentru a testa rapid o funcție, pentru a rula teste automate și pentru a obține rapoarte de coverage.

Funcția testată se numește `linear_search(v, key)`. Ea primește o listă `v` de exact 5 numere întregi și o valoare `key`. Dacă valoarea se află în listă, funcția returnează poziția primei apariții. Dacă valoarea nu se află în listă, funcția returnează `-1`.

Am ales această funcție deoarece este simplă ca idee, dar permite testarea mai multor situații: date valide, date invalide, valori aflate la începutul sau finalul listei, element lipsă, element repetat și verificarea comportamentului în cazul unor intrări greșite.

## Structura proiectului

```text
tss-linear-search-testing/
│
├── src/
│   ├── __init__.py
│   └── linear_search.py
│
├── tests/
│   ├── __init__.py
│   ├── test_black_box.py
│   ├── test_white_box.py
│   └── test_random.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── oracle.py
├── requirements.txt
├── critical_points.json
├── README.md
└── .gitignore
```

În folderul `src` se află funcția testată. În folderul `tests` am separat testele în funcție de metoda folosită: teste black-box, teste white-box și teste generate aleatoriu. Fișierul `oracle.py` este folosit pentru testele random, ca să compar rezultatul funcției mele cu o implementare independentă.

## Specificația funcției

Funcția `linear_search(v, key)` trebuie să respecte următoarele reguli:

* `v` trebuie să fie listă;
* lista trebuie să aibă exact 5 elemente;
* toate elementele listei trebuie să fie numere întregi;
* `key` trebuie să fie număr întreg;
* dacă `key` apare în listă, se returnează indexul primei apariții;
* dacă `key` nu apare în listă, se returnează `-1`;
* pentru date invalide se folosesc excepții (`TypeError` sau `ValueError`).

Codul funcției este următorul:

```python
def linear_search(v, key):
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
```

## Configurația folosită

| Componentă        | Valoare            |
| ----------------- | ------------------ |
| Sistem de operare | Windows            |
| Editor            | Visual Studio Code |
| Limbaj            | Python 3.12        |
| Testare           | pytest             |
| Coverage          | coverage.py        |
| CI/CD             | GitHub Actions     |
| Repository        | GitHub             |

Nu am folosit mașină virtuală. Proiectul a fost lucrat local în Visual Studio Code și apoi urcat pe GitHub.

## Instalare și rulare

Pentru instalarea dependențelor:

```bash
python -m pip install -r requirements.txt
```

Pentru rularea testelor:

```bash
python -m pytest
```

Pentru coverage:

```bash
python -m coverage run --branch -m pytest
python -m coverage report -m
python -m coverage html
```

Raportul HTML se generează local în:

```text
htmlcov/index.html
```

Folderul `htmlcov` nu este urcat pe GitHub, deoarece este generat automat.

## Testare black-box

Pentru testarea black-box am pornit de la specificație, nu de la cod. Am încercat să acopăr situațiile pe care utilizatorul funcției le poate întâlni.

Am folosit următoarele clase de echivalență:

| Caz                                | Exemplu                    | Rezultat așteptat |
| ---------------------------------- | -------------------------- | ----------------- |
| Valoarea este pe prima poziție     | `[7, 1, 2, 3, 4]`, `key=7` | `0`               |
| Valoarea este în interiorul listei | `[1, 2, 7, 3, 4]`, `key=7` | `2`               |
| Valoarea este pe ultima poziție    | `[1, 2, 3, 4, 7]`, `key=7` | `4`               |
| Valoarea nu există                 | `[1, 2, 3, 4, 5]`, `key=9` | `-1`              |
| Valoarea apare de mai multe ori    | `[3, 1, 3, 4, 3]`, `key=3` | `0`               |
| Lista are lungime prea mică        | `[1, 2, 3, 4]`             | `ValueError`      |
| Lista are lungime prea mare        | `[1, 2, 3, 4, 5, 6]`       | `ValueError`      |
| Parametrul `v` nu este listă       | `"12345"`                  | `TypeError`       |
| `key` nu este întreg               | `"3"`                      | `TypeError`       |
| Lista conține element invalid      | `[1, 2, "3", 4, 5]`        | `TypeError`       |

Aceste teste se află în fișierul:

```text
tests/test_black_box.py
```

## Analiza valorilor de frontieră

În cazul acestei funcții, frontierele cele mai importante sunt legate de lungimea listei și de poziția elementului căutat.

Am testat:

* listă cu exact 5 elemente;
* listă cu 4 elemente;
* listă cu 6 elemente;
* element căutat pe poziția `0`;
* element căutat pe poziția `4`.

Aceste cazuri sunt importante deoarece erorile apar des la marginile intervalelor. De exemplu, dacă funcția nu ar trata corect lungimea listei, ar putea accepta date care nu respectă specificația.

## Testare white-box

Pentru testarea white-box m-am uitat la structura funcției și am ales teste care să execute toate ramurile importante.

Am verificat:

* cazul în care `v` nu este listă;
* cazul în care lista nu are lungimea 5;
* cazul în care `key` nu este întreg;
* cazul în care lista conține un element care nu este întreg;
* cazul în care elementul este găsit;
* cazul în care elementul nu este găsit;
* cazul în care bucla se oprește repede;
* cazul în care bucla ajunge până la final.

Aceste teste se află în:

```text
tests/test_white_box.py
```

## Testare aleatoare

Pentru testarea aleatoare am generat liste de 5 numere întregi și valori `key` folosind modulul `random`. Am folosit `random.seed(...)` pentru ca rezultatele să poată fi reproduse.

Am creat două teste:

* unul cu 100 de cazuri generate aleatoriu;
* unul cu 500 de cazuri generate aleatoriu.

Pentru verificarea rezultatului am folosit un oracol independent, aflat în `oracle.py`:

```python
def oracle_linear_search(v, key):
    try:
        return v.index(key)
    except ValueError:
        return -1
```

Am folosit acest oracol ca să nu compar funcția cu ea însăși. Ideea este ca testele random să verifice rezultatul printr-o metodă separată.

## Rezultatele testelor

Comanda rulată local:

```bash
python -m pytest
```

Rezultatul obținut:

```text
collected 20 items

tests\test_black_box.py ..........                              [ 50%]
tests\test_random.py ..                                         [ 60%]
tests\test_white_box.py ........                                [100%]

20 passed in 0.06s
```

Toate cele 20 de teste au trecut.

## Rezultatele coverage

Comanda rulată:

```bash
python -m coverage report -m
```

Rezultatul obținut:

```text
Name                      Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------
oracle.py                     5      0      0      0   100%
src\__init__.py               0      0      0      0   100%
src\linear_search.py         14      0     14      0   100%
tests\__init__.py             0      0      0      0   100%
tests\test_black_box.py      27      0      0      0   100%
tests\test_random.py         19      0      4      0   100%
tests\test_white_box.py      26      0      0      0   100%
---------------------------------------------------------------------
TOTAL                        91      0     18      0   100%
```

Rezultatul arată că testele acoperă toate instrucțiunile și ramurile detectate de `coverage.py`. Pentru funcția `linear_search.py`, coverage-ul este 100%.

Consider totuși că un coverage de 100% nu înseamnă automat că programul este perfect. Coverage-ul arată că liniile au fost executate, dar nu garantează singur că toate comportamentele posibile au fost verificate. Din acest motiv am inclus și testare aleatoare și am pregătit proiectul pentru mutation testing.

## Mutation testing

Pentru mutation testing am inclus `mutmut` în dependențele proiectului. Scopul mutation testing este să verifice dacă testele pot detecta modificări mici în cod.

Comenzile folosite pentru rulare sunt:

```bash
mutmut run
mutmut results
```

În această etapă, ideea principală este următoarea: dacă o modificare mică în cod nu este detectată de teste, atunci suita de teste mai poate fi îmbunătățită. Dacă testele pică după modificarea generată, mutantul este considerat omorât.

Mutation testing este util mai ales pentru că merge mai departe decât coverage-ul. Două suite de teste pot avea același coverage, dar una poate fi mai bună decât cealaltă dacă detectează mai mulți mutanți.

## Comparație între testele manuale și testele random

| Criteriu                 | Teste manuale                  | Teste random                         |
| ------------------------ | ------------------------------ | ------------------------------------ |
| Număr de teste           | 18 teste manuale               | 2 teste care generează 600 de cazuri |
| Control asupra cazurilor | Mare                           | Mai mic                              |
| Cazuri de frontieră      | Alese intenționat              | Nu sunt garantate mereu              |
| Efort de scriere         | Mai mare                       | Mai mic după ce generatorul există   |
| Oracol                   | Valori așteptate scrise manual | Oracol independent                   |
| Rol principal            | Verifică situații clare        | Explorează mai multe combinații      |

Testele manuale mi s-au părut mai bune pentru cazurile clare, cum ar fi lungimea invalidă sau elementul de pe prima/ultima poziție. Testele random sunt utile deoarece pot încerca multe combinații într-un timp scurt, dar fără un oracol independent nu ar fi foarte valoroase.

## Puncte critice

Am notat câteva puncte critice în fișierul `critical_points.json`. Le-am considerat importante deoarece sunt zone unde o greșeală ar schimba comportamentul funcției:

* validarea tipului pentru `v`;
* validarea lungimii listei;
* validarea tipului pentru `key`;
* returnarea primei apariții;
* returnarea valorii `-1` când elementul lipsește.

Un caz important este cel în care `key` apare de mai multe ori. Funcția nu trebuie să returneze orice poziție, ci prima apariție.

## GitHub Actions

Am configurat un workflow în:

```text
.github/workflows/ci.yml
```

Workflow-ul rulează automat la fiecare push pe branch-ul `main`.

În pipeline se execută:

* instalarea Python;
* instalarea dependențelor;
* rularea testelor cu `pytest`;
* rularea coverage;
* generarea raportului HTML de coverage;
* încărcarea raportului ca artifact.

După o primă încercare eșuată, am corectat fișierul `ci.yml`, iar ultimele rulări din GitHub Actions au trecut cu succes. Badge-ul de la începutul README-ului arată statusul curent al pipeline-ului.

## Utilizarea unui tool de IA

În realizarea proiectului am folosit ChatGPT ca instrument de sprijin. L-am folosit pentru explicații și organizare, nu pentru a copia un proiect existent.

L-am folosit în special pentru:

* clarificarea structurii proiectului;
* explicarea comenzilor Git;
* înțelegerea erorilor din terminal;
* organizarea testelor pe categorii;
* formularea unei prime variante de documentație;
* corectarea workflow-ului GitHub Actions.

Exemple de prompturi folosite:

```text
Vreau să fac tema T1 la Testarea Sistemelor Software în Python. Cum ar trebui să structurez proiectul?
```

```text
Am o funcție linear_search(v, key). Ce teste black-box, white-box și random pot scrie pentru ea?
```

```text
Cum urc un proiect din Visual Studio Code pe GitHub pas cu pas?
```

```text
GitHub Actions workflow run failed. Cum verific problema?
```

Răspunsurile primite au fost adaptate la proiectul meu. Am rulat local testele, am verificat rezultatele și am modificat fișierele în funcție de erorile apărute. De exemplu, workflow-ul GitHub Actions nu a mers din prima, iar apoi l-am simplificat ca să ruleze corect testele și coverage-ul.

Consider că AI-ul a fost folosit ca ajutor tehnic, dar rezultatul final a fost verificat prin rulări locale și prin pipeline-ul de pe GitHub.

## Concluzii

Prin acest proiect am aplicat mai multe metode de testare pe o funcție simplă, dar care are suficiente cazuri relevante. Testele black-box au fost utile pentru a verifica funcția din perspectiva specificației. Testele white-box au fost utile pentru a verifica ramurile codului. Testele random au adăugat mai multe combinații de intrări și au folosit un oracol independent.

Rezultatul final a fost:

* 20 de teste trecute;
* 100% statement coverage;
* 100% branch coverage;
* pipeline GitHub Actions funcțional.

Cel mai important lucru observat este că o suită de teste nu trebuie evaluată doar după numărul de teste. Contează și ce situații sunt acoperite, dacă există cazuri de frontieră și dacă rezultatul este verificat corect.

## Referințe

[1] Pytest Documentation, https://docs.pytest.org/, Data ultimei accesări: 12 iunie 2026.
[2] Coverage.py Documentation, https://coverage.readthedocs.io/, Data ultimei accesări: 12 iunie 2026.
[3] GitHub Actions Documentation, https://docs.github.com/en/actions, Data ultimei accesări: 12 iunie 2026.
[4] Mutmut Documentation, https://mutmut.readthedocs.io/, Data ultimei accesări: 12 iunie 2026.
[5] OpenAI, ChatGPT, https://chatgpt.com/, Data generării: 12 iunie 2026.
