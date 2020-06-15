import datetime

NORMALIZE = 1000000.0

def convert_time(unix_time):
    return datetime.datetime.fromtimestamp(unix_time/NORMALIZE)
