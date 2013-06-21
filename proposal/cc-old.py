#! /usr/bin/python
import sys
import os


file_base="thesis-proposal"
private_location='~/Dropbox/thesis/proposal'
public_location='~/Dropbox/Public/thesis'
rollback_folder="rollback"
pmu_folder="pmu"
multicast_folder = "multicast"


 
print "\n\n************************************************************************************************************************************************************************************************************** \n"

cmd = 'bibtex %s > bib.out' %(file_base)
print "\t Step (1a):  executing '%s'" %(cmd)
os.system(cmd)


cmd = 'pdflatex %s.tex > compile.out' %(file_base)
print "\t Step (1b):  executing '%s'" %(cmd)
os.system(cmd)

cmd = 'bibtex %s > bib.out' %(file_base)
print "\t Step (1c):  executing '%s'" %(cmd)
os.system(cmd)

cmd = 'pdflatex %s.tex > compile.out' %(file_base)
print "\t Step (1d):  executing '%s'" %(cmd)
os.system(cmd)



# COPY .tex and PDF FILES TO private location
print "\t Step (2):  copying files .tex files to '%s', '%s/%s', '%s/%s', and '%s/%s'" %(private_location,private_location,rollback_folder,private_location,pmu_folder,private_location,multicast_folder)

# base files
cmd = 'cp *.tex %s.pdf %s' %(file_base,private_location)
print "\t\t (a) executing '%s'" %(cmd)
os.system(cmd)

# rollback files
cmd = 'cp %s/*.tex %s/%s' %(rollback_folder,private_location,rollback_folder)
print "\t\t (b) executing '%s'" %(cmd)
os.system(cmd)

# pmu files
cmd = 'cp %s/*.tex %s/%s' %(pmu_folder,private_location,pmu_folder)
print "\t\t (c) executing '%s'" %(cmd)
os.system(cmd)

# multicast files
cmd = 'cp %s/*.tex %s/%s' %(multicast_folder,private_location,multicast_folder)
print "\t\t (d) executing '%s'" %(cmd)
os.system(cmd)


# COPY FIGS TO private location
if len(sys.argv) == 1: # if no command line arguments, then copy figs to dropbox
	print "\t Step (3):  copying figures to %s " %(private_location)
	
	cmd = 'cp figs/*.pdf %s/figs' %(private_location)
	os.system(cmd)

	print "\t\t (a) ran command '%s' " %(cmd)
	cmd = 'cp figs/src/*.graffle  %s/figs/src'  %(private_location)
	print "\t\t (b) ran command '%s' " %(cmd)
	os.system(cmd)

else: # else (if any comand line argument, then don't copy figs to dropbox
	print "\t Step (3):  SKIPPED copying figures to %s" %(private_location)


# COPY FINAL PDF TO public_location 
cmd = 'cp %s.pdf %s' %(file_base,public_location)
print "\t Step (4):  executing '%s' " %(cmd)
os.system(cmd)



print "\n************************************************************************************************************************************************************************************************************** \n\n"
