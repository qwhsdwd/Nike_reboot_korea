import time
import requests
from datetime import datetime


def get_webservertime(host):
    start=time.time()
    headers = {"user-agent": "Mizilla/5.0"}
    response = requests.get(host, headers=headers)
    print("程序共耗时 {}".format(time.time()-start))
    ts=response.headers['Date']
    # # 将GMT时间转换成北京时间
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # print(ltime)
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    # print(ttime)
    dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "%02u:%02u:%02u" % (ttime.tm_hour+1, ttime.tm_min, ttime.tm_sec)# 首尔时间
    server_time=dat+" "+tm
    # print("访问服务器返回的时间:\t{} {}".format(dat, tm))
    print("访问服务器返回的时间:\t{}".format(server_time))
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("本地时间:\t\t%s"%now)
    server_time_datetime=datetime.strptime(server_time, '%Y-%m-%d %H:%M:%S')
    now_datetime=datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
    print(server_time_datetime-now_datetime)

if __name__ == '__main__':

    host = "https://www.nike.com/kr/ko_kr"
    get_webservertime(host)
