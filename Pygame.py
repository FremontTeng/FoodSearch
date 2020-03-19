import pygame
import math
import copy
from time import sleep
import FoodSearch
from Function import *
list_dictss ={'Canteen 1':[{'Chicken Rice/Noodles': ['Non-Halal','Not vege',2.00,6.00],
                'Beef Noodles': ['Non-Halal','Non-Veg',2.50,6.50],
                'Western Cuisine': ['Non-Halal','Non-Veg',3.00,10.00],
                'Mala Talk': ['Non-Halal','Non-Veg',2.00,10.00],
                'Handmade Noodles': ['Non-Halal','Non-Veg',2.00,7.00],
                'Chinese Cuisine': ['Non-Halal','Non-Veg',2.50,10.00],
                'Economical Rice': ['Non-Halal','Non-Veg',1.50,7.00],
                'Drinks Stall': ['Halal','Veg',2.50,10.00]},
                '0700-2100',10,455,418,'Red/Green Campus Rider, 179/179A, all alight at opp hall 1 bus-stop'],
 'Canteen 2': [{'Kathy’s Bakery': ['Non-Halal','Non-Veg',0.50,3.00],
                  'Japanese.Western': ['Halal','Non-Veg',3.50,8.00],
                  'Ayam Penyet': ['Halal','Non-Veg',3.00,7.00],
                  'Chicken Rice': ['Non-Halal','Non-Veg',2.00,6.00],
                  'Xiao Long Bao': ['Non-Halal','Non-Veg',2.50,7.00],
                  'Korean Cuisine': ['Non-Halal','Non-Veg',2.50,8.50],
                  'Yong Tau Foo': ['Non-Halal','Non-Veg',1.50,7.00],
                   'Sichuan Cuisine': ['Non-Halal','Non-Veg',2.50,5.00],
                   'Shandong Big Bun': ['Non-Halal','Non-Veg',0.50,5.00],
                   'Economical Rice': ['Non-Halal','Non-Veg',1.50,7.00],
                   'Waffles': ['Non-Halal','Veg',1.00,4.00],
                  'La Kopi': ['Halal','Veg',1.00,5.00]},
                  '0700-2100',10,495,349,'Red/Green Campus Rider, 179/179A, all alight at hall 2 bus-stop'],
    'Pioneer':[{'Thai Store': ['Non-Halal','Not vege',3.00,25.00],
                  'Economic Rice/Bee Hoon': ['Non-Halal','Non-Veg',1.50,6.00],
                  'Yong Tao Fu/Mini Wok': ['Non-Halal','Non-Veg',2.00,10.00],
                  'Korean Food': ['Halal','Non-Veg',3.50,10.00],
                  'Fruit Juice Stall': ['Halal','Veg',1.50,5.00],
                   'Drinks Stall': ['Halal','Veg',2.50,5.00]},
                '0700-2100', 10,538,540,'Red/Green Campus Rider, 179/179A, all alight at opp hall 1 bus-stop'],
     'North Hill':[{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'A&W Noodle': ['Non-Halal','Non-Veg',4.00, 5.00],
                        'Mala': ['Non-Halal','Not vege',4.00, 6.00],
                       'YUM': ['Non-Halal','Non-Veg',4.5,7.0],
                        'Ah Boon Fish Soup': ['Halal','Non-Veg',4.0,5.5,765,233]},
                        '0700-2200',10,765,233,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Canteen 11': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,708,172,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Canteen 9': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,568,252,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Thamarin': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,677,117,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Canteen A': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,293,233,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Canteen B': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,198,434,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],
    'Quad': [{'mix rice': ['Non-Halal','Non-Veg',2.40, 5.00],
                        'Japanese Cuisine': ['Non-Halal','Non-Veg',3.80, 6.80],
                        'Waffles & Pastries': ['Halal','Not-Veg',1.80, 3.50],
                       'Noodle Stall': ['Non-Halal','Non-Veg',4.00,5.00],
                        'Sichuan Fragrant Garden': ['Non-Halal','Non-Veg',4.00,8.00]},
                   '0700-2400',10,189,326,'Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop'],}

List_dict ={'Canteen 1':
 ['0700-2100' #opening hrs
, 3 #ranking
, '455,418'#location
, ['Red/Green Campus Rider, Campus Weekend Rider, 179/179A, all alight at hall 1 bus-stop']#Miscelleanous Information
,{'Chicken Rice/Noodles': ['Non-Halal','Non-Veg',2.00,6.00,
                            ["Chicken rice","Chicken noodles"]
                            ]},

                  {'Beef Noodles': ['Non-Halal','Non-Veg',2.50,6.50,
                                    ['Beef Noodles']
                                    ]},

                  {'Western Cuisine': ['Non-Halal','Non-Veg',3.00,10.00,
                                       ['Fish and Chips','Chicken Chop']
                                       ]},

                  {'Mala Talk': ['Non-Halal','Non-Veg',2.00,10.00,
                                ["Mala"]
                                 ]},

                  {'Handmade Noodles': ['Non-Halal','Non-Veg',2.00,7.00,
                                        ["Fishball Noodles"]
                                        ]},

                  {'Chinese Cuisine': ['Non-Halal','Non-Veg',2.50,10.00,
                                        ["Fried Rice"]
                                       ]},

	      {'Economical Rice': ['Non-Halal','Non-Veg',1.50,7.00,
                                   ["Fried Rice"]
                                   ]},

	      {'Drinks Stall': ['Halal','Veg',2.50,10.00,
                                ["Watermelon"]
                                ]}


  ],


    'Canteen 2':
['0700-2100' #opening hrs
, 10 #ranking
, '450,400'#location
, ['Red/Green Campus Rider, Campus Weekend Rider, 179/179A, all alight at hall 1 bus-stop'#Miscelleanous Information
   ],
                 {'Kathy’s Bakery': ['Non-Halal','Non-Veg',0.50,3.00,["Hotdog"]]},
                  {'Japanese.Western': ['Halal','Non-Veg',3.50,8.00,["Chicken Bento Set"]]},
                  {'Ayam Penyet': ['Halal','Non-Veg',3.00,7.00,["Chicken Rice"]]},
                  {'Chicken Rice': ['Non-Halal','Non-Veg',2.00,6.00,["Chicken Rice"]]},
                  {'Xiao Long Bao': ['Non-Halal','Non-Veg',2.50,7.00,["Siew Mai"]]},
                  {'Korean Cuisine': ['Non-Halal','Non-Veg',2.50,8.50,["Kimichi Fried Rice"]]},
	      {'Yong Tau Foo': ['Non-Halal','Non-Veg',1.50,7.00,["Souped Rice"]]},
	      {'Sichuan Cuisine': ['Non-Halal','Non-Veg',2.50,5.00,["Beef Noodles"]]},
	      {'Shandong Big Bun': ['Non-Halal','Non-Veg',0.50,5.00,["Steamed Buns" ]]},
	      {'Economical Rice': ['Non-Halal','Non-Veg',1.50,7.00,["Mixed Veg Rice"]]},
	      {'Waffles': ['Non-Halal','Veg',1.00,4.00,["Australian Cream Waffle"]]},
                  {'La Kopi': ['Halal','Veg',1.00,5.00,["Teh O"]]}


 ],

'Pioneer Food Court':
['0700-2100' #opening hrs
, 5 #ranking
, '300,278'#location
, ['Red/Green Campus Rider, Campus Weekend Rider, 179/179A, all alight at hall 1 bus-stop']#Miscelleanous Information
,
                 {'Thai Store': ['Non-Halal','Not-Veg',3.00,25.00,["Pineapple Fried Rice"]]},
                  {'Economic Rice/Bee Hoon': ['Non-Halal','Non-Veg',1.50,6.00,["Bee Hoon"]]},
                  {'Yong Tao Fu/Mini Wok': ['Non-Halal','Non-Veg',2.00,10.00,["Fish Soup"]]},
                  {'Korean Food': ['Halal','Non-Veg',3.50,10.00,["Raumen","Kimchi Fried Rice"]]},
                  {'Fruit Juice Stall': ['Halal','Veg',1.50,5.00,["Watermelon","Kiwi"]]},
	      {'Drinks Stall': ['Halal','Veg',2.50,5.00,["Lemon Tea","Teh O"]]},
                  {'Western Stall': ['Halal','Non-Veg',2.50,8.00,["Pasta","Spaghetti", "Chicken", "Pork", "Salad"]]}


  ],

     'Canteen North Hill':


['0700-2200'
,1
,'756,233'
,['Blue Campus opp hall 11 bus-stop or Red Campus, 199 hall 11 bus-stop']
  ,
  {'Mix Rice':['Non-Halal','Non-Veg',2.40, 5.00,["Mixed Veg Rice"]]},
                        {'A&W Noodle': ['Non-Halal','Non-Veg',4.00, 5.00,["Spaghetti"]]},
                        {'Mala': ['Non-Halal','Not-Veg',4.00, 6.00,["Mala"]]},
                       {'YUM': ['Non-Halal','Non-Veg',4.5,7.0,["Fish and Chips"]]},
		{'Ah Boon Fish Soup': ['Halal','Non-Veg',4.0,5.5,765,233,["Fish Soup"]]}

],

    'Quad Cafe':
['0700-2200'
,2
,'189,326'
,['Green Campus Rider/ Campus Weekend Rider alight at Administration Building OR Red Campus Rider/Campus Weekend Rider alight Outside School of Biological Sciences']
,
{'Mix Economic Rice': ['Non-Halal','Non-Veg',2.10, 4.00,["Mixed Veg Rice"]]},
{'Fruits and Beverages': ['Halal','Veg',1.20, 3.00,["Watermelon"]]},
{'Korea Food': ['Halal','Non-Veg',2.60, 6.50,["Cheesy Raumen"]]},
{'Chicken Rice': ['Halal','Non-Veg',2.80, 4.00,["Chicken Rice"]]},
{'Nasi Pandang': ['Halal','Non-Veg',3.00, 5.50,["Nasi Lemak"]]},
{'Fried Yong Tau Fu': ['Halal','Non-Veg',2.40, 4.00,["Yong Tau Fu"]]},
{'Anada Kitchen': ['Halal','Non-Veg',1.20, 6.50,["Prata"]]}

],


    'North Spine Food Court':

[
'0700-2200'
,6
,'293,233'
,['Red Campus Rider/ Campus Weekend Rider, Bus 179, 179A alight Outside Canteen A & Lee Wee Nam Library / Opposite NIE OR Blue Campus Rider , Bus 199 alight Outside Canteen A & Lee Wee Nam Library / Outside NIE']
,
{'Italian Pasta': ['Non-Halal','Non-Veg',3.80, 7.00,["Fish and Chips","Tomato Pasta", "Chicken", "Fish", "Pork Chop"]]},
{'Vietnam Cuisine': ['Non-Halal','Non-Veg',4.20, 6.00,["Glass Noodles"]]},
{'BBQ Delight': ['Non-Halal','Non-Veg',4.50, 6.50,["Roasted Chicken"]]},
{'Japanese/Korean Delight': ['Non-Halal','Non-Veg',4.50, 7.00,["Bento Set"]]},
{'Claypot Rice': ['Non-Halal','Non-Veg',3.80, 7.50,["Chicken Claypot Rice"]]},
{'Fishball Noodles': ['Non-Halal','Non-Veg',2.90, 4.50,["Fish Ball Noodles"]]},
{'Roasted Duck': ['Non-Halal','Non-Veg',1.20, 6.50,["Prata"]]}

],

'Koufu':

['0700-2200'
,7
,'198,434'
,['Red Campus Rider/ Campus Weekend Rider, Bus 179, 179A alight Outside Canteen A & Lee Wee Nam Library / Opposite NIE OR Blue Campus Rider , Bus 199 alight Outside Canteen A & Lee Wee Nam Library / Outside NIE']


    ,
    {'Indian Food': ['Halal','Non-Veg',3.00, 8.00,["Prata","Curry chicken"]]},
{'Yong Tau Fu': ['Non-Halal','Non-Veg',2.00, 7.00,["Yong Tau Fu"]]},
{'Chicken Rice Stall’': ['Non-Halal','Non-Veg',2.50, 6.50,["Roasted Chicken Rice, Steamed Chicken Rice"]]},
{'Pasta Stall': ['Non-Halal','Non-Veg',3.50, 7.00,["Pasta", "Spaghetti"]]},
{'Mixed Vegetables Rice': ['Non-Halal','Non-Veg',2.50, 8.50,["Mixed Vegetables Rice"]]},
{'Japanese Store': ['Non-Halal','Non-Veg',3.00, 6.00,["Udon", "Curry Chicken Cutlet", "Curry Pork Cutlet"]]},
{'Desserts Stall': ['Non-Halal',1.20, 6.50,["Desserts"]]},
{'Beverages': ['Halal',1.00, 5.00,["Drinks"]]},
{'Dim Sum': ['Non-Halal','Non-Veg',0.50, 3.00,["Steamed Buns", "Siew Mai", "Rice"]]},
{'Vegetarian Stall': ['Non-Halal','Veg',1.00, 6.50,["Vegetarian Rice"]]},
{'Salad Stall': ['Non-Halal','Veg',1.20, 5.00,["Salads"]]},
{'Rice Bowl Stall': ['Non-Halal','Non-Veg',1.00, 5.00,["Rice"]]}


],

'MacDonald’s':

['0700-2200'
,4
,'198,434'
,['Red Campus Rider/ Campus Weekend Rider, Bus 179, 179A alight Outside Canteen A & Lee Wee Nam Library / Opposite NIE OR Blue Campus Rider , Bus 199 alight Outside Canteen A & Lee Wee Nam Library / Outside NIE']
,

    {'MacDonald’s': ['Halal','Non-Veg',2.00, 13.00,["MacDonald’s", "MacSpicy", "MacChicken","BigMac", "Fillet O Fish", "MacNuggests", "Fries", "Drinks"]]},


],

'Peach Garden Chinese Restaurant':

['1100-2200'
,8
,'198,434'
,['Red Campus Rider/ Campus Weekend Rider, Bus 179, 179A alight Outside Canteen A & Lee Wee Nam Library / Opposite NIE OR Blue Campus Rider , Bus 199 alight Outside Canteen A & Lee Wee Nam Library / Outside NIE']
,

    {'Peach Garden Chinese Restaurant': ['Non-Halal','Non-Veg', 5.00, 50.00,["Steamed Buns", "Rice", "Chicken", "Carrot Cake", "Springrolls", "Fish", "Pork", "Drinks"]]}
],

'Pizza Hut Express':

['1100-2200'
,9
,'198,434'
,['Red Campus Rider/ Campus Weekend Rider, Bus 179, 179A alight Outside Canteen A & Lee Wee Nam Library / Opposite NIE OR Blue Campus Rider , Bus 199 alight Outside Canteen A & Lee Wee Nam Library / Outside NIE']
,

    {'Pizza Hut Express': ['Halal','Non-Veg', 4.00, 30.00,["Pizza", "Pasta", "Rice", "Drinks"]]}
]



 }




bus_stop = {"Hall 11" : (743,206,1), "Grad Hall" : (770,136,2) ,"Hall 23" : (653,110,3) ,"Hall 12 & 13": (446,80,4),
            "LWN library" : (319,197,5) , "SCE" : (166,225,6) ,"SPMS" : (78,355,7) , "Hall 7" : (94,491,8),
            "Innovation Centre" : (226,483,9) ,"Hall 4" : (361,511,10) ,"Hall 1": (479,511,11) ,"Canteen 2" : (507,343,12),
            "Hall 8 & 9" : (599,264,13)}


foodlist = []
canteenlist = []



for a in List_dict.items():
    canteenlist.append([a[0],(a[1][-2])])
    for b in a[1]:
        try:
            for c in b.values():
                for d in c[4]:
                    e = d.upper()
                    foodlist.append([a[0],e])
        except:
            pass
#Colour index
b = (0,0,0)
hh = (82, 86, 158)
bl= (6, 158, 36)
w = (255,255,255)
y = (181, 154, 3)

# First Condition
run = True
getlocation = False
preference = False
halals = False
criteria = False
choose = True
looping = True





while looping:
    FoodSearch.routine_update()
    print()
    print("1 : Location")
    print("2 : Food Search")
    print("3 : Ranking")
    print("4 : Pricing")
    print("5 : Update Information")
    print("6 : What time is it?")
    print("0 : Exit")

    selection_interface = input("Select by :")
    if selection_interface == "2":
        #looping = False

        #print (foodlist)
        #print(canteenlist)


        while True:
            print("")
            FoodSearch.search_by_food(List_dict)
            break
        continue
    elif selection_interface == "1":
        looping = False
        try:
            pygame.init()
            pygame.font.init()
            introScreenImage = pygame.image.load("New Map.png")
            screen = pygame.display.set_mode((1200,800))
            screen.blit(introScreenImage,(0,0))
            pygame.display.flip()
            while run:
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                while not getlocation:
                    display_text("Select your location",w,820,30,25,pygame,screen)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            mx, my = pygame.mouse.get_pos()
                            location = (mx,my)
                            pin_image = pygame.image.load("Pin1.png")
                            screen.blit(pin_image,(mx-9,my-30))
                            pygame.display.update()
                            print(location)
                            display_text("Select your location",b,820,30,25,pygame,screen)
                            display_text("{0} is your location coordinate".format(location),y,820,8,15,pygame,screen)
                            pygame.display.update()
                            getlocation = True
                            Canteen_location=[(455,418),(708,172),(765,233),(568,252),(293,233),(198,434),(189,326),(677,117),(538,540),(495,349)]
                            for i in Canteen_location:
                                draw_line(location,i,pygame,screen)
                dicts_new, distance_list = total_distance(list_dictss,location,copy)
                prices , distance = preferences(preference,pygame,screen)
                halal , vege = halal(halals,pygame,screen)
                screen.fill(w)
                pygame.display.update()
                sorted_distance = distance_sort(distance_list)

                if prices==1:
                    price_display(dicts_new,sorted_distance,choose,pygame,screen,list_dictss)
                else:
                    distance_display(dicts_new,sorted_distance,choose,pygame,screen,list_dictss)

            pygame.quit()
        except:
            pass
    elif selection_interface == "3":
        #looping = False
        while True:
            print()
            FoodSearch.search_by_ranking()
            break
        continue
    elif selection_interface == "4":
        #looping = False
        while True:
            print()
            FoodSearch.search_by_pricing()
            break
        continue
    elif selection_interface == "0":
        looping = False
        print()
        print("Thank you for your time and see you again!")
        print()
        exit()
        break
    elif selection_interface == "5":
        FoodSearch.update_info()
        continue
    elif selection_interface == "6":
        FoodSearch.time()
        continue
    else:
        continue

    if selection_interface == "1":
        print("")
        print("")
        print("Which Canteen that you choose? ")
        choosed_location,the_canteen = please_choose(list_dictss)
        bus_stops = find_bus_stop(location, bus_stop ,choosed_location,math)



        pygame.init()
        pygame.font.init()
        introScreenImage = pygame.image.load("New Map.png")
        screen = pygame.display.set_mode((1000,650))
        screen.blit(introScreenImage,(0,0))
        pygame.display.flip()
        pin_image = pygame.image.load("Pin1.png")
        runs = True
        try:
            while runs:

                pygame.time.delay(100)

        #Pin and texxt for bus-stop
                screen.blit(pin_image,(mx-9,my-30))
                screen.blit(pin_image,(bus_stop[bus_stops][0]-9,bus_stop[bus_stops][1]-30))
                screen.blit(pin_image,(bus_stop[choosed_location][0]-9,bus_stop[choosed_location][1]-30))
                screen.blit(pin_image,(list_dictss[the_canteen][3]-9,list_dictss[the_canteen][4]-30))
                pygame.draw.rect(screen, w, [mx-9, my-44, 300, 30])
                pygame.draw.rect(screen, w, [bus_stop[bus_stops][0]-9, bus_stop[bus_stops][1]-43, 300, 30])
                pygame.draw.rect(screen, w, [bus_stop[choosed_location][0]-9, bus_stop[choosed_location][1]-43,300,30])
                pygame.draw.rect(screen, w, [list_dictss[the_canteen][3]-9, list_dictss[the_canteen][4]-43,300,30])
                display_text("Your Location",hh,mx-9,my-50,25,pygame,screen)
                display_text("The {0}'s bus stop".format(bus_stops),hh,bus_stop[bus_stops][0]-9,bus_stop[bus_stops][1]-50,25,pygame,screen)
                display_text("The Canteen".format(bus_stops),hh,list_dictss[the_canteen][3]-9,list_dictss[the_canteen][4]-50,25,pygame,screen)
                display_text("The {0}'s bus stop".format(choosed_location),hh,bus_stop[choosed_location][0]-9,bus_stop[choosed_location][1]-50,25,pygame,screen)




                draw_line((mx,my),(bus_stop[bus_stops][0],bus_stop[bus_stops][1]),pygame,screen)
                draw_line((bus_stop[bus_stops][0],bus_stop[bus_stops][1]),(bus_stop[choosed_location][0],bus_stop[choosed_location][1]),pygame,screen)
                draw_line((bus_stop[choosed_location][0],bus_stop[choosed_location][1]),(list_dictss[the_canteen][3],list_dictss[the_canteen][4]),pygame,screen)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
        except:
            print("")

        print("")
        print("")
        print("Any feedbacck for the program? ")
        print("If there is no feedback please enter: None")
        Feedback = input()
        if Feedback.upper() == "NONE":
            print("Thank you")
        else:
            feedback_file = open("Feedback.txt","a")
            feedback_file.write("\n" + Feedback+ "\n\n")
            feedback_file.close()
            print("Thank you")
    else:
        break
