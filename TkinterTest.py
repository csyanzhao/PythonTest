from tkinter import *

root = Tk()

textLabel = Label(root,text="有些心疼，又带着欣喜。\n她那么简单，不好看，却努力的开着，\
\n为了迎合清风掠心的柔情，一直努力的开着，\n半盏清歌的招摇，\
肆意葱茏。\n而我，恰巧路过。于是，\n喜意便盈盈的生了起来，带\
着异样的温暖和朴素，\n将心，都染了湿湿的绿，盎然的，\n万千端倪。", justify=LEFT, padx=10) #Label 标签控件；可以显示文本和位图

textLabel.pack(side=LEFT)

mainloop()