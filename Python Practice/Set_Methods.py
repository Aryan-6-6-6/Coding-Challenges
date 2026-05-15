# Python Set Methods: Categorized by Mutability with Individual Outputs

# Mutable Methods (Modify the Original Set)
# ------------------------------------------
# Example set
my_set = {1, 2, 3}

# Add a single element to the set
my_set.add(4)
print("After add(4):", my_set)

# Remove all elements from the set
my_set.clear()
print("After clear():", my_set)

# Remove a specific element; no error if it doesn't exist
my_set = {1, 2, 3}
my_set.discard(2)
print("After discard(2):", my_set)

# Remove a specific element; raises KeyError if it doesn't exist
my_set.remove(1)
print("After remove(1):", my_set)

# Remove and return an arbitrary element; raises KeyError if set is empty
my_set = {1, 2, 3}
arbitrary_element = my_set.pop()
print("After pop():", my_set, "Popped Element:", arbitrary_element)

# Update the set with the union of itself and other sets
my_set = {1, 2, 3}
my_set.update({4, 5})
print("After update({4, 5}):", my_set)

# Update the set with the intersection of itself and other sets
my_set.intersection_update({3, 4, 5})
print("After intersection_update({3, 4, 5}):", my_set)

# Update the set by removing elements found in other sets
my_set = {1, 2, 3, 4}
my_set.difference_update({2, 3})
print("After difference_update({2, 3}):", my_set)

# Update the set with symmetric difference (elements in either set but not both)
my_set = {1, 2, 3, 4}
my_set.symmetric_difference_update({3, 4, 5})
print("After symmetric_difference_update({3, 4, 5}):", my_set)


# Immutable Methods (Do Not Modify the Original Set)
# --------------------------------------------------
# Example sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Return a shallow copy of the set
new_set = set1.copy()
print("After copy():", new_set)

# Return the union of sets
union_set = set1.union(set2)
print("After union(set2):", union_set)

# Return the intersection of sets
intersection_set = set1.intersection(set2)
print("After intersection(set2):", intersection_set)

# Return the difference of sets
difference_set = set1.difference(set2)
print("After difference(set2):", difference_set)

# Return the symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("After symmetric_difference(set2):", symmetric_difference_set)

# Check if two sets are disjoint
are_disjoint = set1.isdisjoint(set2)
print("After isdisjoint(set2):", are_disjoint)

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("After issubset(set2):", is_subset)

# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("After issuperset(set2):", is_superset)
