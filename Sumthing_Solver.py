# SUMTHING SOLVER

import re
from itertools import permutations

def print_format(print_input, print_output):
    # PRINT FORMAT AS CARDS
    card_top = " ____ "
    card_top2 = "|    |"
    card_bottom = "|____|"
    spacing = "\t    "
    print_hand = (5 * card_top + "\n" + 5 * card_top2 + 
          f"\n|{print_input[0]:^4}||{print_input[1]:^4}||{print_input[2]:^4}||{print_input[3]:^4}||{print_input[4]:^4}|\n"
          + 5 * card_bottom + "\n" + spacing + card_top + "\n" + spacing + card_top2 + "\n" + spacing + 
          f"|{print_output:^4}|" + "\n" + spacing + card_bottom + "\n")
    return print_hand

def sumthing_solver(solve_input, solve_output):
    # BRUTE FORCE SOLVER
    kp = list(permutations(solve_input))
    op = list(set(list(permutations(['+','+','+','+','-','-','-','-','/','/','/','/','*','*','*','*'],4)))) 
    solved = False
    
    # GENERATING ALL PERMUTATIONS OF INPUTS, BINARY OPERATORS, PARENTHESES
    for n in range(len(kp)):
        for p in range(len(op)):
            potential_solution = ''.join([str(kp[n][0]),op[p][0],str(kp[n][1]),op[p][1],str(kp[n][2]),op[p][2],str(kp[n][3]),op[p][3],str(kp[n][4])])
            potential_solution1 = ''.join([str(kp[n][0]),op[p][0],'(',str(kp[n][1]),op[p][1],'(',str(kp[n][2]),op[p][2],'(',str(kp[n][3]),op[p][3],str(kp[n][4]),')))'])
            potential_solution2 = ''.join([str(kp[n][0]),op[p][0],'(',str(kp[n][1]),op[p][1],'((',str(kp[n][2]),op[p][2],str(kp[n][3]),')',op[p][3],str(kp[n][4]),'))'])
            potential_solution3 = ''.join([str(kp[n][0]),op[p][0],'((',str(kp[n][1]),op[p][1],str(kp[n][2]),')',op[p][2],'(',str(kp[n][3]),op[p][3],str(kp[n][4]),'))'])
            potential_solution4 = ''.join([str(kp[n][0]),op[p][0],'((',str(kp[n][1]),op[p][1],'(',str(kp[n][2]),op[p][2],str(kp[n][3]),'))',op[p][3],str(kp[n][4]),')'])
            potential_solution5 = ''.join([str(kp[n][0]),op[p][0],'(((',str(kp[n][1]),op[p][1],str(kp[n][2]),')',op[p][2],str(kp[n][3]),')',op[p][3],str(kp[n][4]),')'])
            potential_solution6 = ''.join(['(',str(kp[n][0]),op[p][0],str(kp[n][1]),')',op[p][1],'(',str(kp[n][2]),op[p][2],'(',str(kp[n][3]),op[p][3],str(kp[n][4]),'))'])
            potential_solution7 = ''.join(['(',str(kp[n][0]),op[p][0],str(kp[n][1]),')',op[p][1],'((',str(kp[n][2]),op[p][2],str(kp[n][3]),')',op[p][3],str(kp[n][4]),')'])
            potential_solution8 = ''.join(['(',str(kp[n][0]),op[p][0],'(',str(kp[n][1]),op[p][1],str(kp[n][2]),'))',op[p][2],'(',str(kp[n][3]),op[p][3],str(kp[n][4]),')'])
            potential_solution9 = ''.join(['(',str(kp[n][0]),op[p][0],'(',str(kp[n][1]),op[p][1],'(',str(kp[n][2]),op[p][2],str(kp[n][3]),')))',op[p][3],str(kp[n][4])])
            potential_solution10 = ''.join(['(',str(kp[n][0]),op[p][0],'((',str(kp[n][1]),op[p][1],str(kp[n][2]),')',op[p][2],str(kp[n][3]),'))',op[p][3],str(kp[n][4])])
            potential_solution11 = ''.join(['((',str(kp[n][0]),op[p][0],str(kp[n][1]),')',op[p][1],str(kp[n][2]),')',op[p][2],'(',str(kp[n][3]),op[p][3],str(kp[n][4]),')'])
            potential_solution12 = ''.join(['((',str(kp[n][0]),op[p][0],str(kp[n][1]),')',op[p][1],'(',str(kp[n][2]),op[p][2],str(kp[n][3]),'))',op[p][3],str(kp[n][4])])
            potential_solution13 = ''.join(['((',str(kp[n][0]),op[p][0],'(',str(kp[n][1]),op[p][1],str(kp[n][2]),'))',op[p][2],str(kp[n][3]),')',op[p][3],str(kp[n][4])])
            potential_solution14 = ''.join(['(((',str(kp[n][0]),op[p][0],str(kp[n][1]),')',op[p][1],str(kp[n][2]),')',op[p][2],str(kp[n][3]),')',op[p][3],str(kp[n][4])])
            
            # CHECKING IF ANY SOLUTIONS EQUAL THE TARGET. THE TRY SKIPS DIVIDE BY ZERO ERRORS            
            try:
                if eval(potential_solution) == solve_output:
                    print(potential_solution, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution1) == solve_output:
                    print(potential_solution1, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution2) == solve_output:
                    print(potential_solution2, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution3) == solve_output:
                    print(potential_solution3, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution4) == solve_output:
                    print(potential_solution4, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution5) == solve_output:
                    print(potential_solution5, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution6) == solve_output:
                    print(potential_solution6, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution7) == solve_output:
                    print(potential_solution7, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution8) == solve_output:
                    print(potential_solution8, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution9) == solve_output:
                    print(potential_solution9, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution10) == solve_output:
                    print(potential_solution10, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution11) == solve_output:
                    print(potential_solution11, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution12) == solve_output:
                    print(potential_solution12, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution13) == solve_output:
                    print(potential_solution13, " = ", solve_output)
                    solved = True
                    break
            except: pass
            try:
                if eval(potential_solution14) == solve_output:
                    print(potential_solution14, " = ", solve_output)
                    solved = True
                    break
            except: pass
        if solved == True:
            break
    else:
        print("No solution exists.")

if __name__ == "__main__":
    print("Welcome to the Sumthing Solver!")

    try:
        # Prompt user for 5 numbers
        raw_input = input("Enter 5 input numbers (separated by spaces): ")
        solve_input = list(map(int, raw_input.strip().split()))
        if len(solve_input) != 5:
            raise ValueError("You must enter exactly 5 numbers.")

        # Prompt user for target
        solve_output = int(input("Enter the target number: "))

        print("\n🃏 Your hand and target:\n")
        print(print_format(solve_input, solve_output))

        print("🔍 Solving...\n")
        sumthing_solver(solve_input, solve_output)

    except Exception as e:
        print("❌ Error:", e)