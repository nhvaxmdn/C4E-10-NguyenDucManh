inventory = {"apples":430, "bananas":312,"oranges":525}
print(inventory)

del inventory["apples"]
print(inventory)


opposites = {"up":"down","right":"wrong","yes":"no"}
alias = opposites
coppy = opposites.copy() 
alias["right"] = "left"
