#pusher
#box
#destination
#map

#set pusher coordinate
#rep: P
pusher_x = 1
pusher_y = 0

#set box ccoordinate
#rep: B
boxes = [
        {"x": 1, "y": 2},
        {"x": 2, "y": 4}
]

#set destination coordinate
#rep: D
dest_es = [
    {"x": 3, "y": 5},
    {"x": 1, "y": 4}
    ]

#set map_size

size_x = 6
size_y = 6
##############################################################################

def check_over(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True

    return False

##############################################################################

def check_box(box_x, box_y, boxes, dx, dy):
    rest_box = ( box for box in boxes if box["x"] != box_x or box["y"] != box_y)
    return check_box(box_x + dx, box_y + dy, rest_box)



##############################################################################
def map_(size_x, size_y, pusher_x, pusher_y, boxes):
    for y in range(size_y):
        for x in range(size_x):
            if x == pusher_x and y == pusher_y:
                print(" P ", end ="")
            elif check_over(x,y,boxes):
                print(" B ", end = "")
            elif check_over(x, y, dest_es):
                print(" D ", end="")
            else:
                print(" - ", end ="")
        print()

##############################################################################

def is_in_map(x, y, size_x, size_y):
    return 0 <= x < size_x and 0 <= y < size_y

##############################################################################

def you_win(boxes, dest_es):
    for box in boxes:
        if box not in dest_es:
            return False
    return True
##############################################################################
def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy = dy - 1
    elif direction == "A":
        dx = dx - 1
    elif direction == "S":
        dy = dy + 1
    elif direction == "D":
        dx = dx + 1
    else:
        print("==========================ERROR=========================")
        print("  You enter wrong button please do this again bruhhh ><  ")
        print("========================================================")

    return dx, dy

####################################################################################

# main GAME_LOOP
while True:
    map_(size_x, size_y, pusher_x, pusher_y, boxes)
    direction = input("What is your move? W/A/S/D ? \n").upper()
    # Xu ly dau vao
    dx, dy = input_process(direction)
    if  check_over(pusher_x + dx, pusher_y + dy, boxes):
        for box in boxes:
        # Truoc mat " P " la hop
            if is_in_map(box["x"] + dx, box["y"] + dy, size_x, size_y):
                box["x"] += dx
                box["y"] += dy
                pusher_x = pusher_x + dx
                pusher_y = pusher_y + dy
                break
            else:
                print("=============ERROR=============")
                print("   You can't push bruhh :((")
                print("===============================")
    else:
        #Cho " P " dau hop di chuyen
        if is_in_map( pusher_x + dx,pusher_y + dy,size_x,size_y):
            pusher_x += dx
            pusher_y += dy
        else:
            print("=============ERROR=============")
            print(" You can't go there bruhh :((")
            print("===============================")
    if  you_win(boxes,dest_es):
            print("===============================")
            print("       You win, Bruhh :P")
            print("====|====|===|===|===|=====|=======")
            print("=====|==|=|=|====|===|==|==|=======")
            print("======|====|=====|===|=====|=======")
            break





