output = "output.txt" #expected output from ROPgadget

pruned = []
implemented = ["ret", "pop", "add", "inc", "sub", "mov"]
registers = ["eax", "ebx", "ecx", "edx", "eip", "esp", "ebp"]

keywords = implemented + registers
blacklist = ["bad word"] #if you need to blacklist things

with open(output) as f:
    pruned = [line for line in f if any(word in line for word in implemented)]
    pruned = [line for line in pruned if not(any(word in line for word in blacklist))]
    for line in pruned:
        print line