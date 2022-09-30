import timeit

import pandas as pd


def generator(n: int):
    df = pd.read_csv('test_dataset.csv')
    df['age'] = df['age'].astype('int')
    df['country_code'] = df['country_code'].fillna('NN')
    return df[:n].to_dict(orient='records')


def pandas_num_time(n: int):
    SETUP = f"""
from __main__ import generator
import pandas as pd

g = generator({n})
df = pd.DataFrame(g)
    """

    TEST = """
df['age'].apply(lambda x: x * 10)
    """

    t = timeit.repeat(setup=SETUP, stmt=TEST, repeat=3, number=100)
    avg_t = sum(t) / len(t)

    return avg_t


def pandas_str_time(n: int):
    SETUP = f"""
from __main__ import generator
import pandas as pd
    
g = generator({n})
df = pd.DataFrame(g)
    """

    TEST = """
df["country_code"].apply(lambda x: x.lower())
    """

    t = timeit.repeat(setup=SETUP, stmt=TEST, repeat=3, number=100)
    avg_t = sum(t) / len(t)

    return avg_t


def builtin_num_time(n: int):
    SETUP = f"""
from __main__ import generator
import pandas as pd

g = generator({n})
"""

    TEST = """
list(map(lambda x: x["age"] * 10, g))
    """

    t = timeit.repeat(setup=SETUP, stmt=TEST, repeat=3, number=100)

    return min(t)


def builtin_str_time(n: int):
    SETUP = f"""
from __main__ import generator
import pandas as pd
    
g = generator({n})
"""

    TEST = """
list(map(lambda x: x["country_code"].lower(), g))
    """

    t = timeit.repeat(setup=SETUP, stmt=TEST, repeat=3, number=100)

    return min(t)


if __name__ == '__main__':
    test_range = [100, 1000, 10000, 50000, 100000, 200000, 300000, 400000, 500000]
    save = True

    result = []
    for n in test_range:
        str_p_t = pandas_str_time(n)
        num_p_t = pandas_num_time(n)
        str_b_t = builtin_str_time(n)
        num_b_t = builtin_num_time(n)

        result.append({
            'pandas_str': str_p_t,
            'builtin_str': str_b_t,
            'pandas_num': num_p_t,
            'builtin_num': num_b_t,
            'count': n
        })
        print(f'count: {n}\n'
              f'p_str: {str_p_t} p_num: {num_p_t}\n'
              f'b_str: {str_b_t} b_num: {num_b_t}\n')
        print('==========================================\n')

    if save:
        result_df = pd.DataFrame(result)
        result_df.to_csv('apply_result.csv', index=False)
