class Pet:
    def init(self, pet_name):
        self.name = pet_name
    def play_fetch(self):
        print("Your pet" + self.name + " seemed to be happy to play fetch")

orange_cat = Pet("Miles")
small_dog = Pet("Fido")

print(orange_cat.name)
small_dog.play_fetch()
