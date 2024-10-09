import datetime

x = datetime.datetime.today()
epoch = datetime.datetime(1970, 1, 1)

print((x-epoch).total_seconds())