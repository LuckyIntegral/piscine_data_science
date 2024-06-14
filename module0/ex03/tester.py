''' tester for the function NULL_not_found '''
from NULL_not_found import NULL_not_found
import math

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

# NULL_not_found(' ')
# NULL_not_found(True)
# NULL_not_found(42)
# NULL_not_found('dfd')
# NULL_not_found(math.pi)
# NULL_not_found(math.nan)
# NULL_not_found(math.inf)
