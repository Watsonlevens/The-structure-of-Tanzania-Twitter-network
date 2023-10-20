#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:17:13 2021

@author: watsonlevens
"""
import networkx as nx
import random
import numpy as np

N = 1514435 # Network size # population size
n_p = 1 # Number of parent nodes
n_q = 40 # Number of neighbours
q = 1 # Probability of a new node to attach to neighbouring nodes
m0 = n_p + n_q + 1 # Initial number of edges
Gi=nx.empty_graph(create_using=nx.DiGraph())  # Initial empty graph
# A function returning an initial friend of friend network
def initial_Friend_of_a_friend_model(Gi,m0):   #Initial graph
    Initial_Nodes = np.random.permutation(m0) # List of initial nodes 
    for node1 in Initial_Nodes: # Make n_p + n_q connections
        for node2 in Initial_Nodes:
            if node1 != node2: # Avoid self loop
                Gi.add_edge(node1, node2) # Add edge 
    return Gi
     
   
def Friend_of_a_friend_model(G,N,m0):                
    for source in range(m0, N): # Start connection from m0 node and stop at N
        #################################################################################################################                    
        # Step1. Pick one node randomly and make connection.
        # ########################################################################################################################                                                           
        nodes = [nod for nod in G.nodes()]
        node = random.choice(nodes)

        neighbours = [nbr for nbr in G.neighbors(node) # neighborhoods are nodes followed by target
                                    if not G.has_edge(source, nbr) # If no edge btn source node and nbr node (followed node)
                                    and not nbr == source] # If neighbor node is not equal to source node       
        G.add_node(source) ## Adding node to the network # SOURCE MUST BE ADDED AFTER RANDOM SAMPLING SO AS 
                           ## TO AVOID SELF LOOP WHEN ADDING EDGES
        G.add_edge(source, node) # Add edge 
    
        #################################################################################################################                    
        # Step2. Pick n_q nodes randomly and with prob q, make connection.
        # ########################################################################################################################                                                                               
        num_nbrs =0
        while num_nbrs<n_q and len(neighbours)>0: 
            nbr = neighbours.pop(random.randrange(len(neighbours))) # Choose randomly among the many nbrs available
            if q >random.random():  
               G.add_edge(source, nbr) # Add edge 
               num_nbrs = num_nbrs + 1
    return G 

