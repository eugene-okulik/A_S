import datetime

heta_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(heta_date, '%b %d, %Y - %X')

month_name = python_date.strftime("%B")

print(month_name)

adjusted_date = datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M')

print(adjusted_date)
