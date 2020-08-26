from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import re #正则表达式
import requests
import paddlehub as hub

module = hub.Module(name="ernie_gen_lover_words")

def butonck():
    #改变lab颜色
    buttonx["fg"]="green"
    #获取输入框值
    textx=entryx.get()
    #去掉字符串前后空格
    textx=textx.strip()
    if textx=='':
      #弹出提示框
      messagebox.showinfo("提示","输入不可为空")
    else:
        test_texts = [str(textx)]
        results = module.generate(texts=test_texts, use_gpu=True, beam_width=1)
        for result in results:
            # print(result)
            lab2=Label(rview,text = result,fg="red",font=("宋体", 13))
            lab2.grid(row=2,columnspan=2)
#创建窗口
rview=Tk()
#标题
rview.title("不是直男 想尽办法爱你")
#窗口大小 长高用小写x隔开
#rview.geometry("600x300")
# 图标
rview.iconbitmap('bitbug_favicon.ico')
#窗口基于屏幕的坐标 +x轴+y轴
rview.geometry("+500+200")
#创建lab标签
labelx=Label(rview,text="关键词",font=("宋体",20))
#显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0,column=0)
#创建输入框
entryx=Entry(rview,font=("宋体",20))
#显示输入框
entryx.grid(row=0,column=1)
#创建按钮
buttonx=Button(rview,text="确定生成",font=("宋体",20),command=butonck)
#显示按钮
buttonx.grid(row=0,column=2)
#显示后改变按钮属性
#buttonx["width"]=2


#消息循环 显示窗口
rview.mainloop()
