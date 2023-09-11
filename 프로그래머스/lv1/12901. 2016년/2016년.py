import datetime

def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']

    date_2016 = datetime.date(2016, a, b).weekday()
    answer = days[date_2016]

    return answer
