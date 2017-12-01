import random
import matplotlib.pyplot as plt

year = set()
years = []

for i in range(5001):
    years.append(random.randint(0,100))
year = set(years)
d = {}
for i in years:
    if i not in d.keys():
        d[i] = 1;
    else:
        d[i] += 1;

x = []
y = []
for i in d.keys():
    x.append(i);
    y.append(d[i]);
plt.hist(years)
plt.show()
print(d)