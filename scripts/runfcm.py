"""

@author: andreas

Test file that shows how fcm class can be used 

"""
import fcm
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


No_of_FCMs = 1
lambda_value = 1
Iterations = 25
results = []

for case in range(0,1):
    
    G_List = []
    
    for q in range(0,No_of_FCMs):
        # for each subFCM 
        
        #get weights and activation levels from csv files 
        ww = np.genfromtxt('../foivos/ww.csv',delimiter=',')
        al = np.genfromtxt('../foivos/random.csv',delimiter=',')
        
#        ww = np.genfromtxt('../mlfcmdata/betologic/ww_fcm'+str(q+1)+'.csv',delimiter=',')
#        al = np.genfromtxt('../mlfcmdata/betologic/al_fcm'+str(q+1)+'_'+str(case)+'.csv',delimiter=',')
        
    #    ww = ww.transpose()
    #    n = ww.shape[0]
    #    smax = np.zeros((1,n))
    #    
    #    
    #    for b in range(0,n):
    #        for c in range(0,n):
    #            smax[0,b] = smax[0,b]+ww[c,b]
    #            
    #    smax = abs(smax)
    #    totmax=  np.amax(smax)
    #    ww = ww/totmax
    #    
    #    ww = np.around(ww,decimals=3)
    #    al = np.around(al,decimals=3)
    
        H = fcm.fcm_class.fcm_from_matrix_to_graph(ww,al,0,Iterations+1)
    
        G_List.append(H)
    
    
#    G_List = fcm.fcm_class.pi_fcm_alg_graph(G_List,0,1,Iterations+1, lambda_value)
    G_List = fcm.fcm_class.aa_fcm_alg_graph(G_List,0,1,Iterations+1, lambda_value)
    #G_List = fcm.fcm_class.cnfcm_alg_graph(G_List,0,1,Iterations+1, lambda_value)
    
    results.append(G_List[0].node[36]['value'][Iterations])

print("Lamda value:",lambda_value)
print("Final Activation Level:",results)


colors = []
colors.append('cyan')
colors.append('grey')
colors.append('green')
colors.append('red')
colors.append('blue')
colors.append('yellow')

finalALs = []
fcms = []
fcms.append('')


for q in range(0,No_of_FCMs):
    
    H=G_List[q]

    pos=nx.spring_layout(H)
    labels = nx.get_edge_attributes(H,'weight')
    nodelabels = nx.get_node_attributes(H, 'value')

    finalnodelabels = {}
    colormap = []
    plt.figure()
    plt.title("FCM "+str(q))
    for i in range(0,len(H.node)):
        plt.plot(nodelabels[i],linewidth=2.0)
        finalnodelabels.update({i:nodelabels[i][-2]})
        finalALs.append(np.around(nodelabels[i][-2],decimals=3))
        
        colormap.append(colors[int(H.node[i]['color'])])

    plt.xlim(0, Iterations-1)
    plt.ylim(0, 1)
    plt.ylabel('Activation Level')
    plt.xlabel('Iterations')
    plt.show()
    
    plt.title("FCM "+str(q))
    plt.figure()
    nx.draw(H,pos,node_size=2200,node_color=colormap, font_size=8)
    nx.draw_networkx_edge_labels(H,pos,edge_labels=labels,font_size=10)
    nx.draw_networkx_labels(H,pos,labels=finalnodelabels)

