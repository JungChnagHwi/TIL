from py import Pokemon

class Pikachu(Pokemon):
    no = 25
    type = '전기'

    def __init__(self, name, lv=5):
        #부모 클래스의 메서드를 호출하고자 할 때 사용
        super().__init__()
        #부모 클래스의 메서드를 직접 호출 -> self 연산자로 넘겨야 함
        Pokemon.__init__(self)
        self.name = name 
        self.lv = lv

        #최초의 피카츄가 태어났을 때만, 총 정보를  기록
        #first_child
        super().increase_spcies('피카츄')

        self.number = Pokemon.number_of_pokemon

p1 = Pikachu('지우개')
print(p1.name)
print(Pokemon.number_of_pokemon)
print(Pokemon.discovered_species)
#여기까지


