import datetime
now = input("Today: ")
today_name = now.split(" - ")[0]
today = now.split(" - ")[1]
num_next_day = int(input("n = "))

symbol = {
    "S" : "sunny",
    "C" : "cloudy",
    "D" : "drizzle",
    "F" : "fog",
    "R" : "rain"
}


def next_day(day_name):
    day = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    index = day.index(day_name)
    if index == len(day) - 1:
        index = -1
    return day[index + 1]


file = open("dubaothoitiet.txt", "r")
lines = file.readlines()
check = False
for i in range(len(lines)):
    date = lines[i].split(":")[0]
    if today == date:
        check = True
        print(f"weather forecast for {num_next_day} days: ")
        for j in range(1, num_next_day + 1):
            day_name = next_day(today_name)
            today_name = day_name
            try:
                date = lines[i + j].split(':')[0]
                status = lines[i + j].split(':')[1].replace("\n", "")
                print(f"{day_name} - {date}: {symbol[status]}")
            except:
                year = int(date.split("/")[2])
                month = int(date.split("/")[1])
                day = int(date.split("/")[0])
                next_date = datetime.datetime(year, month, day) + datetime.timedelta(days=1)
                date = f"{next_date.strftime('%d')}/{next_date.strftime('%m')}/{next_date.strftime('%Y')}"
                print(f"{day_name} - {date}: chua co thong tin")
if check == False:
    print("chua co thong tin")
file.close()
