# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:13:20 2020

@author: andreas
"""
import numpy as np
import matplotlib.pyplot as plt
import fcm
import pso

def function(x):
    
    No_of_FCMs = 6
    lambda_value = 0.6
    Iterations = 20

    G_List = []
    
    for q in range(0,No_of_FCMs):
        # for each subFCM 
         
        ww = np.genfromtxt('../mlfcmdata/betologic/ww_fcm'+str(q+1)+'.csv',delimiter=',')
        al = np.genfromtxt('../mlfcmdata/betologic/al_fcm'+str(q+1)+'_0.csv',delimiter=',')
        i_index = 0
        if q == 0:
            al[0][0] = x[i_index]     #1 Governance (FCM0)
            i_index+=1
            al[1][0] = x[i_index]     #2 Infrastructure and Management Services
            i_index+=1
            al[2][0] = x[i_index]     #3 Maintainability & Evolvability
            i_index+=1
            al[3][0] = x[i_index]     #4 Operational Complexity
            i_index+=1
            al[4][0] = x[i_index]     #5 Business Complexity
            i_index+=1
            al[5][0] = x[i_index]     #6 Reliability
            i_index+=1
            al[6][0] = x[i_index]     #7 Security
            i_index+=1
            al[7][0] = x[i_index]     #8 Cost
            i_index+=1
            al[8][0] = x[i_index]     #9 Design
            i_index+=1
            al[9][0] = x[i_index]     #10 DevOps
            i_index+=1
            al[10][0] = x[i_index]    #11 Data Migration
            i_index+=1
            al[11][0] = 0
        elif q == 1:
            al[0][0] = 0            #Governance (FCM1)
            al[1][0] = x[i_index]    #12 Decentralized Governance
            i_index+=1
            al[2][0] = x[i_index]    #13 Data Governance
            i_index+=1
        elif q == 2:
            al[0][0] = 0            #Infrastructure and Management Services (FCM2)
            al[1][0] = x[i_index]    #14 Containerization
            i_index+=1
            al[2][0] = x[i_index]    #15 Scalability/Elasticity
            i_index+=1
            al[3][0] = x[i_index]    #16 Monitoring
            i_index+=1
            al[4][0] = x[i_index]    #17 Serverless Architecture
            i_index+=1
        elif q == 3:
            al[0][0] = 0            #Cost (FCM3)
            al[1][0] = x[i_index]    #18 Migration Cost
            i_index+=1
            al[2][0] = x[i_index]    #19 Operations Cost
            i_index+=1
        elif q == 4:
            al[0][0] = 0            #Design (FCM4)
            al[1][0] = x[i_index]    #20 Design For Failure
            i_index+=1
            al[2][0] = x[i_index]    #21 Granularity and Bounded Context
            i_index+=1
            al[3][0] = x[i_index]    #22 Service Contracts
            i_index+=1
            al[4][0] = x[i_index]    #23 Communication Model
            i_index+=1
            al[5][0] = x[i_index]    #24 Decentralization
            i_index+=1
        else:
            al[0][0] = 0            #DevOps (FCM5)
            al[1][0] = x[i_index]    #25 Organization Culture
            i_index+=1
            al[2][0] = x[i_index]    #26 Skilled and Educated DevOps Teams
            i_index+=1
            al[3][0] = x[i_index]    #27 Tool Support
            i_index+=1
            al[4][0] = x[i_index]    #28 Continues Activities
            i_index+=1
            al[5][0] = x[i_index]    #29 Automated Tasks
            i_index+=1
            al[6][0] = x[i_index]    #30 Information Sharing
        
        H = fcm.fcm_class.fcm_from_matrix_to_graph(ww,al,0,Iterations+1)
        G_List.append(H)
    
    G_List = fcm.fcm_class.aa_fcm_alg_graph(G_List,0,1,Iterations+1, lambda_value)
    return  abs(G_List[0].node[11]['value'][Iterations]-0.2)
    

lb = [0]*30
ub = [1]*30

pso_iterations = 100

plt.ylabel('Fitness')
plt.xlabel('Iterations')
plt.xlim(0, pso_iterations )
plt.ylim(0.0, 0.4)
plt.title('Target Value: 0.1 (Very Low)')

for k in range(5):
    
    xopt, fopt, ch = pso.pso(function, lb, ub, debug=False, maxiter=pso_iterations)
    if fopt<=0.04:
        plt.plot(np.arange(len(ch)), ch)

plt.show()