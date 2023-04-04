class DistanceConversion:
    def __init__(self):
        self.__distance = float(input("Enter distance in m: "))

    def __m_to_cm(self):
        return self.__distance * 100

    def __m_to_km(self):
        return self.__distance / 1000

    def __m_to_inch(self):
        return self.__distance * 39.37

    def convert(self):
        cm = self.__m_to_cm()
        km = self.__m_to_km()
        inch = self.__m_to_inch()
        return (cm, km, inch)

    def display(self):
        cm, km, inch = self.convert()
        print(f"{self.__distance}m ={cm}cm")
        print(f"{self.__distance}m ={km}km")
        print(f"{self.__distance}m ={inch}inch")


distance = DistanceConversion()
distance.display()