''' Write time formatter '''
import time

unix_time = time.time()

print(f"Seconds since January 1, 1970: {unix_time:,} or {unix_time:e} in scientific notation")
print(time.strftime('%b %d %Y'))
