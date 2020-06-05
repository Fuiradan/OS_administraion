import sentry_sdk
import math
sentry_sdk.init("https://6108b3617c624ea391c9f3a13401fd18@o400108.ingest.sentry.io/5258203")


a = -1

try:
    result = math.sqrt(a)
    print(result)
except Exception:
    sentry_sdk.capture_message('Ошибка №54565616. Входная переменная отрицательная')


#ошибка деления на ноль
division_by_zero = 1 / 0

with sentry_sdk.configure_scope() as scope:
    scope.set_tag('sentry_tag')
    scope.set_tag('Lab_6')

mas = [1,1,1,1,1,1,1]
sum = 0
for i in range(mas):
   sum += 1 