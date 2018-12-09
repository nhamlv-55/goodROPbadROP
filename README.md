# goodROPbadROP
repo for ECE750 final project
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
