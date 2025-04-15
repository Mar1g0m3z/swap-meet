import uuid


class Item:
    def __init__(self, id=None, condition=0, age=None):
        if id is None:
            self.id = uuid.uuid4().int
        elif not isinstance(id, int):
            raise TypeError("Id should be an integer")
        else:
            self.id = id

        if not isinstance(condition, (int, float)):
            raise TypeError("Condition should be an number")
        self.condition = condition
        
        if age is not None and not isinstance(age, (int, float)):
            raise TypeError("Age should be an number")
        self.age = age
        
    def get_category(self):
        return self.__class__.__name__
    
    def additional_text(self):
        return ""

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}.{self.additional_text()}"

    def condition_description(self):
        if self.condition == 0:
            return "Condition unknown"

        if isinstance(self.condition, float):
            self.condition = round(self.condition)

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

    def age_description(self):
        if self.age is None:
            return "Age unknown"

        if self.age >= 50:
            return "Vintage"
        elif self.age >=7:
            return "Old"
        elif self.age >=3:
            return "Fair"
        elif self.age >0:
            return "Almost new"
        else:
            return "New"
