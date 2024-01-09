class Person:
    def __init__(self,firstname, lastname, name, age, gender, occupation, eyecolor):
        self.__firstname = firstname
        self.__lastname = lastname
        self.name = name
        self.age = age
        self._gender = gender
        self.__occupation = occupation #robi to private hodnotu
        self.eyecolor = eyecolor

    def meno(firstname, lastname):
        print(patrik.__firstname, patrik.__lastname)
#pozdrav a age su methods
    def pozdrav(self):
        print(f"Ahoj, volám sa {self.name} a mám {self.age} rokov")

    def age_by_pocetrokov(self, pocetrokov):
        self.age += pocetrokov
        print(f"{self.name} now has an age of {self.age} years.")


veronika = Person(firstname = "Pavla", lastname = "Christova", name="Veronika", age=27, gender="female", occupation="captain", eyecolor = "green")
veronika.pozdrav()

patrik = Person(firstname = "Pato", lastname = "Dendis", name="Patrik", age=30, gender="male", occupation="programmer", eyecolor = "brown")
patrik.pozdrav()


veronika.age_by_pocetrokov(5)
print(veronika.age)


print(veronika.eyecolor)

patrik.name = "Igor"
print(patrik.name)

veronika.gender = "Marill"
print(veronika.gender)


print(veronika.__occupation)
veronika.meno()