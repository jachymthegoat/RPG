class Weapon:
    """
    Weapon reprezentuje zbran ve hre
    
    @Author: jachymnacovsky
    @Date: 01.12.2024
    """
    def __init__(self,name:str,attack:int,defense:int):
        self._name = name
        self._attack = attack
        self._defense = defense

    @property
    def attack(self) -> int:
        return self._attack
    
    @property
    def defense(self) -> int:
        return self._defense
    
    def get_attack(self) -> int:
        "Vraci utok"
        return self.attack
    
    def get_defense(self) -> int:
        "Vraci obranu"
        return self.defense
    
    def __str__(self) -> str:
        "Vraci se string ve formatu jmeno [utok/obrana]"
        ret = f"{self._name} [{self._attack}/{self._defense}]"
        return ret