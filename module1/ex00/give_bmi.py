''' module1/ex00 '''


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    ''' returns list of bmi from list of heights and weights
    BMI = weight / height ^ 2
    '''
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ''' returns list of filtered bmis '''
    return list(map(lambda x: x > limit, bmi))
