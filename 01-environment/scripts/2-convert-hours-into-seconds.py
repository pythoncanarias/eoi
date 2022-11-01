seconds = 12345

seconds = seconds % (24 * 3600)
hour = seconds // 3600

seconds %= 3600
minutes = seconds // 60

seconds %= 60

result = f"{hour}:{minutes}:{seconds}"

print(result)
