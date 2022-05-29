class Item:
    def __init__(self,name,quantity,description):
        self.name=name;
        self.quantity=quantity;
        self.description=description
    def effect(self):
        print(f"using {self.name}")
        self.quantity=self.quantity-1
        if self.quantity==0:
            del self
    def use(self,target):
        self.effect()