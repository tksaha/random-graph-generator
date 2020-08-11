import os; 
import sys; 
import networkx as nx; 
import numpy as np; 
from generateUniformRandom_Undirected import *; 

# numer of random copies 
# @Param 2
nRandom  = int (sys.argv[2]); 


common_file_name = sys.argv[1][ :sys.argv[1].rfind(".")];
# generate nRandom copies of  writer file 
write_files = []; 

for	nrandom	in	range(0,nRandom):
	dirname = 'output/'
	filename = dirname + common_file_name + 'random_'+ str(nrandom)+'.txt' 
	if	not(os.path.exists(dirname)):
		os.mkdir(dirname)		
	file_ = open (filename,'w')	
	write_files.append(file_) 

print (write_files)

def	generate_random_graph_and_write (g,graph_id_processing,id_of_file_write):
	#print g.nodes(); 
	#print g.edges(); 
	
	gx_prev = nx.Graph(); 
	gx_prev.add_nodes_from(g.nodes(data=True)); 
	gx_prev.add_edges_from(g.edges()); 

	uniq_graph_counter = 0; 
	#print gx_prev.edges(); 
	
	while	True:
		rnd_int = np.random.randint(10000,size=1);
		gx_new = generate_Random_Undirected (gx_prev,rnd_int[0]);

		if	len(gx_new.edges()) >0:
			gx_prev = nx.Graph(); 
			gx_prev.add_nodes_from(gx_new.nodes(data=True)); 
			gx_prev.add_edges_from(gx_new.edges());
		
			uniq_graph_counter = uniq_graph_counter +1; 
			id_of_file_write = id_of_file_write +1; 	
			
			write_files[id_of_file_write].write('t'+' '+'#'+' '+ str(graph_id_processing)+os.linesep);
			for	nodes	in	gx_new.nodes(data=True):
				write_files[id_of_file_write].write('v'+' '+str(nodes[0])+' '+str(gx_new.nodes[nodes[0]]['label'])+os.linesep);

			for	edges	in	gx_new.edges():
				write_files[id_of_file_write].write('e'+' '+str(edges[0])+' '+str(edges[1])+' '+'1'+os.linesep); 

			write_files[id_of_file_write].flush(); 	

		#print uniq_graph_counter;
		if	uniq_graph_counter ==nRandom: 
			break; 
		


	#print uniq_graph_counter; 



def	read_graph_and_generate_random_graph (graph_file_name): 

	graph_id_processing = 0; 
	g = nx.Graph(); 

	for	line	in	graph_file_name: 
		line_elems = line.strip().split(" "); 
		#print line_elems; 
		if	line_elems[0]=='t':
			if	graph_id_processing >= 1:
				generate_random_graph_and_write (g,graph_id_processing,-1); 
				
			g = nx.Graph(); 
			graph_id_processing = graph_id_processing +1; 

		if	line_elems[0] =='v': 
			g.add_node(int(line_elems[1]),label=int(line_elems[2]));
		if	line_elems[0]=='e':
			g.add_edge(int(line_elems[1]), int(line_elems[2])); 

	# For the very last graph
	generate_random_graph_and_write (g,graph_id_processing,-1); 

		
	
file_name = open (sys.argv[1]); 
read_graph_and_generate_random_graph(file_name); 
			
			
