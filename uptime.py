s = "4396.08"
# s = "10250.207"
hours, seconds = divmod(float(s), 3600)


# print(f'{hours:.0f} ч. {seconds:.3f} сек.')
f = open('uptime.html', 'w')

message = """<html>
<head>
    <meta charset="utf-8">
    <title>Статус системы</title>
</head>
<body><p>Сервер работает уже {hours} ч. {seconds} мин.</p></body>
</html>""".format(hours=hours, seconds=seconds)
f.write(message)
f.close()
