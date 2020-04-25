import arrow

now = arrow.now('Asia/Istanbul')
print(now.utcoffset())

