
def ft_tqdm(lst: range) -> None:
    ''' This function is a mock of tqdm.
    It takes a range object and iterates over it, printing the progress bar.
    '''
    TOTAL = len(lst)
    ALINMENT = len(str(TOTAL)) + 1
    for i in lst:
        RATE = (i + 1) * 100 // TOTAL
        PROGGRES_BAR = "█" * RATE + " " * (100 - RATE)
        print(f'{RATE:3}%|{PROGGRES_BAR}|{i + 1:{ALINMENT}}/{TOTAL}', end='\r')
        yield i
