import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class Captura:
	width = None
	height = None
	vid = None

	def __init__(self,camera=0):
		self.vid = cv2.VideoCapture(camera)


		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def get_frame(self):

		x,img1 = self.vid.read()
		img = cv2.flip(img1, 180)
		
		return(x,img)


class App:
	imgs = 0

	def __init__(self, janela, titulo, camera=0):

		self.janela = janela
		self.camera = camera
		self.janela.title(titulo)
		self.janela.geometry = ('600x800')

		self.vid = Captura(self.camera)

		self.canvas = tkinter.Canvas(janela, height = 500, width = 700)
		self.canvas.pack()
		self.BTN_print = tkinter.Button(janela, text="Print", width=20, command=self.print, bg='GREY').place(x=50,y=480)

		self.delay = 15
		self.update()

		self.janela.mainloop()

	def print(self):
		x, frame = self.vid.get_frame()
		if x:
			cv2.imwrite("positivas/{}.jpg".format(self.imgs), frame)
			self.imgs +=1

	def update(self):

		x, frame = self.vid.get_frame()

		if x:
			height = 0
			width = 23
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(width, height, image = self.photo, anchor = tkinter.NW)
			self.janela.after(self.delay, self.update)


App(tkinter.Tk(), "Tkinter e OpenCV")
