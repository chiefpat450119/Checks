from datetime import datetime, timezone, timedelta
import math
local_timezone = timezone(timedelta(hours=8))
est = timezone(timedelta(hours=-5))
release = datetime(2022, 2, 18, 0, 0, 0, 0, tzinfo=est)
now = datetime.now(tz=local_timezone)
difference = release - now
days = difference.days
hours =  math.floor(difference.seconds/3600)
minutes = math.floor((difference.seconds%3600)/60)
seconds = difference.seconds%60
print(f"The release is in {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
bruh = input('Press ENTER to continue')