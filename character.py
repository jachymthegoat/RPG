from weapon import Weapon

class Character:
    """
    Character reprezentuje postavu v RPG hre

    @Author: jachymnacovsky
    @Date: 01.12.2024
    """
    HAND_RIGHT : int = 0
    HAND_LEFT : int = 1

    def __init__(self,name:str,strength:int,agility:int,vitality:int):
        self._name = name
        self._strength = strength
        self._agility = agility
        self._vitality = vitality
        self._current_vitality = vitality
        self._right_hand_empty = True
        self._left_hand_empty = True
        self.rightweapon : Weapon
        self.leftweapon : Weapon

    def attack(self) -> int:
        "Vraci celkovy vypocitany utok"
        total_attack = self._strength
        if not self._right_hand_empty:
            total_attack += self.rightweapon.get_attack()
        if not self._left_hand_empty:
            total_attack += self.leftweapon.get_attack()
        return total_attack

    def defend(self,attack:int) -> int:
        "Spocita celkovou obranu a vrati utrzene poskozeni"
        total_defense = self._agility
        if not self._right_hand_empty:
            total_defense += self.rightweapon.get_defense()
        if not self._left_hand_empty:
            total_defense += self.leftweapon.get_defense()

        damage = max(0, attack-total_defense)
        self._current_vitality -= damage
        self._current_vitality = max(0,self._current_vitality)
        return damage
    
    def is_alive(self) -> bool:
        "Zjisti jestli je postava nazivu"
        if self._current_vitality>0:
            return True
        return False
    
    def take_weapon(self,weapon: Weapon | None, hand:int) -> bool:
        "Dava postave do rukou zbrane"
        if hand == 0:
            if self._right_hand_empty and weapon is not None:
                self.rightweapon = weapon
                self._right_hand_empty = False
                return True
        elif hand == 1:
            if self._left_hand_empty and weapon is not None:
                self.leftweapon = weapon
                self._left_hand_empty = False
                return True
        return False
    
    def __str__(self) -> str:
        "Vraci string ve formatu jmeno [zivoty] (utok/obrana)"
        attack_value = self.attack()
        defense_value = self._agility
        if not self._left_hand_empty:
            defense_value += self.leftweapon.get_defense()
        if not self._right_hand_empty:
            defense_value += self.rightweapon.get_defense()
        return f"{self._name} [{self._current_vitality}] ({attack_value}/{defense_value})"