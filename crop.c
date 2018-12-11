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

void move_val_to(int val, int address){
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



int main(){
	int choice = 0;

	//bounded
	for(int i =0; i< 10; i++){
		print_state();
		choice = nd();
		printf("%d\n", choice);
		assume(choice>0 && choice<=7);
		if(choice ==1){
			printf("pop eax\n");
			eax = pop();
		}
				
		if (choice ==2){
			printf("pop ecx\n");
			ecx = pop();
		}
		if (choice == 3){
				// mov %eax, (%ecx)

				assume(ecx>=0 && ecx<5);
				move_val_to(eax, ecx);
				printf("mov eax, (ecx): %d %d\n", eax, ecx);
		}		
		if(choice == 4){
				eax++;
				printf("inc eax\n");
		}		
		if(choice == 5){
				ebx++;
				printf("inc ebx\n");
		}		
		if(choice == 6){
				ecx++;
				printf("inc ecx\n");
		}		
		if(choice == 7){
				edx++;
				printf("inc edx\n");
		}
		print_state();
	}
	print_state();

	sassert(s3!=3);	
	return 0;
}
