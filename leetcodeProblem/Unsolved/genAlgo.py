import random

class GenAlgorithm():

    def __init__(self):
        
        self.mono = {
            "A":3, "B":1, "C":1, "D":8,
            "E":1, "F":1, "G":9, "H":1,
            "I":2, "J":2
        }

        self.maximum = 10
        self.dnaCount = 8
        self.mono_val = [v for v in self.mono.values()]

    def dnaMaker(self):
        dna = []
        dnaCluster = []
        count = 0
        knapsackVal = 0
        while count < self.dnaCount :
            for v in self.mono.values() :
                randNum = random.randint(0,1)
                if randNum == 1 and self.maximum - v >= 0 :
                    dna.append(1)
                    self.maximum = self.maximum - v
                    knapsackVal += v
                else :
                    dna.append(0)

                if len(dna) % len(self.mono) == 0 :
                    dna.append(knapsackVal)
                    dnaCluster.append(dna) 
                    dna = []
                    knapsackVal = 0
                    self.maximum = 10

            count += 1
        
        return dnaCluster
    


    def dnaAttr(self, dna_shuugo):
        global avg_val
        global highest_val_dna
        temp_val = 0
        highest_val_dna = []
        for chr in dna_shuugo:
            temp_val += chr[len(chr)-1]
            if chr[len(chr)-1] == self.maximum :
                highest_val_dna.append(chr)


        avg_val = temp_val / len(dna_shuugo)
        
        if not highest_val_dna :
            temp_highest = avg_val
            temp_chr = []
            for chr in dna_shuugo:
                if chr[len(chr)-1] >= temp_highest :
                    temp_highest = chr[len(chr)-1]
                    temp_chr = chr

            highest_val_dna.append(temp_chr)

        def iterate():
            for i in dna_shuugo :
                print(i)
            
            print("Average Value of DNA Cluster = ",avg_val,"\n", "DNA with highest value = ", highest_val_dna)
        
        return iterate()
    
    def evolve(self, dna_shuugo, num):
        crossover_rate = 0.7
        mutation_rate = 0.1
        def elite_parent():
            if len(highest_val_dna) == 1 and highest_val_dna[0][len(highest_val_dna)-1] == self.maximum :
                new_gene = [chr for chr in dna_shuugo]
                parents = [chr for chr in dna_shuugo if chr[len(chr)-1] < self.maximum and chr[len(chr)-1] >= avg_val]
            elif len(highest_val_dna) == 1:
                new_gene = [chr for chr in dna_shuugo]
                parents = [chr for chr in dna_shuugo if chr[len(chr)-1] >= avg_val]
            else :
                new_gene = [chr for chr in dna_shuugo]
                parents = [chr for chr in dna_shuugo if chr[len(chr)-1] < self.maximum and chr[len(chr)-1] >= avg_val]

            return new_gene, parents
        
        new_gene, _ = elite_parent()
        _ , parents = elite_parent()

        def crossover_mutation():
            i = 0
            temp_child = []
            while i <= len(parents)-2:
                if random.random() <= crossover_rate:
                    child1 = parents[i][:6] + parents[i+1][6:10] 
                    child2 = parents[i+1][:6] + parents[i][6:10]
                    temp_child.append(child1)
                    temp_child.append(child2)
                    child1, child2 = [], []
                    i+=1

                else :
                    i +=1

            if not temp_child :
                return bit_mutation()
            else :
                temp_val = 0
                for chr in temp_child :
                    for i in range(len(chr)) :
                        if chr[i] == 1 :
                            temp_val += self.mono_val[i]
                    

                    if temp_val > self.maximum :
                        chr = parents[random.randint(0,len(parents)-1)]
                        temp_val =0
                    else :    
                        chr.append(temp_val)
                        temp_val = 0

                count = len(temp_child)    
                temp_gene = []
                for p_idx, pGene in enumerate(new_gene):
                    for f_idx, cGene in enumerate(temp_child):

                        if pGene[-1] < cGene[-1]:
                            temp_gene = new_gene[p_idx]
                            new_gene[p_idx] = temp_child[f_idx]
                            temp_child[f_idx] = temp_gene
                            count -= 1
                            break

                    if count == 0:
                        break
                        
                return new_gene
            
        def bit_mutation():
            temp_child = []
            for chr in parents :
                if random.random() <= mutation_rate :
                    count = 1
                    while count == 1 :
                        ranNum = random.randint(0,len(chr)-2)
                        if chr[ranNum] == 0 :
                            chr[ranNum] = 1
                            chr[len(chr)-1] = chr[len(chr)-1] + self.mono_val[ranNum] 

                            count = 0

                    if chr[len(chr)-1] > self.maximum :
                        chr[ranNum] = 0
                        chr[len(chr)-1] = chr[len(chr)-1] - self.mono_val[ranNum]
                    else :
                        for idx, pGene in enumerate(new_gene):
                            if pGene[-1] < chr[-1]:
                                new_gene[idx] = chr
                                break
            
            return new_gene
        if num == 1 :
            return crossover_mutation()
        else :
            return bit_mutation()
        


def main_menu():
    print("""
        auth@amryy
        ========================================
        GENETIC ALGORITHM FOR KNAPSACK PROBLEM
        ========================================
        [1] Generate DNA
        [2] Show Current DNA
        [3] Two-point crossover
        [4] Random Bit mutation
        [5] Randomize
        [6] Exit
    """)      

p = GenAlgorithm()       
if __name__ == "__main__":
    param_switch = False
    while True:
        main_menu()

        choice = input("Select Option > ")

        if choice == "1":
            param_switch = True
            print("Generating DNA...\n")
            dna_shuugo = p.dnaMaker()
            print("DNA Generated") 

        elif choice == "2":
            print("Current DNA:\n")
            if not param_switch :
                print("DNA is not created yet..")
            else :
                print(p.dnaAttr(dna_shuugo))

        elif choice == "3":
            if not param_switch :
                print("DNA is not created yet..")
            else :
                print("Initializing Two-point crossover..")
                dna_shuugo = p.evolve(dna_shuugo, 1)
                print(p.dnaAttr(dna_shuugo))
        
        elif choice == "4":
            if not param_switch :
                print("DNA is not created yet..")
            else :
                print("Initializing Bit Mutation..")
                dna_shuugo = p.evolve(dna_shuugo, 2)
                print(p.dnaAttr(dna_shuugo))
        elif choice == "5":
            if not param_switch :
                print("DNA is not created yet..")
            else :
                for i in range(3):
                    print("Randomizer..")
                    dna_shuugo = p.evolve(dna_shuugo, random.randint(1,2))
                    print(p.dnaAttr(dna_shuugo))
                
        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option.\n")


                    
                        

                
            
            

                

        

       
        
            
    

