import requests
from bs4 import BeautifulSoup
import math
from datetime import datetime

def getPageContent():
    try:
        webpage = requests.get("https://campusloop.cmdo.um.edu.mo/zh_TW/busstopinfo")
        
        # proceed if we established the connect successfully
        if webpage.status_code == 200:
            return BeautifulSoup(webpage.content, "html.parser") # print(soup.prettify())
        else: raise Exception("Not able to connect to the Website!")

    except:
        raise Exception("Not able to connect to the Website! Make sure you have connected to the internet or entered the correct URL!")
        

def getBusList(_soup):
    stop_list = []

    soup = _soup

    stops_tree = soup.find(class_="col-xs-12 tree")
    main_stops = stops_tree.findChildren(class_="main")
    # main_stops = stops_tree.findAll(class_="main", recursive=False)

    for stop in main_stops:
        # bus_existed = stop.find(class_="left out-left").string
        bus_existed = stop.find(class_="left")
        if len(bus_existed.contents) > 2:
            stop_list.append("MP5602")
            # stop_list.append(bus_existed.find('span').contents[0])
            # print(bus_existed.find('span').contents[0])
        else:
            stop_list.append(None)
            # stop_list.append(bus_existed.string)

    return stop_list

def getBusPos(list):
    stops = ["PGH 研究生宿舍巴士站", "E4 劉少榮樓", "N2 大學會堂", "N6 行政樓", "E11 科技學院", "E21 人文社科樓", "E32 法學院", "S4 研究生宿舍南四座(近連廊)"]
    for index, bus in enumerate(list):
        if bus is not None:
            # print(index + 1, bus)
            real_index = (index + 1) / 2 # index is start from 0, I want it to start with 1
            if isinstance(real_index, int): # On the Stop
                status = "已到達"
            elif isinstance(real_index, float): # Between Stops
                status = "正在前往"

            return f"\n{status}【{stops[math.ceil(real_index)]}】" # break the loop

def getNextShift(_soup):
    soup = _soup
    next_shift = soup.find(class_="col-xs-12 title text-center").find('span').string
    return next_shift[4:]

def getBusStatus(_soup):
    soup = _soup
    bus_status = soup.find(class_="col-xs-12 title service text-center").find('span').string
    return bus_status[5:]

def getLastUpdate(_soup):
    soup = _soup
    last_update = soup.find(class_="col-xs-12 title last-update text-center").find('span').string
    return last_update[7:]

def getCurrentTime():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return current_time

webpage = getPageContent()

stop_list = getBusList(webpage)
next_shift = getNextShift(webpage)
bus_status = getBusStatus(webpage)
last_update = getLastUpdate(webpage)

current_time = getCurrentTime()

print("\n\n====================================")
print("下一班車的時間:", next_shift)
print("巴士服務狀態:", bus_status)
print("最後更新時間:", last_update)

print("現在時間:", current_time)

bus_position = getBusPos(stop_list)
print(bus_position)
print("====================================\n")

# print(stop_list)

# testing_list = [None, 'MP5602', None, None, None, None, None, None, None, None, None, None, None, None, None, None]
# print(getBusPos(testing_list))