import subprocess
import argparse
import json

roplog = "rop/roplog"
coutput = "synthezied.c"

subprocess.call(("python rop_log_to_c.py --roplog %s --coutput %s --config config.json"%(roplog, coutput)).split(" "))
subprocess.call(("sea pf %s -m64 --cex=h.ll --show-invars --inline"%(coutput)).split(" "))
subprocess.call(("sea exe -m64 %s h.ll -o OUTPUT"%(coutput)).split(" "))
subprocess.call("./OUTPUT")