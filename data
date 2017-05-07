import turtle


count=10
words=[]
data=[]
yscale=6
xscale=30

def drawline(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)


def drawrectange(t,x,y):
    x=x*xscale
    y=y*yscale
    drawline(t,x-5,0,x-5,y)
    drawline(t,x-5,y,x+5,y)
    drawline(t,x+5,y,x+5,0)
    drawline(t,x+5,0,x-5,0)


def drawbar(t):
    for i in range(count):
        drawrectange(t,i+1,data[i])


def drawtext(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)


def drawgraph(t):
    drawline(t,0,0,360,0)
    drawline(t,0,300,0,0)

    for i in range(count):
        x=i+1
        drawtext(t,x*xscale,-20,words[i-1])
        drawtext(t,x*xscale,data[i-1]*yscale+5,data[i-1])
    drawbar(t)


def robinsone(line):
    for ch in line:
        if ch in "{}[],.""<>/?\|~~":
            line=line.replace(ch," ")
    return line





def robinstwo(line,wordcount):

    line=robinsone(line)
    words=line.split()

    for word in words:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1





def main():
    filename=input("Enter a filename path: ").strip()
    infile=open(filename,"r")
    wordcount={}
    for line in infile:
        robinstwo(line.lower(),wordcount)

    pairs=list(wordcount.items())
    items=[[x,y]for (y,x) in pairs]
    items.sort()

    for i in range(len(items)-1,len(items)-count-1,-1):
        print(items[i][1]+ "\t" +str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    infile.close()




    turtle.title("词频分析柱状图")
    turtle.Turtle()
    turtle.setup(2000,2000,0,0)
    turtle.hideturtle()
    turtle.width(3)
    drawgraph(t)


if __name__=='__main__':
    main()























