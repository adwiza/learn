import os
from datetime import datetime, timedelta, timezone


def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds


s = uptime()
hours, seconds = divmod(float(s), 3600)

timezone_offset = +3.0  # Europe/Moscow (UTC+03:00)
tzinfo = timezone(timedelta(hours=timezone_offset))

# print(f'{hours:.0f} ч. {seconds:.3f} сек.')
f = open('uptime.html', 'w')
statResult = os.stat('uptime.html')
# epoch = datetime(1970, 1, 1, tzinfo=tzinfo)
epoch = datetime(1970, 1, 1, tzinfo=tzinfo)
modified = epoch + timedelta(seconds=statResult.st_mtime)

message = """<html>
<head>
    <meta charset="utf-8">
    <title>Статус системы</title>
</head>
<body>
<p>Сервер работает уже {hours} ч. {seconds} мин.</p>
<p>Последнее обновление {modified}</p>
</body>
</html>""".format(hours=hours, seconds=int(seconds // 60), modified=modified)
f.write(message)
f.close()
