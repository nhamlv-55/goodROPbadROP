#include "seahorn/seahorn.h"
extern int nd(void);

int s0 = 0;
int s1 = 0;
int s2 = 0;
int s3 = 0;
int s4 = 0;

int eax = 0, ebx = 0, ecx = 0, edx = 0;


void print_state(){
	printf("eax: %d, ebx: %d, ecx: %d, edx: %d, ", eax, ebx, ecx, edx);
	printf("[");
	printf("%d ", s0);
	printf("%d ", s1);
	printf("%d ", s2);
	printf("%d ", s3);
	printf("%d ", s4);
	printf("]\n");
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
			s0 = val;
			break;
		case 1:
			s1 = val;
			break;
		case 2:
			s2 = val;
			break;
		case 3:
			s3 = val;
			break;
		case 4:
			s4 = val;
			break;
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

void not_implemented(){
    return;
}
