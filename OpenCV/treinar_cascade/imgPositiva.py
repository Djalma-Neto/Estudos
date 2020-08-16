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

	def get_frame(self, filtro, detect):

		x,img1 = self.vid.read()
		img = cv2.flip(img1, 180)

		img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
		img_cascade = cv2.flip(img2, 180)
		
		if(detect):
			clf1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
			clf2 = cv2.CascadeClassifier('haarcascade_eye.xml')

			face = clf1.detectMultiScale(img_cascade, 1.3, 15)
			olho = clf2.detectMultiScale(img_cascade, 1.3, 15)

			for(x,y,w,h) in face:
	   	 		img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),1)
	   	 		cv2.putText(img, "Face".format(), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

			for(x,y,w,h) in olho:
	   	 		img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),1)
	   	 		cv2.putText(img, "olho".format(), (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		
		if (filtro):
			val = cv2.GaussianBlur(img,(5,5),0)
			#val = cv2.bilateralFilter(img,9,75,75)
			#val = cv2.medianBlur(img,5)
			return(x,val)
		else:
			return(x,cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


class App:
	filtro = False
	detect = False

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
		x, frame = self.vid.get_frame(self.filtro,self.detect)
		if x:
			img = cv2.resize(frame, (100,100))
			cv2.imwrite("positivas/001.jpg", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

	def update(self):

		x, frame = self.vid.get_frame(self.filtro,self.detect)

		if x:
			height = 0
			width = 23
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(width, height, image = self.photo, anchor = tkinter.NW)
			self.janela.after(self.delay, self.update)


App(tkinter.Tk(), "Tkinter e OpenCV")
