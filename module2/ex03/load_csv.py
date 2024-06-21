''' module2/ex00 '''
import pandas as pd


def load(path: str) -> pd.DataFrame:
    ''' load '''
    if path is None or path.endswith('.csv') is False:
        return None
    try:
        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape}')
        return df
    except Exception:
        pass
    return None
