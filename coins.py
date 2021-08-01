import random
class coin:
    def __init__(self,rare = False,clean=True,heads=Ture,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
        if self.is_rare:
            self.value = self.original_value *1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color
    def rust(self):
        self.color = self.rusty_color
    def clean(self):
        self.color = self.clean_color
    def flips(self):
        head_options = [True,False]
        choice = random.choice(head_options)
        self.heads = choice

class one_pence(coin):
    def __init__(self):
        data ={
            "original_value":0.01,
            "clean_color":"bronze",
            "rusty_color":"brownish",
            "num_edges":20.3,
            "thickness":1.52,
            "mass":9.5         
        }
        super().__init__(**data)
       





class pound(coin):
    def __init__(self):
        data ={
            "original_value":1.00,
            "clean_color":"gold",
            "rusty_color":"greenish",
            "num_edges":22.5,
            "thickness":3.15,
            "mass":9.5         
        }
        super().__init__(**data)
       
    