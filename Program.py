import GameTypes
import GameThemes
import FrameworksLanguages
import ExtraChallenges

import random
import csv
try:
    with open("ISUyIBMersHackaton2023.csv", "x") as file:
        writer = csv.writer(file)
        writer.writerow(["Equipo", "Tipo de juego", "Tema del juego", 
                         "Framework/Lenguaje", "Desafío adicional"])
except Exception:
    pass

break_loop = "n"
while break_loop != "s":
    game_type = random.choice(GameTypes.game_types)
    theme = random.choice(GameThemes.game_themes)
    frame_lang = random.choice(FrameworksLanguages.frameworks_languages)
    extra_challenge = random.choice(ExtraChallenges.extra_challenges)

    team = input("Ingrese el nombre del equipo: ")

    ready_string = f'Equipo: {team}, '\
        + f'deberán hacer un juego de tipo: {game_type}, '\
        + f'con una temática de: {theme}, '\
        + f'utilizando el framework y lenguaje: {frame_lang} '\
        + f'e implementar como desafío adicional: {extra_challenge}.'
    print(ready_string)
    
    with open("ISUyIBMersHackaton2023.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([team, game_type, theme, frame_lang, extra_challenge])
    
    break_loop = input('Presione "s" para salir o cualquier otra cosa si desea ingresar otro equipo: ').lower()

