import json
import os

# full path to the memory file
memory_file_path = "D:/david_project/david_memory.json"


# load memory from this file
def load_memory():
    if os.path.exists(memory_file_path):
        with open(memory_file_path, 'r') as file:
            return json.load(file)
    else:
        return{}
    
# save memory to file
def save_memory(memory):
    with open(memory_file_path, 'w') as file:
        json.dump(memory, file, indent=4)

# add or update memory
def add_to_memory(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

# retrieve memory
def get_from_memory(key):
    memory = load_memory()
    return memory.get(key, "I don't remember that.")