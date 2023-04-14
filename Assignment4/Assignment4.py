# Abdulkadir Parlak 2210765025
import sys
import os

try: # IndexError for the number of input file names can occur.
    if len(sys.argv) < 5:
        raise IndexError("number of input files less than expected.")
    elif len(sys.argv) > 5:
        raise IndexError("number of input files more than expected.")

except IndexError as e:
    print("IOError:", e, "(expected 4)")
    with open("Battleship.out", "a+", encoding="utf-8") as f:
        if len(sys.argv) < 5:
            f.write("IOError: number of input files less than expected." + "(expected 4)")
        elif len(sys.argv) > 5:
            f.write("IOError: number of input files more than expected." + "(expected 4)")
    sys.exit()

# File paths for player1
current_path = os.getcwd()
player1_ship_file = sys.argv[1]
player1_ship_file_path = os.path.join(current_path, player1_ship_file)

player1_move_file = sys.argv[3]
player1_move_file_path = os.path.join(current_path, player1_move_file)

# File paths for player2
player2_ship_file = sys.argv[2]
player2_ship_file_path = os.path.join(current_path, player2_ship_file)

player2_move_file = sys.argv[4]
player2_move_file_path = os.path.join(current_path, player2_move_file)

non_existent_files = []
    # IOError can occur here due to absence of some input files.
try:
    if not os.path.exists(player1_ship_file_path):
        raise IOError
except IOError:
    non_existent_files.append(sys.argv[1])

try:
    if not os.path.exists(player2_ship_file_path):
        raise IOError
except IOError:
    non_existent_files.append(sys.argv[2])

try:
    if not os.path.exists(player1_move_file_path):
        raise IOError
except IOError:
    non_existent_files.append(sys.argv[3])

try:
    if not os.path.exists(player2_move_file_path):
        raise IOError
except IOError:
    non_existent_files.append(sys.argv[3])

if len(non_existent_files) == 1:
    print("IOError: input file {} is not reachable.".format(non_existent_files[0]))
    with open("Battleship.out", "a+", encoding="utf-8") as f:
        f.write("IOError: input file {} is not reachable.".format(non_existent_files[0]))
    sys.exit()

elif len(non_existent_files) == 2:
    print("IOError: input files {}, {} are not reachable.".format(non_existent_files[0], non_existent_files[1]))
    with open("Battleship.out", "a+", encoding="utf-8") as f:
        f.write("IOError: input files {}, {} are not reachable.".format(non_existent_files[0], non_existent_files[1]))
    sys.exit()

elif len(non_existent_files) == 3:
    print("IOError: input files {}, {}, {} are not reachable.".format(non_existent_files[0],
                                                                      non_existent_files[1],
                                                                      non_existent_files[2]))
    with open("Battleship.out", "a+", encoding="utf-8") as f:
        f.write("IOError: input files {}, {}, {} are not reachable.".format(non_existent_files[0],
                                                                            non_existent_files[1],
                                                                            non_existent_files[2]))
    sys.exit()

elif len(non_existent_files) == 4:
    print("IOError: input files {}, {}, {}, {} are not reachable.".format(non_existent_files[0],
                                                                          non_existent_files[1],
                                                                          non_existent_files[2],
                                                                          non_existent_files[3]))
    with open("Battleship.out", "a+", encoding="utf-8") as f:
        f.write("IOError: input files {}, {}, {}, {} are not reachable.".format(non_existent_files[0],
                                                                                non_existent_files[1],
                                                                                non_existent_files[2],
                                                                                non_existent_files[3]))
    sys.exit()



hidden_tables = [[["-" for i in range(10)] for j in range(10)], [["-" for i in range(10)] for j in range(10)]]
tables = []
ship_positions = [{}, {}]
ships_of_player1 = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-", "P4": "-"}
ships_of_player2 = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-", "P4": "-"}
hit_counts = [{"C": 0, "D": 0, "S": 0}, {"C": 0, "D": 0, "S": 0}]
total1_hit_count = 0
total2_hit_count = 0

def create_ship_table(player_ship_file_path):
    table = [["-" for i in range(10)] for j in range(10)]
    with open(player_ship_file_path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            temp_lines = lines[i].split(";")
            for j in range(len(temp_lines)):
                if temp_lines[j] == "" or temp_lines[j] == "\n":
                    pass
                if temp_lines[j] == "C\n" or temp_lines[j] == "B\n" or temp_lines[j] == "D\n" or temp_lines[j] == "S\n" or temp_lines[j] == "P\n":
                    temp_lines[j] = temp_lines[j][0]

                if temp_lines[j] == "C":
                    table[i][j] = "C"

                elif temp_lines[j] == "B":
                    table[i][j] = "B"

                elif temp_lines[j] == "D":
                    table[i][j] = "D"

                elif temp_lines[j] == "S":
                    table[i][j] = "S"

                elif temp_lines[j] == "P":
                    table[i][j] = "P"
    tables.append(table)
    return table

def group_ships(optional_player_txt, player_number):
    with open(optional_player_txt, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for k in range(len(lines)):
            lines[k] = lines[k].split(";") # lines[k] = ['P2:10,B', 'right', '\n']
            line_0 = lines[k][0].split(":") # lines[k][0] = ['B1', '6,B']
            number_letter = line_0[1].split(",") # number_letter = ["6", "B"]
            # Above is txt file stuff...
            start_row_index = int(number_letter[0]) - 1
            start_col_index = ord(number_letter[1]) - 65
            if line_0[0][0] == "B":
                if lines[k][1] == "right":
                    end_row_index = start_row_index
                    end_col_index = start_col_index + 3
                else:
                    end_row_index = start_row_index + 3
                    end_col_index = start_col_index
            else: # P1,P2,P3,P4
                if lines[k][1] == "right":
                    end_row_index = start_row_index
                    end_col_index = start_col_index + 1
                else: # down-landed Patrol Boats
                    end_row_index = start_row_index + 1
                    end_col_index = start_col_index
            ship_positions[player_number][line_0[0]] = (start_row_index, end_row_index, start_col_index, end_col_index)
            # B1 = (start_row, end_row, start_col, end_col)

i = 0
def move_player1():
    result = ""
    global hit_counts
    global hidden_tables
    global tables
    global ships_of_player2
    global total2_hit_count
    with open(player1_move_file_path, "r", encoding="UTF-8") as f:
        moves = f.readline().split(";")
        moves = moves[:-1]
        global i
        while i < len(moves):
            print("Player1's Move")
            result += "Player1's Move\n\n"
            print("Round:", i + 1, end="")
            result += "Round:" + str(i + 1)
            if len(str(i + 1)) == 1:
                print("\t\t\t\t\t\tGrid Size: 10x10")
                result += "\t\t\t\t\t\tGrid Size: 10x10\n\n"
            elif len(str(i + 1)) == 2:
                print("\t\t\tGrid Size: 10x10")
                result += "\t\t\t\t\tGrid Size: 10x10\n\n"
            print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            result += "Player1's Hidden Board\t\tPlayer2's Hidden Board\n"
            print(" ", end="")
            result += " "
            print(" A B C D E F G H I J\t\t  A B C D E F G H I J")
            result += " A B C D E F G H I J\t\t  A B C D E F G H I J\n"
            for a in range(10):
                print(str(a + 1), end="")
                result += str(a + 1)
                for b in range(10):
                    if a == 9:
                        print(hidden_tables[0][a][b] + " ", end="")
                        result += hidden_tables[0][a][b] + " "
                    else:
                        print(" " + hidden_tables[0][a][b], end="")
                        result += " " + hidden_tables[0][a][b]
                print("\t\t", end="")
                result += "\t\t"
                print(str(a + 1), end="")
                result += str(a + 1)
                for b in range(10):
                    if a == 9:
                        print(hidden_tables[1][a][b] + " ", end="")
                        result += hidden_tables[1][a][b] + " "
                    else:
                        print(" " + hidden_tables[1][a][b], end="")
                        result += " " + hidden_tables[1][a][b]
                print()
                result += "\n"

            print("Carrier\t\t{}\t\tCarrier\t\t{}".format(ships_of_player1["C"], ships_of_player2["C"]))
            print("Battleship\t{} {}\t\tBattleship\t{} {}".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                                  ships_of_player2["B1"], ships_of_player2["B2"]))
            print("Destroyer\t{}\t\tDestroyer\t{}".format(ships_of_player1["D"], ships_of_player2["D"]))
            print("Submarine\t{}\t\tSubmarine\t{}".format(ships_of_player1["S"], ships_of_player2["S"]))
            print("Patrol Boat\t{} {} {} {}\t\tPatrol Boat\t{} {} {} {}".format(ships_of_player1["P1"],
                                                                                ships_of_player1["P2"],
                                                                                ships_of_player1["P3"],
                                                                                ships_of_player1["P4"],
                                                                                ships_of_player2["P1"],
                                                                                ships_of_player2["P2"],
                                                                                ships_of_player2["P3"],
                                                                                ships_of_player2["P4"]))
            print("Enter your move: {}".format(moves[i]))
            result += "Carrier\t\t{}\t\t\t\tCarrier\t\t{}\n".format(ships_of_player1["C"], ships_of_player2["C"])
            result += "Battleship\t{} {}\t\t\t\tBattleship\t{} {}\n".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                                            ships_of_player2["B1"], ships_of_player2["B2"])
            result += "Destroyer\t{}\t\t\t\tDestroyer\t{}\n".format(ships_of_player1["D"], ships_of_player2["D"])
            result += "Submarine\t{}\t\t\t\tSubmarine\t{}\n".format(ships_of_player1["S"], ships_of_player2["S"])
            result += "Patrol Boat\t{} {} {} {}\t\t\tPatrol Boat\t{} {} {} {}\n\n".format(ships_of_player1["P1"],
                                                                                          ships_of_player1["P2"],
                                                                                          ships_of_player1["P3"],
                                                                                          ships_of_player1["P4"],
                                                                                          ships_of_player2["P1"],
                                                                                          ships_of_player2["P2"],
                                                                                          ships_of_player2["P3"],
                                                                                          ships_of_player2["P4"])
            result += "Enter your move: {}\n\n".format(moves[i])

            moves[i] = moves[i].split(",") # moves[i][0] stores the row of the player's move and moves[i][1] stores the column of the move of the player. i.e. i[0] = "10" and i[1] = "H"
            try:
                row_index, column_index = int(moves[i][0]) - 1, ord(moves[i][1]) - 65

                if tables[1][row_index][column_index] == "-": # Cell is empty.
                    tables[1][row_index][column_index] = "O"
                    hidden_tables[1][row_index][column_index] = "O"

                elif tables[1][row_index][column_index] == "X": # Cell is full.
                    hidden_tables[1][row_index][column_index] = "X"

                elif tables[1][row_index][column_index] == "C":
                    tables[1][row_index][column_index] = "X"  # Cell was a part of a Carrier and it is hit now.
                    hidden_tables[1][row_index][column_index] = "X"
                    hit_counts[1]["C"] += 1
                    total2_hit_count += 1

                elif tables[1][row_index][column_index] == "D":
                    tables[1][row_index][column_index] = "X"  # Cell was a part of a Destroyer and it is hit now.
                    hidden_tables[1][row_index][column_index] = "X"
                    hit_counts[1]["D"] += 1
                    total2_hit_count += 1

                elif tables[1][row_index][column_index] == "S":
                    tables[1][row_index][column_index] = "X"  # Cell was a part of a Submarine and it is hit now.
                    hidden_tables[1][row_index][column_index] = "X"
                    hit_counts[1]["S"] += 1
                    total2_hit_count += 1

                elif tables[1][row_index][column_index] == "B":
                    tables[1][row_index][column_index] = "X"
                    hidden_tables[1][row_index][column_index] = "X"
                    total2_hit_count += 1

                elif tables[1][row_index][column_index] == "P":
                    tables[1][row_index][column_index] = "X"
                    hidden_tables[1][row_index][column_index] = "X"
                    total2_hit_count += 1

                for ship_name in ships_of_player2.keys():
                    if is_ship_sunk(1, ship_name):
                        ships_of_player2[ship_name] = "X"
                break

            except IndexError:
                print("IndexError: wrong input format expected such as (3,E)")
                result += "IndexError: wrong input format expected such as (3,E)\n\n"
                i += 1

            except ValueError:
                print("IndexError: row index is not found")
                result += "IndexError: row index is not found\n\n"
                i += 1

            except TypeError:  # My code doesn't give IndexError when column letter is not found, it gives TypeError.
                print("IndexError: column letter not found")
                result += "IndexError: column letter not found\n\n"
                i += 1

            except Exception:
                print("kaBOOM: run for your life!")
                result += "kaBOOM: run for your life!\n\n"
                i += 1
    i += 1
    return result # It returns the variable result because I will use it later.

j = 0
def move_player2():
    result = ""
    global hit_counts
    global hidden_tables
    global tables
    global ships_of_player1
    global total1_hit_count

    with open(player2_move_file_path, "r", encoding="UTF-8") as l:
        moves = l.readline().split(";")
        moves = moves[:-1]
        global j
        while j < len(moves):
            print("Player2's Move")
            result += "Player2's Move\n\n"
            print("Round:", j + 1, end="")
            result += "Round:" + str(j + 1)
            if len(str(j + 1)) == 1:
                print("\t\t\t\t\t\tGrid Size: 10x10")
                result += "\t\t\t\t\t\tGrid Size: 10x10\n\n"
            elif len(str(j + 1)) == 2:
                print("\t\t\tGrid Size: 10x10")
                result += "\t\t\t\t\tGrid Size: 10x10\n\n"
            print("Player1's Hidden Board\t\tPlayer2's Hidden Board")
            result += "Player1's Hidden Board\t\tPlayer2's Hidden Board\n"
            print(" ", end="")
            result += " "
            print(" A B C D E F G H I J\t\t  A B C D E F G H I J")
            result += " A B C D E F G H I J\t\t  A B C D E F G H I J\n"
            for a in range(10):
                print(str(a + 1), end="")
                result += str(a + 1)
                for b in range(10):
                    if a == 9:
                        print(hidden_tables[0][a][b] + " ", end="")
                        result += hidden_tables[0][a][b] + " "
                    else:
                        print(" " + hidden_tables[0][a][b], end="")
                        result += " " + hidden_tables[0][a][b]
                print("\t\t", end="")
                result += "\t\t"
                print(str(a + 1), end="")
                result += str(a + 1)
                for b in range(10):
                    if a == 9:
                        print(hidden_tables[1][a][b] + " ", end="")
                        result += hidden_tables[1][a][b] + " "
                    else:
                        print(" " + hidden_tables[1][a][b], end="")
                        result += " " + hidden_tables[1][a][b]
                print()
                result += "\n"

            print("Carrier\t\t{}\t\tCarrier\t\t{}".format(ships_of_player1["C"], ships_of_player2["C"]))
            print("Battleship\t{} {}\t\tBattleship\t{} {}".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                                  ships_of_player2["B1"], ships_of_player2["B2"]))
            print("Destroyer\t{}\t\tDestroyer\t{}".format(ships_of_player1["D"], ships_of_player2["D"]))
            print("Submarine\t{}\t\tSubmarine\t{}".format(ships_of_player1["S"], ships_of_player2["S"]))
            print("Patrol Boat\t{} {} {} {}\t\tPatrol Boat\t{} {} {} {}".format(ships_of_player1["P1"],
                                                                                ships_of_player1["P2"],
                                                                                ships_of_player1["P3"],
                                                                                ships_of_player1["P4"],
                                                                                ships_of_player2["P1"],
                                                                                ships_of_player2["P2"],
                                                                                ships_of_player2["P3"],
                                                                                ships_of_player2["P4"]))
            print("Enter your move: {}".format(moves[j]))
            result += "Carrier\t\t{}\t\t\t\tCarrier\t\t{}\n".format(ships_of_player1["C"], ships_of_player2["C"])
            result += "Battleship\t{} {}\t\t\t\tBattleship{} {}\n".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                                          ships_of_player2["B1"], ships_of_player2["B2"])
            result += "Destroyer\t{}\t\t\t\tDestroyer\t{}\n".format(ships_of_player1["D"], ships_of_player2["D"])
            result += "Submarine\t{}\t\t\t\tSubmarine\t{}\n".format(ships_of_player1["S"], ships_of_player2["S"])
            result += "Patrol Boat\t{} {} {} {}\t\t\tPatrol Boat\t{} {} {} {}\n\n".format(ships_of_player1["P1"],
                                                                                          ships_of_player1["P2"],
                                                                                          ships_of_player1["P3"],
                                                                                          ships_of_player1["P4"],
                                                                                          ships_of_player2["P1"],
                                                                                          ships_of_player2["P2"],
                                                                                          ships_of_player2["P3"],
                                                                                          ships_of_player2["P4"])
            result += "Enter your move: {}\n\n".format(moves[j])

            moves[j] = moves[j].split(",") # j[0] stores the row of the player's move and j[1] stores the column of the move of the player. i.e. j[0] = "10" and j[1] = "H"
            try:
                row_index, column_index = int(moves[j][0]) - 1, ord(moves[j][1]) - 65

                if tables[0][row_index][column_index] == "-": # Cell is empty.
                    tables[0][row_index][column_index] = "O"
                    hidden_tables[0][row_index][column_index] = "O"

                elif tables[0][row_index][column_index] == "X": # Cell is full.
                    hidden_tables[0][row_index][column_index] = "X"

                elif tables[0][row_index][column_index] == "C":
                    tables[0][row_index][column_index] = "X" # Cell was a part of a Carrier and it is hit now.
                    hidden_tables[0][row_index][column_index] = "X"
                    hit_counts[0]["C"] += 1
                    total1_hit_count += 1

                elif tables[0][row_index][column_index] == "D":
                    tables[0][row_index][column_index] = "X"  # Cell was a part of a Destroyer and it is hit now.
                    hidden_tables[0][row_index][column_index] = "X"
                    hit_counts[0]["D"] += 1
                    total1_hit_count += 1

                elif tables[0][row_index][column_index] == "S":
                    tables[0][row_index][column_index] = "X"  # Cell was a part of a Submarine and it is hit now.
                    hidden_tables[0][row_index][column_index] = "X"
                    hit_counts[0]["S"] += 1
                    total1_hit_count += 1

                elif tables[0][row_index][column_index] == "B":
                    tables[0][row_index][column_index] = "X"
                    hidden_tables[0][row_index][column_index] = "X"
                    total1_hit_count += 1

                elif tables[0][row_index][column_index] == "P":
                    tables[0][row_index][column_index] = "X"
                    hidden_tables[0][row_index][column_index] = "X"
                    total1_hit_count += 1

                for ship_name in ships_of_player1.keys():
                    if is_ship_sunk(0, ship_name):
                        ships_of_player1[ship_name] = "X"
                break

            except IndexError:
                print("IndexError: wrong input format expected such as (3,E)")
                result += "IndexError: wrong input format expected such as (3,E)\n\n"
                j += 1

            except ValueError:
                print("ValueError: row index is not found")
                result += "ValueError: row index is not found\n\n"
                j += 1

            except TypeError: # My code doesn't give IndexError when column letter is not found, it gives TypeError.
                print("IndexError: column letter not found")
                result += "IndexError: column letter not found\n\n"
                j += 1

            except Exception:
                print("kaBOOM: run for your life!")
                result += "kaBOOM: run for your life!\n\n"
                j += 1
    j += 1
    return result  # It returns the variable result because I will use it later.

def is_ship_sunk(player_index, ship_name): # is ship is sunk it returns True, otherwise False
    global tables
    global ship_positions
    global hit_counts

    if ship_name[0] == "C":
        if hit_counts[player_index]["C"] == 5:
            return True
        return False

    elif ship_name[0] == "D":
        if hit_counts[player_index]["D"] == 3:
            return True
        return False

    elif ship_name[0] == "S":
        if hit_counts[player_index]["S"] == 3:
            return True
        return False

    # B1 = (start_row, end_row, start_col, end_col)
    if ship_positions[player_index][ship_name][0] == ship_positions[player_index][ship_name][1]: # right landed ships
        if ship_name[0] == "B": # B1, B2
            if tables[player_index][ship_positions[player_index][ship_name][0]][ship_positions[player_index][ship_name][2]: ship_positions[player_index][ship_name][3] + 1] == ["X"]*4: # this long expression is B1 ship.
                return True
        else: # P1, P2, P3, P4 (right-landed patrol boats)
            if tables[player_index][ship_positions[player_index][ship_name][0]][ship_positions[player_index][ship_name][2]: ship_positions[player_index][ship_name][3] + 1] == ["X"]*2:
                return True
    else: # down-landed ships
        if ship_name[0] == "B": # Battleships
            for i in range(4):
                if tables[player_index][ship_positions[player_index][ship_name][0] + i][ship_positions[player_index][ship_name][2]] == "X":
                    pass
                else:
                    return False
            return True
        else: # Patrol boats
            for i in range(2):
                if tables[player_index][ship_positions[player_index][ship_name][0] + i][ship_positions[player_index][ship_name][2]] == "X":
                    pass
                else:
                    return False
            return True

def main():
    global ships_of_player1
    global ships_of_player2
    global total1_hit_count
    global total2_hit_count

    # Ship boards are created and ships are grouped
    create_ship_table(player1_ship_file_path)
    create_ship_table(player2_ship_file_path)
    group_ships("OptionalPlayer1.txt", 0)
    group_ships("OptionalPlayer2.txt", 1)

    # The game is being played in the while loop.
    with open("Battleship.out", "a+", encoding="utf-8") as output_file:
        print("Battle of Ships Game")
        output_file.write("Battle of Ships Game\n\n")
        while True:
            output_file.write(move_player1())
            output_file.write(move_player2())
            if total1_hit_count == 27:
                if total2_hit_count == 27:
                    print("It's a draw!")
                    output_file.write("It's a draw!\n\n")
                    break
                else:
                    print("Player2 wins!")
                    output_file.write("Player2 wins!\n\n")
                    break
            elif total2_hit_count == 27:
                print("Player1 wins!")
                output_file.write("Player1 wins!\n\n")
                break

    # Printing final information
        print("Final Information")
        output_file.write("Final Information\n\n")
        print("Player1's Board\t\t\tPlayer2's Board")
        output_file.write("Player1's Board\t\t\t\tPlayer2's Board\n")
        print(" ", end="")
        output_file.write(" ")
        print(" A B C D E F G H I J\t\t  A B C D E F G H I J")
        output_file.write(" A B C D E F G H I J\t\t  A B C D E F G H I J\n")
        for a in range(10):
            print(str(a + 1), end="")
            output_file.write(str(a + 1))
            for b in range(10):
                if a == 9:
                    print(tables[0][a][b] + " ", end="")
                    output_file.write(tables[0][a][b] + " ")
                else:
                    print(" " + tables[0][a][b], end="")
                    output_file.write(" " + tables[0][a][b])
            print("\t\t", end="")
            output_file.write("\t\t")
            print(str(a + 1), end="")
            output_file.write(str(a + 1))
            for b in range(10):
                if a == 9:
                    print(tables[1][a][b] + " ", end="")
                    output_file.write(tables[1][a][b] + " ")
                else:
                    print(" " + tables[1][a][b], end="")
                    output_file.write(" " + tables[1][a][b])
            print()
            output_file.write("\n")

        print("Carrier\t\t{}\t\tCarrier\t\t{}".format(ships_of_player1["C"], ships_of_player2["C"]))
        print("Battleship\t{} {}\t\tBattleship\t{} {}".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                              ships_of_player2["B1"], ships_of_player2["B2"]))
        print("Destroyer\t{}\t\tDestroyer\t{}".format(ships_of_player1["D"], ships_of_player2["D"]))
        print("Submarine\t{}\t\tSubmarine\t{}".format(ships_of_player1["S"], ships_of_player2["S"]))
        print("Patrol Boat\t{} {} {} {}\t\tPatrol Boat\t{} {} {} {}".format(ships_of_player1["P1"],
                                                                            ships_of_player1["P2"],
                                                                            ships_of_player1["P3"],
                                                                            ships_of_player1["P4"],
                                                                            ships_of_player2["P1"],
                                                                            ships_of_player2["P2"],
                                                                            ships_of_player2["P3"],
                                                                            ships_of_player2["P4"]))

        output_file.write("Carrier\t\t{}\t\t\t\tCarrier\t\t{}\n".format(ships_of_player1["C"], ships_of_player2["C"]))
        output_file.write("Battleship\t{} {}\t\t\t\tBattleship\t{} {}\n".format(ships_of_player1["B1"], ships_of_player1["B2"],
                                                                                ships_of_player2["B1"], ships_of_player2["B2"]))
        output_file.write("Destroyer\t{}\t\t\t\tDestroyer\t{}\n".format(ships_of_player1["D"], ships_of_player2["D"]))
        output_file.write("Submarine\t{}\t\t\t\tSubmarine\t{}\n".format(ships_of_player1["S"], ships_of_player2["S"]))
        output_file.write("Patrol Boat\t{} {} {} {}\t\t\tPatrol Boat\t{} {} {} {}\n".format(ships_of_player1["P1"],
                                                                                            ships_of_player1["P2"],
                                                                                            ships_of_player1["P3"],
                                                                                            ships_of_player1["P4"],
                                                                                            ships_of_player2["P1"],
                                                                                            ships_of_player2["P2"],
                                                                                            ships_of_player2["P3"],
                                                                                            ships_of_player2["P4"]))

main()