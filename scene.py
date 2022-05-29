import os
clear = lambda: os.system("clear")
class SceneNode:
    def __init__(self,text,id):
        self.text=text;
        self.id=id

class SceneEdge:
    def __init__(self,text,fn,hidden_check,n1id,n2id):
        self.text=text
        self.parent=n1id;
        self.child=n2id;
        self.travel_function=fn
        self.hidden_function=hidden_check
    def is_hidden(self,player):
        if not self.hidden_function:
            return False;
        return self.hidden_function(player);
    def travel(self,player):
        if(self.travel_function):
            self.travel_function(player)
        else:
            print("\n\n**\n\n")
class SceneGraph:
    def __init__(self):
        self.root=None;
        self.nodes=[]
        self.edges=[]
        self.visible_node=None;
        self.visible_edges=[]
    def add(self, node=None,edge=None):
        if node:
            self.nodes.append(node)
        if edge:
            self.edges.append(edge)
    def set_visible_edges(self,player=None):
        self.visible_edges=[]
        for x in self.edges:
            if x.parent == self.visible_node.id:
                if not x.is_hidden(player):
                    self.visible_edges.append(x)
    def travel(self,option,player=None):
        try:
            vnid = self.visible_edges[option].child
        except:
            vnid = 0
        try:
            self.visible_edges[option].travel(player)
        except:
            #there are no possible answers:
            self.visible_edges.append(self.edges[0])
            self.visible_edges[0].travel(player)
        self.set_visible_node(vnid)
        self.set_visible_edges(player)
    def set_visible_node(self,id):
        for x in self.nodes:
            if x.id == id:
                self.visible_node=x
                break
    def display(self):
        print(self.visible_node.text);
        for i,x in enumerate(self.visible_edges):
            print(f'{i}: {x.text}')
    def play(self,player):
        player.display()
        self.display()
        opt = self._play()
        self.travel(opt,player)

        self.play(player)        
    def _play(self):
        while True:
            try:
                opt = int(input('what do you do? :'))
                clear()
                return opt
            except:
                print("only a number please")
   