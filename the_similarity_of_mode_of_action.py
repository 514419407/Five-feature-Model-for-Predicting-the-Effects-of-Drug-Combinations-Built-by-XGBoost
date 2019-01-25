import numpy as np
import networkx as nx
f=open(r'drug_pairs.txt')
g=open('drug_target_similar.txt','w')
for i in f:
	temp=i.split('\t')
	try:
		target1_num=len(G[temp[0]])#G is a DAG with the attributes: 'inhibit' or 'activate'
		target2_num=len(G[temp[1]])
		score=0
		weight=0
		for target1 in G[temp[0]]:#if no directional target, then except
				try:
					all_shortest_paths=list(nx.all_shortest_paths(G,source=temp[1], target=target1))
				except:
					all_shortest_paths=[]
				if all_shortest_paths:
					len_all_shortest_paths=len(all_shortest_paths)#no use
					pathscore_list_temp=[]
					for path in all_shortest_paths:
						direction_temp='activation'
						for j in range(len(path)-1):
							if G[path[j]][path[j+1]]==direction_temp:
								direction_temp='activation'
							else:
								direction_temp='inhibition'
						if direction_temp==G[temp[0]][target1]['attribute']:
							pathscore_list_temp.append(1)
						else:
							pathscore_list_temp.append(-1)
					score+=sum(pathscore_list_temp)/float(len(pathscore_list_temp))
					weight+=abs(sum(pathscore_list_temp)/float(len(pathscore_list_temp)))
					print 'haha'
		for target2 in G[temp[1]]:#if no directional target, then except
				try:
					all_shortest_paths=list(nx.all_shortest_paths(G,source=temp[0], target=target2))
				except:
					all_shortest_paths=[]
				if all_shortest_paths:
					len_all_shortest_paths=len(all_shortest_paths)#no use
					pathscore_list_temp=[]
					for path in all_shortest_paths:
						direction_temp='activation'
						for j in range(len(path)-1):
							if G[path[j]][path[j+1]]==direction_temp:
								direction_temp='activation'
							else:
								direction_temp='inhibition'
						if direction_temp==G[temp[1]][target2]['attribute']:
							pathscore_list_temp.append(1)
						else:
							pathscore_list_temp.append(-1)
					score+=sum(pathscore_list_temp)/float(len(pathscore_list_temp))
					weight+=abs(sum(pathscore_list_temp)/float(len(pathscore_list_temp)))
					print 'hehe'
		g.write(temp[0]+'\t'+temp[1]+'\t'+str(score/weight)+'\n')
	except:
		g.write(temp[0]+'\t'+temp[1]+'\t'+'\n')

g.close()
