#! /usr/bin/python
import sys
import os


file_base="thesis"
file_base12="chapter12"
file_base3="chapter3"

private_location='~/Dropbox/thesis/full'
shared_location='~/Dropbox/thesis/thesis-chapters'
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

cmd = 'bibtex %s > bib.out' %(file_base3)
print "\t Step (1e):  executing '%s'" %(cmd)
os.system(cmd)


cmd = 'pdflatex %s.tex > compile.out' %(file_base3)
print "\t Step (1f):  executing '%s'" %(cmd)
os.system(cmd)

cmd = 'bibtex %s > bib.out' %(file_base3)
print "\t Step (1g):  executing '%s'" %(cmd)
os.system(cmd)

cmd = 'pdflatex %s.tex > compile.out' %(file_base3)
print "\t Step (1h):  executing '%s'" %(cmd)
os.system(cmd)


# COPY .tex and PDF FILES TO private location
print "\t Step (2):  copying files .tex files to '%s', '%s/%s', '%s/%s', and '%s/%s'" %(private_location,private_location,rollback_folder,private_location,pmu_folder,private_location,multicast_folder)

# base files
cmd = 'mv %s.pdf %s.pdf' %(file_base,file_base12)
print "\t\t (a) executing '%s'" %(cmd)
os.system(cmd)


# base files
cmd = 'cp *.tex %s.pdf %s.pdf %s' %(file_base12,file_base3,private_location)
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
cmd = 'cp %s.pdf %s.pdf %s' %(file_base12,file_base3,public_location)
print "\t Step (4):  executing '%s' " %(cmd)
os.system(cmd)

# COPY FINAL PDF TO public_location 
cmd = 'cp %s.pdf %s.pdf %s' %(file_base12,file_base3,shared_location)
print "\t Step (4):  executing '%s' " %(cmd)
os.system(cmd)

print "\n************************************************************************************************************************************************************************************************************** \n\n"
