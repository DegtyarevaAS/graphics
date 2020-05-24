import matplotlib
import matplotlib.pyplot as plt
import numpy as np


infile = open('input.txt')
for i in range(3):
        i = infile.readline()
text  = infile.readlines()
out = []
for i in text:
        tmp = i.split(';')
        out.append([tmp[0],tmp[2],tmp[3][:len(tmp[3])-1]])
labels = []
men_means = []
women_means = []

for i in out:
        labels.append(i[0])
        men_means.append(int(i[1]))
        women_means.append(int(i[2]))

x = np.arange(len(labels))  # the label locations
width = 0.5
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_ylabel('Численность')
ax.set_title('Распределение по возрастам и полу')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()