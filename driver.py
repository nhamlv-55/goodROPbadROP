import subprocess
import argparse
import json
import sys
import time

use_cfi = sys.argv[1]
config = sys.argv[2]
coutput = "/tmp/"+sys.argv[3]+"_"+use_cfi+".c"

subprocess.call(("touch %s"%(coutput)).split(" "))
subprocess.call(("python rop_log_to_c.py --roplog %s --coutput %s --use_cfi %s --config %s"%("rop/roplog", coutput, use_cfi, config)).split(" "))
print(">>>>Start solving")
start = time.time()
print(time.ctime())
subprocess.call(("sea bpf --bound=10 %s -m64 --cex=%s.ll --show-invars --inline"%(coutput, coutput)).split(" "))
end = time.time()
print(">>>>Finish solving")
print(time.ctime())
subprocess.call(("sea exe -m64 %s %s.ll -o %s.exe"%(coutput, coutput, coutput)).split(" "))
subprocess.call("%s.exe"%coutput)
print(end - start)
