from config import *

class nikeRobot():

    def __init__(self,id,pwd,shoes_size,url,start_time,ip_proxy):

        self.id=id
        self.pwd=pwd
        self.shoes_size=shoes_size
        self.url=url
        self.start_time=start_time
        self.ip_proxy=ip_proxy

        self.chrome_options = webdriver.chrome.options.Options()
        self.chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        if len(self.ip_proxy) == 3:
            self.chrome_options.add_argument("--proxy-server={}://{}:{}".format(ip_proxy[0],ip_proxy[1],ip_proxy[2])) #添加代理
        self.chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])  # 防止被检测为机器操作 window.navigator.webdriver返回undefined
        self.chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        self.chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        self.chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # self.chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        # self.chrome_options.add_argument(f'user-agent={user_agent}')
        # driver_path="/Users/quweihao/Downloads/chromedriver" #手动指定使用的浏览器位置
        # self.driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_options)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.start=None

    def login(self):

        self.start=time()

        # 等待界面出现
        self.driver.get("https://www.nike.com/kr/ko_kr/")
        self.driver.implicitly_wait(10)
        time1 = time()
        print("打开主页共耗时{:.3f}".format(time1 - self.start))
        WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_link_text(u"로그인"))
        # 等待로그인按键
        self.driver.find_element_by_link_text(u"로그인").click()
        # 点击로그인
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='kakao-sync-modal-login']/div/div/div")))
        # 等待出现js登陆框
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='카카오계정으로 로그인'])[1]/following::span[1]").click()
        # 点击登陆

        self.driver.find_element_by_id("j_username").click()
        self.driver.find_element_by_id("j_username").clear()
        self.driver.find_element_by_id("j_username").send_keys(self.id)
        self.driver.find_element_by_id("j_password").click()
        self.driver.find_element_by_id("j_password").clear()
        self.driver.find_element_by_id("j_password").send_keys(self.pwd)
        # 输入账号和密码
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='로그인 유지하기'])[1]/following::button[1]"))
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='로그인 유지하기'])[1]/following::button[1]").click()
        time2 = time()
        print("成功登陆,登陆共耗时{:.3f}".format(time2 - time1))
        time3 = time()

    def robot_start(self, kakao_phone, kakao_birth):

        while 1:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            if now > self.start_time:
                print("到了{}".format(now))
                newwindow = 'window.open("{}")'.format(self.url)
                self.driver.execute_script(newwindow)
                # 移动句柄，对新打开页面进行操作
                self.driver.switch_to.window(self.driver.window_handles[1])
                # 到新界面
                print("已经到鞋子页面")
                self.driver.switch_to.window(self.driver.window_handles[0])
                # 移动句柄到主页
                self.driver.close()
                # 关闭主页以节省带宽
                self.driver.switch_to.window(self.driver.window_handles[0])
                # 重新回到鞋子界面

        # 等待界面出现
                self.driver.find_element_by_link_text(u"사이즈 선택").click()
                sleep(0.1)
                # self.driver.find_element_by_xpath(u"//*[@id='selectSize']/option[8]").click()
                # self.driver.find_element_by_xpath(
                #     u"(.//*[normalize-space(text()) and normalize-space(.)='사이즈 선택'])[2]/following::span[10]").click()
                # self.driver.find_element_by_xpath(
                #     u"(.//*[normalize-space(text()) and normalize-space(.)='사이즈 선택'])[2]/following::span[1]").click()
                self.driver.find_element_by_xpath("//ul[@class='select-body']//a[@data-value='42']/span").click()
                self.driver.find_element_by_xpath("//*[@class='btn-link width-max xlarge btn-login']").click()
                time3 = time()
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='btn-link xlarge btn-order width-max']")))
                # sleep(0.1)
                self.driver.find_element_by_xpath("//span[@typename='{}']".format(self.shoes_size)).click()
                # # 点击鞋子型号
                self.driver.find_element_by_xpath("//a[@class='btn-link xlarge btn-order width-max']").click()
                # 点击바로구매按键
                ##############################################################################################################################
                self.driver.find_element_by_xpath("//*[@for='Reason_1']").click()
                # 选择一般配送
                self.driver.find_element_by_id("btn-next").click()
                # 点击다음 단계 진행
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//button[@class='button xlarge width-max']")))
                self.driver.find_element_by_xpath("//*[@class='label font-size-s']").click()
                # 点击위 주문의 상품, 가격, 할인, 배송정보에 동의합니다
                self.driver.find_element_by_xpath("//*[@class='button xlarge width-max']").click()
                # 点击 결제하기

                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='imp-dialog customizable payment-kakaopay pc']")))
                iframe = self.driver.find_elements_by_tag_name('iframe')
                self.driver.switch_to.frame(iframe[len(iframe)-2])

                WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='list_gnb']")))
                li=self.driver.find_elements_by_xpath("//ul[@class='list_gnb']")[0]
                li.click()
                self.driver.find_element_by_id("userPhone").click()
                self.driver.find_element_by_id("userPhone").clear()
                self.driver.find_element_by_id("userPhone").send_keys("01029972828")
                self.driver.find_element_by_id("userBirth").click()
                self.driver.find_element_by_id("userBirth").clear()
                self.driver.find_element_by_id("userBirth").send_keys("970105")
                self.driver.find_element_by_id("userPost").submit()

                # except TimeoutException:
                #     print("没有找到元素")

                print("到付款共耗时{:.3f}".format(time()-time3))
                print("总过程耗时{:.3f}".format(time()-self.start))
                sleep(3)
                # l[1].click()
                # sleep(50)

                # print(driver.window_handles)
                # print(li)
        # driver.switch_to.frame(driver.find_elements_by_xpath("//*[@class='imp-dialog customizable payment-kakaopay pc']/iframe[2]"))
        # sleep(3)
        # driver.find_elements_by_xpath("//*[@class='list_gnb']").click()
        # print(dr)




def main():

    user_name="qwhsdwd@gmail.com"
    user_passwd="qwh961126!"
    url="https://www.nike.com/kr/launch/t/men/fw/nike-sportswear/CK2630-200/rxsg96/air-force-1-gtx"
    shoes_size="260"
    start_time="2019-10-26 21:54:00"
    kakao_phone="01029972828"
    kakao_birth="970105"
    ip_proxy=[]
    # 单线程
    nike_robot1=nikeRobot(user_name,user_passwd,shoes_size,url,start_time,ip_proxy)
    nike_robot1.login()
    nike_robot1.robot_start(kakao_phone,kakao_birth)
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


if __name__ == '__main__':

    main()

