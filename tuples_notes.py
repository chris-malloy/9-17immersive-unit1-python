# lists are really handy.  But they are changeable!  Mutations occur.
#What if you wanted something that couldn't be changed? imutable
# A typle is in all ways a. list, except:
# 1. It's values cannot be changed
# 2. It uses () instead of []

a_tuple = [1,2,3]
print a_tuple
print a_tuple[1]




# Dictionaries 
# Dictionaries are just like lists, but instead of numbered indices, they have ENlgish indices number


name = "Rob"
gender = "Male"
height = "Tall"

# A list makes no snce to tie them together...
# person = [
# 	"Rob",
# 	"Male",
# 	"tall"
# ]

person = {
	"name": "Rob",
	"gender":"Male",
	"height":"Tall"
}

# print person["name"]
# print person["gender"]
zombie = {}
zombie["weapon"] = "axe"
zombie["health"] = 100
zombie["speed"] = 10

print zombie
for key, value in zombie.items():
	print "Zombie has a key of %s with a value of %s." % (key, value)
	print "Zombie has a key of %s with a vlaue of %s" % (key, zombie[key])

# Del will remove the key and value!
del zombie["speed"]
print zombie


is_nighttime = True
if(is_nighttime):
	zombie["health"] += 50

# prut lists and dictionaries together!
zombies = [] 
zombies.append({
	'speed': 10,
	'weapon':'fist'
	# 'name':'Joe'
	})
zombies.append({
	'speed':15,
	'weapon': 'bat',
	'name': 'Willie'
	'victim':[
		'Bob',
		'Aaron'
		]
})
print zombies[1]['victimes'][1]





