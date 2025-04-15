class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        other_vendor.inventory.append(self.inventory.pop(0))
        self.inventory.append(other_vendor.inventory.pop(0))
        
        return True
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        
        result = None

        for item in items:
            if result == None or item.condition > result.condition:
                result = item

        return result

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_item = other_vendor.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        result = self.swap_items(other_vendor, my_item, their_item)

        return result
    
    def get_newest(self):
        if not self.inventory:
            return None

        result = None
        for item in self.inventory:
            if item.age and (result == None or item.age < result.age):
                result = item
                
        return result
        
    def swap_by_newest(self, other_vendor):
        my_newest = self.get_newest()
        their_newest = other_vendor.get_newest()

        result = self.swap_items(other_vendor, my_newest, their_newest)

        return result


