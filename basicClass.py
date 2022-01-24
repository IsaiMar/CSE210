# class person:
#     pass


# isai = person()
# print(isai)

# isai.full_name = "Isai Eduardo Mar Garcia"
# print(isai.full_name)


# class people:
#     def __init__(self):
#         pass
# isai = people()
# print(isai)

# mar = people()
# print(mar)


class Person:
    
    def __init__(self,full_name="", age="0"):
        self.full_name = full_name
        self.age = age
        self.restaurant = []

    def add_restaurant(self,restaurant):
        self.restaurants.append(restaurant)

    def get_restaurant(self):
        return self.restaurants
    
    def get_favorite_restaurant(self):
        best = -1
        favorite = Restaurant("","","$",-1)
        for r in self.restaurants:

        
class Restaurant:

    def __init__():


isai = Person("Isai Eduardo Mar Garcia", "22")
print(isai)
print(isai.full_name)
print(isai.age)

miriam = Person("Miriam Christine Seely", "21")
print(miriam)
print(miriam.full_name)
print(miriam.age)

little_ceasars = Restaurant 


