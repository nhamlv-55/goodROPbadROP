import subprocess
import argparse
import json
import sys
import time

roplog = sys.argv[1]
coutput = roplog.split("/")[-1]+".c"

subprocess.call(("touch %s"%(coutput)).split(" "))
subprocess.call(("python rop_log_to_c.py --roplog %s --coutput %s --config config.json"%(roplog, coutput)).split(" "))
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
