from tkinter import *
from nikeRobot import nikeRobot

root=Tk()

root.title("NikeRobot")

user_name_input = StringVar()
user_passwd_input = StringVar()
url_input = StringVar()
shoes_size_input = StringVar()
start_time_input = StringVar()
kakao_phone_input = StringVar()
kakao_birth_input = StringVar()

Label(root,text="NIKE账号").grid(row=1,column=0)
Entry(root,textvariable=user_name_input).grid(row=1,column=1)
Label(root,text="NIKE密码").grid(row=2,column=0)
Entry(root,textvariable=user_passwd_input).grid(row=2,column=1)
Label(root,text="鞋子链接").grid(row=3,column=0)
Entry(root,textvariable=url_input).grid(row=3,column=1)
Label(root,text="鞋子码数").grid(row=4,column=0)
Entry(root,textvariable=shoes_size_input).grid(row=4,column=1)
Label(root,text="开始时间(格式:2020-01-01 00:00:00)").grid(row=5,column=0)
Entry(root,textvariable=start_time_input).grid(row=5,column=1)
Label(root,text="kakao电话(格式01012345678)").grid(row=6,column=0)
Entry(root,textvariable=kakao_phone_input).grid(row=6,column=1)
Label(root,text="kakao生日(格式960101)").grid(row=7,column=0)
Entry(root,textvariable=kakao_birth_input).grid(row=7,column=1)


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

but=Button(root,text="开始",command=get_str).grid(row=8,column=1)

root.mainloop()
