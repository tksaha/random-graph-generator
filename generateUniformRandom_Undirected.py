import os; 
import networkx as nx; 
import random; 
import sys; 
import numpy as np; 
    
    
# Concept is coming from paper title "A Markov chain monte carlo 
# method for generating random (0,1)-matrices with given marginals


# nRandom: number of random graphs to generate
def	generate_Random_Undirected (g_org,  rndSeed):
	
	g = nx.Graph(); 
	g.add_nodes_from (g_org.nodes(data=True)); 
	g.add_edges_from (g_org.edges()); 
	
	all_nodes= g.nodes(); #list of nodes
	all_edges= g.edges(); #list of edges

	#print len(all_edges); 

	npass = len(all_edges); 
	swap_counter = 0; 
	
	np.random.seed(rndSeed); 

	# a large number of times	
	for	ntimes 	in	range (0,3*npass):
		# Select two edges to swap 
		# Iterate through nodes  (n*n) for directed graphs 
		all_edges= g.edges(); #list of edges
		
		en = np.random.choice (len(all_edges), 2, replace=False); 
		
		# Before swapping whether there is an edge exist already within 
		# swap pair. Two edges: (i, j) , (k, l). 
		# after swap (i,k), (j, l) 
		
		i = all_edges[en[0]][0]; 
		j = all_edges[en[0]][1]; 


		k = all_edges[en[1]][0];
		l = all_edges[en[1]][1];

		# Ensure it's rectangular
		# We are avoiding compact alternating Hexagonal 
		# not in same row or column
		if	i==k or j==l :
			continue; 


		if	g.has_edge(i,l) or   g.has_edge(j,k):
			continue; 
		#Else remove current edge 
		#Add new edge

		# No self edge

		if	(i==l) or (j==k):
			continue; 

		# to ensure connectivity 
		#if	not(g.has_edge (i,k)) and  not(g.has_edge(j,l)):
		#	continue; 

		total_edges_prev  =  len(g.edges()); 

		g.add_edge (i,l); 
		g.add_edge (j,k); 
		
		total_edge_after_adding = len(g.edges()); 
	
		g.remove_edge(i,j); 
		g.remove_edge(k,l); 

		total_edges_now = len(g.edges()); 
		
		if	total_edges_now != total_edges_prev:
			print (total_edges_prev) 
			print (total_edge_after_adding)
			print (total_edges_now)
			print ('not equal')
		
		# check still connected or not
		if	not(nx.is_connected (g)):
			# add back edge
			# Try another change
			g.add_edge (i,j); 
			g.add_edge (k,l); 

			g.remove_edge(i,l); 
			g.remove_edge(j,k); 
			
		else:
			swap_counter = swap_counter +1; 


	print ('swap-counter:'+str(swap_counter))
	return g;
	
