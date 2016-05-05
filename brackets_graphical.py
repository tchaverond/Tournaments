# -*- coding: utf-8 -*

from Tkinter import*
import random
import sys



# list contanining all matches that have to be played / have been played, in order
global decider
decider = []


class Match :

	def __init__(self, id_team1, id_team2, name1, name2, top_x, top_y, bottom_x, bottom_y, phase) :

		self.id_team1 = id_team1
		self.id_team2 = id_team2
		self.name1 = name1
		self.name2 = name2
		self.coords = [top_x,top_y,bottom_x,bottom_y]
		self.played = False
		self.phase = phase


	def __repr__(self) :

		return "Match between "+self.name1+" and "+self.name2+ ", played : "+str(self.played)+", during phase : "+str(self.phase)


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
		self.x_size = 100
		self.y_size = 40
		self.x_gap = 40
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

	# TODO : comments + organization
	# make sure there are enough nb_teams = len(names)
	def draw_sb(self, nb_teams = 16, names = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]) :

		mult_2 = [2**i for i in xrange(1,13,1)]

		if nb_teams > mult_2[len(mult_2)-1] :

			print "Number of teams is too high."
			return -1

		order = sb_placement(nb_teams)
		order.reverse()

		if nb_teams in mult_2 :

			phase = 1
			matches_to_add = 0

		else :

			phase = 2
			matches_to_add = min([nb_teams-i for i in mult_2 if (nb_teams-i) > 0])
			closest_upper = min([i for i in mult_2 if i > nb_teams])
			suporder = sb_placement(closest_upper)
			#print order,suporder

			for i in xrange(1,matches_to_add+1,1) :

				id1 = suporder[2*order[i-1]-2]
				id2 = suporder[2*order[i-1]-1]

				top_x = self.x_gap
				top_y = self.y_gap + (order[i-1]-1)*(self.y_size+self.y_gap)
				bottom_x = top_x + self.x_size
				bottom_y = top_y + self.y_size
				self.tree.create_rectangle(top_x,top_y,bottom_x,bottom_y,outline="black")
				self.tree.create_text(top_x+2,top_y+2,anchor="nw",text=names[id1-1])
				self.tree.create_line(top_x,top_y+self.y_size/2,bottom_x,top_y+self.y_size/2,fill="black")
				self.tree.create_text(top_x+2,top_y+self.y_size/2+2,anchor="nw",text=names[id2-1])

				decider.append(Match(id1,id2,names[id1-1],names[id2-1],top_x,top_y,bottom_x,bottom_y,phase-1))



		imax = (nb_teams-matches_to_add)/2
		order.reverse()

		
		while imax > 0 :

			for i in xrange(1,imax+1,1) :

				top_x = phase*self.x_gap + (phase-1)*self.x_size
				top_y = i*self.y_gap + (i-1)*self.y_size + ((2**(phase-1))-1)*(0.5*(self.y_size+self.y_gap))*((2*i)-1)
				bottom_x = top_x + self.x_size
				bottom_y = top_y + self.y_size
				self.tree.create_rectangle(top_x,top_y,bottom_x,bottom_y,outline="black")
				self.tree.create_line(top_x,top_y+self.y_size/2,bottom_x,top_y+self.y_size/2,fill="black")


				id1 = order[2*i-2]
				id2 = order[2*i-1]
				name1 = "TBD"
				name2 = "TBD"


				if imax == (nb_teams-matches_to_add)/2 :

					if order[2*i-2] <= nb_teams-matches_to_add*2 :
						name1 = names[id1-1]
						self.tree.create_text(top_x+2,top_y+2,anchor="nw",text=name1)

					if order[2*i-1] <= nb_teams-matches_to_add*2 :
						name2 = names[id2-1]
						self.tree.create_text(top_x+2,top_y+self.y_size/2+2,anchor="nw",text=name2)


				decider.append(Match(id1,id2,name1,name2,top_x,top_y,bottom_x,bottom_y,phase))


			phase += 1
			imax = imax/2



def sb_placement(n) :

	nb_teams = n
	matches = [1,2]
	phase = 2

	while 2**phase <= nb_teams :

		for i in xrange(1,2*len(matches),2) :

			if (i+1)%4 == 2 :
				matches.insert(i,((2**phase)+1)-matches[i-1])

			else :
				matches.insert(i-1,((2**phase)+1)-matches[i-1])

		phase += 1

	return matches


pouet = Window()

nb_teams = int(sys.argv[1])

names = []

for i in xrange(nb_teams) :
	
	names.append("".join([random.choice(['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']) for j in xrange(3)]))

pouet.draw_sb(nb_teams,names)
for match in decider :
	print match
pouet.master.mainloop()