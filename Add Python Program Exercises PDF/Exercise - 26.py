# Exercise - 26: Handshakes

def printHandshakes(people):
    totalHandshakes = 0
    for count,i in enumerate(people):
        for j in people[count + 1:]:
            # print(f"{i} shakes hand with {j}") 
            totalHandshakes += 1 


    return totalHandshakes

# print(printHandshakes(['Alice', 'Bob', 'Carol', 'David'])) 
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
            
