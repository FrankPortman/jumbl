import datetime
from pytz import timezone
import random
import time
import tzlocal

normalizer = 2
num_commits = 12
garbled = []
normalized_samples = num_commits / normalizer

start_date = datetime.datetime(2017, 4, 1, 9)
end_date = datetime.datetime(2017, 4, 1, 17)
time_range = end_date - start_date

# Get semi-garbled garbled points
# Tune normalizer to make more or less random/clumpy
# High values are more evenly spread out
# Low values are more truly random but can clump for low input
for i in range(normalized_samples):
    low_range = float(i) / normalized_samples
    high_range = (float(i) + 1) / normalized_samples
    for j in range(normalizer):
        garbled.append(random.uniform(low_range, high_range))

garbled = sorted(garbled)

# Get new times
deltas = [datetime.timedelta(seconds=x * time_range.total_seconds()) for x in garbled]
new_times = [(start_date + x).replace(microsecond=0) for x in deltas]

tz = tzlocal.get_localzone()
new_times = [tz.localize(x) for x in new_times]


## to do
# get all commits authored by you in a range
# pretty print the proposed times and diffs (along with message)
# user says yes or regenerate
# change commit and author date in a loop if user says yes
# ???
#profit
