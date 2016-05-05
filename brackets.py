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

			teams_still_in = []
			for team in teamlist :
				if still_playing[team] == True :
					teams_still_in.append(team)


			for i in xrange(0,len(teams_still_in)-1,2) :

				if teams_still_in[i] < teams_still_in[i+1] :
					points[teams_still_in[i]] += 1
					still_playing[teams_still_in[i+1]] = False
					owner[teams_still_in[i+1]] = teams_still_in[i]
				else :
					points[teams_still_in[i+1]] += 1
					still_playing[teams_still_in[i]] = False
					owner[teams_still_in[i]] = teams_still_in[i+1]

			print teams_still_in

		print owner
		print points

		cur_points = points.values()

		for team in points.keys() :
			if owner[team] != 0 :
				points[team] = cur_points[team-1] + 0.1*cur_points[owner[team]-1]

		for team in points.keys() :
			points[team] = round(points[team],5)

		print points

			



world = Pool(24)
world.Simul()