pi = 3.14

movel(p[0.35,0,0.09,pi,0.272,0]) #Starting position

#reference points
Pos0 = p[0.4,0.04,-0.09,pi,0.272,0] #un palatized start point
Pos1 = p[0.5,-0.15,-0.09,pi,0.272,0] #palatized start point

# Pile characteristics

pileHeight = 4
pileWidth = 2
pileLength = 1

btwnheight = 0.036 #mushroom height
btwnDis = 0.05 #The distance between the cylinders
number = 0 #Number of cylinders traveled

#movel(Pos000, a=1.2, v=0.25, t=4, r=0)
#movel(Pos010, a=1.2, v=0.25, t=4, r=0)

# a=1.2, v=0.25, t=4, r=0)

#RX 3.14
#RY 0.272

Pos1[0] = Pos1[0] - 0.06

while number < pileHeight * pileWidth * pileLength:
	if number % pileHeight == 0:
		if number % (pileHeight * pileWidth) == 0:
			Pos1[1] = Pos1[1] + 0.06
			Pos1[0] = Pos1[0] - 0.06
		elif number != 0:
			Pos1[0] = Pos1[0] + 0.06
		end
	end

	cylPos0 = Pos0
	cylPos1 = Pos1
	
	#calculating new position for cylinder
	cylPos0[0] = Pos0[0] + btwnDis*number
	cylPos1[2] = Pos1[2] + btwnheight*(number % pileHeight)
    
    #calculating the between travel for the cylinder
	cylPos0travel = cylPos0
	cylPos1travel = cylPos1

	#Making the travel for the cylinder 5 centimeters above the air
	cylPos0travel[2] = cylPos0[2] + 0.06
	cylPos1travel[2] = cylPos1[2] + 0.06


	movej(p[cylPos0[0],cylPos0[1] + 0.06,cylPos0[2],cylPos0[3],cylPos0[4],cylPos0[5]]) #Going behind
	movel(cylPos0 , a=1.2, v=0.25) #Grabing
	movel(cylPos0travel, a=1.2, v=0.25) #moving up

	movej(cylPos1travel, a=1.2, v=0.25) #move it over
	movel(cylPos1, a=1.2, v=0.25) #move it down
	movel(p[cylPos1[0],cylPos1[1] + 0.06,cylPos1[2],cylPos1[3],cylPos1[4],cylPos1[5]]) #place it
	movel(p[cylPos1travel[0],cylPos1travel[1] + 0.06,cylPos1travel[2],cylPos1travel[3],cylPos1travel[4],cylPos1travel[5]])
	movel(cylPos0travel)


	movej(p[ cylPos0[0],cylPos0[1] + 0.06,cylPos0[2],cylPos0[3],cylPos0[4],cylPos0[5] ]) #Back behind
	
	number = number + 1
	

	end