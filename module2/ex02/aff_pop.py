''' module2/ex01/aff_life.py '''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from load_csv import load


def convertor(nbr: str) -> int:
    ''' convertor '''
    if nbr.endswith('K'):
        return int(float(nbr[:-1]) * 1000)
    elif nbr.endswith('M'):
        return int(float(nbr[:-1]) * 1000000)
    try:
        return int(nbr)
    except ValueError:
        return nbr


def format_year_axis(x, pos):
    ''' formats the year axis '''
    if x < 1000:
        return str(int(x))
    elif x < 1000000:
        return f"{x / 1000:.0f}K"
    else:
        return f"{x / 1000000:.0f}M"


def aff_pop(df: pd.DataFrame, country1: str, country2: str) -> None:
    ''' aff_pop '''

    data = df.loc[(df['country'] == country1) | (df['country'] == country2)]

    data = data[data.columns[:252]].copy()

    for col in data[1:]:
        data[col] = data[col].apply(convertor)

    matplotlib.use('Qt5Agg')
    plt.title('Population Projection')

    plt.plot(
        list(map(int, data.columns[1:])),
        data[data.columns[1:]].values[0],
        color='g',
        label=country2
        )
    plt.plot(
        list(map(int, data.columns[1:])),
        data[data.columns[1:]].values[1],
        color='b',
        label=country1
        )

    plt.gca().get_yaxis().set_major_formatter(
        plt.FuncFormatter(format_year_axis)
        )
    plt.gca().get_xaxis().set_major_locator(plt.MaxNLocator(8))

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()


def main():
    ''' entry point for the module '''
    df = load('population_total.csv')
    if df is not None:
        try:
            aff_pop(df, 'Belgium', 'Austria')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('Failed to load dataset')


if __name__ == '__main__':
    main()
