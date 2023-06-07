import random
import time

"""
This code provided is an AI of 24 game using depth-first search
Both sets of code generates a random set of 4 integers then goes
through a series of operations to try and reach the goal of 24.
Also, at the end it tells the processing time it took to find a solution 
if there is one.

"""
# This method generates a random list of 4 integers in range [1,13]
# @param values: an empty list originally
# @return values: a full list of 4 generated integers
def generate_start_node(values):
    while len(values) < 4:
        value = random.randint(1,13)
        values.append(value)
    return values


# This method finds the first solution and returns it with depth-first-search
# @params node: set of integers (probably wrong word to describe)
# @path_sequence: a sequence of strings where each string describes an action of a state
# @return: bool True or False
def single_solution_24_game(node,path_sequence):
    if len(node) == 1:
        if node[0] == 24:
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
                if single_solution_24_game([a + b] + remaining_node,path_sequence):
                    tuple = (str(a) + "add" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Subtraction
                if single_solution_24_game([a - b] + remaining_node,path_sequence):
                    tuple = (str(a) + "sub" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Multiplication
                if single_solution_24_game([a * b] + remaining_node,path_sequence):
                    tuple = (str(a) + "mu" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Division
                if b != 0 and single_solution_24_game([a / b] + remaining_node,path_sequence):
                    tuple = (str(a) + "div" + str(b))
                    path_sequence.append(tuple)
                    return True

    return False  

#Main function that calls the functions above
def main():
    
    values = []
    path_sequence = []
    node = generate_start_node(values)
    print("FIRST PROGRAM: ")
    print("Input: ", node)
    start = time.time()
    if single_solution_24_game(node,path_sequence):
        print("Yes it does reach to 24")
        path_sequence.reverse()
        print("Found Solution:", path_sequence)

    else:
        print("It never reaches to 24")
    end = time.time()
    processing_time = (end - start) * 10**3
    print("Processing time: " + str(processing_time) + "ms")
    
main()

# Nested functions
# outer function contains the variable "path_solutions" to store paths
# that lead to goal value 24
# @param node : list of integers
# @return path_solutions : list of strings containing paths to solutions
def multiple_solutions_24_game(node):
    path_solutions = []
    
    # Similar function to one above except it does not return a boolean value
    # Stores solutions to the list in the outer function
    # @param node : list of integers
    # @param path_sequence: an initialised empty list

    def find_a_solution(node, path_sequence=[]):
        if len(node) == 1:
            if node[0] == 24:
                path_solutions.append(path_sequence)
            return
            
            
        for i in range(len(node)):
            for j in range(len(node)):
                if i != j:
                    a = node[i]
                    b = node[j]
                    remaining_node = [node[k] for k in range(len(node)) if k != i and k != j]
            
                    # Addition
                    tuple = (str(a) + "add" + str(b))
                    find_a_solution([a + b] + remaining_node,path_sequence + [tuple])
                        

                    # Subtraction
                    tuple = (str(a) + "sub" + str(b))
                    find_a_solution([a - b] + remaining_node,path_sequence + [tuple])
                        
                    # Multiplication
                    tuple = (str(a) + "mu" + str(b))
                    find_a_solution([a * b] + remaining_node,path_sequence + [tuple])
                        

                    # Division
                    if b != 0:
                        tuple = (str(a) + "div" + str(b))
                        find_a_solution([a / b] + remaining_node,path_sequence + [tuple])
                        
    find_a_solution(node)
    return path_solutions

# Main function that generates start node then passes it on to the function above    
def main2():
    values = []
    node = generate_start_node(values)
    print("SECOND PROGRAM: ")
    print("Input: ", node)
    start = time.time()
    solutions = multiple_solutions_24_game(node)
    end = time.time()
    processing_time = (end-start) * 10**3
    if solutions:
        print("Here are the different solutions: ")
        for solution in solutions:
            print(solution)
    else:
        print("No solutions found")
    print("Processing time: " + str(processing_time) + "ms")

main2()


