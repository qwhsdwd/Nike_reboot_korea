from tkinter import *
from time import *
from PIL import Image, ImageTk
from nikeRobot import nikeRobot
import threading


def clear_log():

    with open("./log/logging.log","w")as f:
        f.write("")

def main():


    def center_window(w, h):
        # 获取屏幕 宽、高
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # 计算 x, y 位置
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root=Tk()

    root.title("NikeRobot")
    x,y=500,600 #宽500，长230
    center_window(x,y)

    user_name_input = StringVar()
    user_passwd_input = StringVar()
    url_input = StringVar()
    shoes_size_input = StringVar()
    start_time_input = StringVar()
    kakao_phone_input = StringVar()
    kakao_birth_input = StringVar()


    def handle_focus_in_time_example(_):
        time_example.delete(0, END)
        time_example.config(fg='black')

    def handle_focus_out_time_example(_):
        time_example.delete(0, END)
        time_example.config(fg='grey')
        time_example.insert(0, "Example:01-01 23:59:00")

    def handle_focus_in_phone_example(_):
        phone_example.delete(0, END)
        phone_example.config(fg='black')

    def handle_focus_out_phone_example(_):
        phone_example.delete(0, END)
        phone_example.config(fg='grey')
        phone_example.insert(0, "Example:01012345678")

    def handle_focus_in_birth_example(_):
        birthday_example.delete(0, END)
        birthday_example.config(fg='black')

    def handle_focus_out_birth_example(_):
        birthday_example.delete(0, END)
        birthday_example.config(fg='grey')
        birthday_example.insert(0, "Example:990101")

    def handle_focus_in_shoe_size_example(_):
        shoe_size_example.delete(0, END)
        shoe_size_example.config(fg='black')

    def handle_focus_out_shoe_size_example(_):
        shoe_size_example.delete(0, END)
        shoe_size_example.config(fg='grey')
        shoe_size_example.insert(0, "如有多个鞋码请用,号隔开")

    def thread_it(func, *args):
        '''将函数打包进线程'''
        # 创建
        t = threading.Thread(target=func, args=args)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    Label(root,text="NIKE账号").grid(row=1,column=0)
    user_name_example=Entry(root,textvariable=user_name_input)
    user_name_example.grid(row=1,column=1)
    Label(root,text="NIKE密码").grid(row=2,column=0)
    user_passwd_example=Entry(root,textvariable=user_passwd_input,show="*")
    user_passwd_example.grid(row=2,column=1)
    Label(root,text="鞋子链接").grid(row=3,column=0)
    url_example=Entry(root,textvariable=url_input)
    url_example.grid(row=3,column=1)
    Label(root,text="鞋子码数").grid(row=4,column=0)
    shoe_size_example=Entry(root,textvariable=shoes_size_input)
    shoe_size_example.grid(row=4,column=1)
    Label(root,text="开始时间").grid(row=5,column=0)
    time_example=Entry(root,textvariable=start_time_input)
    time_example.grid(row=5,column=1)
    Label(root,text="电话").grid(row=6,column=0,sticky=W)
    phone_example=Entry(root,textvariable=kakao_phone_input)
    phone_example.grid(row=6,column=1)
    Label(root,text="生日").grid(row=7,column=0,sticky=W)
    birthday_example=Entry(root,textvariable=kakao_birth_input)
    birthday_example.grid(row=7,column=1)

    time_example.bind("<FocusIn>",handle_focus_in_time_example)
    time_example.bind("<Return>",handle_focus_out_time_example("Example:01-01 23:59:00"))
    phone_example.bind("<FocusIn>",handle_focus_in_phone_example)
    phone_example.bind("<Return>",handle_focus_out_phone_example("Example:01012345678"))
    birthday_example.bind("<FocusIn>",handle_focus_in_birth_example)
    birthday_example.bind("<Return>",handle_focus_out_birth_example("Example:990101"))
    shoe_size_example.bind("<FocusIn>",handle_focus_in_shoe_size_example)
    shoe_size_example.bind("<Return>",handle_focus_out_shoe_size_example("如有多个鞋码请用,号隔开"))

    def get_str():

        L = list()
        L.append(user_name_input.get())
        L.append(user_passwd_input.get())
        L.append(url_input.get())
        L.append(shoes_size_input.get())
        L.append(start_time_input.get())
        L.append(kakao_phone_input.get())
        L.append(kakao_birth_input.get())

        qwh = nikeRobot(L[0], L[1], L[3], L[4], [])
        qwh.login()
        qwh.robot_start(L[2], L[5], L[6])


    img_open = Image.open('./image/nike_robot.png')
    out=img_open.resize((230,230),Image.ANTIALIAS)
    img_png = ImageTk.PhotoImage(out)
    label_img = Label(root, image = img_png)
    label_img.grid(row=0,column=4,rowspan=10,sticky=E)

    log=Label(root,text="日志输出").grid(row=9,column=0)

    text=Text(root,height=25,width=67)
    text.grid(row=10,column=0,columnspan=9)
    text.configure(borderwidth=0,background=root.cget('background'))

    def clear_log():
        text.delete(0.0, END)
    but1=Button(root,text="开始",command=lambda :thread_it(get_str),height=1,width=7).grid(row=12,column=0)
    but2=Button(root,text="清除日志",command=lambda :thread_it(clear_log),width=7).grid(row=12,column=1,sticky=W)
    # but3=Button(root,text="退出程序",command=quit,width=7).grid(row=12,column=4,sticky=E)

    def read_log_file():

        fpath = "./log/logging.log"
        fp_r = open(fpath, 'r')

        while True:
            sleep(0.1)
            line_r = fp_r.readline()
            text.insert(END,line_r)

    thread_it(read_log_file)
    try:
        root.mainloop()
    except Exception as e:
        text.insert(END,e)

if __name__ == '__main__':
    clear_log()
    main()
