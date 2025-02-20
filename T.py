import itertools
import tkinter as tk
from itertools import permutations, product

def can_place(rectangles, container_width, container_height, placements):
    # Create a container grid initialized to False (indicating empty cells)
    grid = [[False] * container_width for _ in range(container_height)]
    
    for rect, (x, y) in zip(rectangles, placements):
        rect_width, rect_height = rect
        # Check if the rectangle fits in the container at the given position
        if x + rect_width > container_width or y + rect_height > container_height:
            return False
        # Check for overlap with already placed rectangles
        for i in range(rect_width):
            for j in range(rect_height):
                if grid[y + j][x + i]:
                    return False
        # Place the rectangle in the grid
        for i in range(rect_width):
            for j in range(rect_height):
                grid[y + j][x + i] = True
                
    return True

def brute_force_2d_packing_multiple(container_width, container_height, rectangles):
    # Generate all permutations of the rectangles
    all_permutations = permutations(rectangles)
    
    for perm in all_permutations:
        # Generate all possible placements for the rectangles in the permutation
        for placements in itertools.product(
            *(product(range(container_width - w + 1), range(container_height - h + 1)) for w, h in perm)
        ):
            if can_place(perm, container_width, container_height, placements):
                return placements, perm
                
    return None

def visualize_packing(container_width, container_height, rectangles, placements):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=container_width * 50, height=container_height * 50)
    canvas.pack()
    
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    
    for (rect_width, rect_height), (x, y), color in zip(rectangles, placements, colors):
        canvas.create_rectangle(
            x * 50, y * 50, (x + rect_width) * 50, (y + rect_height) * 50,
            fill=color, outline="black"
        )
    
    root.mainloop()

# Exemples d'utilisation
container_width = 10
container_height = 10
rectangles = [(3, 2), (2, 2), (5, 3)]

result = brute_force_2d_packing_multiple(container_width, container_height, rectangles)
if result:
    placements, perm = result
    print(f"Possible placements for the rectangles {rectangles} in a container of size ({container_width}, {container_height}):")
    for rect, placement in zip(perm, placements):
        print(f"Rectangle {rect} placed at top-left corner: {placement}")
    visualize_packing(container_width, container_height, perm, placements)
else:
    print("No valid placement found.")
