import numpy as np 
from numpy import random

##########################################################
# Simple Monte Carlo code to estimate number of expected #
# events in muon coincidence counter of arbitrary size   #
# and efficiency.                                        #
##########################################################

muon_flux = 1 #min^-1 cm^-2
paddle_size_x = 30 #cm
paddle_size_y = 15 #cm
dist_between_paddles = 30 #cm
muon_counter = 0 #Initially set to 0
runtime = 2 #"Time" in minutes that simulation runs for
detEfficiency = 0.45

#Define random muon start position in plane of detector 1
def start_pos_randomizer():
	start_pos_x = random.rand()*paddle_size_x
	start_pos_y = random.rand()*paddle_size_y
	return start_pos_x, start_pos_y
	
angle_list = []
probability_list = []
normalized_list = []

#Muon incidence angle distribution follows cos^2 
def angle_distribution():
	#Create half of cos^2 distribution for use as a probability distribution	
	for i in np.linspace(0,np.pi/2, 1000):
		angle_list.append(i)
		probability_list.append((4/np.pi)*(np.cos(i))**2)
	
	#Create normalized "discrete" distribution from this continuous cos^2 distribution
	#Probably better solutions than this "discrete" setup
	for k in probability_list:
		normalized_list.append((1/sum(probability_list))*k)

angle_distribution()		


#Use cos^2 distribution of muon angles to give a probable path for the generated muon event in terms of angle to x and y axes
def particle_path_randomizer():
		
	theta_x = np.random.choice( angle_list, p = normalized_list )
	theta_y = np.random.choice( angle_list, p = normalized_list )
	
	#Equal probability of negative and positive angles
	sign_multiplier_x = np.random.choice( [-1,1], p = [0.5, 0.5] )
	theta_x = theta_x * sign_multiplier_x
	sign_multiplier_y = np.random.choice( [-1,1], p = [0.5, 0.5] )
	theta_y = theta_y * sign_multiplier_y
	return theta_x, theta_y
	

#Calculate final position of particle based on angle of travel using trigonometry
def final_position(start_pos_x, start_pos_y):
	final_x = start_pos_x + dist_between_paddles * np.tan(theta_y) * np.cos(theta_x)
	final_y = start_pos_y + dist_between_paddles * np.tan(theta_y) * np.sin(theta_x)
	
	return final_x, final_y

#Check if particle lands in detection area (I know global variables are bad)
def coincidence_checker(final_x, final_y):
	global muon_counter
	if final_x <= paddle_size_x and final_x >=0 and final_y <= paddle_size_y and final_y >= 0:
		muon_counter += 1

#Run the simulation for runtime [minutes] 
for i in range(muon_flux * paddle_size_x * paddle_size_y * runtime):
	x, y = start_pos_randomizer()
	print("Generating event...")
	print(x,y)
	theta_x, theta_y = particle_path_randomizer()
	print(theta_x, theta_y)
	final_x, final_y = final_position(x,y)
	coincidence_checker(final_x, final_y)

print("Final muon count is " + str(muon_counter))
print("Expect to see " + str(detEfficiency*muon_counter))


	
	
