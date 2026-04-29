# ─────────────────────────────────────────
#  LINKED LIST — Delivery Route
#  Each stop is a node connected to the next
# ─────────────────────────────────────────
class Node:
    def __init__(self, stop):
        self.stop = stop
        self.next = None   


# ─────────────────────────────────────────
#  STACK — Status Log 
#  push = add event,  pop = undo event
# ─────────────────────────────────────────
class Stack:
    def __init__(self):
        self.data = []   

    def push(self, msg):
        self.data.append(msg)       

    def pop(self):
        if not self.data:
            print("  Stack is empty!")
            return
        print("  Undone:", self.data.pop())   

    def print_stack(self):
        if not self.data:
            print("  (empty)")
            return
        for msg in reversed(self.data):       
            print(" >>", msg)


# ─────────────────────────────────────────
#  PACKAGE — holds one delivery
# ─────────────────────────────────────────
class Package:
    def __init__(self, pid, slot):
        self.id   = pid
        self.slot = slot

        stops = ["Warehouse", "Sorting Hub", "Local Depot", "Delivered"]
        self.head = None
        tail = None
        for s in stops:
            node = Node(s)
            if not self.head:
                self.head = node
                tail = node
            else:
                tail.next = node
                tail = node

        self.current = self.head   
    def advance(self):
        if not self.current.next:
            print("  Already delivered!")
            return
        self.current = self.current.next    
        print(f"  {self.id} moved to: {self.current.stop}")

    def print_route(self):
        node = self.head
        route = ""
        while node:
            if node == self.current:
                route += f"[{node.stop}]"   
            else:
                route += node.stop
            if node.next:
                route += " -> "
            node = node.next
        print(" ", route)


# ─────────────────────────────────────────
#  ARRAY — Warehouse (5 fixed slots)
#  None = empty,  else holds package ID
# ─────────────────────────────────────────
SIZE      = 5
warehouse = [None] * SIZE    
def find_slot():
    for i in range(SIZE):
        if warehouse[i] is None:
            return i
    return -1   # warehouse full


# ─────────────────────────────────────────
#  MAIN — menu loop
# ─────────────────────────────────────────
def main():
    packages = []
    log      = Stack()
    count    = 0

    print("=== Package Delivery Tracker (Python) ===\n")

    while True:
        print("1. Add package")
        print("2. Advance route")
        print("3. Show route")
        print("4. Show status log")
        print("5. Undo last event")
        print("0. Exit")
        choice = input("Choice: ").strip()
        print()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":  
            slot = find_slot()
            if slot == -1:
                print("  Warehouse full!\n")
                continue
            pid = f"PKG-{count + 1}"
            pkg = Package(pid, slot)
            packages.append(pkg)
            warehouse[slot] = pid
            log.push(f"{pid} added to slot {slot}")
            print(f"  Added {pid} to slot {slot}")
            count += 1

        elif choice == "2":   
            idx = int(input("  Package index (0-based): "))
            if idx < 0 or idx >= len(packages):
                print("  Invalid index!")
            else:
                packages[idx].advance()
                log.push(f"{packages[idx].id} -> {packages[idx].current.stop}")

        elif choice == "3":   
            idx = int(input("  Package index: "))
            if idx < 0 or idx >= len(packages):
                print("  Invalid index!")
            else:
                packages[idx].print_route()

        elif choice == "4":   
            print("  --- Status Log ---")
            log.print_stack()

        elif choice == "5":   
            log.pop()

        else:
            print("  Invalid choice!")

        print()


if __name__ == "__main__":
    main()
