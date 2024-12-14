from weapon import Weapon
from character import Character

class RPG:
    """
    Hlavni trida urcujici rpg hru

    @Author: jachymnacovsky
    @Date: 01.12.2024
    """
    def input_character(self)-> Character:
        "Zjisti udaje o postave"
        print("Zadejte informace o postavě:")
        name = input("Jméno: ")
        strength = int(input("Síla: ").strip())
        agility = int(input("Hbitost: ").strip())
        vitality = int(input("Vitalita: ").strip())
        return Character(name,strength,agility,vitality)
    
    def input_weapon(self) -> Weapon | None:
        "Zjisti udaje o zbranich"
        print("Zadejte informace o zbrani (nebo prázdný řádek pro žádnou zbraň):")
        name = input("Název: ").strip()
        if not name:
            return None
        attack = int(input("Útočná síla: ").strip())
        defense = int(input("Obranná síla: ").strip())
        return Weapon(name,attack,defense)
    
    def equip_character(self, character: Character, left: Weapon | None, right: Weapon | None):
        "Postave se nactou zbrane"
        if left:
            character.take_weapon(left, Character.HAND_LEFT)
        if right:
            character.take_weapon(right, Character.HAND_RIGHT)

    def fight(self, character1: Character, character2: Character) -> Character:
        "Souboj urci viteze"
        attacker = character1
        defender = character2
        while attacker.is_alive() and defender.is_alive():
            attack_power = attacker.attack()
            defender.defend(attack_power)

            attacker, defender = defender, attacker

        return attacker if attacker.is_alive() else defender

    def run(self):
        print("Postava 1:")
        character1 = self.input_character()
        left_weapon1 = self.input_weapon()
        right_weapon1 = self.input_weapon()

        print("Postava 2:")
        character2 = self.input_character()
        left_weapon2 = self.input_weapon()
        right_weapon2 = self.input_weapon()

        self.equip_character(character1, left_weapon1, right_weapon1)
        self.equip_character(character2, left_weapon2, right_weapon2)

        print("\nZačíná souboj!")
        winner = self.fight(character1, character2)

        print(f"\nVítěz: {winner}")  



if __name__ == "__main__":
    rpg = RPG()
    rpg.run()