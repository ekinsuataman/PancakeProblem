from simpleai.search import SearchProblem,breadth_first, depth_first,limited_depth_first,iterative_limited_depth_first, uniform_cost, greedy, astar
from random import shuffle
from datetime import datetime
from simpleai.search.viewers import WebViewer
#SearchProblem
my_viewer = WebViewer()
class PancakeProblem(SearchProblem):

    def __init__(self, initial):
        super().__init__(initial)
        self.initial_state = tuple(initial)
        self.goal = tuple(sorted(initial))
        self.size = len(initial)
        self.c = 0
    
    def actions(self,state):
        possible_actions = []
        for i in range(2,self.size+1):
            possible_actions.append(i)
        return possible_actions

    def cost(self, state, action, state2):
        self.c = self.c = action
        return self.c

    def result(self,state,action):
        firstPart = state[:action]
        secondPart = state[action:self.size]
        new_state = tuple(reversed(firstPart)) + secondPart
        return new_state
           
    def is_goal(self,state):
        return state == self.goal
 
    '''def heuristic(self,node):
        return sum(s != g for (s, g) in zip(node.state, self.goal))'''
   
    def heuristic(self,node):
        score = 0
        lilen = self.size
        if (self.initial_state[0] != lilen): score = score + 1
        i = 0
        while (i < lilen-1):
            x = self.initial_state[i]
            plus1 = x + 1
            minus1 = x - 1
            if ((self.initial_state[i+1] != plus1) & (self.initial_state[i+1] != minus1)): ## if a pancake's neighbor is not an adjacent pancake, the heuristic score increases
                score = score + 1                                                          ## i.e. we're further from the goal line
            i = i + 1
        return score
        
    '''def heuristic(self,node):
        cost = 0
        if self.initial_state[0] != len(self.initial_state):
            cost += 1
        for i in range(len(self.initial_state) - 1):
            if (abs(self.initial_state[i + 1] - self.initial_state[i]) > 1):
                cost += 1
        return cost'''
    
#Searching functions
def BFS(SearchingProblem):
    print("---Breadth First Search---")
    before = datetime.now()
    search = breadth_first(SearchingProblem)
    #search = breadth_first(SearchingProblem,viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)

def DFS(SearchingProblem):
    print("---Depth First Search---")    
    before = datetime.now()
    search = depth_first(SearchingProblem,graph_search=(True))
    #search = depth_first(SearchingProblem,graph_search=(True),viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)

def UCS(SearchingProblem):
    print("---Uniform Cost Search---")
    before = datetime.now()
    search = uniform_cost(SearchingProblem)
    #search = uniform_cost(SearchingProblem,viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->",(after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-"*40)
    #print('Stats: ')
    #print(my_viewer.stats)

def LDS(SearchingProblem):
    print("---Depth Limited Search---")
    before = datetime.now()
    search = limited_depth_first(SearchingProblem,10)#Tur limit
    #search = limited_depth_first(SearchingProblem,10,viewer=my_viewer)#Tur limit
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)
           
def ILDS(SearchingProblem):
    print("---Iterative LDS Search---")
    before = datetime.now()
    search = iterative_limited_depth_first(SearchingProblem)
    #search = iterative_limited_depth_first(SearchingProblem,viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)
    
def GBFS(SearchingProblem):
    print("---Greedy Best First Search---")
    before = datetime.now()
    search = greedy(SearchingProblem,lambda node: node.state)
    #search = greedy(SearchingProblem,lambda node: node.state,viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)
    
def Astar(SearchingProblem):
    print("---AStar Search---")
    before = datetime.now()
    search = astar(SearchingProblem)
    #search = astar(SearchingProblem,viewer=my_viewer)
    after = datetime.now()
    print("Path -->",search.path())
    print("Time -->", (after - before).total_seconds())
    print("Path cost-->",search.cost)
    print("-" * 40)
    #print('Stats: ')
    #print(my_viewer.stats)
    
def AllAlgorithms(SearchingProblem):
    print(("#" * 15) + "\n# Uniformed Searchss #\n" + ("#" * 15))
    BFS(SearchingProblem)
    UCS(SearchingProblem)
    DFS(SearchingProblem)
    LDS(SearchingProblem)
    ILDS(SearchingProblem)
    print(("#" * 15) + "\n# Informed Searchss  #\n" + ("#" * 15))
    GBFS(SearchingProblem)
    Astar(SearchingProblem)

print("\nWelcome to Pancake Sorter with Artificial Intellegent Program\n")

while True:
    try:
        numberOfPancakes = int(input("Enter number of pancakes: "))
    except:
        print("Type an integer")
        continue

    pancakes = []
    items = []
    while True:
        orderChoice = input("Do you want to enter ordering?: ")
        if orderChoice.lower() == "yes":
            print("Enter top to bottom ordering between [0 - ",numberOfPancakes-1,"]"," separated by spaces: ",sep="")
            items = input("")
            x = 0
            for i in range(numberOfPancakes):
                pancakes.append(int(items[x]))
                x=x+2
                
            break                                  
        elif orderChoice.lower() == "no":
            for i in range(numberOfPancakes):
                pancakes.append(i)
            shuffle(pancakes)
            break
        else:
            print("Type only 'yes' or 'no' ")

    pancake_problem = PancakeProblem(pancakes)

    print("initial state: (", end = "")
    for eleman in pancakes:
        if pancakes.index(eleman) == len(pancakes)-1:
            print (eleman, end = "", flush = True)
        else:
            print (eleman, end = ", ", flush = True)
    print(")")

    while True:
        print("\nChoose searching algorithm to calculate")
        algorithm = int(input("1 - Breadth First Search\n"
              "2 - Depth First Search\n"
              "3 - Uniform Cost Search\n"
              "4 - Limited Depth Search\n"
              "5 - Iterative LDS Search\n"
              "6 - Greedy Best First Search\n"
              "7 - Astar Search\n"
              "8 - All algorithms\n"))

        if algorithm == 1:
            BFS(pancake_problem)
        elif algorithm == 2:
            DFS(pancake_problem)
        elif algorithm == 3:
            UCS(pancake_problem)
        elif algorithm == 4:
            LDS(pancake_problem)
        elif algorithm == 5:
            ILDS(pancake_problem)
        elif algorithm == 6:
            GBFS(pancake_problem)
        elif algorithm == 7:
            Astar(pancake_problem)
        elif algorithm == 8:
            AllAlgorithms(pancake_problem)
        else:
            print("Invalid input")
            continue
        if input("Want to calculate with different algorithm? [yes]/[no]") =="no":
            break

    if input("\nWant to calculate different pancakes order? [yes]/[no]") == "no":
        break
print("developed by Ekin Şuataman)