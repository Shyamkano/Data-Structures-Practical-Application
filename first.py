import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Node class for Linked List and Trees
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # For Doubly Linked List
        self.left = None
        self.right = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current:
            if current.value == value:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                return
            current = current.next

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                self._insert(current_node.right, value)
            else:
                current_node.right = Node(value)

    def traverse(self):
        elements = []
        self._traverse(self.root, elements)
        return elements

    def _traverse(self, node, elements):
        if node:
            self._traverse(node.left, elements)
            elements.append(node.value)
            self._traverse(node.right, elements)

    def draw_tree(self, ax, x, y, dx):
        if self.root:
            self._draw_node(ax, self.root, x, y, dx)

    def _draw_node(self, ax, node, x, y, dx):
        ax.text(x, y, str(node.value), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
        if node.left:
            ax.plot([x, x - dx], [y - 0.1, y - 0.3], color='black')
            self._draw_node(ax, node.left, x - dx, y - 0.3, dx / 2)
        if node.right:
            ax.plot([x, x + dx], [y - 0.1, y - 0.3], color='black')
            self._draw_node(ax, node.right, x + dx, y - 0.3, dx / 2)

# Stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def traverse(self):
        return self.items[::-1]  # Return reversed for display

# Queue class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def traverse(self):
        return self.items

# Priority Queue class
class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value, priority):
        self.items.append((value, priority))
        self.items.sort(key=lambda x: x[1])  # Sort based on priority

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def traverse(self):
        return [item[0] for item in self.items]

# Graph class
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # Ensure both vertices exist in the graph
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def traverse(self):
        return self.graph

    def plot_graph(self):
        G = nx.Graph()  # Create a new Graph object from NetworkX

        for node, edges in self.graph.items():
            for edge in edges:
                G.add_edge(node, edge)

        pos = nx.spring_layout(G)  # Positioning of nodes
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
        plt.title("Graph Representation")
        plt.show()

# Hash Table class
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def traverse(self):
        return self.table

# Create the application window
app = ctk.CTk()
app.geometry("900x600")
app.title("Data Structures Practical Application")

# Initialize data structures
singly_linked_list = SinglyLinkedList()
doubly_linked_list = DoublyLinkedList()
binary_search_tree = BinarySearchTree()
stack = Stack()
queue = Queue()
priority_queue = PriorityQueue()
graph = Graph()
hash_table = HashTable()

# Function to display content in the main area
def display_content(content):
    for widget in main_content_frame.winfo_children():
        widget.destroy()  # Clear previous content

    label = ctk.CTkLabel(main_content_frame, text=content, font=("Arial", 18))
    label.pack(pady=20)

# Function to clear main content area for new buttons
def clear_main_content():
    for widget in main_content_frame.winfo_children():
        widget.destroy()

# Function for Singly Linked List display
def display_singly_linked_list():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value to insert/delete")
    entry_value.pack(pady=10)

    def insert_value():
        value = entry_value.get()
        if value:
            singly_linked_list.insert(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Linked List: " + ", ".join(singly_linked_list.traverse()))

    def delete_value():
        value = entry_value.get()
        if value:
            singly_linked_list.delete(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Linked List: " + ", ".join(singly_linked_list.traverse()))

    ctk.CTkButton(main_content_frame, text="Insert", command=insert_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Delete", command=delete_value).pack(pady=5)

# Function for Doubly Linked List display
def display_doubly_linked_list():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value to insert/delete")
    entry_value.pack(pady=10)

    def insert_value():
        value = entry_value.get()
        if value:
            doubly_linked_list.insert(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Doubly Linked List: " + ", ".join(doubly_linked_list.traverse()))

    def delete_value():
        value = entry_value.get()
        if value:
            doubly_linked_list.delete(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Doubly Linked List: " + ", ".join(doubly_linked_list.traverse()))

    ctk.CTkButton(main_content_frame, text="Insert", command=insert_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Delete", command=delete_value).pack(pady=5)

# Function for Binary Search Tree display
def display_binary_search_tree():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value to insert")
    entry_value.pack(pady=10)

    def insert_value():
        value = entry_value.get()
        if value:
            binary_search_tree.insert(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Binary Search Tree: " + ", ".join(map(str, binary_search_tree.traverse())))

    ctk.CTkButton(main_content_frame, text="Insert", command=insert_value).pack(pady=5)

# Function for Stack display
def display_stack():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value to push/pop")
    entry_value.pack(pady=10)

    def push_value():
        value = entry_value.get()
        if value:
            stack.push(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Stack: " + ", ".join(stack.traverse()))

    def pop_value():
        value = stack.pop()
        display_content(f"Popped: {value}\nStack: " + ", ".join(stack.traverse()))

    ctk.CTkButton(main_content_frame, text="Push", command=push_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Pop", command=pop_value).pack(pady=5)

# Function for Queue display
def display_queue():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value to enqueue/dequeue")
    entry_value.pack(pady=10)

    def enqueue_value():
        value = entry_value.get()
        if value:
            queue.enqueue(value)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Queue: " + ", ".join(queue.traverse()))

    def dequeue_value():
        value = queue.dequeue()
        display_content(f"Dequeued: {value}\nQueue: " + ", ".join(queue.traverse()))

    ctk.CTkButton(main_content_frame, text="Enqueue", command=enqueue_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Dequeue", command=dequeue_value).pack(pady=5)

# Function for Priority Queue display
def display_priority_queue():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value and priority (comma separated)")
    entry_value.pack(pady=10)

    def enqueue_value():
        try:
            value, priority = entry_value.get().split(',')
            priority_queue.enqueue(value.strip(), int(priority.strip()))
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Priority Queue: " + ", ".join(priority_queue.traverse()))
        except ValueError:
            display_content("Invalid input. Use format: value, priority")

    def dequeue_value():
        value = priority_queue.dequeue()
        display_content(f"Dequeued: {value}\nPriority Queue: " + ", ".join(priority_queue.traverse()))

    ctk.CTkButton(main_content_frame, text="Enqueue", command=enqueue_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Dequeue", command=dequeue_value).pack(pady=5)

# Function for Graph display
def display_graph():
    clear_main_content()

    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter edge (u,v)")
    entry_value.pack(pady=10)

    def add_edge():
        try:
            u, v = entry_value.get().split(',')
            graph.add_edge(u.strip(), v.strip())
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content(f"Graph: {graph.traverse()}")
            graph.plot_graph()  # Plot the graph after adding an edge
        except ValueError:
            display_content("Invalid input. Use format: u,v")

    ctk.CTkButton(main_content_frame, text="Add Edge", command=add_edge).pack(pady=5)

# Function for Hash Table display
def display_hash_table():
    clear_main_content()

    entry_key = ctk.CTkEntry(main_content_frame, placeholder_text="Enter key to insert/delete")
    entry_key.pack(pady=5)
    
    entry_value = ctk.CTkEntry(main_content_frame, placeholder_text="Enter value")
    entry_value.pack(pady=5)

    def insert_value():
        key = entry_key.get()
        value = entry_value.get()
        if key and value:
            hash_table.insert(key, value)
            entry_key.delete(0, tk.END)
            entry_value.delete(0, tk.END)  # Clear the entry
            display_content("Hash Table: " + str(hash_table.traverse()))

    def delete_value():
        key = entry_key.get()
        if key:
            hash_table.delete(key)
            entry_key.delete(0, tk.END)  # Clear the entry
            display_content("Hash Table: " + str(hash_table.traverse()))

    ctk.CTkButton(main_content_frame, text="Insert", command=insert_value).pack(pady=5)
    ctk.CTkButton(main_content_frame, text="Delete", command=delete_value).pack(pady=5)

# Create main content frame
main_content_frame = ctk.CTkFrame(app)
main_content_frame.pack(pady=20)

# Create buttons for each data structure
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

ctk.CTkButton(button_frame, text="Singly Linked List", command=display_singly_linked_list).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Doubly Linked List", command=display_doubly_linked_list).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Binary Search Tree", command=display_binary_search_tree).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Stack", command=display_stack).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Queue", command=display_queue).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Priority Queue", command=display_priority_queue).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Graph", command=display_graph).pack(side=tk.LEFT, padx=10)
ctk.CTkButton(button_frame, text="Hash Table", command=display_hash_table).pack(side=tk.LEFT, padx=10)

# Start the application
app.mainloop()
