#gif cracker written by nokocode released under wtfpl
#Do wtf ever you want with it...
import os
import subprocess

#imageFile must be in current directory, feel free to change this. 
imageFile = 'gif1.gif'
#wordlist is the script separated by spaces. 
wordList = "Velvet Sullivans lost the reservations for our office party, because the person who took the reservation had been fired. There were 200 of us, the entire department. Chief started yelling but the hostess held firm and explained that the whole bar and grill was booked for a banks St. Patrick's Day party. Back on the bus Chief yelled. Back on the bus and in the cars I was seated next to Henry (Or Henri) in the first row. Chief was perched next to the driver, guiding him at sub-5 miles per hour speeds up La cienaga in a brute-force search for any establishment with sufficient capacity.The bus was the bloated payload of the convoy, surrounded by a swarm of employee cars that blocked lanes while passengers deboarded and sprinted through traffic to check the wait time at every possible restaurant for a party of 200. Angry commuters began to hold down horns in a continuous atonal scream. Like a battleship squeezing through a canal, the bus and it's attended motorcadeplugged the street from edge to edge, pushing northward relentlessly at 1 mile per hour to avoid any number of fines we might be subject to if we halted even for a second.In a desperate bid to avoid our vile parade, trailing cars spilled into oncoming lanes, attempting illegal u-turns and side-swiping south-bound traffic, leaving an impassible battlefield of accidents and insurance disputes in our wake. Our fastest scout cars fanned out into side streets, checking with two or three restaurants. Then accelerating to rejoin the convoy at the next intersection.At some point in the melee Chief had locked the driver in the bus's bathroom, and taken the wheel himself. Debra, one of the scouts, pulled up alongside us and shouted that the Mexican place two blocks up had a ballroom with 150 person capacity. It wasn't perfect, but it would have to do. Chief floored it to edge out a rival bus of German tourists and shot onto the winding entrance ramp of a parking structure.Still in hot pursuit, willfully blind to signage-bar in trucks and busses, he held his speed and began to recite the regulators code in clenched teeth.we heard the scream of tearing metal as both sides of the bus scraped against the ramps curved walls, emitting a shower of orange sparks until it was physically impossible for the bus to advance. With the door wedged shut against the wall and the roofs emergency exit a foot below the ceiling, we had no choice but to clamber out through half-lowered windows. The trailing throng of employee cars was suffocatingly close behind and unable to reverse, forcing drivers to abandon their vehicles on the ramp. By the time we made it to the restaurant the German tourists had claimed the ballroom. We ordered 400 tacos to go, and ate them mournfully.Something is going to happen in 18 days."
responseArray = []
 
wordListArray = wordList.split(" ");
wordListArrayLength = len(wordListArray)
i = 0
while(i < wordListArrayLength):
	#for windows change gifshuffle to gifshuffle.exe, for unix leave as gifshuffle
	stringResponse = subprocess.check_output(["gifshuffle", "-C", "-p", wordListArray[i], imageFile])
	print(stringResponse)
	if(stringResponse != "Warning: residual of 4 bits not uncompressed"):
		responseArray.append(stringResponse)
	i += 1

print "\n"
print "\n"
newString = ''
for item in responseArray:
	newString += item + "\n"

print newString
print len(newString)
outFile = open('textDocument.txt', 'w')
outFile.write(newString)
outFile.close()