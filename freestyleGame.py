import sys
import random
import time
def main():
    print("Pick a range of values: ")
    min_val = int(input("Minimum value: "))
    max_val = int(input("Maximum value: "))
    num_of_vals = int(input("Enter number of values to be generated: "))
    values = []
    for i in range(4):
        input = int(input("Enter Number: "))
        values.append()

def generate_start_node(values,num_of_vals, min, max):
    while len(values) < num_of_vals:
        value = random.randint(min,max)
        values.append(value)
    return values