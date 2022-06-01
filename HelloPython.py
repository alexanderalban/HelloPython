# Printing messages, creating variables
print("Hello World")


msg = "Hello World"
print(msg)


# Multiplication and other equations
print(8 * 3.57)
print(((5+30)*20)/10)

# Let's say you find 20 coins in the woods. You put them in a magic replicator, which spits out 10 coins a day. A raven
# (who likes the shiny coins) flies in your window and steals 3 coins a week. How many coins to you have after a year?
found_coins = 20
magic_coins = 10
stolen_coins = 3

total_coins = found_coins + magic_coins * 365 - stolen_coins * 52

print("Total coins equals", total_coins)

# You installed a scarecrow which means the raven can only steal two coins a week. How many would you have after a year?
stolen_coins = 2

total_coins = found_coins + magic_coins * 365 - stolen_coins * 52

print("Updated total coins is", total_coins)

# You bang the side of the machine and it spits out and extra three coins each time.
magic_coins = 13
total_coins = found_coins + magic_coins * 365 - stolen_coins * 52

print("Even better! Now it's", total_coins)
