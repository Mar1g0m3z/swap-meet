from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, age=0, fabric="Unknown"):
        
        super().__init__(id, condition, age)
        
        self.fabric = fabric

    def additional_text(self):
        return f" It is made from {self.fabric} fabric."
    
    # def __str__(self):
    #     return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
