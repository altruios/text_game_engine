class Player:
    def __init__(self,name):
        self.name=name;
        self.health=100;
        self.defence=100;
        self.wit=100;
        self.speed=100;
        self.vision=100;
        self.dexterity=100;
        self.wisdom=100;
        self.confidence=100;
        self.fear=100;
        self.misery=100;
        self.hate=100;
        self.delerium=100;
        self.love=100;
        self.happy=100;
        self.doom=100;
        self.anxiety=100;
        self.dreams=100;
        self.desire=100;
        self.risk=100;
        self.spite=100;
        self.determination=100;
        self.honesty=100;
        self.calm=100;
        self.sad=100;
        self.curiosity=100;
        self.level=100;
        self.respawn=0;
        self.is_alive=True;
        self.inventory=[]
    def add_to_inventory(self,item):
        found=False;
        for x in self.inventory:
            if x.name==item.name:
                x.quantity=x.quantity+item.quantity
                found=True;
        if not found:
            self.inventory.append(item)
    def use_item(self,item_name,target):
        item = self.search_inventory(item_name)
        item.use(self,target)
    def search_inventory(self,item_name):
        for x in self.inventory:
            if x.name == item_name:
                return x
    def display(self):
       print(vars(self))