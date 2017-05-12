#! /usr/local/bin/python3.4

# Code Written By Gabriel Chen
# Last Updated: 05/06/2017
#

# Sudoku is a combinatorial number placement puzzle, where in a 9x9 matrix each column and each row (as well as each
# quadrant, 9 in total) contains one of each number from 1-9 given some initial fixed values already placed in the
# puzzle.

# We will represent the 9x9 matrix as a 2D array: [[], [], [], ..., []]

# Fill in the initial fixed values:
# We will represent blanks (places to be filled in) with 0
initial_state = [[7, 6, 0, 0, 0, 9, 0, 4, 2],
                 [4, 0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 6, 0, 9],
                 [0, 0, 0, 2, 0, 0, 1, 6, 0],
                 [0, 5, 0, 9, 1, 6, 0, 3, 0],
                 [0, 1, 4, 0, 0, 7, 0, 0, 0],
                 [2, 0, 6, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 7, 0, 0, 0, 0, 6],
                 [5, 4, 0, 6, 0, 0, 0, 7, 1]]

# The following code only solves the Sudoku, it assumes the given puzzle only has one unique solution
# Step 1: Go to each "0" entry and fill in the ones that has only one possible value
# Step 2: Go to each remaining "0" entry and fill in all possible values for that box
# Step 3: Check out each row, col, grid and check for single numbers. For example: row 1: only one entry has the
#         possibility for 6, that entry is 6.
def list_possible_values(rows, cols, prev_stage):
    possible_values = [i for i in range(1, 10)]
    rowVals = []
    colVals = []
    # A quadrant is every 3x3 matrix, quadVals at most will have 4 values, as the rowVals and colVals would capture
    # the other four boxes that is not the current box under test
    quadVals = []
    for i in range(9):
        if prev_stage[rows][i] != 0:
            rowVals.append(prev_stage[rows][i])
        if prev_stage[i][cols] != 0:
            colVals.append(prev_stage[i][cols])
    quady, posy = divmod(rows, 3)
    quadx, posx = divmod(cols, 3)
    # Quadrant cases
    # Case 1: Top left
    if (posy == 0) and (posx == 0):
        for i in range(1,3):
            for j in range(1,3):
                if prev_stage[rows+i][cols+j] != 0:
                    quadVals.append(prev_stage[rows+i][cols+j])
    # Case 2: Top mid
    elif (posy == 0) and (posx == 1):
        for i in range(1,3):
            if prev_stage[rows+i][cols+1] != 0:
                quadVals.append(prev_stage[rows+i][cols+1])
            if prev_stage[rows+i][cols-1] != 0:
                quadVals.append(prev_stage[rows+i][cols-1])
    # Case 3: Top right
    elif (posy == 0) and (posx == 2):
        for i in range(1,3):
            for j in range(1,3):
                if prev_stage[rows+i][cols-i] != 0:
                    quadVals.append(prev_stage[rows + i][cols - j])
    # Case 4: Mid left
    elif (posy == 1) and (posx == 0):
        for j in range(1,3):
            if prev_stage[rows+1][cols+j] != 0:
                quadVals.append(prev_stage[rows+1][cols+j])
            if prev_stage[rows-1][cols+j] != 0:
                quadVals.append(prev_stage[rows-1][cols+j])
    # Case 5: Mid mid
    elif (posy == 1) and (posx == 1):
        if prev_stage[rows + 1][cols + 1] != 0:
            quadVals.append(prev_stage[rows + 1][cols + 1])
        if prev_stage[rows - 1][cols + 1] != 0:
            quadVals.append(prev_stage[rows - 1][cols + 1])
        if prev_stage[rows + 1][cols - 1] != 0:
            quadVals.append(prev_stage[rows + 1][cols - 1])
        if prev_stage[rows - 1][cols - 1] != 0:
            quadVals.append(prev_stage[rows - 1][cols - 1])
    # Case 6: Mid right
    elif (posy == 1) and (posx == 2):
        for j in range(1,3):
            if prev_stage[rows+1][cols-j] != 0:
                quadVals.append(prev_stage[rows+1][cols-j])
            if prev_stage[rows-1][cols-j] != 0:
                quadVals.append(prev_stage[rows-1][cols-j])
    # Case 7: Bot left
    elif (posy == 2) and (posx == 0):
        for i in range(1,3):
            for j in range(1,3):
                if prev_stage[rows-i][cols+j] != 0:
                    quadVals.append(prev_stage[rows-i][cols+j])
    # Case 8: Bot mid
    elif (posy == 2) and (posx == 1):
        for i in range(1,3):
            if prev_stage[rows-i][cols+1] != 0:
                quadVals.append(prev_stage[rows-i][cols+1])
            if prev_stage[rows-i][cols-1] != 0:
                quadVals.append(prev_stage[rows-i][cols-1])
    # Case 9: Bot right
    elif (posy == 2) and (posx == 2):
        for i in range(1,3):
            for j in range(1,3):
                if prev_stage[rows-i][cols-i] != 0:
                    quadVals.append(prev_stage[rows - i][cols - j])

    resulting_possible_values = possible_values.copy()
    for i in possible_values:
        if (i in rowVals) or (i in colVals) or (i in quadVals):
            resulting_possible_values.remove(i)
    return resulting_possible_values

'''
Before quad
[7, 6, [1, 3, 5, 8], [1, 3, 5, 8], [3, 5, 8], 9, [3, 5, 8], 4, 2]
[4, [3, 7, 8, 9], [1, 3, 5, 7, 8, 9], [1, 3, 5, 8], [3, 5, 6, 7, 8, 9], 2, [3, 5, 7, 8, 9], [1, 5, 8, 9], [3, 5, 7, 8]]
[[1, 3], [2, 3, 7, 8], [1, 2, 3, 5, 7, 8], [1, 3, 4, 5, 8], [2, 3, 4, 5, 7, 8], [1, 3, 4, 5, 8], 6, [1, 2, 5, 8], 9]
[[3, 9], [3, 7, 8, 9], [3, 5, 7, 8, 9], 2, [3, 4, 5, 7, 8, 9], [3, 4, 5, 8], 1, 6, [3, 4, 5, 7, 8]]
[8, 5, [2, 7], 9, 1, 6, [2, 4, 7], 3, [4, 7]]
[[3, 6, 9], 1, 4, [3, 5, 8], [2, 3, 5, 6, 8, 9], 7, [2, 3, 5, 8, 9], [2, 5, 8, 9], [3, 5, 8]]
[2, [3, 7, 8, 9], 6, [1, 3, 4, 5, 8], [3, 4, 5, 7, 8, 9], [1, 3, 4, 5, 8], [3, 4, 5, 7, 8, 9], [1, 5, 8, 9], [3, 4, 5, 7, 8]]
[[1, 3, 9], [2, 3, 8, 9], [1, 2, 3, 5, 8, 9], 7, [2, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [2, 3, 4, 5, 8, 9], [1, 2, 5, 8, 9], 6]
[5, 4, [2, 3, 8, 9], 6, [2, 3, 8, 9], [3, 8], [2, 3, 8, 9], 7, 1]
After quad
[7, 6, [1, 3, 5, 8], [1, 3, 5, 8], [3, 5, 8], 9, [3, 5, 8], 4, 2]
[4, [3, 8, 9], [1, 3, 5, 8, 9], [1, 3, 5, 8], [3, 5, 6, 7, 8], 2, [3, 5, 7, 8], [1, 5, 8], [3, 5, 7, 8]]
[[1, 3], [2, 3, 8], [1, 2, 3, 5, 8], [1, 3, 4, 5, 8], [3, 4, 5, 7, 8], [1, 3, 4, 5, 8], 6, [1, 5, 8], 9]
[[3, 9], [3, 7, 9], [3, 7, 9], 2, [3, 4, 5, 8], [3, 4, 5, 8], 1, 6, [4, 5, 7, 8]]
[8, 5, [2, 7], 9, 1, 6, [2, 4, 7], 3, [4, 7]]
[[3, 6, 9], 1, 4, [3, 5, 8], [3, 5, 8], 7, [2, 5, 8, 9], [2, 5, 8, 9], [5, 8]]
[2, [3, 7, 8, 9], 6, [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [5, 8, 9], [3, 4, 5, 7, 8]]
[[1, 3, 9], [3, 8, 9], [1, 3, 8, 9], 7, [2, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [2, 3, 4, 5, 8, 9], [2, 5, 8, 9], 6]
[5, 4, [3, 8, 9], 6, [2, 3, 8, 9], [3, 8], [2, 3, 8, 9], 7, 1]
'''

def capture_single_values(stage_one):
    for rows in range(9):
        for cols in range(9):
            if stage_one[rows][cols] == 0:
                pList = list_possible_values(rows, cols, initial_state)
                if len(pList) == 1:
                    stage_one[rows][cols] = int(pList[0])
                    return stage_one, 0
    return stage_one, 1

def eliminate_zeroes(stage_two, stage_one):
    for rows in range(9):
        for cols in range(9):
            if stage_two[rows][cols] == 0:
                stage_two[rows][cols] = list_possible_values(rows, cols, stage_one)
    return stage_two

def find_single_in_groups(stage_three):
    stage_three = find_single_row(stage_three)
    #stage_three = find_single_col(stage_three)
    #stage_three = find_single_grid(stage_three)
    return stage_three


'''
End of stage 2:
[7, 6, [1, 3, 5, 8], [1, 3, 5, 8], [3, 5, 8], 9, [3, 5, 8], 4, 2]
[4, [3, 8, 9], [1, 3, 5, 8, 9], [1, 3, 5, 8], [3, 5, 6, 7, 8], 2, [3, 5, 7, 8], [1, 5, 8], [3, 5, 7, 8]]
[[1, 3], [2, 3, 8], [1, 2, 3, 5, 8], [1, 3, 4, 5, 8], [3, 4, 5, 7, 8], [1, 3, 4, 5, 8], 6, [1, 5, 8], 9]
[[3, 9], [3, 7, 9], [3, 7, 9], 2, [3, 4, 5, 8], [3, 4, 5, 8], 1, 6, [4, 5, 7, 8]]
[8, 5, [2, 7], 9, 1, 6, [2, 4, 7], 3, [4, 7]]
[[3, 6, 9], 1, 4, [3, 5, 8], [3, 5, 8], 7, [2, 5, 8, 9], [2, 5, 8, 9], [5, 8]]
[2, [3, 7, 8, 9], 6, [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [5, 8, 9], [3, 4, 5, 7, 8]]
[[1, 3, 9], [3, 8, 9], [1, 3, 8, 9], 7, [2, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [2, 3, 4, 5, 8, 9], [2, 5, 8, 9], 6]
[5, 4, [3, 8, 9], 6, [2, 3, 8, 9], [3, 8], [2, 3, 8, 9], 7, 1]

After find single row:
[7, 6, [1, 3, 5, 8], [1, 3, 5, 8], [3, 5, 8], 9, [3, 5, 8], 4, 2]
[4, [3, 8, 9], [1, 3, 5, 8, 9], [1, 3, 5, 8], 6, 2, [3, 5, 7, 8], [1, 5, 8], [3, 5, 7, 8]]
[[1, 3], [2, 3, 8], [1, 2, 3, 5, 8], [1, 3, 4, 5, 8], 7, [1, 3, 4, 5, 8], 6, [1, 5, 8], 9]
[[3, 9], [3, 7, 9], [3, 7, 9], 2, [3, 4, 5, 8], [3, 4, 5, 8], 1, 6, [4, 5, 7, 8]]
[8, 5, [2, 7], 9, 1, 6, [2, 4, 7], 3, [4, 7]]
[6, 1, 4, [3, 5, 8], [3, 5, 8], 7, [2, 5, 8, 9], [2, 5, 8, 9], [5, 8]]
[2, [3, 7, 8, 9], 6, [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [3, 4, 5, 8, 9], [5, 8, 9], [3, 4, 5, 7, 8]]
[[1, 3, 9], [3, 8, 9], [1, 3, 8, 9], 7, [2, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8], [2, 3, 4, 5, 8, 9], [2, 5, 8, 9], 6]
[5, 4, [3, 8, 9], 6, [2, 3, 8, 9], [3, 8], [2, 3, 8, 9], 7, 1]

'''


def find_single_row(cur_stage):
    returnlist = []
    for row_num, i in enumerate(cur_stage):
        current_row = []
        occurence = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for entry in i:
            if type(entry) is list:
                for x in entry:
                    occurence[int(x) - 1] += 1
        singled_value = []
        for value, occur in enumerate(occurence):
            if occur == 1:
                singled_value.append(value+1)

        for replace in singled_value:
            for index, entries in enumerate(cur_stage[row_num]):
                if type(entries) is list:
                    if replace in entries:
                        current_row.append(replace)
                    else:
                        current_row.append(entries)
                else:
                    current_row.append(entries)
        if len(singled_value) == 0:
            current_row = i
        returnlist.append(current_row)
    return returnlist

def find_single_col(cur_stage):
    for i in cur_stage:
        current_col = []
        occurence = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for entry in i:
            if type(entry) is list:
                for x in entry:
                    occurence[int(x) - 1] += 1


def main():
    # STEP 1
    stage_one = initial_state.copy()
    # status bit for repeating step 1 when there's a single possible value
    stage_one_status = 0
    while stage_one_status == 0:
        stage_one, stage_one_status = capture_single_values(stage_one)
    # END OF STEP 1
    # STEP 2
    stage_two = stage_one.copy()
    stage_two = eliminate_zeroes(stage_two, stage_one)
    # END OF STEP 2
    # STEP 3
    stage_three = stage_two.copy()
    stage_three = find_single_in_groups(stage_three)
    for i in stage_three:
        print(i)



if __name__ == "__main__":
    main()
