#!/usr/bin/env python


import glob
import os 
import numpy as np 
import librosa
import fnmatch

folder_path = "/Users/siddharthagrawal/Desktop/deep_learning/Assignment_3/Code/train/dr1/fecd0"
wav_file_array = []
wrd_file_array = []
encoded_wav_samples = {}
os.chdir(folder_path)

for file in glob.glob("*.wav"):
	wav_file_array.append(file)


for file in glob.glob("*.wrd"):
	os.rename(file,  file +'.txt')
	
for file in glob.glob("*.wrd.txt"):
	#print file
	wrd_file_array.append(file)


for file in wav_file_array:
	y, sr = librosa.load(file, sr=16000)
	for wrd_file in wrd_file_array:
		#print wrd_file
		a = wrd_file.split('.')
		b = file.split('.')
		if a[0] == b[0]:
			print "found file"
			with open(wrd_file) as f:
			    word_boundaries = []
			    for line in f:
			        a = line.split( )
			        word_boundaries.append(int(a[0]))
			        word_boundaries.append(int(a[1]))

			encoded_wav_samples[file] = (y,word_boundaries)
			break



print encoded_wav_samples












