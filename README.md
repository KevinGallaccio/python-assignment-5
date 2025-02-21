# Assignment 5 - Implementing a Custom ArrayList in Python

## **Overview**
This project is a Python implementation of **Assignment #5** from Coders Campus, which involves creating a custom resizable list, similar to Java's `ArrayList`. The assignment was originally written in Java, and I translated it into Python while ensuring it maintained the same behavior.

---

## **Original Java Assignment Instructions**

### **Objective**
This assignment focuses on **algorithms**, specifically implementing a **custom ArrayList data structure** from scratch.

🔹 **Rules:** No looking at Java's source code for `ArrayList`! 🚫🧐  
🔹 **Task:** Implement all abstract methods from the `CustomList` interface via the `CustomArrayList` class.

### **Requirements**
1. **Grow the backing array when needed:**
   - If the backing `Object[]` array is full, it should **double in size**.
   - When adding the 11th element, increase the array from **10 to 20**.
   - When adding the 21st element, increase from **20 to 40**, etc.
   - We do **not** need to worry about removing elements for this assignment.

2. **Test the implementation** using a `CustomListApplication` class with a `main` method.
   - Add more than 10 elements to verify resizing works.

### **Java Test Example**
```java
CustomList<String> myCustomList = new CustomArrayList<>();
myCustomList.add("element 1"); // Add at least 10-20 more elements

// Validate elements exist in the list
for (int i=0; i<myCustomList.getSize(); i++) {
    System.out.println(myCustomList.get(i));
}
```

🔗 **Starter Repo:** [CodersCampus/Assignment5starter](https://github.com/CodersCampus/Assignment5starter)

---

## **Translating This to Python**
### **Challenges & Lessons Learned**

### **1️⃣ Java’s `ArrayList` vs. Python’s `list`**
- **Java’s `ArrayList`** requires **manual resizing** when full (we use `System.arraycopy()` or `Arrays.copyOf()`).
- **Python’s `list`** dynamically resizes **automatically**, but for this assignment, I had to implement manual resizing **to mimic Java's behavior**.

### **2️⃣ No Generics in Python**
- Java’s `ArrayList<T>` allows **type enforcement** at compile time.
- Python **doesn't have generics** the same way, so our `CustomList` can store **any data type dynamically**.

### **3️⃣ Java’s `System.arraycopy()` vs. Python’s List Copying**
- In Java, we use:
  ```java
  Object[] newArray = Arrays.copyOf(items, items.length * 2);
  ```
- In Python, we need to manually copy elements into a new list:
  ```python
  resized_list = [None] * (len(self.items) * 2)
  resized_list[:len(self.items)] = self.items  # Pythonic slicing
  self.items = resized_list
  ```
- **Performance difference:** Java is optimized for array copying, while Python requires **interpreted execution**, making it slightly slower.

### **4️⃣ No Private Methods in Python?**
- Java allows `private` methods (`private void resize()`), but Python doesn’t have true private methods.
- **Workaround:** Prefix methods with `_` (soft private) or `__` (name mangling):
  ```python
  def __resize(self):  # Private method using name mangling
  ```

### **5️⃣ Method Naming Differences**
- **Java uses `getSize()`, Python prefers `size()`** (or `len(self.items)`).
- I had to **avoid naming conflicts** between the `size()` method and the `self.size` attribute by renaming `self.size → self.list_size`.

---

## **Python Implementation - `CustomList`**
Here’s my final Python version:
```python
class CustomList:
    def __init__(self):
        self.list_size = 0
        self.items = [None] * 10

    def add(self, item):
        if self.list_size == len(self.items):
            self.__resize()
        self.items[self.list_size] = item
        self.list_size += 1

    def size(self):
        return self.list_size

    def get(self, index):
        return self.items[index]

    def __resize(self):
        resized_list = [None] * (len(self.items) * 2)
        resized_list[:len(self.items)] = self.items  # Pythonic way to copy list
        self.items = resized_list

    def __repr__(self):
        return f'{self.items[:self.list_size]}'
```

---

## **Testing in `main.py`**
```python
from customlist import CustomList

# Test basic functionality
my_list = CustomList()
my_list.add("apple")
print("My List Size: ", my_list.size())
print(my_list)
my_list.add("banana")
print("Added, 'banana', My NEW List Size: ", my_list.size())
print(my_list)
print("Getting index 1 item: ", my_list.get(1))

# Test resizing
my_second_list = CustomList()
for i in range(11):
    my_second_list.add(i)
print("My Second List Size: ", my_second_list.size())
print(my_second_list)
print("Getting index 5 item: ", my_second_list.get(5))

# Test performance with 1,000,000 items
my_huge_list = CustomList()
for i in range(1000000):
    my_huge_list.add(f"item {i}")
print("My Huge List Size: ", my_huge_list.size())
print("Getting index 500 item: ", my_huge_list.get(500))
print("Getting index 999999 item: ", my_huge_list.get(999999))
```

---

## **Conclusion**
✅ Successfully implemented a **resizable list in Python** that mimics Java’s `ArrayList`.  
✅ Learned key differences between **Java and Python memory handling**.  
✅ **Performance note:** Java’s `ArrayList` is **faster** due to compiled optimizations, while Python’s list resizing is **slower but flexible**.

**Next steps:** In Assignment 7, I’ll implement `remove(index)` and `add(item, index)` using **Test-Driven Development (TDD)** in Python! 🚀🐍

---

**🛠️ Built With:**
- Python 3
- No external libraries (pure Python implementation)

📌 **Author:** [Your Name]  
📌 **GitHub Repo:** [Your Repo Link]

🚀 **Ready for the next challenge!**

