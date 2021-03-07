# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:26:20 2019

@author: andreas
"""

import networkx as nx

G = nx.DiGraph()


G.add_node(1, value=0.2)
G.add_node(2, value=0.6)
G.add_node(3, value=0.4)



nx.draw_networkx(G)

