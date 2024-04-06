from Items import *

# The actual item list that is used to keep track of current items
item_list_actual = []

# Item lists that hold the set items for each level
item_list1 = [Phone(), Papers(), VHS(), Camera(), Calculator(), Cassette(), Pen()]
item_list2 = [SmokingPipe(), Keys(), Notebook(), MultiTool(), Cuffs(), Vial(), Watch(), MagnifyingGlass()]
item_list3 = [ScrewdriverA(), ScrewdriverB(), ScrewdriverC(), AllenKeys(), Caliper(), TWrench(), Wrench(), Hammer(),
              Pliers(), Mallet(), Pencil(), Screws()]

# Create a 10x10 2d array to represent the empty puzzle case, filled with zeroes to represent empty grid spaces
rows, cols = (10, 10)
case_arr = [[0 for i in range(cols)] for j in range(rows)]

# Start the item list at 0, point for placing item at 0, current level to 0, and volumes to 100
item_point = 0
# Placement point is organized so that the first two digits are the Y coordinates
# and the last two digits are the x coordinates i.e. 810 = {x:10, y:08}
# Y coordinates are also more positive the more they go down while X coordinates move right the more positive they are
placement_point = 0
level_number = 0
music_volume = 100
effect_volume = 100


# Clear the item list before setting it to the desired levels items
def set_item_list(level_num):
    global item_list_actual

    item_list_actual.clear()
    match level_num:
        case 1:
            item_list_actual = item_list1.copy()
        case 2:
            item_list_actual = item_list2.copy()
        case 3:
            item_list_actual = item_list3.copy()


# Change level num to input value then set the actual item list to that levels items
def change_level_num(num):
    global level_number
    level_number = num
    set_item_list(level_number)


# Set variables to their default values, except for the actual item list, which is set to that for the desired level
def reset(level_num):
    global item_point, case_arr, placement_point
    case_arr.clear()
    set_item_list(level_num)
    case_arr = [[0 for i in range(cols)] for j in range(rows)]
    item_point = 0
    placement_point = 0


# Check if the case has any empty slots (has a 0 in any slot) and return boolean with that information
def check_complete():
    for i in range(len(case_arr)):
        for j in range(len(case_arr[0])):
            if case_arr[i][j] == 0:
                return False
    return True


# Place item by filling out 1's into the case array
def fit_item(item):
    for i in range(len(item.arr)):
        for j in range(len(item.arr[0])):
            # Try placing the array for the current item, starting at the placement point, returning if it doesn't fit
            # or if there is already something placed there.
            try:
                if item.arr[i][j] == 1 and case_arr[int(i + (placement_point / 100))][j + (placement_point % 100)] != 0:
                    return
            except IndexError:
                return

    # Places item into case by putting 1's where the item is located
    for i in range(len(item.arr)):
        for j in range(len(item.arr[0])):
            if item.arr[i][j] == 1:
                case_arr[int(i + (placement_point / 100))][j + (placement_point % 100)] = 1

    # Remove the item from the list
    item_list_actual.remove(item)

    return
