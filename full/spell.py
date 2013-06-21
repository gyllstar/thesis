#! /usr/bin/python
import sys
import os


#file_base="thesis-proposal"
#private_location='~/Dropbox/thesis/proposal'
#public_location='~/Dropbox/Public/thesis'
rollback_folder="rollback"
pmu_folder="pmu"
multicast_folder = "multicast"
folderList = list()
folderList.append(rollback_folder)
folderList.append(pmu_folder)
folderList.append(multicast_folder)


 
print "\n\n********************************************************************************************************************************************************************************************************** "

for folder in folderList:
	print "\n \t spell checking %s/*.tex files" %(folder)
	for file in os.listdir(folder):
		if file.endswith(".tex"):
			cmd = 'aspell -c %s/%s' %(folder,file)
			os.system(cmd)

print "\n\n*********************************************************************************************************************************************************************************************************** \n"

#for file in os.listdir(rollback_folder):
#	if file.endswith(".tex"):
#		cmd = 'aspell -c %s/%s' %(rollback_folder,file)
#		os.system(cmd)



#cmd = 'bibtex %s > bib.out' %(file_base)
#print "\t Step (1a):  executing '%s'" %(cmd)
#os.system(cmd)

