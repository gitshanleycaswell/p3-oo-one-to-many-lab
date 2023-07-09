import ipdb 


class Pet:
    PET_TYPES =["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    all = []

    def __init__(self, name="Name", pet_type="dog", owner ="Owner"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def get_pet_type(self):
        return self._pet_type
    
    def set_pet_type(self, new_type):
        if new_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self._pet_type = new_type

    pet_type = property(get_pet_type, set_pet_type)

class Owner:
    def __init__(self, name="Name"):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(owner_pets, key=lambda pet: pet.name)


