#problem statement baased on handle comples logic in game development:write a program check multiple conditons such as health and status.
#approach: We can use an if statement to check if the health of the player is greater than 0 and if the status of the player is "alive". We can use the logical operator "and" to check if both conditions are true. If both conditions are true, then we can print a message saying that the player is alive. Otherwise, we can print a message saying that the player is dead.
health=100
status="alive"
if(health>0 and status=="alive"):
    print("player is alive")
else:
    print("player is dead")
