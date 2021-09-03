
from collections import Counter
import plotly.figure_factory as go
import plotly.graph_objects as ff
import statistics
import random
import pandas as pd
import csv


df=pd.read_csv("c110data.csv")
data=df["temp"]. tolist()

population_mean = statistics.mean(data)
population_std = statistics.stdev(data)

print("mean ==> ",population_mean)
print("std==> ",population_std)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



def show_fig(mean_list):
 df = mean_list
 mean = statistics.mean(mean_list)
 print("mean =>", mean)

 fig = ff.create_distplot([df],["temp"],show_hist = False)
 fig.add_trace(go.Scattter(x=[mean,mean],y=[0,1],mode ="lines",mean=mean)
 fig.show()


def setup():
  mean_list=[]
  for i in range (0,100):
      set_of_means = random_set_of_means(100)
      mean_list.append(set_of_means)

      show_fig(mean_list)

setup()   



]