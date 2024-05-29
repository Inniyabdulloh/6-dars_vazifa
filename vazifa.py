
class Person: # vazifa 2
    counter = 0
    objects = []
    def __init__(self, name):
        self.name = name
        self.objects.append(self)

    def __iter__(self):
        return self

    def __repr__(self):
            return self.name

    def __next__(self):
        try:
            obj = self.objects[Person.counter]
            Person.counter += 1
        except IndexError:
            Person.counter = 0
            raise StopIteration
        return obj



Person('po')
Person("taylung")
Person("kai")

for obj in Person('shifu'):
    print(obj)


class Car: # vazifa 3
    counter = 0
    cars = []
    filter_cars = []
    def __init__(self, name, model, kompany, color):
        self.name = name
        self.model = model
        self.kompany = kompany
        self.color = color
        car_dict = {'name':self.name, 'model':self.model, 'kompany':self.kompany, 'color':self.color}
        self.cars.append(car_dict)

    @staticmethod
    def my_filter(filter_car, value):
        for car in Car.cars:
            # print(f"key:{car[filter_car]} value:{value}" )
            if car[filter_car] == value:
                Car.filter_cars.append(car)


    def __iter__(self):
        filter_car = input("filterni tanlang: name, model, kompany, color  ")
        value = input(f"{filter_car}=?  ")
        Car.my_filter(filter_car, value)
        return self

    def __next__(self):
        try:
            obj = self.filter_cars[Car.counter]
            Car.counter += 1
        except IndexError:
            Car.counter = 0
            Car.filter_cars.clear()
            raise StopIteration

        return obj


    def __repr__(self):
            return self.name


Car('damas', 'damas 2', 'GM', 'oq')
Car('damas', 'damas 2', 'GM', 'oq')
Car('damas', 'damas 2', 'GM', 'oq')
Car('damas', 'damas 2', 'GM', 'oq')
Car('nexia', 'nexia 3', 'GM', 'oq')
Car('nexia', 'nexia 3', 'GM', 'oq')
Car('nexia', 'nexia 3', 'GM', 'qora')
Car('cobalt', 'cobalt 4 ', 'GM', 'qora')
Car('cobalt', 'cobalt 4 ', 'GM', 'qora')

# for car in Car('cobalt', 'cobalt 4 ', 'GM', 'oq'):
#     print(car)



class Student:  # vazifa 4
    counter = 0
    students = []
    __id = 1
    def __init__(self, f_name, l_name):
        self.__id = Student.__id
        self.f_name = f_name
        self.l_name = l_name
        self.students.append(self)
        Student.__id += 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            obj = self.students[Student.counter]
            Student.counter += 1
        except IndexError:
            Student.counter = 0
            raise StopIteration

        return obj.__id

    def __repr__(self):
            return self.f_name

Student('taylung', 'kai')
Student('kai', 'po')

# for obj in Student('taylung', 'kai'):
#     print(obj)