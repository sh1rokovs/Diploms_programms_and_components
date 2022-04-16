import csv
from numpy import *
from scipy.fftpack import fft
import matplotlib.pyplot as plt

list_with_time = []
list_with_amp = []

with open('data1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_with_time.append(float(row['time']))
        list_with_amp.append(float(row['amp']))


print(list_with_time[-1::])
print(len(list_with_time))
print(list_with_amp)
print(len(list_with_amp))
