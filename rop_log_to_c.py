import sys

output = sys.argv[1] #expected output from ROPgadget

pruned = []
implemented = ["ret", "pop", "add", "inc", "sub", "mov", "xor"]
registers = ["eax", "ebx", "ecx", "edx"]

keywords = implemented + registers
blacklist = ["esi", "edi", "al", "ah", "bh", "bl", "cl", "ch", "dl", "dh", "es", "ss", "byte", "0x", " + ", "gs:" , "[0]"] #if you need to blacklist things
MAX_GADGET_LENGTH = 3

def check_gadget(gadget):
    inst = gadget.split(" ; ")
    if len(inst)==0 or len(inst)>MAX_GADGET_LENGTH:
        return False
    for i in inst:
        ops = i.split(" ")
        if ops[0] not in implemented:
            return False
        for w in blacklist:
            if w in i:
                return False
    return True

def gadget_to_c(gadget, name):
    print "//", gadget
    insts = gadget.split(" ; ")
    block = "void %s(){\n"%name
    for i in insts:
        block+=inst_to_c(i)
    block+="}\n"
    return block

def inst_to_c(inst):
    result = ""
    op = inst[:3]
    args = inst[4:]
    if op=="inc":
        if "dword" in args:
            result = "\t%s++;\n"%args[-4:-1]
        else:
            result = "\t%s++;\n"%args
    elif op=="pop":
        result = "\t%s = pop();\n"%args
    elif op=="add" or op=="sub":
        return "\t%s();\n"%"not_implemented"
        a1, a2 = args.split(", ")
        if "dword ptr" in a1 and "dword ptr" not in a2:
            result = "\t%s_to_pointer(%s, %s);\n"%(op, a1[-4:-1], a2)
        elif "dword ptr" not in a1 and "dword ptr" in a2:
            result = "\t%s_from_pointer(%s, %s);\n"%(op, a1, a2[-4:-1])
        elif "dword ptr" in a1 and "dword ptr" in a2:
            result = "\t%s_from_pointer_to_pointer(%s, %s);\n"%(op, a1[-4:-1], a2[-4:-1])
        else:
            if op=="add":
                result = "\t%s = %s + %s;\n"%(a1, a1, a2)
            if op=="sub":
                result = "\t%s = %s - %s;\n"%(a1, a1, a2)
    elif op=="mov":
        target, val = args.split(", ")
        if "dword" in target and "dword" not in val:
            result = "\tmove_mem_const(%s, %s);\n"%(target[-4:-1], val)
        elif "dword" not in target and "dword" in val:
            result = "\t%s = move_reg_mem(%s);\n"%(target, val[-4: -1])
        else:
            if target.isdigit():
                #result = "\tmove_reg_const(%sm %s);\n"%(target, val)
                result = "\t%s = %s;\n"%(target, val)
               #result = "\tmove_reg_reg(%s, %s);\n"%(target, val)
    elif op=="xor":
        a1, a2 = args.split(", ")
        if a1==a2:
            result = "\t%s = 0;\n"%a1    
    elif op=="ret":
        result = "\treturn;\n"
    else:
        result = "\t%s();\n"%"not_implemented"
    return result

with open(output) as f:
    pruned = []
    data = f.readlines()
    for l in data:
        if l.startswith("0") and l.endswith("ret\n"):
            _ = l.strip().split(" : ")
            address = _[0]
            gadget = _[1]
            if check_gadget(gadget):
                pruned.append([address, gadget])
    #    pruned = [line for line in f if any(word in line for word in implemented)]
    #    pruned = [line for line in pruned if not(any(word in line for word in blacklist))]
    for i in range(len(pruned)):
        gadget_name = "gadget_"+str(i)
        print gadget_to_c(pruned[i][1], gadget_name)
    print len(pruned)
