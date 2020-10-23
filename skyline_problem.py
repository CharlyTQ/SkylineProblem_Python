#Skyline Problem

#Input: [Li,Ri,Hi]  Li: x coordinate start  Ri: x coordinate end  Hi: Y height
#Output: [xi,yi]  keypoints coordinates

#Building class to store the Input format [Li, Ri, Hi]
class Building:
	def __init__(self, start_point, end_point, height):
		self.Li = start_point
		self.Ri = end_point
		self.Hi = height
#Critical points class to store the edges of each building (x,y) and add an "Is the edge the start or end of the bulding"
class critical_points:
	def __init__(self, x , y , isstart):
		self.x = x
		self.y = y
		self.isstart = isstart

#Function to print the buildings
def building_list(array):
	x=0
	for building in array:
		x+= 1
		print('Building', x,':', building.Li, building.Ri, building.Hi, sep=' ')

#Transform the building array in critpoints and sort them using th x coordinate parameter (-  +) 
def sort_array(city_array):
	critpoints_list = []
	for building in city_array:
		critpoints_list.append(critical_points(building.Li,building.Hi,True))
		critpoints_list.append(critical_points(building.Ri,building.Hi,False))

	critpoints_list.sort(key=lambda critical_points: critical_points.x)
	
	#for item in critpoints_list:
		#print(item.x,item.y,item.isstart,sep=' ')

	return critpoints_list

#Function to obtain the skyline edge points
def trace_skyline(array):
	prev_maxheight = 0
	trace_points = []
	temp_list = [0]

	for point in array:
		if (point.isstart):
			if point.y not in array:
				temp_list.append(point.y)

		else:
			if point.y in temp_list:
				temp_list.remove(point.y)

		maxheight = max(temp_list)

		if (prev_maxheight != maxheight):
			trace_points.append([point.x, maxheight])
			prev_maxheight = maxheight	

	return trace_points


#Create an array with all the buildings using our Input Format [Li,Ri,Hi]
city_array = [Building(2,9,10), Building(3,6,15), Building(5,12,12), Building(13, 16, 10), Building(15,17,5)]
#Print list of all buildings
building_list(city_array)
#Sort the array in x coordinates and apply an ending point criteria
crit_array = sort_array(city_array)
#Print Crit points
output = trace_skyline(crit_array)
print('Skyline')
for item in output:
	print(item)


