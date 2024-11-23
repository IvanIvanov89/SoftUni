from math import floor
BookPages = int(input())
PagesPerHour = int(input())
DaysPerBook = int(input())

#TimePerBook = BookPages // PagesPerHour
TimePerBook2 = floor(BookPages / PagesPerHour)
#print(TimePerBook2)

#HoursPerDay = TimePerBook // DaysPerBook
HoursPerDay2 = floor(TimePerBook2 / DaysPerBook)
#print(TimePerBook)

print(HoursPerDay2)
