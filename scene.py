import os
import sys
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
    def travel(self,player,display=None):
        if(self.travel_function):
            self.travel_function(player,display=display)
        else:
            display=display+"\n\n**\n\n"
class SceneGraph:
    def __init__(self):
        self.root=None;
        self.nodes=[]
        self.edges=[]
        self.visible_node=None;
        self.visible_edges=[]
        self.displays=["",""]
        self.display_width=100
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
            self.visible_edges[option].travel(player,display=self.update_display)
        except:
            #there are no possible answers:
            self.visible_edges.append(self.edges[0])
            self.visible_edges[0].travel(player,display=self.update_display)
        self.set_visible_node(vnid)
        self.set_visible_edges(player)
    def set_visible_node(self,id):
        for x in self.nodes:
            if x.id == id:
                self.visible_node=x
                break
    def display(self):
        s="";
        s=s+(self.visible_node.text);
        s=s+"\n\n"
        for i,x in enumerate(self.visible_edges):
            s=s+(f'\n{i}: {x.text}')
        return s
    def play(self,player):
        self.update_display(
            0,
            text_data=[
                player.display(self.display_width),
                self.display()
            ],
            rewrite=True
        )
        opt = self._play()
        self.travel(opt,player)

        self.play(player)        
    def _play(self):
        
        while True:
            try:
                opt = int(input('what do you do? :'))
                clear()
                return opt

            except KeyboardInterrupt:
                clear()
                sys.exit()
            except:
                print("only a number please")
    def output(self,display, text):
        self.displays[display]=self.displays[display]+text;
    def clear_output(self,display=None,every=False):
        if every:
            for i,x in enumerate(self.displays):
                self.displays[i]=""
        elif display:
            self.displays[display]=""
        clear()
    def update_display(self,screen,text_data,add=False,rewrite=False):

        t1=self.displays[0]
        t2=self.displays[1]
        if rewrite:
            self.clear_output(every=True)
            self.output(0,text_data[0])
            self.output(1,text_data[1])
        elif add:
            clear()
            self.displays[screen]=self.displays[screen]+text_data
        else:
            clear()
            self.displays[screen]=text_data
        self.display_merge()
    def display_merge(self):
        dw = self.display_width
        box_of_lines = [x.split("\n") for x in self.displays]

        ld = max([len(x) for x in box_of_lines])
        option_count = len(self.visible_edges)
        while len(box_of_lines[1])<ld:
            box_of_lines[1].insert(len(box_of_lines)-(option_count-1),"")


        for i in range(ld):
            s=""
            for d in box_of_lines:
                try:
                    s=s+pad(d[i],self.display_width)
                except:
                    s=s+pad("",self.display_width)
            print(s)
def pad(line,leng):
    l = len(line)
    d = leng-l;
    s = " "
    for x in range(d):
        if x%2==0:
            line=line+s
        else:
            line=s+line
    
    line=line+"<"
    line=">"+line

    return line