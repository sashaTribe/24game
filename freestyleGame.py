import sys
import random
import time

def generate_start_node(values,num_of_vals, min, max):
    while len(values) < num_of_vals:
        value = random.randint(min,max)
        values.append(value)
    return values

def single_solution_M_game(node,path_sequence,goal_val):
    if len(node) == 1:
        if node[0] == goal_val:
            return True
        else:
            path_sequence.clear()
            return False
    for i in range(len(node)):
        for j in range(len(node)):
            if i != j:
                a = node[i]
                b = node[j]
                remaining_node = [node[k] for k in range(len(node)) if k != i and k != j]

                # Addition
                if single_solution_M_game([a + b] + remaining_node,path_sequence, goal_val):
                    tuple = (str(a) + "add" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Subtraction
                if single_solution_M_game([a - b] + remaining_node,path_sequence,goal_val):
                    tuple = (str(a) + "sub" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Multiplication
                if single_solution_M_game([a * b] + remaining_node,path_sequence, goal_val):
                    tuple = (str(a) + "mu" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Division
                if b != 0 and single_solution_M_game([a / b] + remaining_node,path_sequence, goal_val):
                    tuple = (str(a) + "div" + str(b))
                    path_sequence.append(tuple)
                    return True

    return False  

def main():
    path_sequence = []
    print("Pick a range of values: ")
    min_val = int(input("Minimum value: "))
    max_val = int(input("Maximum value: "))
    num_of_vals = int(input("Enter number of values to be generated: "))
    values = []
    start_node = generate_start_node(values, num_of_vals,min_val,max_val)
    goal_val = int(input("Enter goal value: "))
    print("Input node: ", start_node)
    start = time.time()
    if single_solution_M_game(start_node,path_sequence, goal_val):
        print("Yes it does reach to ", goal_val)
        path_sequence.reverse()
        print("Found Solution:", path_sequence)

    else:
        print("It never reaches to ", goal_val)
    end = time.time()
    processing_time = (end - start) * 10**3
    print("Processing time: " + str(processing_time) + "ms")

main()