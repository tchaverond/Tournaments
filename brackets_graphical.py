# -*- coding: utf-8 -*

from Tkinter import*


class Window :

	def __init__(self) :

		self.master = Tk()
		self.master.title("Brackets... brackets everywhere !")
		#self.master.geometry("1300x650")          # seems kinda pointless

		self.see = True

		# both probably rendered useless, as the Canvas is now virtually infinite
		#self.w = 1300
		#self.h = 1000

		self.x_size = 80
		self.y_size = 40
		self.x_gap = 20
		self.y_gap = 8

		frame = Frame(self.master)
		frame.pack()

		scrollbar = Scrollbar(frame)
		scrollbar.pack(side=RIGHT,fill=Y)

		self.tree = Canvas(frame,bg='white',scrollregion=(0,0,1000,1000),yscrollcommand=scrollbar.set)
		self.tree.bind_all("<MouseWheel>", self._on_mousewheel)
		self.tree.pack()

		scrollbar.config(command=self.tree.yview)

	def _on_mousewheel(self, event):
		self.tree.yview_scroll(event.delta, "units")



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
pouet.draw_sb(32)
pouet.master.mainloop()