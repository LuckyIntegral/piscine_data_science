''' module2/ex01/aff_life.py '''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from load_csv import load


def formatter(x, pos):
    ''' formatter for gdp axis '''
    if x < 1000:
        return str(int(x))
    elif x < 1000000:
        return f"{x / 1000:.0f}K"
    else:
        return f"{x / 1000000:.0f}M"


def projection_life(df_ipp: pd.DataFrame, df_ley: pd.DataFrame) -> None:
    ''' projection_life
    Args:
        df_ipp (pd.DataFrame): income per person dataset
        df_ley (pd.DataFrame): life expectancy dataset
    Description:
        Plots the life expectancy against the income per person
    '''

    df_ipp = df_ipp[['country', '1900']]
    df_ley = df_ley[['country', '1900']]
    df_joined = pd.merge(df_ipp, df_ley, on='country', how='inner')

    matplotlib.use('Qt5Agg')
    plt.title('1900')

    plt.plot(
        df_joined['1900_x'],
        df_joined['1900_y'],
        marker='o',
        linestyle='None'
        )

    plt.gca().set_xscale('log')
    plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(formatter))
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.show()


def main():
    ''' entry point for the module '''
    df_ipp = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_ley = load('life_expectancy_years.csv')
    if df_ipp is not None and df_ley is not None:
        try:
            projection_life(df_ipp, df_ley)
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('Failed to load dataset')


if __name__ == '__main__':
    main()
