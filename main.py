#testteststestest
class Customer:
    def __init__(self, name,phone):
        self.__name = name
        self.phone = phone
        self.__cars = []

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, raqam):
        if len(raqam) == 12:
            self.__phone = raqam
        else:
            raise ValueError('telefon raqami 12 tadan iborat bolilishi kerak')


    @property
    def cars(self):
        return self.__cars[:]

    def add_car(self, car):
        self.__cars.append(car)

    def list_cars(self):
        for car in self.__cars:
            print(car)


class Car:
    def __init__(self,model,year,mileage):

        self.__model = model
        self.year = year
        self.__mileage = mileage



    @property
    def model(self):
        return self.__model


    @property
    def year(self):
        return self.__year


    @year.setter
    def year(self,year):

        if year > 1990:
            self.__year = year
        else:
            raise ValueError("Eski moshinani qabul qilmaymiz")


    @property

    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self,mileage):
        if mileage > self.__mileage:
            self.__mileage = mileage
        else:
            raise ValueError("Mileage faqat oshadi!")



matiz = Car('Matiz',2026,10567)

matiz.mileage = 233388
print(matiz.mileage)








