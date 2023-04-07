import random

# Initialize the boxes
boxes = ['A', 'B', 'C', 'D', 'E']

# Select a random box to hide the object
object_box = random.choice(boxes)

# Start searching for the object
current_box = random.choice(boxes)
for i in range(7):
    print(f"Step {i+1}: Object is not in {current_box}")
    # Determine the possible next boxes to move to
    possible_boxes = []
    if current_box != 'A':
        possible_boxes.append(boxes[boxes.index(current_box)-1])
    if current_box != 'E':
        possible_boxes.append(boxes[boxes.index(current_box)+1])
    # Move to a random next box
    current_box = random.choice(possible_boxes)
    # Check if the object is found
    if current_box == object_box:
        print(f"Step {i+2}: Object is in {current_box}")
        break
