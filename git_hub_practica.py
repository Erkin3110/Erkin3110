from os import system as sys
sys ("cls")

class Odam:
    def __init__(self,fullname: str, color: str, country: str, relegion: str, year: str):
        self.fullname = fullname
        self.color = color
        self.country = country
        self.relegion = relegion
        self.year = year

    def get_info(self):
        return f"""odamning fullname: {self.fullname}
 odamning rangi: {self.color}
 odamning mamlakati: {self.country}
 odamning dini :{self.relegion}
 odamning birth_yili: {self.year} """

simple = Odam("Sadio Mane","qora", "africa", "islom", "1993")
print(simple.get_info())