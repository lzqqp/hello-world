import wx
def hello(event):
    print('hello,word')
app=wx.App()
win=wx.Frame(None,title='hello,wxPython',size=(200,100))
button=wx.Button(win,label='hello')

win.show()
app.MainLoop()
