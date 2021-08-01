import random
health = 50
difficulty = 3
portionHealth = int(random.randint(25,50)/difficulty)
health +=portionHealth

print(health)
