#include "seahorn/seahorn.h"
extern int nd(void);

void print_state(){
	printf("%seax: %d, ebx: %d, ecx: %d, edx: %d, ", "\x1B[32m", eax, ebx, ecx, edx);
	printf("[");
	printf("%d ", s0);
	printf("%d ", s1);
	printf("%d ", s2);
	printf("%d ", s3);
	printf("%d ", s4);
	printf("] ");

	printf("{");
	printf("%d ", m0);
	printf("%d ", m1);
	printf("%d ", m2);
	printf("}\n %s", "\x1B[0m");
}

int pop(){
	int reg = s4;
	s4 = s3;
	s3 = s2;
	s2 = s1;
	s1 = s0;
	s0 = -1;
	return reg;
}

void move_mem_const(int address, int val){
	switch(address){
		case 0:
			m0 = val;
			break;
		case 1:
			m1 = val;
			break;
		case 2:
			m2 = val;
			break;
		default:
			return;
	}
}

int move_reg_mem(int address){
	switch(address){
		case 0:
			return s0;
			break;
		case 1:
			return s1;
			break;
		case 2:
			return s2;
			break;
		case 3:
			return s3;
			break;
		case 4:
			return s4;
			break;
	}
}

void add_to_pointer(int address, int val){
	switch(address){
		case 0:
			m0+= val;
			break;
		case 1:
			m1+= val;
			break;
		case 2:
			m2+= val;
			break;
		default:
			return;
	}
}

int add_from_pointer(int reg, int address){
	switch(address){
		case 0:
			return reg+m0;
			break;
		case 1:
			return reg+m1;
			break;
		case 2:
			return reg+m2;
			break;
		default:
			assert(0);
	}
}

void not_implemented(){
    return;
}
