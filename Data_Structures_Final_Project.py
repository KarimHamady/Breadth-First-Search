import numpy as np


# Create a class node containing a key and a pointer
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create a class queue
class Queue:

    # Constructor: Initiate front and rear pointers to None
    def __init__(self):
        self.front = self.rear = None

    # function to check where function is empty or not
    def is_empty(self):
        return self.front is None

    # ENQUEUE function: It enqueues an element(item in this case) into the queue by creating a new node and rearranging pointers
    def enqueue(self, item):
        temp = Node(item)

        # condition for the first element enqueued in the queue
        if self.rear is None:
            self.front = self.rear = temp
            return
        # creating a pointer to the new node created and changing the position of the rear pointer
        self.rear.next = temp
        self.rear = temp

    def frontt(self):
        return self.front.data

    # DEQUE function: It removes the first element in the queue
    def deque(self):
        # condition to make sure we are not removing nothing
        if self.is_empty():
            return True
        # changing the position of the front pointer
        temp = self.front
        self.front = temp.next
        # condition if this is the last element to be removed
        if self.front is None:
            self.rear = None

    # function that prints the values of the elements in the queue
    def print_queue(self):
        # condition if the queue is empty, then there's nothing to print
        if self.is_empty():
            print('Empty Queue')
            return
        # store the front pointer in another pointer
        temp_point = self.front
        # loop over all the elements
        while temp_point is not None:
            print(temp_point.data)
            temp_point = temp_point.next

    # function that clears all keys in the queue by calling the deque function in a loop
    def clear(self):
        while not self.is_empty():
            self.deque()


def breadth_first_search(size, adjacency_matrix):
    # Requesting from the user to enter the number he wishes to search for
    goal = int(input('Choose a number that you want to search for: '))

    # Starting from node 1 as assumed/ enqueuing it to the list and adding it to visited nodes
    print(1)
    q = Queue()
    q.enqueue(1)
    visited = [1]

    # Keep looping until q is empty which means all nodes are visited
    while not q.is_empty():

        # Storing the first element in the queue to keep track of the path for the BFS
        first = q.frontt()
        q.deque()

        # Loop over every row in the adjacency matrix to check for edges
        for a in range(1, size + 1):

            # Enqueuing the node if there is an edge from the node we're in to another node and making sure that the
            # node to be visited is not visited before ( This is to avoid being stuck in infinite loops/cycles)
            if a not in visited and adjacency_matrix[first - 1, a - 1] == 1:
                print(a)
                visited.append(a)
                q.enqueue(a)

                # Returning when the node we're searching for is found
                if goal == a:
                    print(f"There is a path from 1 to {goal}")
                    return

    # When all nodes are visited and the function didn't return, this means that there is no path from 1 to the node
    # that the user is searching for
    print(f"There is no path from 1 to {goal}")


def main():
    # Requesting from the user to insert the number of nodes to initialize the adjacency matrix
    n = int(input("Enter the number of nodes for the graph G to be created: "))
    a = np.zeros((n, n), dtype=int)

    # Requesting from the user to choose between a directed and undirected graph
    print("Do you want the graph to be directed or undirected?")
    directed = input(" Type 'directed' or 'undirected' to choose: ").lower()
    # This loop is to ensure that the user doesn't enter any other invalid input like numbers or unknown words
    while directed != 'directed' and directed != 'undirected':
        directed = input("Please enter if 'directed' or 'undirected' only: ")
    if directed == 'directed':
        directed = True
    elif directed == 'undirected':
        directed = False

    # Requesting from the user to insert all edges in the graph or create the graph.
    print('''Enter the edges: 
    To add an edge type '1 and 2' to create an edge from 1 to 2 if directed and adds an edge from 2 to 1 if undirected")
    If you wish to create the graph type:"Create"'''
          )
    edges = input("> ").split()
    # This loop is to keep inserting edges until the user asks to create the graph and stops inserting more edges
    while edges[0] != 'Create':
        # When the user enters '1 and 2' for example, first node is taken as 1 and second node as 2
        # This is done using .split() and list indexing
        first_node = int(edges[0])
        second_node = int(edges[2])

        if 0 < first_node <= n and 0 < second_node <= n:

            # This block of code checks if the graph is directed or undirected to decide whether to insert an edge from
            # 1 to 2 for example only or from 1 to 2 and 2 to 1
            if directed:
                a[first_node - 1, second_node - 1] = 1
            else:
                a[first_node - 1, second_node - 1] = 1
                a[second_node - 1, first_node - 1] = 1
        edges = input("> ").split()

    # This is to show the adjacency matrix for the user
    print(a)
    # Calling breadth first search function
    breadth_first_search(n, a)


if __name__ == "__main__":
    main()
