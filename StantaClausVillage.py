from datetime import datetime


class Village():
    village_name = "SANTA CLAUS VILLAGE"
    latitude = "N 66° 32.6168'"
    longitude = "E 25° 50.8318'"
    def __init__(self): 
        pass
    def __str__(self):
        return f"{self.village_name} is located at {self.latitude} and {self.longitude}"



class Building(Village):
    def __init__(self, year_of_construction, storeys_number, building_area=""):
        self.year_of_construction = year_of_construction
        self.storeys_number = storeys_number
        self.building_area = building_area

##    def __str__(self):
##        return f"built in: {self.year_of_construction}\nstoreys number: {self.storeys_number}\n\
##location: {self.village_name} ,  {self.latitude}  {self.longitude}"
    

class Factory(Building):
    function = "factory"
    factory_production = ""
    factory_workers = []

    def production(self, prod ):
        self.factory_production = prod
        return self.factory_production

    def add_worker(self, worker):
        self.factory_workers.append(worker)
        return self.factory_workers 

    def __str__(self):
        return f"building function: {self.function}\nproduction: {self.factory_production}\n\
built in: {self.year_of_construction}\nstoreys number: {self.storeys_number}\n\
location: {self.village_name} ,  {self.latitude}  {self.longitude}" 



class ResidentialBbuilding(Building):
    function = "residential building"
    inhabitants = 0
    def inhabitants_nb(self, inhabitants):
        self.inhabitants_nb = inhabitants
        return self.inhabitants_nb

    def addinhabitant(self, number):
        try:
            self.inhabitants += int(number)
        except:
            pass
        return self.inhabitants

    def removeinhabitant(self, number):
        try:
            self.inhabitants -= int(number)
        except:
            pass
        return self.inhabitants

    def __del__(self): 
        print(f"{function} deleted.")

    def __str__(self):
        return f"building function: {self.function}\nnumber of inhabitants: {self.inhabitants}\n\
built in: {self.year_of_construction}\nstoreys number: {self.storeys_number}\n\
location: {self.village_name} ,  {self.latitude}  {self.longitude}" 



class StClaus():
    personal_name = "SANTA CLAUS "
    role = "The boss of all bosses"
    status = "saint"
    def __init__(self):   
        pass
    def __str__(self):
        return f"name: {self.personal_name}\nrole: {self.role}\nstatus: {self.status}" 



class Elf():
    def __init__(self, name, birth_year=""):
        self.name = name
        self.birth_year = birth_year
        try:
            self.age = datetime.now().year - int(self.birth_year)
        except:
            self.age = "unknown"
    


class FactoryWorker(Elf):
    profession = "factory worker"
    specialist = ""
    efficiency = 0
    def specialization(self, spec):
        self.specialist = spec
        return self.specialist

    def producted_pieces(self, number):
        try:
            self.efficiency = self.efficiency + int(number)
        except:
            pass

    def get_efficiency(self):
        print(f"{self.name} has produced {self.efficiency} pieces of {self.specialist}")

    def __str__(self):
        return f"name: {self.name}\nage: {self.age}\nprofession: {self.profession}\n\
specialization: {self.specialist}" 



class Animal():
    species = ""
    def __init__(self, name, coat_color, birth_year= ""):
        self.name = name
        self.birth_year = birth_year
        self.coat_color = coat_color
        try:
            self.age = datetime.now().year - int(self.birth_year)
        except:
            self.age = "unknown"

    def __str__(self):
        return f"species: {self.species}\nname: {self.name}\n\
coat color: {self.coat_color}\nage: {self.age}"

    

class Reindeer(Animal):
    species = "reindeer"
    super(Animal).__str__()
    def __del__(self): 
        print(f"Reindeer named {self.name} deleted.")



class Dog(Animal):
    species = "dog"
    super(Animal).__str__()
    def __del__(self): 
        print(f"Dog named {self.name} deleted.")    



        

print("\n---Santa Claus Village information------")
st_claus_village= Village()
print(st_claus_village)

print("\n\n-----Santa Claus------")
santa_claus = StClaus()
print(santa_claus)



print("\n\n-----factory workers information------------")
ron = FactoryWorker("Ron" , 1999)
ron.specialization("teddy bears")
print(ron)
print("\n--information about the production achievements")
ron.producted_pieces(3)
ron.get_efficiency()
print("\n")
tim = FactoryWorker("Tim" , 2001)
tim.specialization("plush bunnies")
print(tim)


print("\n\n-----------factory  ------------")
toys_factory = Factory(1988, 4, 25)
#---set factory producytion profile--
toys_factory.production("plush toys")
toys_factory.add_worker(ron)
toys_factory.add_worker(tim)
print(toys_factory)
toys_factory.add_worker(ron)
toys_factory.add_worker(tim)
print("\n factory workers:\n")
for i in range(len(toys_factory.factory_workers)):
    print(f"{toys_factory.factory_workers[i]}\n")


print("\n\n-----------elfs' house ------------")
house_of_elfs = ResidentialBbuilding(1988, 4, 25)
house_of_elfs.inhabitants_nb(7)
print(house_of_elfs)
print("\n--after adding inhabitants--")
house_of_elfs.addinhabitant(13)
print(house_of_elfs)
print("\n--after removing inhabitants--")
house_of_elfs.removeinhabitant(10)
print(house_of_elfs)



print("\n\n------reindeer ------------")
rudolf= Reindeer("Rudolf", "brown", 2013)
print(rudolf)

print("\n\n-------dog ---------")
barry= Dog("Barry","white")
print(barry)



        
