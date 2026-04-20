days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
sorted_days = sorted(days.keys()) # items()는 키와 값을 튜플로 반환, keys()는 키만 반환, values()는 값만 반환
print(sorted_days)

sorted_days = sorted(days.items(), key=lambda x: x[1]) # key는 정렬 기준이 되는 요소를 지정하는 매개변수, lambda는 익명 함수를 정의하는 키워드, x는 items()로 반환된 튜플의 각 요소를 나타냄, x[1]은 튜플의 두 번째 요소인 값(일 수)을 기준으로 정렬
print(sorted_days)

answer = input()
for month in days.keys():
    if answer in month:
        print(days[month])
        break