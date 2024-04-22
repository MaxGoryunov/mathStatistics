import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import math

def Normal(n):
    return np.random.normal(0, 1, n)

def Cauchy(n):
    return np.random.standard_cauchy(n)

def Student(n):
    return np.random.standard_t(3, n)

def Poisson(n):
    return np.random.poisson(10, n)

def Uni(n):
    return np.random.uniform(-math.sqrt(3), math.sqrt(3), n)

def drawPlots(label, func, bound):
    figure, axes = plt.subplots(1, 3, figsize=(20, 10))
    for index, count in enumerate(ns):
        # print("here")
        values = func(count)
        sbn.histplot(values, ax=axes[index], stat='density', kde=True, bins=min(count//2, 10))
        axes[index].set_xlabel('Values')
        axes[index].set_title(f'N = {count}')
    figure.savefig(f'{label}.jpg')

ns = np.array([10, 50, 1000])

label = 'Normal_distribution'
func = Normal
bound = [-5, 5]
drawPlots(label, func, bound)

label = 'Cauchy_distribution'
func = Cauchy
bound = [-5, 5]
drawPlots(label, func, bound)

label = 'Student_distribution'
func = Student
bound = [-5, 5]
drawPlots(label, func, bound)

label = 'Poison_distribution'
func = Poisson
bound = [-20, 20]
drawPlots(label, func, bound)

label = 'Uniform_distribution'
func = Uni
bound = [-5, 5]
drawPlots(label, func, bound)


np.random.poisson(1, 2)