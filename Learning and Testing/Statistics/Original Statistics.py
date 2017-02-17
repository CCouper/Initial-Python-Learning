import statistics

exampleList = [1,2,3,4,5,6,7,8,9,10]

#At least mean and standard deviation are built into python 3 in
#the statistics module

x=statistics.mean(exampleList)
y=statistics.stdev(exampleList)
print("The mean is ",x," and the standard deviation is ",y,".")
