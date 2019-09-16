#crear imagen
from tkinter import *
from PIL import Image , ImageDraw , ImageTk
blanco = (255, 255, 0)

image1 = Image.new("RGB", (400,300) , blanco)
pintura = ImageDraw.Draw(image1)

print(type(pintura))

pintura.line( [10,0,10,100] , fill="black" )
pintura.line( [10,100,100,100] , fill="black" )
pintura.rectangle( [110,110,150,150] , fill="black" )

#guardarimagen
filename = "Prueba.png"
image1.save(filename)

#mostrar imagen guardada
pantaya = Tk()
imagen = Image.open("Prueba.png")
nuevoancho = 150

alto,ancho = 500,500

foto = ImageTk.PhotoImage(imagen)
canvas = Canvas(pantaya, height=alto , width=ancho)
canvas.create_image(100, 80, image=foto)

canvas.pack(side = TOP, expand= True , fill=BOTH)
pantaya.mainloop()
