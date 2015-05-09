from sys import argv #import argv module from sys.

script, filename = argv #First parameter means the filesame of scprit,
						#second one means the parameter type in shell or cmd that following the script.

txt = open(filename) #Open the filename that input in shell.

print "Here's your file %r:" % filename #printing out the filename.
print txt.read() #Raw output content of the txt file. should equal to 'cat' in shell. 

print "Type the filename again:" #ask user to input another filename again
file_again = raw_input("> ") #user's input content equal to file_again.

txt_again = open(file_again) #open filename that user input.

print txt_again.read() #raw output content of filename.

txt.close()
txt_again.close()