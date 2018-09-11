from tkinter import *
from PIL import Image as Img
from PIL import ImageSequence as Ims
from tkinter.filedialog import *
from shutil import rmtree
from os import makedirs
#
info = {
    'path':[]
}  #用 字典型 info 来存放 所读取所有文件的 path

def make_app():
    app = Tk()
    Label(app,text='compress tool', font=('Arial', 10)).pack()
    Listbox(app, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(app,text='| pick |', command=select).pack()
    Button(app,text='| start |', command=compress).pack()
    app.geometry('300x400')
    return app

def compress():
     for f in info['path']:
        output = f.split('/')[-1]
        out='C:/Users/dori/Desktop/pic/%s' % output   #在本程序目录下输出图片
        gif = Img.open(f)
        imgs = [i.copy() for i in Ims.Iterator(gif)]
        dura = gif.info['duration']/0.9
        index = 0
        imglist = []
        file = './%s' % output         #
        makedirs(file)
        for frame in imgs:
            x = 135
            y = 10
            w = 250
            h = 220
            region = frame.crop((x, y, x + w, y + h))
            region.save(file+"/%d.png" % index)  #当然这里用quality=N 则下面就不需要对读出来数据处理
            im = Img.open(file+"/%d.png" % index)
            im.thumbnail((198, 198), Img.ANTIALIAS)  #数据处理
            imglist.append(im)
            index += 1
        imglist[0].save(out, 'gif', save_all=True, append_images=imglist[1:], loop=0, duration=dura)
        rmtree(file)

def select():
    f_name=askopenfilenames()
    lbox=app.children['lbox']
    info ['path'] = f_name
    if info['path']:
        for name in f_name:
            lbox.insert(END, name.split('/')[-1])

app=make_app()
app.mainloop()