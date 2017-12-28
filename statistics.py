import sys
import math
from collections import Counter
N= int(input())
x=[int(input()) for i in range(int(N))]


def myMean(x, N):
	mean = float(sum(x)) / N
	mean_rounded = round(mean, 1)
	return(mean_rounded)

def myMedian(x, N):
	x.sort()
	if (N % 2) == 0:
		top = (N//2)
		bot = top - 1
		median = float((x[top] + x[bot])) / 2
	else:
		middle = (N/2)
		median = x[middle]
	median_rounded = round(median, 1)
	return(median_rounded)

def myMode(x, N):
	same = [(x.count(i)) for i in set(x)]
	counts = [(i, x.count(i)) for i in set(x)]
	possible_modes = list()
	for num, count in counts:
		if count == max(same):
			possible_modes.append(num)
	mode = min(possible_modes)
	return(mode)

def myStdDev(x, N):
	m = float(sum(x)) / N
	sd_i = list()
	for i in x:
		sd_i.append(math.pow((i-m), 2))
	sd = math.sqrt((sum(sd_i) / N))
	sd_rounded = round(sd, 1)
	return(sd_rounded)

def myConfidenceInterval(x, N):
	m = float(sum(x)) / N
	sd_i = list()
	for i in x:
		sd_i.append(math.pow((i-m), 2))
	sd = math.sqrt((sum(sd_i) / N))
	sigma_m = sd / math.sqrt(N)
	upper = m + (1.96) * (sigma_m)
	lower = m - (1.96) * (sigma_m)
	upper_rounded = round(upper, 1)
	lower_rounded = round(lower, 1)
	printstr = str(lower_rounded) + " " + str(upper_rounded)
	return(printstr)

# Convert results into strings and add line break
print_mean = str(myMean(x, N)) + "\n"
print_median = str(myMedian(x, N)) + "\n"
print_mode = str(myMode(x, N)) + "\n"
print_stddev = str(myStdDev(x, N)) + "\n"
print_confidenceinterval = str(myConfidenceInterval(x, N)) + "\n"

# Output arguments using stdout
sys.stdout.write(print_mean)
sys.stdout.write(print_median)
sys.stdout.write(print_mode)
sys.stdout.write(print_stddev)
sys.stdout.write(print_confidenceinterval)
