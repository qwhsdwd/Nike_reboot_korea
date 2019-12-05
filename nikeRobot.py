from config import *


class nikeRobot():

    def __init__(self, id, pwd, shoes_size, start_time, ip_proxy):

        self.id = id
        self.pwd = pwd
        self.shoes_size = shoes_size
        self.start_time = start_time
        self.ip_proxy = ip_proxy

        self.chrome_options = webdriver.chrome.options.Options()
        self.chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        if len(self.ip_proxy) == 3:
            self.chrome_options.add_argument(
                "--proxy-server={}://{}:{}".format(ip_proxy[0], ip_proxy[1], ip_proxy[2]))  # 添加代理
        self.chrome_options.add_experimental_option('excludeSwitches', [
            'enable-automation'])  # 防止被检测为机器操作 window.navigator.webdriver返回undefined
        self.chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        self.chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        # self.chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # self.chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # self.chrome_options.add_argument("user-agent=Mozilla/60.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/6037.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/6037.36")
        # user_agent = 'Mozilla/60.0 (X11; Linux x86_64) AppleWebKit/6037.36 (KHTML, like Gecko) Chrome/60.0.3112.600 Safari/6037.36'
        # self.chrome_options.add_argument(f'user-agent={user_agent}')
        # driver_path="./chrome_driver/chromedriver.exe" #手动指定使用的浏览器位置
        # self.driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_options)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.start = None

    def login(self):

        self.start = time()
        # 等待界面出现
        self.driver.get("https://www.nike.com/kr/ko_kr/")
        self.driver.implicitly_wait(10)
        time1 = time()
        logger.debug("打开主页,耗时{:.3f}".format(time1 - self.start))
        WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text(u"로그인"))
        # 等待로그인按键
        self.driver.find_element_by_link_text(u"로그인").click()
        # 点击로그인
        # try:
        #     # WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='kakao-sync-modal-login']/div/div/div")))
        #     # # 等待出现js登陆框
        #     # self.driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='카카오계정으로 로그인'])[1]/following::span[1]").click()
        #     # # 点击登陆
        #     self.driver.find_element_by_id("j_username").click()
        # except TimeoutException or NoSuchElementException:
        #     logger.warning("登陆过程中元素没有找到,正在刷新界面重新登录")
        #     self.driver.refresh()
        #     WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_link_text(u"로그인"))
        #     # 等待로그인按键
        #     self.driver.find_element_by_link_text(u"로그인").click()
        #     # 点击로그인
        #     WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='kakao-sync-modal-login']/div/div/div")))
        #     # 等待出现js登陆框
        #     self.driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='카카오계정으로 로그인'])[1]/following::span[1]").click()
        #     # 点击登陆

        self.driver.find_element_by_id("j_username").click()
        self.driver.find_element_by_id("j_username").clear()
        self.driver.find_element_by_id("j_username").send_keys(self.id)
        self.driver.find_element_by_id("j_password").click()
        self.driver.find_element_by_id("j_password").clear()
        self.driver.find_element_by_id("j_password").send_keys(self.pwd)
        # 输入账号和密码
        WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='로그인 유지하기'])[1]/following::button[1]"))
        sleep(0.5)
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='로그인 유지하기'])[1]/following::button[1]").click()
        sleep(1)
        time2 = time()
        logger.debug("成功登陆,耗时{:.3f}".format(time2 - time1))

    def robot_start(self, url, kakao_phone, kakao_birth):

        try:

            while 1:
                now = datetime.datetime.now().strftime('%m-%d %H:%M:%S.%f')
                if now > self.start_time:

                    time3 = time()
                    logger.debug("到了{}".format(now[:14]))
                    newwindow = 'window.open("{}")'.format(url)
                    self.driver.execute_script(newwindow)
                    # 移动句柄，对新打开页面进行操作
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    # 到新界面
                    logger.debug("到鞋子页面,耗时{:.3f}".format(time() - time3))
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    # 移动句柄到主页
                    self.driver.close()
                    # 关闭主页以节省带宽
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    # 重新回到鞋子界面
                    n = 1
                    while 1:
                        if "COMING SOON" in self.driver.page_source and n < 11:
                            self.driver.refresh()
                            logger.warning("鞋子码数没有出，正在尝试第{}次刷新".format(n))
                            n += 1
                        elif n >= 11:
                            logger.error("已经刷新10次界面，退出程序")
                            exit()
                        else:
                            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
                                (By.XPATH, "//*[@class='btn-link xlarge btn-order width-max']")))
                            # sleep(0.1)
                            # try:
                            # with open("nike.html","w") as f:
                            #     f.write(self.driver.page_source)

                            time4 = time()
                            shoes_size = list()
                            html = etree.HTML(self.driver.page_source)
                            shoesSize = html.xpath(
                                "//div[@class='opt-list']//span[not(@disabled='disabled')][@class='input-radio']//label[@class='']")
                            for shoe in shoesSize:
                                shoes_size.append(shoe.text)
                            logger.debug("现有尺码{}".format(shoes_size))
                            if self.shoes_size not in shoes_size:
                                logger.warning("选择的尺码没货，自动选择现货中最小尺码")
                                self.shoes_size = str(min(shoes_size))

                            self.driver.find_element_by_xpath("//span[@typename='{}']".format(self.shoes_size)).click()
                            # 点击鞋子型号
                            self.driver.find_element_by_xpath(
                                "//a[@class='btn-link xlarge btn-order width-max']").click()
                            # 点击바로구매按键
                            logger.debug("选择{}码成功，到付款界面".format(self.shoes_size))

                            self.driver.find_element_by_xpath("//*[@for='Reason_1']").click()
                            # 选择一般配送
                            self.driver.find_element_by_id("btn-next").click()
                            # 点击다음 단계 진행

                            try:
                                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@class='button xlarge width-max']")))
                                self.driver.find_element_by_xpath("//*[@class='label font-size-s']").click()
                                # 点击위 주문의 상품, 가격, 할인, 배송정보에 동의합니다
                            except NoSuchElementException:
                                logger.warning("在选择配送界面没有找到元素，正在重试")
                                self.driver.find_element_by_xpath("//*[@class='label font-size-s']").click()
                                # 再次尝试
                            self.driver.find_element_by_xpath("//*[@class='button xlarge width-max']").click()
                            # 点击 결제하기
                            try:
                                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@class='imp-dialog customizable payment-kakaopay pc']")))
                                iframe = self.driver.find_elements_by_tag_name('iframe')
                            except TimeoutException:
                                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
                                    (By.XPATH, "//div[@class='imp-dialog customizable payment-kakaopay pc']")))
                                iframe = self.driver.find_elements_by_tag_name('iframe')

                            self.driver.switch_to.frame(iframe[len(iframe) - 2])

                            WebDriverWait(self.driver, 60).until(
                                EC.visibility_of_element_located((By.XPATH, "//ul[@class='list_gnb']")))
                            li = self.driver.find_elements_by_xpath("//ul[@class='list_gnb']")[0]
                            li.click()
                            self.driver.find_element_by_id("userPhone").click()
                            self.driver.find_element_by_id("userPhone").clear()
                            self.driver.find_element_by_id("userPhone").send_keys(kakao_phone)
                            self.driver.find_element_by_id("userBirth").click()
                            self.driver.find_element_by_id("userBirth").clear()
                            self.driver.find_element_by_id("userBirth").send_keys(kakao_birth)
                            self.driver.find_element_by_id("userPost").submit()

                            logger.debug("尽快在kakao上完成付款，总耗时{:.3f}".format(time() - time3))
                            sleep(6)
                            return

        except Exception as e:
            logger.error(e)


class MyThread(threading.Thread):

    def __init__(self, func):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)
        self.func = func

    def run(self):
        self.result = self.func()

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


if __name__ == '__main__':
    user_name = "qwhsdwd@gmail.com"
    user_passwd = "qwh961126!"
    # url = "https://www.nike.com/kr/ko_kr/t/adult-unisex/fw/action-outdoor/BQ6817-006/oaic91/nike-sb-dunk-low-pro"
    # url = "https://www.nike.com/kr/ko_kr/t/men/fw/running/BQ1671-002/ifaa28/nike-odyssey-react-2-shield"
    url = "https://www.nike.com/kr/launch/t/women/fw/nike-sportswear/CD8178-001/lhkq64/ws-vapor-street-ow"
    url = "https://www.nike.com/kr/ko_kr/t/men/fw/basketball/BQ4631-001/jrek84/kyrie-6-ep"
    shoes_size = "240"
    start_time = "10-31 10:00:00"
    kakao_phone = "01029972828"
    kakao_birth = "970105"
    ip_proxy = []

    nike_robot1 = nikeRobot(user_name, user_passwd, shoes_size, start_time, ip_proxy)
    nike_robot1.login()
    nike_robot1.robot_start(url, kakao_phone, kakao_birth)

# while 1:
#     start = time.clock()
#     try:
#         driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[60]").click()
#         print '已定位到元素'
#         end=time.clock()
#         break
#     except:
#         print "还未定位到元素!"
#
# print '定位耗费时间：'+str(end-start)
#
