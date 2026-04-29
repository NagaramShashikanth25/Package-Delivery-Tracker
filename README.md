# 📦 Package Delivery Tracker

> A beginner-friendly DSA project built in **Python** and **C++** that simulates a real-world package delivery system using **Array**, **Linked List**, and **Stack**.

---

## 🧠 Data Structures Used

| Structure | Role | Time Complexity |
|---|---|---|
| **Array** | Warehouse slots (fixed storage) | O(1) read/write, O(n) search |
| **Linked List** | Delivery route (chain of stops) | O(1) advance |
| **Stack** | Status history + Undo (LIFO) | O(1) push/pop |

---

## 🚀 Features

- ✅ Add a new package to the warehouse
- ✅ Advance a package through the delivery route
- ✅ View the current route of any package
- ✅ See full status log (stack)
- ✅ Undo the last event

---

## 🗺️ Delivery Route (Linked List)

```
Warehouse --> Sorting Hub --> Local Depot --> Delivered
```

Each stop is a `Node` with a pointer to the next stop.  
Moving forward = `current = current.next` → **O(1)**

---

## 🏗️ Project Structure

```
📦 package-delivery-tracker
 ┣ 📄 delivery_tracker.py       ← Python version
 ┣ 📄 delivery_tracker_simple.cpp  ← C++ version
 ┗ 📄 README.md
```

---

## ▶️ How to Run

### Python
```bash
python3 delivery_tracker.py
```

### C++
```bash
g++ -o tracker delivery_tracker_simple.cpp
./tracker
```

---

## 🖥️ Sample Output

```
=== Package Delivery Tracker ===

1. Add package
2. Advance route
3. Show route
4. Show status log
5. Undo last event
0. Exit
Choice: 1

  Added PKG-1 to slot 0

Choice: 2
  Package index (0-based): 0
  PKG-1 moved to: Sorting Hub

Choice: 3
  Package index: 0
  Warehouse -> [Sorting Hub] -> Local Depot -> Delivered
```

---

## 📚 Concepts Covered

- **Array** — fixed-size sequential storage
- **Linked List** — dynamic chain of nodes with pointers
- **Stack (LIFO)** — last in, first out event logging
- **Pointer traversal** — moving through linked nodes
- **Undo mechanism** — using stack pop

---

## 🙋 Viva Questions Covered

1. Why Array for warehouse? → Fixed size, O(1) index access
2. Why Linked List for route? → Sequential, O(1) pointer move
3. Why Stack for history? → LIFO order, perfect for undo
4. What is LIFO? → Last In First Out
5. Time complexity of each operation? → See table above

---

## 👨‍💻 Author

Made as a DSA mini-project covering **Arrays**, **Linked Lists**, and **Stacks**.

---

## 📝 License

This project is open source and free to use for educational purposes.
