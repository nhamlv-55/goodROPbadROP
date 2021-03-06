# goodROPbadROP
repo for ECE750 final project

## Dependencies
Triton and everything it needs: https://github.com/JonathanSalwan/Triton

## TODO list:
We can bend the story however we want, but I think we should have at least the following:
- A C program ```target.c```
- 2 binaries compiled from ```target.c```: ```target_with_cfi```, and ```target_without_cfi```
(for our purposes, we may disable any ASLR and NEX for both)
- 1 ROP chain (could be an actual payload) ```badROP``` such that:
    - that can exploit ```target_without_cfi```.
    - cannot exploit ```target_with_cfi```.
- 1 ROP chain ```goodROP``` that can exploit both binaries.
- Something to generate those 2 ROP chains (the end goal).

## HOW TO RUN CROP.C

```
sea pf crop.c -m64 --cex=h.ll --show-invars --inline
sea exe -m64 crop.c h.ll -o OUTPUT
./OUTPUT
```
## HOW TO RUN THE WHOLE PIPELINE
```
python rop_log_to_c.py rop/roplog > tail.c
cat head.c tail.c > merge.c

sea pf merge.c -m64 --cex=h.ll --show-invars --inline
sea exe -m64 merge.c h.ll -o OUTPUT
./OUTPUT
```

