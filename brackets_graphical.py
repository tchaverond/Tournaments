# -*- coding: utf-8 -*

from Tkinter import*


class Window :

	def __init__(self) :

		self.master = Tk()
		self.master.title("Brackets... brackets everywhere !")
		#self.master.geometry("1300x650")          # just in case of

		# -__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__- #
		# -__-__-__-__-__-__-__-__-__-                                      Window's Layout                                       -__-__-__-__-__-__-__-__-__- #
		# -__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__- #

		# dimensions of the main window, according to the user's device
		self.w = self.master.winfo_screenwidth() * 0.8
		self.h = self.master.winfo_screenheight() * 0.8

		# master frame
		frame = Frame(self.master)
		frame.pack()

		# scrollbars
		scrollbarv = Scrollbar(frame)
		scrollbarv.pack(side=RIGHT,fill=Y)
		scrollbarh = Scrollbar(frame,orient=HORIZONTAL)
		scrollbarh.pack(side=BOTTOM,fill=X)

		# canvas in which we draw the brackets
		self.tree = Canvas(frame,bg='white',xscrollcommand=scrollbarh.set,yscrollcommand=scrollbarv.set,width=self.w,height=self.h)
		self.tree.bind("<Button-4>", self.on_mousewheel)
		self.tree.bind("<Button-5>", self.on_mousewheel)
		self.tree.bind("<Configure>",self.on_configure)
		self.tree.pack()

		scrollbarh.config(command=self.tree.xview)
		scrollbarv.config(command=self.tree.yview)

		# -__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__- #
		# -__-__-__-__-__-__-__-__-__-                                                                                            -__-__-__-__-__-__-__-__-__- #
		# -__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__- #


		# size of elements in brackets
		self.x_size = 80
		self.y_size = 40
		self.x_gap = 20
		self.y_gap = 8


	# vertical slider to be active on mousewheel
	def on_mousewheel(self, event):
		direction = 1
		if event.num == 4 :
			direction = -1
		self.tree.yview_scroll(direction, "units")

	# adapting the range of the vertical slider
	def on_configure(self, event) :
		self.tree.configure(scrollregion=self.tree.bbox('all'))



	#         |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||         #

	def draw_sb(self, nb_teams = 16) :

		if nb_teams not in [2,4,8,16,32,64,128] :

			# TO DO
			pass
			

		imax = nb_teams/2
		phase = 1

		while imax > 0 :

			for i in xrange(1,imax+1,1) :

				top_x = phase*self.x_gap + (phase-1)*self.x_size
				top_y = i*self.y_gap + (i-1)*self.y_size + ((2**(phase-1))-1)*(0.5*(self.y_size+self.y_gap))*((2*i)-1)
				bottom_x = top_x + self.x_size
				bottom_y = top_y + self.y_size
				self.tree.create_rectangle(top_x,top_y,bottom_x,bottom_y,outline="black")
				self.tree.create_line(top_x,top_y+self.y_size/2,bottom_x,top_y+self.y_size/2,fill="black")

			phase += 1
			imax = imax/2


pouet = Window()
pouet.draw_sb(256)
pouet.master.mainloop()