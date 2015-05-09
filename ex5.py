zed_name = 'Zed A. Shaw'
zed_age = 35 # not a lie
zed_height = 74 # inches
zed_height_cm  = "%d * zed_height" % 2.54
zed_weight = 180 # lbs
zed_eyes = 'Blue'
zed_teeth = 'White'
zed_hair = 'Brown'

print "Let's talk about %r." % zed_name
print "He's %r inches and $r tall." % (zed_height, zed_height_cm)
print "He's %r prouds heavy." % zed_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (zed_eyes, zed_hair)
print "His teeth are usually %r depending on the coffee." % zed_teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (zed_age, zed_height, zed_weight, zed_age + zed_height + zed_weight)