from customlist import CustomList

my_list = CustomList()
my_list.add("apple")
print("My List Size: ", my_list.size())
print(my_list)
my_list.add("banana")
print("Added, 'banana', My NEW List Size: ", my_list.size())
print(my_list)
print("Getting index 1 item: ",my_list.get(1))

print("- - - - - - - - - - -")

my_second_list = CustomList()
for i in range(11):
    my_second_list.add(i)
print("My Second List Size: ", my_second_list.size())
print(my_second_list)
print("Getting index 5 item: ",my_second_list.get(5))

print("- - - - - - - - - - -")

# Here, Python is much slower than Java at creating a 1,000,000 items list! Interesting :)
my_huge_list = CustomList()
for i in range(1000000):
    my_huge_list.add(f"item {i}")
print("My Huge List Size: ", my_huge_list.size())
print("Getting index 500 item: ",my_huge_list.get(500))
print("Getting index 999999 item: ",my_huge_list.get(999999))