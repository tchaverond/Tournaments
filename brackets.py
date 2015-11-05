# -*- coding: utf-8 -*

import random


class Pool:

	def __init__(self,n=16) :

		self.pool = [i for i in xrange(1,n+1,1)]


	def Simul(self) :

		for i in xrange(0,1,1) :

			random.shuffle(self.pool)
			print self.pool

			self.Single_bracket(self.pool)


	def Single_bracket(self, teamlist) :

		points = {}
		still_playing = {}
		owner = {}


		for team in teamlist :
			points[team] = 0
			still_playing[team] = True
			owner[team] = 0


		while still_playing.values().count(True) > 1 :

			temp = []
			for team in teamlist :
				if still_playing[team] == True :
					temp.append(team)


			for i in xrange(0,len(temp)-1,2) :

				if temp[i] < temp[i+1] :
					points[temp[i]] += 1
					still_playing[temp[i+1]] = False
					owner[temp[i+1]] = temp[i]
				else :
					points[temp[i+1]] += 1
					still_playing[temp[i]] = False
					owner[temp[i]] = temp[i+1]

			print temp

		print owner
		print points

		temp = points.values()

		for team in points.keys() :
			if owner[team] != 0 :
				points[team] = temp[team-1] + 0.1*temp[owner[team]-1]

		for team in points.keys() :
			points[team] = round(points[team],5)

		print points

			



world = Pool(24)
world.Simul()