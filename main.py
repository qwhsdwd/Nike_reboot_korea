from config import *
from nikeRobot import nikeRobot


if __name__ == '__main__':

    user_name = "qwhsdwd@gmail.com"
    user_passwd = "qwh961126!"
    url = "https://www.nike.com/kr/ko_kr/t/adult-unisex/fw/action-outdoor/BQ6817-006/oaic91/nike-sb-dunk-low-pro"
    url = "https://www.nike.com/kr/ko_kr/t/men/fw/running/BQ1671-002/ifaa28/nike-odyssey-react-2-shield"
    shoes_size = "250"
    start_time = "2019-10-31 10:00:00"
    kakao_phone = "01029972828"
    kakao_birth = "970105"
    ip_proxy = []

    # user_name=input("NIKE账号: ")
    # user_passwd=input("NIKE密码: ")
    # url=input("鞋子网址: ")
    # shoes_size=input("鞋子码数: ")
    # start_time=input("开始时间(格式:2020-01-01 00:00:00)")
    # kakao_phone=input("kakao电话(格式01012345678): ")
    # kakao_birth=input("kakao生日(格式960101): ")


    # 单线程
    nike_robot1 = nikeRobot(user_name, user_passwd, shoes_size, start_time, ip_proxy)
    # nike_robot2=nikeRobot("1209663518@qq.com","wudi1996!",shoes_size,start_time,ip_proxy)
    nike_robot1.login()
    nike_robot1.robot_start(url, kakao_phone, kakao_birth)

    # t1=threading.Thread(target=nike_robot1.robot_start,args=(url,kakao_phone,kakao_birth))
    # t2=threading.Thread(target=nike_robot2.robot_start,args=(url,kakao_phone,kakao_birth))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    ###################################################################################################
    # 多线程
    # T=list()
    # start=time()
    # db=database.query()
    # if isinstance(db,tuple):
    #     print("获取数据库中 {} 条信息,共耗时{:.3}".format(len(db),(time()-start)))
    #
    #     # for i in range(len(db)):
    #     #     print(db[i])
    #     for i in range(len(db)):
    #         t = threading.Thread(target=login_and_robot, args=(db[i][1], db[i][2],url))
    #         t.start()
    #         T.append(t)
    #     for i in range(len(T)):
    #         T[i].join()
    # else:
    #     print("数据库连接失败,错误原因是{}".format(db))
    ####################################################################################################
