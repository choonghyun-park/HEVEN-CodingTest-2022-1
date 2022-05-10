import sys
import tkinter
from PIL import Image, ImageTk, ImageDraw

map_input=[]
bs = 1

def create_circle(x, y, r, canvasName,num): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    if num==1:
        return canvasName.create_oval(x0, y0, x1, y1, fill='red')
    elif num==2:
        return canvasName.create_oval(x0, y0, x1, y1, fill='blue')

def create_circle_d(x, y, r, draw,num): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    if num==1:
        return draw.ellipse((x0, y0, x1, y1), fill=(255,0,0))
    elif num==2:
        return draw.ellipse((x0, y0, x1, y1), fill=(0,0,255))

if __name__ == "__main__":
    
    testCase = int(input())
    if testCase>10 or testCase<=0:
        print("Wrong Input")
        exit(0)
    for i in range(testCase):
        mapSize_width, mapSize_height =input().split()
        mapSize_width = int(mapSize_width)
        mapSize_height = int(mapSize_height)

        map_i = [list(map(int, input().split())) for _ in range(mapSize_height)]
        map_input.append(map_i)

    tk = tkinter.Tk()
    tk.title("HEVEN Map")
    # canvas = tkinter.Canvas(width=mapSize_width*bs,height=mapSize_height*bs,bg='black')
    # drawing map
    for i in range(testCase):
        map_i = map_input[i]
        image1 = Image.new("RGB",(mapSize_width,mapSize_height))
        draw = ImageDraw.Draw(image1)
        for y in range(mapSize_height):
            for x in range(mapSize_width):
                if map_i[y][x]==0:
                    draw.rectangle((x*bs, y*bs, x*bs+bs, y*bs+bs), fill=(255,255,255))
                if map_i[y][x]==3:
                    draw.rectangle((x*bs, y*bs, x*bs+bs, y*bs+bs), fill=(0,0,0))
                if map_i[y][x]==1:
                    draw.rectangle((x*bs, y*bs, x*bs+bs, y*bs+bs), fill=(255,255,255))
                    create_circle_d(x*bs,y*bs,3,draw,1)
                if map_i[y][x]==2:
                    draw.rectangle((x*bs, y*bs, x*bs+bs, y*bs+bs), fill=(255,255,255))
                    create_circle_d(x*bs,y*bs,3,draw,2)

                # if map_i[y][x]==0:
                #     canvas.create_rectangle(x*bs, y*bs, x*bs+bs, y*bs+bs, fill="white")
                # if map_i[y][x]==3:
                #     canvas.create_rectangle(x*bs, y*bs, x*bs+bs, y*bs+bs, fill="black")
                # if map_i[y][x]==1:
                #     canvas.create_rectangle(x*bs, y*bs, x*bs+bs, y*bs+bs, fill="white")
                #     create_circle(x*bs,y*bs,3,canvas,1)
                # if map_i[y][x]==2:
                #     canvas.create_rectangle(x*bs, y*bs, x*bs+bs, y*bs+bs, fill="white")
                #     create_circle(x*bs,y*bs,3,canvas,2)
        image1.save("./%d.png"%(i+1))
        # canvas.pack()
        # tk.mainloop()