from triton import TritonContext, ARCH, Instruction, REG
from capstone import *

#Given a gadget, we want to extract a SMT representation

def main():
    code = [(0x1000, "\x83\xc4\x08"),
            (0x1003, "\x5b"),
            (0x1004, "\xc3")]

    ctxt = TritonContext()
    ctxt.setArchitecture(ARCH.X86)

    #load instructions
    for (addr, opcode) in code:
        inst = Instruction()
        inst.setOpcode(opcode)
        inst.setAddress(addr)
        if not ctxt.processing(inst):
            print "Fail an instruction"
        print inst
        expr = inst.getSymbolicExpressions()[0]
        print expr

if __name__ == '__main__':
    main()


