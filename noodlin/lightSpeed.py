#velocity calculations
'''Specifications:
===================
Prompt user for a floating point number, representing percentage of the speed of light
your ship will travel. Your program then prints the following information:
• the weight of the ship. Assume the ship weighs 70,000 kilograms, the weight of the empty space
shuttle orbiter, when at rest.
• The times the astronauts experience for trips to:
o Alpha Centauri: 4.3 Light Years
o Barnard’s Star: 6.0 Light Years
o Betelgeuse (in the Milky Way): 309 Light Years
o Andromeda Galaxy (closest galaxy): 2,000,000 Light Years
'''
numStr = raw_input("Please enter velocity (as a percentage of speed of light): ")
print("Ship is traveling at ", numStr, "of the speed of light.")


      
floatVar = float(numStr)

shuttleWt = 70000
