# -__-__-__-__-__-__-__-__-__-     Algorithm placing teams in a single bracket tree according to their individual seed     -__-__-__-__-__-__-__-__-__- #

# first try (but fail)

# nb_teams = 16
# temp = [1,nb_teams]
# pouet = nb_teams
# count = 1
# while pouet > 2 :
# 	for i in xrange(0,count,1) :
# 		match = nb_teams*(i%2)*int(i<2) + (nb_teams/2)*int(i>=2) + ((-1)**i)*(pouet/2)+1 
# 		temp.append(match)
# 		temp.append(nb_teams+1 - match)
# 		# if i%2 == 0 :
# 		# 	temp.append((pouet/2)+1)
# 		# 	temp.append(nb_teams+1 - ((pouet/2)+1))
# 		# else :
# 		# 	temp.append((nb_teams-pouet/2)+1)
# 		# 	temp.append(nb_teams+1 - ((nb_teams-pouet/2)+1))
# 	pouet = pouet/2
# 	count = count*2
# 	print pouet,count
# 	print temp
# print temp


# working version
nb_teams = 16
matches = [1,2]
phase = 2

while 2**phase <= nb_teams :

	for i in xrange(1,2*len(matches),2) :

		if (i+1)%4 == 2 :
			matches.insert(i,((2**phase)+1)-matches[i-1])

		else :
			matches.insert(i-1,((2**phase)+1)-matches[i-1])

	phase += 1

print matches