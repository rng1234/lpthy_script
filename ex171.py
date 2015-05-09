from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

text = open(from_file).read()

print "Your original file is %d." % len(text)

print "Does the output file exist? %s" % exists(to_file)

print "Let's do this"

writetxt = open(to_file, "w")
writetxt.write(text)

print "done"
