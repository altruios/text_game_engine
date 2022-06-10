class World:
    def __init__(self,scene):
        self.player=None;
        self.scene=scene;
        pass
    def add_player(self,player):
        self.player=player;
        self.scene.add
    def play(self):
        self.scene.play(self.player)
    def title_screen(self):
        self.scene.clear_output(every=True)
        title_screen_text_data = [x for x in self.scene.nodes if x.id=="TITLE"][0].text
        self.scene.update_display(1,title_screen_text_data)