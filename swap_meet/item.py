import uuid


class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition
        

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        # self.condition = condition

        if self.condition == 1:
            return "Used by trolls, better burn it"
        elif self.condition == 2:
            return "Barely usable, needs lots of sanitation first"
        elif self.condition == 3:
            return "Usable, but still needs to be sanitized"
        elif self.condition == 4:
            return "Almost new, take it!"
        elif self.condition == 5:
            return "Perfect. I think they stored it in a museum"
