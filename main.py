E = 0
W = 1

class Tree:
    
    def __init__(self):
        self.nodes = [] # 
        self.id    = 0    
        pass
    
    def addRoot(self,val):
        node = {'value': val, 'parent': -1, 'id': -1}
       
        self.nodes.append(node)
        return node
        
    
    def addChildOf(self,parent_node, val):
        node = {'value': val, 'parent': parent_node.get('id'), 'id': self.id}
        self.id = self.id + 1
        self.nodes.append(node)
        return node
    
        
    def addChildOfList(self,parent_node, ls):
        new_nodes = []
        for node in ls:
            n = {'value': node, 'parent': parent_node.get('id'), 'id': self.id}
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
        print move
        print move in self.nodes
        if move in [n.get('value') for n in self.nodes]:
            return True
        False
            
tree = Tree()



def dfs(stack, node):
    
    for item in stack:
        item.visited = 1
        if len(Tree.discoverMoveNodes(item)) > 0: 
            stack.extend(Tree.addChildOfList(Tree.discoverMoveNodes(item)))
                dfs(stack, node)
        
    t.printTree


start = (E,E,E,E) #initial
goal  = (W,W,W,W)

stack = []
t = Tree()

root = t.addRoot(start)
dfs(stack, root)



    



    
