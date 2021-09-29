import datetime
now = input("Today: ")
todayName = now.split(" - ")[0]
today = now.split(" - ")[1]
numNextDay = int(input("n = "))

symbol = {
    "S" : "sunny",
    "C" : "cloudy",
    "D" : "drizzle",
    "F" : "fog",
    "R" : "rain"
}

def nextDay(dayName):
    day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    index = day.index(dayName)
    if index == len(day) - 1:
        index = -1
    return day[index + 1]

file = open("dubaothoitiet.txt", "r")
lines = file.readlines()
for i in range(len(lines)):
    date = lines[i].split(":")[0]
    if today == date:
        print("weather forecast for 4 days: ")
        for j in range(1, numNextDay + 1):
            dayName = nextDay(todayName)
            todayName = dayName
            try:
                date = lines[i + j].split(':')[0]
                status = lines[i + j].split(':')[1].replace("\n", "")
                print(f"{dayName} - {date}: {symbol[status]}")
            except:
                year = int(date.split("/")[2])
                month = int(date.split("/")[1])
                day = int(date.split("/")[0])
                nextDate = datetime.datetime(year, month, day) + datetime.timedelta(days=1)
                date = f"{nextDate.strftime('%d')}/{nextDate.strftime('%m')}/{nextDate.strftime('%Y')}"
                print(f"{dayName} - {date}: chua co thong tin")
    else:
        print("chua co thong tin")
        break
file.close()