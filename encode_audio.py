#!/usr/bin/env python

import numpy as np 
import librosa
import os
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error



class Encoder(object):
	def __init__(self):
		self.audio_file = '/Users/siddharthagrawal/Desktop/deep_learning/Assignment_3/Code/train/dr1/fecd0/sa1.wav'
		self.y, self.sr = librosa.load(self.audio_file, sr=16000)
		#self.resampled = librosa.resample(self.y, self.sr, 16000)
		print self.y, self.sr

		


	def encode(self):

		print self.sr
		print self.y
		
		
		#print y, sr

















if __name__ == '__main__':
	encoder = Encoder()
	#encoder.encode()