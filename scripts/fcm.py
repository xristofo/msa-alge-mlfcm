"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
author:     andreas c. 
            xristofo@gmail.com
updated:    21/5/2017
description:Fuzzy Cognitive Maps implementation class 

function sigmoid(x, lamda)
    description:
        threshold function, keeps activation level in range [0..1] 
    input : 
        x: float number in range [-1..1]  
        lamda: lamda factor [0..10]        
    return : float number in range [0..1] 

function fcm_alg(WW, Al, Iterations)
    description: fcm algorithm implementation
    input : 
        WW: nxn matrix that keeps weight values(float) in range [-1..1]  
        Al: 1xn vector that keeps initial activation levels (float) [0..1]        
        Iterations: (Integer) number of iterations 
    return : 
        ALs: iterations x n (integer), keeps activation level values
            along iterations
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import numpy as np
import networkx as nx

class fcm_class:
    
    def fcm_from_matrix_to_graph(WW, Al, depth, Iters):
        "Create a graph based on a given matrix"    
        G = nx.DiGraph(depth=depth)
        n = WW.shape[0]

        for k in range(0,n):
            G.add_node(k, {"value":[0]*Iters, "link":Al[k][1], "color":Al[k][2]})
            G.node[k]['value'][0]=round(Al[k][0],5)
     
        for i in range(0,n):
            for j in range(0,n):
                if (WW[i][j] != 0): G.add_edge(i,j,weight= round(WW[i][j],5))
                #if (WW[i][j] != 0): G.add_edge(i,j)
                
        return G

#    def fcm_alg_graph(G_List, G_index, Start_Iter, End_Iter, l):
#        
#        G = G_List[G_index]
#        
#        for g in range(Start_Iter,End_Iter):
#            #for each iteration
#            for node in G:
#                #for each node in the graph
#
#                if G.node[node]['link']>0:
#                    Linked_G_Index = int(G.node[node]['link'])
#                    G_List[Linked_G_Index].node[0]['value'][g-1]=G.node[node]['value'][g-1]
#                    G_List = fcm_class.fcm_alg_graph(G_List,Linked_G_Index, g, g+1, l)
#                    G.node[node]['value'][g-1] = G_List[Linked_G_Index].node[0]['value'][g]
#                    
#                SumIn = 0
#                for edge in G.in_edges(node):
#                    #for each incoming edge
#                    x,y = edge
#                    if g==1:
#                        Alold = 0
#                    else:
#                        Alold = G.node[x]['value'][g-2]
#                        
#                    Alnew = G.node[x]['value'][g-1]
#                    
#                    DAl = Alnew - Alold
#                    SumIn = SumIn+ (G[x][y]['weight'] * DAl)
#                    
#                Ai = G.node[node]['value'][g-1]
#                
#                if Ai!=0:
#                    Ai = (np.log((1-Ai)/Ai))/-l
#                else:
#                    Ai = 0
#                
#                x = (1*SumIn+0.5*Ai)/1.5
#                
#                if SumIn==0:
#                    newAl = G.node[node]['value'][g-1]
#                else:
#                    newAl = round(fcm_class.sigmoid(x,l),5)
#                    
#                G.node[node]['value'].append(newAl)
#        G_List[G_index] = G      
#        return G_List    
    
    def aa_fcm_alg_graph(G_List, G_index, Start_Iter, End_Iter, l):
            
            G = G_List[G_index]
            
            for g in range(Start_Iter,End_Iter):
                #for each iteration
                for node in G:
                    #for each node in the graph
    
                    if G.node[node]['link']>0:
                        Linked_G_Index = int(G.node[node]['link'])
                        G_List[Linked_G_Index].node[0]['value'][g-1]=G.node[node]['value'][g-1]
                        G_List = fcm_class.aa_fcm_alg_graph(G_List,Linked_G_Index, g, g+1, l)
                        G.node[node]['value'][g-1] = G_List[Linked_G_Index].node[0]['value'][g]
                        
                    SumIn = 0
                    for edge in G.in_edges(node):
                        #for each incoming edge
                        x,y = edge
                        if g==1:
                            Alold = 0
                        else:
                            Alold = G.node[x]['value'][g-2]
                        
                        Alnew = G.node[x]['value'][g-1]
                    
                        DAl = (Alnew - Alold)
                        
                        SumIn = SumIn+ (G[x][y]['weight'] * DAl)
                    
                    Ai = G.node[node]['value'][g-1]
                
                    if Ai!=0:
                        Ai = (np.log((1-Ai)/Ai))/-l
                    else:
                        Ai = 0
                    
                    infactor = 1.2
                    x = infactor*SumIn + Ai
#                    x = (1*SumIn+1.2*Ai)/2.2
                    
                    if SumIn==0:
                        newAl = G.node[node]['value'][g-1]
                    else:
                        newAl = round(fcm_class.sigmoid(x,l),5)
                    
                    G.node[node]['value'][g]=newAl
                    
            G_List[G_index] = G      
            return G_List    
        
    def pi_fcm_alg_graph(G_List, G_index, Start_Iter, End_Iter, l):
            
            G = G_List[G_index]
            
            for g in range(Start_Iter,End_Iter):
                #for each iteration
                for node in G:
                    #for each node in the graph
    
                    if G.node[node]['link']>0:
                        Linked_G_Index = int(G.node[node]['link'])
                        G_List[Linked_G_Index].node[0]['value'][g-1]=G.node[node]['value'][g-1]
                        G_List = fcm_class.aafcm_alg_graph(G_List,Linked_G_Index, g, g+1, l)
                        G.node[node]['value'][g-1] = G_List[Linked_G_Index].node[0]['value'][g]
                        
                    SumIn = 0
                    for edge in G.in_edges(node):
                        #for each incoming edge
                        x,y = edge
                       
                        
                        Alnew = G.node[x]['value'][g-1]
                    
                        SumIn = SumIn+ (G[x][y]['weight'] * (2*Alnew-1))
                    
                    Ai = G.node[node]['value'][g-1]
                
                    
                    x = SumIn + (2*Ai-1)
#                    x = (0.5*SumIn+1*Ai)/1.5
                    
                    if SumIn==0:
                        newAl = G.node[node]['value'][g-1]
                    else:
                        newAl = round(fcm_class.sigmoid(x,l),5)
                    
                    G.node[node]['value'][g]=newAl
                    
            G_List[G_index] = G      
            return G_List 

#    def acfcm_alg_graph(G_List, G_index, Start_Iter, End_Iter, l):
#            
#            G = G_List[G_index]
#            
#            for g in range(Start_Iter,End_Iter):
#                #for each iteration
#                for node in G:
#                    #for each node in the graph
#    
#                    if G.node[node]['link']>0:
#                        Linked_G_Index = int(G.node[node]['link'])
#                        G_List[Linked_G_Index].node[0]['value'][g-1]=G.node[node]['value'][g-1]
#                        G_List = fcm_class.acfcm_alg_graph(G_List,Linked_G_Index, g, g+1, l)
#                        G.node[node]['value'][g-1] = G_List[Linked_G_Index].node[0]['value'][g]
#                        
#                    SumIn = 0
#                    for edge in G.in_edges(node):
#                        #for each incoming edge
#                        x,y = edge
#                        if g==1:
#                            Alold = 0
#                        else:
#                            Alold = G.node[x]['value'][g-2]
#                        
#                        Alnew = G.node[x]['value'][g-1]
#                    
#                        DAl = Alnew #- Alold)
#                        
#                        SumIn = SumIn+ (G[x][y]['weight'] * DAl)
#                    
#                    Ai = G.node[node]['value'][g-1]
#                
#                    Si = round(fcm_class.sigmoid(SumIn,l),5)
#                
#                    newAl = (Si+Ai)/2
#                    
#                                        
#                    G.node[node]['value'][g]=newAl
#                    
#            G_List[G_index] = G      
#            return G_List    
#
#    def cnfcm_alg_graph(G_List, G_index, Start_Iter, End_Iter, l):
#            
#            G = G_List[G_index]
#            Di = 0.1
#            
#            for g in range(Start_Iter,End_Iter):
#                #for each iteration
#                for node in G:
#                    #for each node in the graph
#    
#                    if G.node[node]['link']>0:
#                        Linked_G_Index = int(G.node[node]['link'])
#                        G_List[Linked_G_Index].node[0]['value'][g-1]=G.node[node]['value'][g-1]
#                        G_List = fcm_class.cnfcm_alg_graph(G_List,Linked_G_Index, g, g+1, l)
#                        G.node[node]['value'][g-1] = G_List[Linked_G_Index].node[0]['value'][g]
#                        
#                    SumIn = 0
#                    for edge in G.in_edges(node):
#                        #for each incoming edge
#                        x,y = edge
#                        Alnew = G.node[x]['value'][g-1]
#                        SumIn = SumIn+ (G[x][y]['weight'] * Alnew)
#                        
#                    Ai = G.node[node]['value'][g-1]
#                    
#                    if ((SumIn >= 0) and (Ai >= 0)):
#                        fm = Ai + SumIn - (SumIn*Ai)
#                    elif (SumIn<0) and (Ai<0) and (abs(Ai)<=1) and (abs(SumIn)<=1):
#                        fm = Ai + SumIn + (SumIn * Ai)
#                    elif ((Ai==1) and (SumIn==-1)) or ((Ai==-1 and SumIn==1)):
#                        fm = (Ai+SumIn) / (1- min(Ai,SumIn))
#                    else:
#                        fm = (Ai+SumIn)/(1-min(abs(Ai),abs(SumIn)))
#                        
#                    newAl = fm - Di*Ai
#                    
#                    if newAl>1:
#                        newAl=1
#                    if newAl<-1:
#                        newAl=-1
#                    try:
#                        G.node[node]['value'][g]=newAl
#                    except:
#                        print(str(g))
#                        
#                    
#            G_List[G_index] = G      
#            return G_List    
#    

        
    def sigmoid(x, lamda):
        
        return  1/(1+math.exp(-lamda*x))
    
        
    def fcm_alg(WW, Al, Iterations):
        
        finalALs = np.zeros((Al.shape[0],Iterations))
        lamda = 1
        n = WW.shape[0]
        Alold = np.zeros(n,float)
        finalALs[:,0]=Al
        
        for g in range(1,Iterations):
            Alnew = np.copy(finalALs[:,g-1])
            
            Alold[:] = finalALs[:,g-2]
            
            
            for j in range(0,n):
                Ai = 0
                Si = 0
                SumIn = 0

                for i in range(0,n):
                    DAl = (Alnew[i]-Alold[i])
#                    DAl = min(DAl,Alnew[i])
#                    DAl = Alnew[i]
                    SumIn = WW[i,j]*DAl
                    Si = Si + SumIn
                
                if Alnew[j]!=0:
                    Ai = Alnew[j]#(np.log((1-Alnew[j])/Alnew[j]))/-lamda
                else:
                    Ai = 0
                
                x = Si+(Ai)
                
                if Si==0:
                    finalALs[j,g] = Alnew[j] 
                else:
                    finalALs[j,g] = round(fcm_class.sigmoid(x,lamda),5)
                    
        return (finalALs)
    
#    def fcm_alg1(WW, Al, Iterations):
#        
#        finalALs = np.zeros((Al.shape[0],Iterations))
#        lamda = 1
#        n = WW.shape[0]
#        Alold = np.zeros(n,float)
#        finalALs[:,0]=Al
#        
#        for g in range(1,Iterations):
#            Alnew = np.copy(finalALs[:,g-1])
#            
#            Alold[:] = finalALs[:,g-2]
#            
#            
#            for j in range(0,n):
#                Ai = 0
#                SumIn = 0
#                SumWeight = 0 
#
#
#                for i in range(0,n):
##                    DAl = Alnew[i]
#                    DAl = (Alnew[i]-Alold[i])
#                    SumIn = SumIn + WW[i,j]*DAl
#                    SumWeight = SumWeight+WW[i,j]
#                
##                Ai = Alnew[j]
#                if Alnew[j]!=0:
#                    Ai = (np.log((1-Alnew[j])/Alnew[j]))/-lamda
#                else:
#                    Ai = 0
#                
#                x = Ai+(SumIn/abs(SumWeight))
#                
#                if SumIn==0:
#                    finalALs[j,g] = Alnew[j] 
#                else:
#                    finalALs[j,g] = round(fcm_class.sigmoid(x,lamda),5)
#                    
#        return (finalALs)