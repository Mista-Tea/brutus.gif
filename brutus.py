#gif cracker written by nokocode released under wtfpl
#Do wtf ever you want with it...
import os
import subprocess
import re

#user changable variables
scriptName = '17.txt'
imageFile = 'gif4.gif'
newTextFileName = 'textDocument.txt'
#for os 0 = *nix based os 1=windows based os for install.
operatingSystem = 0
#for compression, 0 = no compression,
#1 = only compression, 
#2 = compression and no compression side by side
compressionSetting = 0

#change settings for os
if(operatingSystem == 0):
	gifShuffleRun = 'gifshuffle'
else:
	gifShuffleRun = 'gifshuffle.exe'
print gifShuffleRun

wordFile = open(scriptName, 'r')

#open file with giant word list or use wordlist to be your selection of words open('oldfile.txt', 'r') for reference
wordList = wordFile.read()
wordList = re.sub(r'\W+', ' ', wordList)
wordFile = open(scriptName, 'w')
wordFile.write(wordList)
wordFile.close()
#wordlist is the script separated by spaces. 

responseArray = []
 
wordListArray = wordList.split(" ");
wordListArrayLength = len(wordListArray)
i = 0
while(i < wordListArrayLength):
	#responses from terminal , stringResponse with -C adds compression, without does not. tries standard capitalization, all caps, all lower and how it was presented in file. 
	#normal case

	responseArray.append("\n" + str(i) + ":" + wordListArray[i] + ":" + "\n")
	if(compressionSetting != 1):
		stringResponse = subprocess.check_output([gifShuffleRun, "-p", wordListArray[i], imageFile])
		responseArray.append(stringResponse)
	if(compressionSetting >0):
		stringResponse = subprocess.check_output([gifShuffleRun, "-C", "-p", wordListArray[i], imageFile])
		responseArray.append(stringResponse)
	#uppercase
	if(compressionSetting != 1):
		stringResponse = subprocess.check_output([gifShuffleRun, "-p", wordListArray[i].upper(), imageFile])
		responseArray.append(stringResponse)
	if(compressionSetting> 0):
		stringResponse = subprocess.check_output([gifShuffleRun, "-C", "-p", wordListArray[i].upper(), imageFile])
		responseArray.append(stringResponse)
	#lowercase
	if(compressionSetting != 1):
		stringResponse = subprocess.check_output([gifShuffleRun, "-p", wordListArray[i].lower(), imageFile])
		responseArray.append(stringResponse)
	if(compressionSetting >0):
		stringResponse = subprocess.check_output([gifShuffleRun, "-C", "-p", wordListArray[i].lower(), imageFile])
		responseArray.append(stringResponse)
	#capitalize first
	if(compressionSetting != 1):
		stringResponse = subprocess.check_output([gifShuffleRun, "-p", wordListArray[i].capitalize(), imageFile])
		responseArray.append(stringResponse)
	if(compressionSetting >0):
		stringResponse = subprocess.check_output([gifShuffleRun, "-C", "-p", wordListArray[i].capitalize(), imageFile])
		responseArray.append(stringResponse)


	i += 1
#add all array items to new string
#so that new file may have all new words
newString = ''
for item in responseArray:
	newString += item + "\n"

outFile = open(newTextFileName, 'w')
outFile.write(newString)
outFile.close()