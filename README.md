# Mini-Projet n°1 – Programmation (UNamur)

Projet réalisé dans le cadre du cours **Programmation – Bac 1 Informatique (Université de Namur)**.  
Le but est de créer un petit jeu textuel basé sur des personnages, des créatures et un système de combat, en utilisant le module `gaming_tools`.

---

## Fonctionnalités principales

- **new_game()** → réinitialise la partie et donne 50 pièces d’or à l’équipe  
- **new_character(name, type)** → crée un nouveau personnage (dwarf, elf, healer, wizard, necromancer)  
- **create_new_creature()** → ajoute une créature avec des stats aléatoires  
- **attack(character, creature)** → gère le combat entre un personnage et une créature  
- **use_special_power(character, target)** → active le pouvoir spécial du personnage  
- **lvl_up(character)** → permet au personnage de gagner en force ou en vie  

---

## Exemple d’utilisation

```python
from main import *

new_game()
new_character("Aragorn", "elf")
create_new_creature()
attack("Aragorn", "creature_1")
use_special_power("Aragorn", "creature_1")
lvl_up("Aragorn")
