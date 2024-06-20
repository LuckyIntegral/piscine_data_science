''' module2/ex01/aff_life.py '''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from load_csv import load


def aff_life(df: pd.DataFrame, country: str) -> None:
    ''' aff_life '''

    data = df.loc[df['country'] == country]

    try:
        matplotlib.use('Qt5Agg')
        plt.title(f'{country} Life expantancy Projection')
        plt.plot(
            list(map(int, data.columns[1:])),
            data[data.columns[1:]].values[0]
            )

        plt.gca().get_yaxis().set_major_locator(plt.MaxNLocator(8))
        plt.gca().get_xaxis().set_major_locator(plt.MaxNLocator(9))

        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.show()
    except Exception as e:
        print(f'Error: {e}')


def main():
    ''' entry point for the module '''
    df = load('life_expectancy_years.csv')
    if df is not None:
        aff_life(df, 'Austria')
    else:
        print('Failed to load dataset')


if __name__ == '__main__':
    main()
