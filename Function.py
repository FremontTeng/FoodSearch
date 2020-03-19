import pygame

#==========================================================================================================================

# Display Text function
def display_text(text,colour,x,y,size,pygame,screen):
    myfont = pygame.font.SysFont('Comic Sans Ms',size)
    texts = myfont.render(text,False,colour)
    screen.blit(texts,(x,y))

#==================================================================================================================================

# Display Line
def draw_line(Start_Pos, End_Pos,pygame,screen):

    bl= (6, 158, 36)

    pygame.draw.line(screen, bl,Start_Pos,End_Pos,3)
    pygame.display.update()

#==================================================================================================================================

#Box text
def box_text_list(lists,to_print,pygame,screen):
    b = (0,0,0)


    initial_location = [10,10]
    for i in range(len(lists)):
        box_text(initial_location,lists[i],pygame,screen)
        pygame.display.update()
        display_text(to_print[i],b,initial_location[0]+150,initial_location[1]+10,20,pygame,screen)
        initial_location[1]+=80

#==================================================================================================================================

#Box and text
def box_text(position, text,pygame,screen):
    rect_image = pygame.image.load("Rect1.png").convert()
    screen.blit(rect_image,position)
    display_text(text,(0,0,0),position[0]+10,position[1]+10,25,pygame,screen)

#=============================================================================================================================

#What to print in the pygame
def print_distance_sort(dicts,thelist):
    canteen=[]
    list_to_print=[]
    for i in thelist:
        for k in dicts:
            if i == dicts[k][6]:
                canteen.append(k)
                list_to_print.append(" : is {0}m from you".format(i))
    return canteen, list_to_print

#=============================================================================================================================

# Finding distance Function
def total_distance(dicts,location,copy):
    total_distance_list = []
    dicts_new = copy.deepcopy(dicts)
    for i in dicts:
        X_dist = location[0] - dicts[i][3]
        Y_dist = location[1] - dicts[i][4]
        total_dist = (((X_dist**2)+(Y_dist**2))**(0.5))*(1.205782)
        dicts_new[i].append(round(total_dist,3))
        total_distance_list.append(round(total_dist,3))
    return dicts_new, total_distance_list

#============================================================================================================================


#=============================================================================================================================
# Merge Sort
def distance_sort(thelist):
    if len(thelist)>1:
        mid = len(thelist)//2
        leftlist = thelist[:mid]
        rightlist = thelist[mid:]
        distance_sort(leftlist)
        distance_sort(rightlist)

        i = 0
        j= 0
        k = 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                thelist[k] = leftlist[i]
                i +=1
            else:
                thelist[k] = rightlist[j]
                j+=1
            k+=1
        while i< len(leftlist):
            thelist[k] = leftlist[i]
            i+=1
            k+=1
        while j < len(rightlist):
            thelist[k] = rightlist[j]
            j+=1
            k+=1
    return(thelist)

#===========================================================================================================================

#Printing the dictionary
def print_distance_sort(dicts,thelist):
    canteen=[]
    list_to_print=[]
    for i in thelist:
        for k in dicts:
            if i == dicts[k][6]:
                canteen.append(k)
                list_to_print.append(" : is {0}m from you".format(i))
    return canteen, list_to_print

#==========================================================================================================================



def halal(halals,pygame,screen):
    b = (0,0,0)
    bl= (6, 158, 36)
    w = (255,255,255)
    y = (181, 154, 3)
    while not halals:
        display_text("Halal/Vegetarian?",w,820,30,25,pygame,screen)
        display_text("Halal (Press h)",w,820,55,25,pygame,screen)
        display_text("Vegetarian (Press v)",w,820,80,25,pygame,screen)
        display_text("Both (Press b)",w,820,105,25,pygame,screen)
        display_text("None of the above (Press n)",w,820,130,25,pygame,screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_h):

                    display_text("Halal/Vegetarian?",b,820,30,25,pygame,screen)
                    display_text("Halal (Press h)",b,820,55,25,pygame,screen)
                    display_text("Vegetarian (Press v)",b,820,80,25,pygame,screen)
                    display_text("Both (Press b)",b,820,105,25,pygame,screen)
                    display_text("None of the above (Press n)",b,820,130,25,pygame,screen)
                    pygame.display.update()
                    halals = True
                    return 1,0
                elif (event.key == pygame.K_v):

                    display_text("Halal/Vegetarian?",b,820,30,25,pygame,screen)
                    display_text("Halal (Press h)",b,820,55,25,pygame,screen)
                    display_text("Vegetarian (Press v)",b,820,80,25,pygame,screen)
                    display_text("Both (Press b)",b,820,105,25,pygame,screen)
                    display_text("None of the above (Press n)",b,820,130,25,pygame,screen)
                    pygame.display.update()
                    halals = True
                    return 0,1
                elif (event.key == pygame.K_n):

                    display_text("Halal/Vegetarian?",b,820,30,25,pygame,screen)
                    display_text("Halal (Press h)",b,820,55,25,pygame,screen)
                    display_text("Vegetarian (Press v)",b,820,80,25,pygame,screen)
                    display_text("Both (Press b)",b,820,105,25,pygame,screen)
                    display_text("None of the above (Press n)",b,820,130,25,pygame,screen)
                    pygame.display.update()
                    halals = True
                    return 0,0
                elif (event.key == pygame.K_b):

                    display_text("Halal/Vegetarian?",b,820,30,25,pygame,screen)
                    display_text("Halal (Press h)",b,820,55,25,pygame,screen)
                    display_text("Vegetarian (Press v)",b,820,80,25,pygame,screen)
                    display_text("Both (Press b)",b,820,105,25,pygame,screen)
                    display_text("None of the above (Press n)",b,820,130,25,pygame,screen)
                    pygame.display.update()
                    halals = True
                    return 1,1
#==========================================================================================================================

def price_sort(lists):
    price_list = []
    for i in lists:
        for j in lists[i][0]:
            if lists[i][0][j][2] not in price_list:
                price_list.append(lists[i][0][j][2])
    distance_sort(price_list)
    return price_list

#=============================================================
def preferences(preference,pygame,screen):
    b = (0,0,0)
    bl= (6, 158, 36)
    w = (255,255,255)
    y = (181, 154, 3)
    while not preference:
        display_text("List according to: ",w,820,30,25,pygame,screen)
        display_text("Price (Press a)",w,820,55,25,pygame,screen)
        display_text("Distance (Press b)",w,820,80,25,pygame,screen)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):

                    display_text("List according to: ",b,820,30,25,pygame,screen)
                    display_text("Price (Press a)",b,820,55,25,pygame,screen)
                    display_text("Distance (Press b)",b,820,80,25,pygame,screen)

                    pygame.display.update()
                    preference = True
                    return 1,0
                elif (event.key == pygame.K_b):

                    display_text("List according to: ",b,820,30,25,pygame,screen)
                    display_text("Price (Press a)",b,820,55,25,pygame,screen)
                    display_text("Distance (Press b)",b,820,80,25,pygame,screen)

                    pygame.display.update()
                    preference = True
                    return 0,1



#===========================================================================================================================

def price_display(dicts_new,sorted_distance,choose,pygame,screen,list_dictss):
    b = (0,0,0)
    bl= (6, 158, 36)
    w = (255,255,255)
    y = (181, 154, 3)
    while choose == True:
        price_list = price_sort(dicts_new)
        price_tier =['Tier 1','Tier 2','Tier 3','Tier 4','Tier 5','Tier 6','Tier 7','Tier 8','Tier 9','Tier 10']
        to_print=["The Cheapest","More Expensive than the 1","More Expensive than the 2","More Expensive than the 3","More Expensive than the 4","More Expensive than the 5","More Expensive than the 6","More Expensive than the 7","More Expensive than the 8","More Expensive than the 9","The most Expensive"]
        box_text_list(price_tier,to_print,pygame,screen)
        last_page = True
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONUP:
                mx,my = pygame.mouse.get_pos()
                X_condition = 12<=mx<=152
                Y_start = 13
                Y_end = 65
                if X_condition and 13<=my<=65:
                    while last_page:
                        screen.fill(w)
                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60
                        for a in price_list[0:2]:
                             for i in dicts_new:
                                for j in dicts_new[i][0]:
                                    if dicts_new[i][0][j][2] == a:
                                        display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                        display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                        texto+=55

                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()

                elif X_condition and Y_start+(80)<=my<=Y_end+(80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[3]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(2*80)<=my<=Y_end+(2*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[4]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(3*80)<=my<=Y_end+(3*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[5]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(4*80)<=my<=Y_end+(4*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[6]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(5*80)<=my<=Y_end+(5*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[7]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(6*80)<=my<=Y_end+(6*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[8]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(7*80)<=my<=Y_end+(7*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[9]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(8*80)<=my<=Y_end+(8*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[11]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(9*80)<=my<=Y_end+(9*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        count = 0
                        texto = 60

                        for i in dicts_new:
                            for j in dicts_new[i][0]:
                                if dicts_new[i][0][j][2] == price_list[11]:
                                    display_text("{0} in {1} with price starts from {2} to {3}".format(j,i,dicts_new[i][0][j][2],dicts_new[i][0][j][3]),b,30,texto,30,pygame,screen)
                                    display_text("     With distance {0} from you".format(dicts_new[i][6]),b,30,texto+30,20,pygame,screen)
                                    texto+=55
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()

#=============================================================================================================================

#Distance display interface
def distance_display(dicts_new,sorted_distance,choose,pygame,screen,list_dictss):
    b = (0,0,0)
    bl= (6, 158, 36)
    w = (255,255,255)
    y = (181, 154, 3)
    while choose == True:
        Canteen , Distance = print_distance_sort(dicts_new,sorted_distance)
        box_text_list(Canteen,Distance,pygame,screen)
        last_page = True
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONUP:
                mx,my = pygame.mouse.get_pos()
                X_condition = 12<=mx<=152
                Y_start = 13
                Y_end = 65
                if X_condition and 13<=my<=65:
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[0]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()

                elif X_condition and Y_start+(80)<=my<=Y_end+(80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[1]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(2*80)<=my<=Y_end+(2*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[2]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(3*80)<=my<=Y_end+(3*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[3]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(4*80)<=my<=Y_end+(4*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[4]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(5*80)<=my<=Y_end+(5*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[5]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(6*80)<=my<=Y_end+(6*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[6]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(7*80)<=my<=Y_end+(7*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[7]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(8*80)<=my<=Y_end+(8*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[8]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()
                elif X_condition and Y_start+(9*80)<=my<=Y_end+(9*80):
                    while last_page:
                        screen.fill(w)

                        box_text((700,730),"Back",pygame,screen)
                        box_text((850,730),"Exit",pygame,screen)
                        for i in list_dictss:
                            texto = 60
                            if Canteen[9]== i:
                                display_text("Operation time: {0}".format(list_dictss[i][1]),b,30,5,15,pygame,screen)
                                display_text("Rank: {0}".format(list_dictss[i][2]),b,30,20,15,pygame,screen)
                                display_text("Bus to use: {0}".format(list_dictss[i][5]),b,30,35,15,pygame,screen)
                                for j in list_dictss[i][0]:
                                    display_text("{0} with price starts from {1} to {2}".format(j,list_dictss[i][0][j][2],list_dictss[i][0][j][2]),b,30,texto,30,pygame,screen)
                                    texto+=45
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                mx1,my1 = pygame.mouse.get_pos()
                                if 700<=mx1<=840 and 730<=my1<=782:
                                    screen.fill(w)
                                    last_page = False
                                elif 850<mx1<=890 and 730<=my1<=782:
                                    pygame.quit()


#===============================================================================================================================
def please_choose(list_dictss):
    condition = True
    while condition:
        count = 1
        for i in list_dictss:
            print("Please enter {0} for {1}".format(count,i))
            count += 1
        the_choose = input()
        if the_choose == "1":
            return "Hall 1","Canteen 1"
            condition = False
        elif the_choose == "2":
            return "Canteen 2","Canteen 2"
            condition = False
        elif the_choose == "3":
            return "Hall 1","Pioneer"
            condition = False
        elif the_choose == "4":
            return "Hall 11","North Hill"
            condition = False
        elif the_choose == "5":
            return "Hall 11","Canteen 11"
            condition = False
        elif the_choose == "6":
            return "Hall 8 & 9","Canteen 9"
            condition = False
        elif the_choose == "7":
            return "Hall 23","Thamarin"
            condition = False
        elif the_choose == "8":
            return "LWN library","Canteen A"
            condition = False
        elif the_choose == "9":
            return "Innovation Centre","Canteen B"
            condition = False
        elif the_choose == "10":
            return "SCE","Quad"
            condition = False
        else:
            print("Wrong input, try again")
            continue
#=========================================================================================================================================

def find_bus_stop(the_location, bus_stop ,choosed_location,math):
    distance = math.inf
    for i in bus_stop:
        X_distance = the_location[0] - bus_stop[i][0]
        Y_distance = the_location[1] - bus_stop[i][1]
        total_distance = (((X_distance)**2)+((Y_distance)**2))**(0.5)
        if total_distance < distance:
            distance = total_distance
            Hall = i

    a = bus_stop[Hall][2]- bus_stop[choosed_location][2]
    b = 13 - abs(a)
    if a < b:
        if a < 0:
            print("Take the red bus from {0}'s bus-stop to {1}'s bus-stop".format(Hall,choosed_location))
        elif a > 0:
            print("Take the blue bus from Opp {0}'s bus-stop to {1}'s bus-stop".format(Hall,choosed_location))
        else:
            print("Just walk to the Canteen")
    elif b < a:
        if a < 0:
            print("Take the blue bus from Opp {0}'s bus-stop to {1}'s bus-stop".format(Hall,choosed_location))
        elif a > 0:
            print("Take the red bus from Opp {0}'s bus-stop to {1}'s bus-stop".format(Hall,choosed_location))
    return Hall

