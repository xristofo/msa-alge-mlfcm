# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:32:45 2019

@author: andreas
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import fcm

class Individual(object):

    def __init__(self, genes=None, individual_size = 20, target_val=0.6, individual_id = None):
        if genes is None:
            self.genes = np.random.randint(1,10,size=individual_size)/10
            self.target_val = target_val
            self.fitness_val = 0
            self.id = individual_id
            self.calculated_value = []
        else:
            self.fitness_val = 0
            self.genes = genes
            self.target_val = target_val
            self.calculated_value = []
            
    def fitness(self, run=False):
        """
        Returns fitness of individual
        Fitness is the difference between target value and the calculated value
        """
        
        if (run==True):
            self.calculated_value = Algorithm(genes=self.genes)
            objectives_no = len(self.calculated_value.result)
            objectives_fitness = 0
            
            for x in self.calculated_value.result:
                objectives_fitness = objectives_fitness + x
            
            objectives_fitness_mean = round(objectives_fitness / objectives_no,3)
                
            self.fitness_val = objectives_fitness_mean #round(abs(self.target_val - calculated_value.result),3)
        return self.fitness_val

class Population(object):

    def __init__(self, pop_size=10, mutate_prob=0.01, retain=5, target_val=0.6, individual_size = 30):
        """
        """
        self.pop_size = pop_size
        self.mutate_prob = mutate_prob
        self.retain = retain
        self.target_val = target_val
        self.fitness_history = []
        self.parents = []
        self.elit = []
        self.done = False
        

        # Create individuals
        self.individuals = []
        for x in range(pop_size):
            self.individuals.append(Individual(genes=None,individual_size=individual_size,target_val=self.target_val,individual_id=x))

    def grade(self, generation=None):
        """
        Grade the generation by getting the average fitness of its individuals
        """
        fitness_sum = 0
        for x in self.individuals:
            fitness_sum += x.fitness(run=True)
        
        mean_fitness = fitness_sum / self.pop_size
        
        pop_fitness = round(mean_fitness,3)
        self.fitness_history.append(pop_fitness)

        self.individuals = list(reversed(sorted(self.individuals, key=lambda x: x.fitness(), reverse=True)))
        # Set Done flag if we hit target
        if (pop_fitness < 0.02) or (self.individuals[0].fitness_val==0):
            pop_fitness = 0
#            self.fitness_history.append(pop_fitness)
            self.done = True

            
        if generation is not None:
            print("Generation:",generation,"Population fitness:", pop_fitness,"Fitness sum:", fitness_sum)
            
    
            
    def select_parents(self):
        """
        Select the fittest individuals (elitist selection) to be the parents of next generation (lower fitness it better in this case)
        Also select non-fittest individuals (roulette wheel) to help get us out of local maximums
        """
        # Sort individuals by fitness (we use reversed because in this case lower fintess is better)
#        self.individuals = list(reversed(sorted(self.individuals, key=lambda x: x.fitness(), reverse=True)))
        # Keep the fittest as parents for next gen
        retain_length = (self.retain/100) * len(self.individuals)
        self.parents = self.individuals[:int(retain_length)]
        self.elit = self.parents[:]

        # select some from unfittest and add to parents array
        unfittest = self.individuals[int(retain_length):]
        max_fitness = sum(uf.fitness() for uf in unfittest)
        
        while len(self.parents)<len(self.individuals):
            pick = random.uniform(0, max_fitness)
            current = 0
            for unfit in unfittest:
                current += unfit.fitness()
                if current < pick:
                    self.parents.append(unfit)
                    break
                
        
    def Crossover(self):
        """
        Crossover the parents to generate a new generation of individuals
        """
        target_children_size = self.pop_size
        children = self.elit[:]
        if len(self.parents) > 0:
            while len(children) < target_children_size:
                father = random.choice(self.parents)
                mother = random.choice(self.parents)
#                if father != mother:
                child_genes = [ random.choice(pixel_pair) for pixel_pair in zip(father.genes, mother.genes)]
                child = Individual(child_genes, target_val=self.target_val)
                children.append(child)
            self.individuals = children
    
    def Mutation(self):
        """
        Alters one gene value at most for each individual
        """
        for x in self.individuals:
            if self.mutate_prob > np.random.rand():
                mutate_index = np.random.randint(len(x.genes))
                x.genes[mutate_index] = np.random.randint(1,10)/10
        
    def evolve(self):
        """
        Evolves curent population to the next generation 
        """
        # 1. Selection
        self.select_parents()
        # 2. Crossover
        self.Crossover()
        # 3. Mutation
        self.Mutation()
        
        # Reset parents and children
        self.parents = []
        self.children = []
        self.elit = []

class Algorithm(object):
    
    def __init__(self, genes=[]):
        
        No_of_FCMs = 6
        lambda_value = 0.5
        Iterations = 20

        G_List = []
    
        for q in range(0,No_of_FCMs):
        # for each subFCM 
         
            ww = np.genfromtxt('../mlfcmdata/betologic/ww_fcm'+str(q+1)+'.csv',delimiter=',')
            al = np.genfromtxt('../mlfcmdata/betologic/al_fcm'+str(q+1)+'_0.csv',delimiter=',')
            i_index = 0
            if q == 0:
                al[0][0] = genes[i_index]     #1 Governance (FCM0)
                i_index+=1
                al[1][0] = genes[i_index]     #2 Infrastructure and Management Services
                i_index+=1
                al[2][0] = genes[i_index]     #3 Maintainability & Evolvability
                i_index+=1
                al[3][0] = genes[i_index]     #4 Operational Complexity
                i_index+=1
                al[4][0] = genes[i_index]     #5 Business Complexity
                i_index+=1
                al[5][0] = genes[i_index]     #6 Reliability
#                i_index+=1
                al[6][0] = genes[i_index]     #7 Security
                i_index+=1
                al[7][0] = genes[i_index]     #8 Cost
                i_index+=1
                al[8][0] = genes[i_index]     #9 Design
                i_index+=1
                al[9][0] = genes[i_index]     #10 DevOps
                i_index+=1
                al[10][0] = genes[i_index]    #11 Data Migration
                i_index+=1
                al[11][0] = 0
            elif q == 1:
                al[0][0] = 0            #Governance (FCM1)
                al[1][0] = genes[i_index]    #12 Decentralized Governance
                i_index+=1
                al[2][0] = genes[i_index]    #13 Data Governance
                i_index+=1
            elif q == 2:
                al[0][0] = 0            #Infrastructure and Management Services (FCM2)
                al[1][0] = genes[i_index]    #14 Containerization
                i_index+=1
                al[2][0] = genes[i_index]    #15 Scalability/Elasticity
                i_index+=1
                al[3][0] = genes[i_index]    #16 Monitoring
                i_index+=1
                al[4][0] = genes[i_index]    #17 Serverless Architecture
                i_index+=1
            elif q == 3:
                al[0][0] = 0            #Cost (FCM3)
                al[1][0] = genes[i_index]    #18 Migration Cost
                i_index+=1
                al[2][0] = genes[i_index]    #19 Operations Cost
                i_index+=1
            elif q == 4:
                al[0][0] = 0            #Design (FCM4)
                al[1][0] = genes[i_index]    #20 Design For Failure
                i_index+=1
                al[2][0] = genes[i_index]    #21 Granularity and Bounded Context
                i_index+=1
                al[3][0] = genes[i_index]    #22 Service Contracts
                i_index+=1
                al[4][0] = genes[i_index]    #23 Communication Model
                i_index+=1
                al[5][0] = genes[i_index]    #24 Decentralization
                i_index+=1
            else:
                al[0][0] = 0            #DevOps (FCM5)
                al[1][0] = genes[i_index]    #25 Organization Culture
                i_index+=1
                al[2][0] = genes[i_index]    #26 Skilled and Educated DevOps Teams
                i_index+=1
                al[3][0] = genes[i_index]    #27 Tool Support
                i_index+=1
                al[4][0] = genes[i_index]    #28 Continues Activities
                i_index+=1
                al[5][0] = genes[i_index]    #29 Automated Tasks
                i_index+=1
                al[6][0] = genes[i_index]    #30 Information Sharing
            
            H = fcm.fcm_class.fcm_from_matrix_to_graph(ww,al,0,Iterations+1)
            G_List.append(H)
    
        G_List = fcm.fcm_class.aa_fcm_alg_graph(G_List,0,1,Iterations+1, lambda_value)
        self.result = []
        self.result.append(abs(G_List[0].node[11]['value'][Iterations]-0.9))
#        self.result.append(abs(G_List[0].node[6]['value'][Iterations]-0.7))
        
    
if __name__ == "__main__":
    
    Results = []
    
    for k in range(5):
        """
        k runs of genetic algorithm
        """
        pop_size = 50
        mutate_prob = 0.1
        retain = 5
        target_val = 0.9
        individual_size = 30
        GENERATIONS = 250
        SHOW_PLOT = True
                
        pop = Population(pop_size=pop_size, mutate_prob=mutate_prob, retain=retain, target_val=target_val, individual_size=individual_size)
    
       
        for x in range(GENERATIONS):
    
            pop.grade(generation=x)
            if pop.done or x==(GENERATIONS-1):
                print("Simulation:", k,"Finished at generation:", x, ", Population fitness:", pop.fitness_history[-1])
                break
            pop.evolve()
            
        finalAL = pop.individuals[0].genes[:]
        Results.append(finalAL)
        
        # Plot fitness history
        if SHOW_PLOT:
            print("Showing fitness history graph")
            plt.plot(np.arange(len(pop.fitness_history)), pop.fitness_history)
            plt.ylabel('Fitness')
            plt.xlabel('Generations')
            plt.xlim(0, GENERATIONS )
            plt.ylim(0.0, 0.3)
            plt.title('Target Value: 0.9 (Very High)')
            plt.show()
