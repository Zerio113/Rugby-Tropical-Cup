import locale
import os
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import qrcode


# Ce code sert à indiquer à Python que l'on voudra afficher des dates
# en français lors de l'utilisation de datetime.strptime()
locale.setlocale(locale.LC_TIME, "fr_FR")


# Chargement des fichiers JSON contenant les événements, les stades et les billets
pathevents = os.path.join('.', 'events.json')
pathstade = os.path.join('.', 'stadiums.json')
pathticket = os.path.join('.', 'tickets.json')

with open(pathevents, 'r', encoding='utf-8') as eventsFile:
    events = json.load(eventsFile)
    
with open(pathstade, 'r', encoding='utf-8') as stadiumsFile:
    stadiums = json.load(stadiumsFile)
    
with open(pathticket, 'r', encoding='utf-8') as ticketsFile:
    tickets = json.load(ticketsFile)


# Préparation des polices
pathfontBold = os.path.join('.', 'Akshar-Bold.ttf')
pathfontMedium = os.path.join('.', 'Akshar-Medium.ttf')
aksharBold = ImageFont.truetype(pathfontBold, 42)
aksharMedium = ImageFont.truetype(pathfontMedium, 42)


# Boucle sur chaque billet...
for i in range(len(tickets)):
    # Récupération de l'identifiant du billet
    billet_id = tickets[i]["id"]
    
    # Préparation des textes à écrire
    
    # Ouverture de l'image de fond
    with Image.open("billet.png") as im:
        # Création du code QR à partir de l'identifiant du billet
        qr = qrcode.QRCode(box_size=4)
        qr.add_data(billet_id)
        qr.make()
        qr_im = qr.make_image()
        
        # Insertion du code QR sur l'image du billet
        im.paste(qr_im, (111, 340))
        
        # Récupération de l'identifiant de l'événement associé à ce billet
        events_id = tickets[i]["event_id"] - 1
        
        # Écriture des informations du match sur le billet
        draw = ImageDraw.Draw(im)
        home_team = events[events_id]["team_home"]
        draw.text((877, 115),home_team, font=aksharBold, anchor='ms')
        
        
        away_team = events[events_id]["team_away"]
        draw.text((877, 242),away_team, font=aksharBold, anchor='ms')

        # Récupération des informations du stade où a lieu l'événement
        stadium_id = events[events_id]["stadium_id"] - 1
        stadium_name = stadiums[stadium_id]["name"]
        draw.text((705, 375), stadium_name, font=aksharMedium)

        stadium_localisation = stadiums[stadium_id]["location"]
        draw.text((1155, 375), stadium_localisation, font=aksharMedium)


        # Récupération de la date et de l'heure de l'événement
        start = events[events_id]["start"]
        date= datetime.fromisoformat(start)

        # Affichage de la date sur l'image du billet
        draw.text((705,485),f"{date.day}/{date.month}/{date.year}", font=aksharMedium)

        # Affichage de l'heure sur l'image du billet
        if date.minute == 0:
            draw.text((1155, 485), f"{date.hour}:00", font=aksharMedium)
        else:
            draw.text((1155, 485), f"{date.hour}:{date.minute}", font=aksharMedium)

        # Récupération de la catégorie du billet et affichage dans l'image
        category = tickets[i]["category"]
        draw.text((650, 605), category, font=aksharMedium)


        # Récupération du numéro de siège du billet et affichage dans l'image
        place = tickets[i]["seat"]
        if place == "free":
            place = "Libre"
        draw.text((845, 605), place, font=aksharMedium)


        # Récupération du prix et de la devise du billet, conversion de la devise en symbole et affichage dans l'image
        price = tickets[i]["price"]
        let = tickets[i]["currency"]
        def devise(let):
            switch = {
                "EUR":'€',
                "NZD": '$',
                "JPY": '¥',
                "USD": '$',
                "CAD": '$',
            }
            return switch.get(let)


        amount = str(price) + " " + devise(let)
        draw.text((995, 605), amount, font=aksharMedium)
        
        # Enregistrement de l'image du billet
        im.save(f'./billets/{billet_id}.png')

