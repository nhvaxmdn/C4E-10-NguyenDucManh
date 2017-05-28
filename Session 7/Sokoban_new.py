#pusher
#box
#destination
#map

#set pusher coordinate
#rep: P
pusher ={
    "x": 1,
    "y": 0
}

pusher_copy = pusher.copy()

old_pusher = pusher_copy.copy()
#set box ccoordinate
#rep: B
boxes =[
    {"x": 1, "y": 2},
    {"x": 2, "y": 4}
    ]

boxes_copy = [box.copy() for box in boxes ]


#set destination coordinate
#rep: D
dest_es = {"x": 3, "y": 5},{"x": 1, "y": 4}


#set map_size

size ={
    "x": 6,
    "y": 7
}
#############################################################################
#level saved

saved_pusher = pusher.copy()

saved_boxes = [box.copy() for box in boxes]

#############################################################################





##############################################################################

def reset_level(saved_pusher, save_boxes):
    global pusher,boxes
    pusher = saved_pusher.copy()
    boxes = [box.copy() for box in saved_boxes]


##############################################################################
def check_over(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item

    return None

##############################################################################

def check_box(box_x, box_y, boxes, dx, dy):
    rest_box = ( box for box in boxes if box["x"] != box_x or box["y"] != box_y)
    return check_box(box_x + dx, box_y + dy, rest_box)



##############################################################################
def print_map(size, pusher, boxes):
    for y in range(size["y"]):
        for x in range(size["x"]):
            if x == pusher["x"] and y == pusher["y"]:
                print(" ☺ ", end ="")
            elif check_over(x,y,boxes):
                print(" █ ", end = "")
            elif check_over(x, y, dest_es):
                print(" ✖ ", end="")
            else:
                print(" - ", end ="")
        print()

##############################################################################

def is_in_map(x, y, size):
    return 0 <= x < size["x"] and 0 <= y < size["y"]

##############################################################################

def check_win(boxes,dest_es):
    count = 0
    for box in boxes:
        if check_over(box["x"],box["y"], dest_es) is not  None:
            count += 1
    if count == len(boxes):
        return True
    else:
        return False




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

def move(item,dx,dy):
    item["x"] += dx
    item["y"] += dy
    return item

####################################################################################
# main GAME_LOOP
while True:
    print_map(size,pusher,boxes)
    direction = input("What is your move? W/A/S/D? \n Enter R to reset the GAME").upper()
    # Xu ly dau vao





    if direction == "R":
        reset_level(saved_pusher,saved_boxes)



    elif direction =="U":

         reset_level(undo_pusher, undo_boxes)
    undo_pusher = pusher.copy()
    undo_boxes = [box.copy() for box in boxes]

    dx, dy = input_process(direction)
    found_box = check_over(pusher["x"] + dx, pusher["y"] + dy, boxes)
    if found_box is not None:
        if check_over(found_box["x"] + dx, found_box["y"] + dy, boxes) is None:
            if is_in_map(found_box["x"] + dx, found_box["y"] + dy, size):
                found_box = move(found_box, dx, dy)
                pusher = move(pusher, dx, dy)
    elif is_in_map(pusher["x"] + dx, pusher["y"] + dy, size):
        pusher = move(pusher, dx, dy)

    if check_win(boxes,dest_es):
        print("♥==♥==♥== FUCKING WIN BRUHHH ==♥===♥==♥")
        print()
        print("========================♥==================")
        print("===========================================")
        print("==♥=======♥=======♥====♥=====♥♥====♥=====")
        print("===♥=====♥==♥====♥=====♥=====♥=♥===♥=====")
        print("====♥===♥====♥==♥======♥=====♥===♥=♥=====")
        print("======♥=======♥========♥=====♥======♥=====")
        break
