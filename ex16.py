from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three line."

line1 = raw_input("First line")
line2 = raw_input("Second line")
line3 = raw_input("Third line")

target.write(("%s%s%s%s%s%s") % (line1,"\n",line2,"\n",line3,"\n"))

target.close()