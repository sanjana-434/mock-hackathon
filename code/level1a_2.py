# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level1a.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
dist.append([0])
res = data['restaurants']['r0']['neighbourhood_distance']
dist[0].extend(res)
for i in range(0,n):
    dist.append([res[i]])
    dist[i+1].extend(data['neighbourhoods']['n'+str(i)]['distances'])
print(len(dist))

# for i in dist:
#     print(i)
order_quantity = []
for i in range(0,n):
    order_quantity.append(data['neighbourhoods']['n'+str(i)]['order_quantity'])
# print(order_quantity)
# print(sum(order_quantity))

capacities = data['vehicles']['v0']['capacity']
# print(capacity)
f.close()


def printknapSack(W, wt, val, n, vis,path):
	K = [[0 for w in range(W + 1)]
			for i in range(n + 1)]
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w and vis[i-1] == 0:
				K[i][w] = max(val[i - 1] 
				+ K[i - 1][w - wt[i - 1]],
							K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]
	res = K[n][W]
	# print(res)
	w = W
	for i in range(n, 0, -1):
		if res <= 0:
			break

		if res == K[i - 1][w]:
			continue
		else:
			vis[i-1] = 1
			path.append(i - 1)
			res = res - val[i - 1]
			w = w - wt[i - 1]

val = []
for i in range(0,n):
	val.append(1)
wt = order_quantity
W = capacities
n = len(val)
vis = []
for i in range(0,n):
	vis.append(0)
print(len(vis))
final_answer = []
while(True):
    path = []
    printknapSack(W, wt, val, n,vis,path)
    final_answer.append(path)
	
    print(path)
    if all(element == 1 for element in vis):
        break
	
print(final_answer)

for i in range(0,len(final_answer)):
    for j in range(0,len(final_answer[i])):
        final_answer[i][j] = 'n'+str(final_answer[i][j])
print(final_answer)

d = {}
for i in range(1,len(final_answer)+1):
	d["path"+str(i)] = ["r0"]
	d["path"+str(i)].extend(final_answer[i-1])
	d["path"+str(i)].append("r0")

dictionary = {"v0": d}
print(dictionary)

json_object = json.dumps(dictionary, indent=4)
 
with open("C:/work-shop/output/level1a_output.json", "w") as outfile:
    outfile.write(json_object)
	


