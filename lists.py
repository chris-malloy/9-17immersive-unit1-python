# student1 = "Mikayla"
# student2 = "Jennifer"
# student3 = "Nikolas"
# student4 = "Zach"

# print student1
# print student2
# print student3
# print student4

# # list is. a single variable with a bunch of numbered (indexed) parts. 
# # An index, in a list, is ALWAYS a number (integer)
# # A list is made with []. Every element is separated by a ,
# students = [
# 	"Mikayla", 
# 	"Jennifer", 
# 	"Nikolas", 
# 	"Zach"
# ]

# print students

atlanta_teams = [
	"Falcons", 
	"Braves",
	"Hawks",
	"Trashers"
]
# print atlanta_teams
# # Wait. Trashers are gone. Use .pop()
# # If you want to specify which index to pop off, set the parameter inside .pop()
# print atlanta_teams.pop()
# # Hey we have a new team.
# atlanta_teams.append("Atl United")
# print atlanta_teams

# now, let's use a loop to remove a team.
# Loop from 0-5
# for i in range(0,5):
# atlanta_team_length = len(atlanta_teams)
# for i in range(0,atlanta_team_length):
# 	# Check to see if the ith element (the one we are on) is thrashers
# 	if(atlanta_teams[i] == "Thrashers"):
# 		thrashers_index = i
		

# # atlanta_teams.pop(thrashers_index)
# print atlanta_teams

# split method
teams_as_a_string = "Falcons, Braves, Hawks, Atl United"
print teams_as_a_string
teams_as_a_list = teams_as_a_string.split(', ')
print teams_as_a_list

# sort method - will put in natural order
sorted_atlanta_teams = atlanta_teams.sort()
print sorted_atlanta_teams

# append method
print atlanta_teams.append("Atl United")

# #reverse method - will put in reverse natural order
# sorted_atlanta_teams.reverse()
# print sorted_atlanta_teams

# slice stuff off
# if you want to copy a part of the list, you can use [x:y]
# This will create a COPY of the array. It will NOT change the original
# It will start at the Xth element, and will stop at the Yth.
# So if we want Braves and Hawks (1,2), we start at 1, we stop before 3
baseball_basketball = atlanta_teams[1:3]
print baseball_basketball

all_but_the_first = atlanta_teams[1:]
print all_but_the_first

# to delete an index, you can use the remove method.
atlanta_teams.remove("Braves") 

# insert... we can insert an element where ever we want.
atlanta_teams.insert(1, "Braves")
print atlanta_teams






















