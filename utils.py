from sets import Set
import random

def check_gadget(gadget, config):
    inst = gadget.split(" ; ")
    if len(inst)==0 or len(inst)>config["MAX_GADGET_LENGTH"]:
        return False
    for i in inst:
        ops = i.split(" ")
        if ops[0] not in config["implemented"]:
            return False
        for w in config["blacklist"]:
            if w in i:
                return False
    return True

def gadget_to_c(gadget_set, gadget, name):
    header = "//" + gadget + "\n"
    insts = gadget.split(" ; ")
    body = ""
    header += "void %s(int prev_choice){\n"%name
    header += '\tprintf("%s\\n");\n'%(gadget)
    tail = "}\n"
    for i in insts:
        body+=inst_to_c(i)
    if body in gadget_set:
        return ""
    else:
        gadget_set.add(body)

        return header+body+tail

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
    elif op=="add":
        # return ""
        # return "\t%s();\n"%"not_implemented"
        a1, a2 = args.split(", ")
        if "dword ptr" in a1 and "dword ptr" not in a2:
            return ""
            result = "\t%s_to_pointer(%s, %s);\n"%(op, a1[-4:-1], a2)
        elif "dword ptr" not in a1 and "dword ptr" in a2:
            result = "\t%s = \t%s_from_pointer(%s, %s);\n"%(a1, op, a1, a2[-4:-1])
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
            return ""
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
        return ""
        result = "\t%s();\n"%"not_implemented"
    return result

def build_Init_block(config):
    Init_block = ""

    for i in range(len(config["Init"]["stack"])):
        val = config["Init"]["stack"][i]
        if val==-1:
            Init_block+="int s%d = nd(); "%(i)
        else:
            Init_block+="int s%d = %d; "%(i, val)
    Init_block+="\n\n"

    for i in range(len(config["Init"]["writeable_memory"])):
        val = config["Init"]["writeable_memory"][i]
        if val==-1:
            Init_block+="int m%d = nd(); "%(i)
        else:
            Init_block+="int m%d = %d; "%(i, val)
    Init_block+="\n\n"

    for r in config["registers"]:
        val = config["Init"][r]
        if val==-1:
            Init_block+="int %s = nd(); "%(r)
        else:
            Init_block+="int %s = %d; "%(r, val)


    Init_block+="\n\n"
    return Init_block

def build_sassert(config):
    sassert = ""
    for i in range(len(config["Goal"]["stack"])):
        val = config["Goal"]["stack"][i]
        if val==-1: #we dont care about the value after the trace
            continue
        else:
            sassert+="s%d == %d && "%(i, config["Goal"]["stack"][i])
    for i in range(len(config["Goal"]["writeable_memory"])):
        val = config["Goal"]["writeable_memory"][i]
        if val==-1: #we dont care about the value after the trace
            continue
        else:
            sassert+="m%d == %d && "%(i, config["Goal"]["writeable_memory"][i])
    for r in config["registers"]:
        val = config["Goal"][r]
        if val==-1: #we dont care about the value after the trace
            continue
        else:
            sassert+="%s == %d && "%(r, config["Goal"][r])
    return "sassert(!(%s))"%sassert[:-3]