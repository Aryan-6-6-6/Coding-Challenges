# Exercise - 37: Change Maker

def makeChange(amount: int) -> dict:
    change = {}
    
    # Quarters (25 cents)
    quarters = amount // 25
    if quarters > 0:
        change['quarters'] = quarters
    amount = amount % 25

    # Dimes (10 cents)
    dimes = amount // 10
    if dimes > 0:
        change['dimes'] = dimes
    amount = amount % 10

    # Nickels (5 cents)
    nickels = amount // 5
    if nickels > 0:
        change['nickels'] = nickels
    amount = amount % 5

    # Pennies (1 cent)
    if amount > 0:
        change['pennies'] = amount

    return change


#  Test Cases
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}

print("All tests passed! Yay it's party time 🎉🎉")
