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


def greedy(node,graph,order,cap,vis,c,path,index,ans):
    while(True):
        dict_ = {}
        idx = 0
        print(graph[node])
        for j in graph[node]:
            dict_[j] = idx
            idx+=1
        
        myKeys = list(dict_.keys())
        myKeys.sort()
        dict_ = {i: dict_[i] for i in myKeys}
        print(dict_)
        flag = 0
        for key, value in dict_.items():
            if (key!=value):
                if (vis[value-1]==0 and c+order[value-1] <= cap):
                    flag = 1
                    vis[value-1] = 1
                    path.append(value)
                    ans.append(index[value-1])
                    c += order[value-1]
        if (flag == 0):
            break
        node = value
    return path,ans


adjacency_matrix = np.array(dist)
index = []
n = 20
for i in range(1,n+1):
    index.append(i)
total_vis = []
vis = []
for i in range(0,len(order_quantity)):
    vis.append(0)
    total_vis.append(0)

final_answer = []
while(len(adjacency_matrix) != 1):
    path,ans = greedy(0,adjacency_matrix,order_quantity,capacities,vis,0,[],index,[0,])
    print(path,ans)
    for i in ans:
        if (i!=0):
            index.remove(i)
    path = sorted(path)
    path.reverse()
    for i in path:
        adjacency_matrix = np.delete(adjacency_matrix, i, axis=0) 
        adjacency_matrix = np.delete(adjacency_matrix, i, axis=1)
        order_quantity.pop(i-1)
        vis.pop(i-1)
    ans.append(0)
    final_answer.append(ans)
    print(ans)

print(final_answer)
for i in range(0,len(final_answer)):
    final_answer[i][0] = 'r0'
    for j in range(1,len(final_answer[i])-1):
        final_answer[i][j] -= 1
        final_answer[i][j] = 'n'+str(final_answer[i][j])
    final_answer[i][-1] = 'r0'
print(final_answer)



dictionary = {"v0": {"path1": final_answer[0],"path2":final_answer[1],"path3":final_answer[2]}}
print(dictionary)

json_object = json.dumps(dictionary, indent=4)
 

with open("C:/work-shop/output/level1a_output.json", "w") as outfile:
    outfile.write(json_object)
