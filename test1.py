from config import *
from log import *
from database import database
from nikeRobot import MyThread



if __name__ == '__main__':


    start=time()

    with open("nike.html","r") as f:
        code=f.read()
    html = etree.HTML(code)
    etree.tostring(html, pretty_print=True)

    test=html.xpath("//div[@class='opt-list']//span[not(@disabled='disabled')][@class='input-radio']//label[@class='']")
    for i in test:
        print(i.text)

    # print(test2)
    # print(test2[0].xpath("//label")[0].text)
    # print(shoes_size_list)
    # print("数据库中鞋子货号的个数是{}".format(len(shoes_size_list)))
    # t1=threading.Thread(target=database)
    t1=MyThread(database)
    t1.start()
    t1.join()
    print(t1.get_result())
    # print(database())
    print("有货的数量:",len(test))
    print("所有鞋子的数量:",len(test))
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

