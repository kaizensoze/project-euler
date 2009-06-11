'''
Created on Apr 5, 2009

@author: anon
'''

dow = [1, 2, 3, 4, 5, 6, 7]

months = { 
            'jan' : 1,
            'feb' : 2,
            'mar' : 3,
            'apr' : 4,
            'may' : 5,
            'jun' : 6,
            'jul' : 7,
            'aug' : 8,
            'sep' : 9,
            'oct' : 10,
            'nov' : 11,
            'dec' : 12
         }

daysInMonth = {
                 1 : 31,
                 2 : 28,
                 3 : 31,
                 4 : 30,
                 5 : 31,
                 6 : 30,
                 7 : 31,
                 8 : 31,
                 9 : 30,
                 10 : 31,
                 11 : 30,
                 12 : 31
              }            

firstDayOfMonthSundayCount = 0

#set the starting data
#incrementally add 7
#check the year for leap year
#when at feb, determine feb numDays based on currYear

isLeapYear = False

year = 1901
month = 1
day = 1
dowIndex = 3 -1

if year % 100 == 0:
    if year % 400 == 0:
        isLeapYear = True
elif year % 4 == 0:
    isLeapYear = True
    
if isLeapYear:
    daysInMonth[2] = 29 

while year <= 2000:
    day = day + 7    
    
    if day > daysInMonth[month]:
        day = day % daysInMonth[month]
        month = month + 1
        if month > 12:
            month = month % 12
            year = year + 1
        firstDay = dow[dowIndex - day + 1]
        if firstDay == 1:
            firstDayOfMonthSundayCount = firstDayOfMonthSundayCount + 1

print(firstDayOfMonthSundayCount)