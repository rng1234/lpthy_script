print """

_________________________________________

	Bingo	 Game
			
			
_________________________________________


"""
input = "> "

name = raw_input("What's your name?")

print "You wake up in a room with no door, a light shaking on the ceiling. What will you do?"
print """
A. Look around
B. Scream
C. Knock the wall
D. Jeck off
"""

answer1 = raw_input(input)

if answer1 == "A":
	print "You got a key. But where's the door?"
	
elif answer1 == "B":
	print "Nothing happen."
	
elif answer1 == "C":
	print "Walls so hard."
	
elif answer1 == "D":
	print "You saved."
	
else:
	print "You doomed."