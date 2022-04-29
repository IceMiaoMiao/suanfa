# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

graph = {}
graph["you"] = ["alice","bob","clare"]
graph["bob"] = ["anji","peggy"]
graph["alice"] = ["peggy"]
graph["clare"] = ["thom","jonnm"]
graph["peggy"] = []
graph["anji"] = []
graph["thom"] = []
graph["jonnm"] = []

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue+=graph[name]
    searched = []
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    search("you")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
