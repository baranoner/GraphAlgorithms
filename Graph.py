class node():
    def __init__(self, name):
        self.name = name 
        self.visited = False
        self.prev = None
        self.neighbors = []   # List of references to adjacent nodes (not node names)
        
        
class DiGraph():
    def __init__(self, edge_list):
        self.edge_list = edge_list
        self.create_nodes()
        self.create_graph() # create edges
        
    def create_nodes(self):
        # Get node names from edge_list and remove duplicates
        self.node_names = list(set([s for s,t in self.edge_list]
                                   +[t for s,t in self.edge_list]))
        # create nodes, store in a dictionary
        self.nodes = {n:node(n) for n in self.node_names}
        
    def create_graph(self):
        for edge in self.edge_list:
            self.add_edge(edge)
            
    def add_edge(self, edge):
        s,t = edge
        self.nodes[s].neighbors.append(self.nodes[t]) # in neighbor list I have nodes (not names)
        ## UNDIRECTED: self.nodes[t].neighbors.append(self.nodes[s])
class BFS():   
    def __init__(self, G):
        self.G = G
        self.traversal = []
        self.queue = Queue()
        self.pos_fr = draw(self.G) # inital position
     
    def traverse(self, v_name):
        self.queue.put(v_name)
        self.G.nodes[v_name].visited = True
        self.traversal.append(v_name)
        draw(self.G, v_name,  pos_fr = self.pos_fr, display= False) # using same position
        
    def bfs(self, s_name):
        self.traverse(s_name)       
        while not self.queue.empty():
            s_name = self.queue.get() # s is node (not node name)
            for t in self.G.nodes[s_name].neighbors: 
                if not t.visited: # all unmarked neighbors
                    self.traverse(t.name)
                    t.prev = s_name 
class DFS():   
    """
    - Mark v = Node[s_name] as visited
    - recursively visit all unmarked neighbors
    """
    def __init__(self, G):
        self.G = G
        self.traversal = []
        self.pos_fr = draw(self.G) # inital position
        
    def dfs(self, s_name):
        self.G.nodes[s_name].visited = True
        self.traversal.append(s_name)
        draw(self.G, s_name,  pos_fr = self.pos_fr, display= False) # using same position
        
        for t in self.G.nodes[s_name].neighbors: # t is node (not node name)
            if not t.visited: # all unmarked neighbors
                t.prev = s_name
                self.dfs(t.name) # recursive visit                    
