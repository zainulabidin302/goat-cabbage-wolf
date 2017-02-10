E = 0
W = 1

class Tree:
    
    def __init__(self):
        self.nodes = [] # 
        self.id    = 0    
        pass
    
    def addRoot(self,val):
        node = {'value': val, 'parent': -1, 'id': -1, 'isVisited': 0}
       
        self.nodes.append(node)
        return node
        
    
    def addChildOf(self,parent_node, val):
        node = {'value': val, 'parent': parent_node.get('id'), 'id': self.id, 'isVisited': 0}
        self.id = self.id + 1
        self.nodes.append(node)
        return node
    
        
    def addChildOfList(self,parent_node, ls):
        new_nodes = []
        for node in ls:
            n = {'value': node, 'parent': parent_node.get('id'), 'id': self.id, 'isVisited': 0}
            new_nodes.append(n)
            self.id = self.id + 1
            self.nodes.append(n)
        return new_nodes
        
        
    def printTree(self):
        print 'agye ho'
        for node in self.nodes:
            print '\t'
            print node
            print node.get('value')
    
    
    def printDFS(self):
        pass
    
    def printBFS(self):
        pass
    
      
    def discoverMoveNodes(self, node):
        
        
        def isValidMove(move):
            if self.isDuplicate(move):
                return False
                
            for m in [(W,W,E,E), (W,W,W,E), (E,E,W,W) , (E,E,E,W), (W,E,E,W), (E,W,W,E)]:
                if m == move:
                    return False
            return True
        def toggle(s):
            if s == W:
                return E
            return W
  
        n_moves = []
        current_move = node.get('value')
        new_move = (toggle(current_move[0]), current_move[1], current_move[2], toggle(current_move[3]))
        
        if isValidMove(new_move):
            n_moves.append(new_move)
        
        new_move = (current_move[0], toggle(current_move[1]), current_move[2], toggle(current_move[3]))
        if isValidMove(new_move):
            n_moves.append(new_move)
            
        new_move = (current_move[0], current_move[1], toggle(current_move[2]), toggle(current_move[3]))
        if isValidMove(new_move):
            n_moves.append(new_move)

        
        return n_moves
 
        
    def isDuplicate(self, move):


        if move in [n.get('value') for n in self.nodes]:
            return True
        False
            
tree = Tree()


def isLeaf(l):
    return len(l) < 1

stack = []
def dfs(root):
    
    newly_discovered_nodes = tree.discoverMoveNodes(root)
    nodes_list = []
    for node in newly_discovered_nodes:
        nodes_list.append(tree.addChildOf(root, node))
        
    stack.extend(nodes_list)    

    #base case
    if isLeaf(nodes_list):
        return stack.pop()

        
    #recursive case
    for node in stack:
        if node.get('isVisited') == 1:
            continue
        
        if node.get('value') == goal:
            print 'result'
            print stack
            return
        
        node['isVisited'] = 1
        dfs(node)
            




start = (E,E,E,E) #initial
goal  = (W,W,W,W)

stack = []
t = Tree()


root = t.addRoot(start)
stack.append(root)
dfs(root)

t.printTree()

    



    
