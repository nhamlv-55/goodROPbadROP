import subprocess
import argparse
import json
import sys
import time

use_cfi = sys.argv[1]
coutput = sys.argv[2]+"_"+use_cfi+".c"

subprocess.call(("touch %s"%(coutput)).split(" "))
subprocess.call(("python rop_log_to_c.py --roplog %s --coutput %s --use_cfi %s --config config.json"%("rop/roplog", coutput, use_cfi)).split(" "))
print(">>>>Start solving")
start = time.time()
print(time.ctime())
subprocess.call(("sea bpf --bound=10 %s -m64 --cex=h.ll --show-invars --inline"%(coutput)).split(" "))
end = time.time()
print(">>>>Finish solving")
print(time.ctime())
subprocess.call(("sea exe -m64 %s h.ll -o OUTPUT"%(coutput)).split(" "))
subprocess.call("./OUTPUT")
print(end - start)
