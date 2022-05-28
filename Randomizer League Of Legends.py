import random

print("Hello! Welcome to my League item randomizer!")

# ALL ITEMS
all_boots = ['Berserker\'s Greaves', 'Boots of Swiftness', 'Ionian Boots of Ludicity',
             'Mercury\'s Threads', 'Mobility Boots', 'Plated Steelcaps', 'Sorcerer\'s Shoes']

all_mythic_items = ["Crown of the Shattered Queen", "Divine Sunderer",
                    "Duskblade of Draktharr", "Eclipse", "Evenshroud",
                    "Everfrost", "Frostfire Gauntlet", "Galeforce", "Goredrinker",
                    "Hextech Rocketbelt", "Immortal Shieldbow", "Imperial Mandate",
                    "Kraken Slayer", "Liandry's Anguish", "Locket of the Iron Solari",
                    "Luden's Tempest", "Moonstone Renewer", "Night Harvester", "Prowler's Claw",
                    "Riftmaker", "Shurelya's Battlesong", "Stridebreaker", "Sunfire Aegis",
                    "Trinity Force", "Turbo Chemtank"]

all_legendary_items = ["Abyssal Mask", "Anathema's Chains", "Archangel's Staff", "Ardent Censer",
                       "Axiom Arc", "Banshee's Veil", "Black Cleaver", "Blade of the Ruined King",
                       "Bloodthirster", "Chempunk Chainsword", "Chemtech Putrifier", "Cosmic Drive",
                       "Dead Man's Plate", "Death's Dance", "Demonic Embrace", "Edge of Night",
                       "Essence Reaver", "Force of Nature", "Frozen Heart", "Gargoyle Stoneplate",
                       "Guardian Angel", "Guinsoo's Rageblade", "Horizon Focus", "Hullbreaker",
                       "Infinity Edge", "Knight's Vow", "Lich Bane", "Lord Dominik's Regards",
                       "Manamune", "Maw of Malmortius", "Mejai's Soulstealer", "Mercurial Scimitar",
                       "Mikael's Blessing", "Morellonomicon", "Mortal Reminder", "Nashor's Tooth",
                       "Navori Quickblades", "Phantom Dancer", "Rabadon's Deathcap", "Randuin's Omen",
                       "Rapid Firecannon", "Ravenous Hydra", "Redemption", "Runaan's Hurricane",
                       "Rylai's Crystal Scepter", "Serpent's Fang", "Serylda's Grudge", "Serylda's Grudge",
                       "Silvermere Dawn", "Spirit Visage", "Staff of Flowing Water", "Sterak's Gage",
                       "Stormrazor", "The Collector", "Thornmail", "Titanic Hydra", "Umbral Glaive",
                       "Vigilant Wardstone", "Void Staff", "Warmog's Armor", "Winter's Approach",
                       "Wit's End", "Youmuu's Ghostblade", "Zeke's Convergence", "Zhonya's Hourglass"]

lanes = ['Top', 'Jungle', 'Mid', 'ADC', 'Support']

champions = ('Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie',
             'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand',
             'Braum', 'Caitlyn', 'Camile', 'Cassiopeia', 'Cho\'Gath', 'Corki', 'Darius',
             'Diana', 'Dr.Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal',
             'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar',
             'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi',
             'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx',
             'Kai\'sa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
             'Kayn', 'Kennen', 'Kha\'zix', 'Kindred', 'Kled', 'Kog\'maw', 'LeBlanc',
             'Lee Sin', 'Leona', 'Lilia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite',
             'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana',
             'Nami', 'Nasus', 'Nautilius', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu & Willump',
             'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke' 'Qiyana', 'Quinn', 'Rakan',
             'Rammus', 'Rek\'sai', 'Rell', 'Renata Glasc', 'Renekton', 'Rengar', 'Riven',
             'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco',
             'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain',
             'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh',
             'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot',
             'Varus', 'Vayne', 'Veigar', 'Vel\'Koz', 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir',
             'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone',
             'Yorick', 'Yuumi', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra')
# ==========================

# AD
close_range_ad_mythic = ['Trinity Force', 'Stridebreaker', 'Goredrinker', 'Divine Sunderer',
                         'Kraken Slayer', 'Galeforce', 'Immortal Shieldbow']
close_range_ad_legendary = ['Black Cleaver', 'Blade of the Ruined King', 'Bloodthirster',
                            'Chempunk Chainsword', 'Death\'s Dance', 'Essence Reaver', 'Infinity Edge',
                            'Maw of Malmortius', 'Mercurai Scimitar', 'Mortal Reminder', 'Navori Quickblades',
                            'Phantom Dancer', 'Ravenous Hydra', 'Stormrazor', 'The Collector',
                            'Titanic Hydra', 'Wit\'s End', 'Guardian Angel']
long_range_ad_mythic = ['Trinity Force', 'Kraken Slayer', 'Galeforce', 'Immortal Shieldbow',
                        'Divine Sunderer']
long_range_ad_legendary = ['Blade of the Ruined King', 'Bloodthirster', 'Death\'s Dance',
                           'Essence Reaver', 'Guinsoo\'s Rageblade', 'Infinity Edge',
                           'Lord Dominik\'s Regards', 'Maw of Malmortius', 'Mercurai Scimitar',
                           'Mortal Reminder', 'Manamune', 'Phantom Dancer', 'Rapid Firecannon',
                           'Runaan\'s Hurricane', 'Stormrazor', 'The Collector', 'Wit\'s End'
                                                                                 'Guardian Angel']
boots_ad = ['Berserker\'s Greaves']
# =========================

# AP
ap_mythic = ['Crown of the Shattered Queen', 'Everfrost', 'Hextech Protobelt',
             'Liandry\'s Anguish', 'Luden\'s Tempest', 'Night Harvester', 'Riftmaker', ]
ap_legendary = ['Archangel\'s Staff', 'Banshee\'s Veil', 'Cosmic Drive', 'Demonic Embrace',
                'Horizon Focus', 'Lich Bane', 'Mejai\'s Soulstealer', 'Morellonomicon',
                'Nashor\'s Tooth', 'Rabadon\'s Deathcap', 'Rylai\'s Crystal Scepter',
                'Shadowflame', 'Void Staff', 'Zhonya\'s Hourglass']
boots_ap = ['Mercury\'s Threads', 'Sorcerer\'s Shoes']
# =========================

# Tank
tank_mythic = ['Divine Sunderer', 'Frostfire Gauntlet', 'Goredrinker', 'Stridebreaker',
               'Sunfire Aegis', 'Turbo Chemtank']
tank_legendary = ['Abyssal Mask', 'Anathema\'s Chains', 'Black Cleaver', 'Dead Man\'s Plate',
                  'Fimbulwinter', 'Force of Nature', 'Frozen Heart', 'Gargoyle Stoneplate',
                  'Hullbreaker', 'Randuin\'s Omen', 'Silvermere Dawn', 'Spirit Visage',
                  'Sterak\'s Gage', 'Thornmail', 'Titanic Hydra', 'Warmog\'s Armor', ]
boots_tank = ['Plated Steelcaps', 'Mercury\'s Threads']
# =========================

# Lethality
lethality_mythic = ['Duskblade of Draktharr', 'Eclipse', 'Prowler\'s Claw',]
lethality_legendary = ['Axiom Arc', 'Edge of Night', 'Umbral Glaive', 'The Collector',
                       'Youmuu\'s Ghostblade', 'Serpent\'s Fang']
boots_lethality = ['Ionian Boots of Ludicity', 'Mobility Boots']
# =========================

# Support AP
support_mythic_ap = ['Imperial Mandate', 'Liandry\'s Anguish', 'Luden\'s Tempest',
                     'Night Harvester', 'Riftmaker', 'Shurelia\'s Battlesong',
                     'Moonstone Renewer', ]
support_legendary_ap = ['Archangel\'s Staff', 'Banshee\'s Veil', 'Cosmic Drive', 'Demonic Embrace',
                        'Horizon Focus', 'Lich Bane', 'Mejai\'s Soulstealer', 'Morellonomicon',
                        'Nashor\'s Tooth', 'Rabadon\'s Deathcap', 'Rylai\'s Crystal Scepter',
                        'Shadowflame', 'Void Staff', 'Zhonya\'s Hourglass', 'Ardent Censer',
                        'Chemtech Purifier', 'Redemption', 'Mikael\'s Blessing',
                        'Staff of Flowing Water', 'Vigilant Wardstone', '']
boots_support_ap = ['Mobility Boots', 'Mercury\'s Threads', 'Sorcerer\'s Shoes']
# =========================

# Support AD
support_mythic_ad = ['Divine Sunderer', 'Goredrinker', 'Shurelia\'s Battlesong', 'Stridebreaker',
                     'Trinity Force']
support_legendary_ad = {'Black Cleaver', 'Blade of the Ruined King', 'Bloodthirster',
                        'Chempunk Chainsword', 'Death\'s Dance', 'Essence Reaver', 'Infinity Edge',
                        'Maw of Malmortius', 'Mercurai Scimitar', 'Mortal Reminder', 'Navori Quickblades',
                        'Phantom Dancer', 'Ravenous Hydra', 'Stormrazor', 'The Collector',
                        'Titanic Hydra', 'Wit\'s End', 'Guardian Angel', 'Knight\'s Vow',
                        'Redemption', 'Vigilant Wardstone', 'Zeke\'s Convergence', }
boots_support_ad = ['Mobility Boots', 'Berserker\'s Greaves', 'Plated Steelcaps', ]
# =========================

# Support Tank
support_mythic_tank = ['Sunfire Aegis', 'Turbo Chemtank', 'Shurelya\'s Battlesong',
                       'Locket of the Iron Solari', 'Frostfire Gauntlet', 'Evenshroud']
support_legendary_tank = ['Abyssal Mask', 'Anathema\'s Chains', 'Black Cleaver', 'Dead Man\'s Plate',
                          'Fimbulwinter', 'Force of Nature', 'Frozen Heart', 'Gargoyle Stoneplate',
                          'Hullbreaker', 'Randuin\'s Omen', 'Silvermere Dawn', 'Spirit Visage',
                          'Sterak\'s Gage', 'Thornmail', 'Titanic Hydra', 'Warmog\'s Armor',
                          'Vigilant Wardstone', 'Zeke\'s Convergence', 'Winter\'s Approach',
                          'Redemption', 'Knight\'s Vow']
boots_support_tank = ['Mobility Boots', 'Plated Steelcaps', 'Mercury\'s Threads']
# =========================

type_of_build = ""
mythic_item = ""
legendary_items = ""
boots = ""
random_champion = random.choice(champions)
random_lane = random.choice(lanes)

print(f"Your random picked champion is {random_champion} as {random_lane}")

question = input("Would you like a randomised build? Y/N: ")

if question.upper() == "Y":
    type_of_build = input("Choose a type of build: "
                          " 'Troll'/'AD'/'AP'/'Tank'/'Lethality'/'Support': ")
    if type_of_build.upper() == "AD":
        type_of_build2 = input("What kind of AD? 'Close'/'Ranged': ")
        if type_of_build2.upper() == "CLOSE":
            mythic_item = random.choice(close_range_ad_mythic)
            legendary_items = random.sample(close_range_ad_legendary, 4)
            boots = random.choice(boots_ad)
        elif type_of_build2.upper() == "RANGED":
            mythic_item = random.choice(long_range_ad_mythic)
            legendary_items = random.sample(long_range_ad_legendary, 4)
            boots = random.choice(boots_ad)

    elif type_of_build.upper() == "AP":
        mythic_item = random.choice(ap_mythic)
        legendary_items = random.sample(ap_legendary, 4)
        boots = random.choice(boots_ap)

    elif type_of_build.upper() == "TANK":
        mythic_item = random.choice(tank_mythic)
        legendary_items = random.sample(tank_legendary, 4)
        boots = random.choice(boots_tank)

    elif type_of_build.upper() == "LETHALITY":
        mythic_item = random.choice(lethality_mythic)
        legendary_items = random.sample(lethality_legendary, 4)
        boots = random.choice(boots_lethality)

    elif type_of_build.upper() == "SUPPORT":
        type_of_build2 = input("What kind of Support? 'AP'/'AD'/'Tank': ")
        if type_of_build2.upper() == "AP":
            mythic_item = random.choice(support_mythic_ap)
            legendary_items = random.sample(support_legendary_ap, 3)
            boots = random.choice(boots_support_ap)

        elif type_of_build2.upper() == "AD":
            mythic_item = random.choice(support_mythic_ad)
            legendary_items = random.sample(support_legendary_ad, 3)
            boots = random.choice(boots_support_ad)

        elif type_of_build2.upper() == "TANK":
            mythic_item = random.choice(support_mythic_tank)
            legendary_items = random.sample(support_legendary_tank, 3)
            boots = random.choice(boots_support_tank)
    elif type_of_build.upper() == "TROLL":
        mythic_item = random.choice(all_mythic_items)
        legendary_items = random.sample(all_legendary_items, 4)
        boots = random.choice(all_boots)

legendary_items = " | ".join(legendary_items)

if question.upper() == "Y":
    print(f""" \n Your build for {type_of_build} {random_champion} on {random_lane} is: 
 Mythic item:  {mythic_item}  
 Legendary items:  {legendary_items} 
 Boots: {boots}  
 GL HF!""")
