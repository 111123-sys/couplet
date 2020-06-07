from tkinter import*
import webbrowser
# coding:utf-8
import json
import requests
import urllib.request
# print("================")
# function: 获取对联

center = "8"
left = "7"
right = "6"
body = {
    'text': '',
    'index': 0
}
headers = {
    'Content-Type': 'application/json',
}
def get_token_key():
    token_key=''
    client_id = 'WfQBUK6E8miYxl9HINu9gGyo'  # 应用的apiKey
    client_secret = 'HO5rfmOE6rEZgjceGB3VFGxMXiYvCokn'  # 应用的secretKey
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
           + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()

    if token_content:
        token_info = json.loads(token_content)
        token_key = token_info['access_token']
        # print(content['refresh_token'])
    return token_key
token=get_token_key()
def coupletsGet(keyword):
    body['text'] = keyword
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/couplets' + '?access_token=' + token
    param = json.dumps(body).encode('utf-8')
    try:
        result = requests.post(url=url, headers=headers, data=param)
        print(result.json()['couplets']['center'])  # 横批
        global center  # 全局变量我来撑控
        center = result.json()['couplets']['center']
        print(result.json()['couplets']['first'])  # 上联
        global left
        left = result.json()['couplets']['first']
        print(result.json()['couplets']['second'])  # 下联
        global right
        right = result.json()['couplets']['second']
    except:
        print('没有对联')
# keyword = "皇帝"
# coupletsGet(keyword)
def chniese_filter(str):
    str0 = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str)
    return str0
def accessTo():
        print("================")
        showWindow = Tk()
        showWindow.title('生成对联')
        width = 600
        height = 200
        screenwidth = showWindow.winfo_screenwidth()
        screenheight = showWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        showWindow.geometry(alignstr)
        showWindow.resizable(width=True, height=True)
        text = entry1.get()
        text0 = chniese_filter(text)
        # c = "8"
        # l = "6"
        # r = "1"
        coupletsGet(text0)
        link = Label(showWindow, text=center, fg="Purple", cursor="hand2")
        link.pack()
        link = Label(showWindow, text=left, fg="Navy", cursor="hand2")
        link.pack()
        link = Label(showWindow, text=right, fg="Crimson", cursor="hand2")
        link.pack()
myWindow = Tk()
#设置标题
myWindow.title('智能对联')
width = 400
height = 100
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=False, height=True)
#标签控件布局
Label(myWindow, text="请输入关键字:                 ",fg = 'DarkKhaki').grid(row=0)
# Label(myWindow, text="output").grid(row=1)
#Entry控件布局
entry1=Entry(myWindow)
# entry2=Entry(myWindow)
entry1.grid(row=0, column=1)
entry1.configure(fg = 'DarkRed')
# entry2.grid(row=1, column=1)
#Quit按钮退出；Run按钮打印计算结果
Button(myWindow, text='退出',command=myWindow.quit,fg = 'DarkSlateGray').grid(row=2, column=0,sticky=W, padx=5, pady=5)
Button(myWindow, text='查询', command=accessTo,fg = 'MediumVioletRed').grid(row=2, column=1, sticky=W, padx=5, pady=5)
#进入消息循环
myWindow.mainloop()