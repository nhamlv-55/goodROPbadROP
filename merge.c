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
// add dword ptr [eax], eax ; ret
void gadget_0(){
	return;
}

// add dword ptr [ebx], 2 ; inc ecx ; ret
void gadget_1(){
	ecx++;
	return;
}

// add dword ptr [ecx], eax ; ret

// add dword ptr [edx], 2 ; ret

// add dword ptr [edx], ecx ; ret

// add eax, 0 ; ret

// add eax, 1 ; ret

// add eax, 2 ; ret

// add eax, 3 ; ret

// add eax, dword ptr [ebx] ; add dword ptr [edx], ecx ; ret

// add eax, dword ptr [ecx] ; add dword ptr [edx], ecx ; ret

// add eax, dword ptr [ecx] ; ret

// add eax, dword ptr [edx] ; inc ecx ; ret

// add eax, ebx ; pop ebx ; ret
void gadget_2(){
	ebx = pop();
	return;
}

// add eax, ecx ; ret

// add eax, edx ; add eax, ecx ; ret

// add eax, edx ; ret

// add ebx, eax ; add dword ptr [edx], ecx ; ret

// add ebx, ecx ; add dword ptr [edx], ecx ; ret

// add ecx, dword ptr [edx] ; ret

// add ecx, ecx ; ret

// add edx, dword ptr [eax] ; add dword ptr [edx], ecx ; ret

// inc dword ptr [ecx] ; ret

// inc eax ; pop eax ; ret
void gadget_3(){
	eax++;
	eax = pop();
	return;
}

// inc eax ; ret
void gadget_4(){
	eax++;
	return;
}

// inc ebx ; ret
void gadget_5(){
	ebx++;
	return;
}

// inc ecx ; ret

// inc edx ; ret
void gadget_6(){
	edx++;
	return;
}

// mov dword ptr [eax], 2 ; xor eax, eax ; ret
void gadget_7(){
	move_mem_const(eax, 2);
	eax = 0;
	return;
}

// mov dword ptr [edx], eax ; mov eax, edx ; ret
void gadget_8(){
	move_mem_const(edx, eax);
	return;
}

// mov dword ptr [edx], eax ; pop ebx ; ret
void gadget_9(){
	move_mem_const(edx, eax);
	ebx = pop();
	return;
}

// mov dword ptr [edx], eax ; ret

// mov eax, 1 ; pop ebx ; ret

// mov eax, 1 ; ret

// mov eax, 2 ; pop ebx ; ret

// mov eax, 2 ; ret

// mov eax, 3 ; ret

// mov eax, 4 ; pop ebx ; ret

// mov eax, 4 ; ret

// mov eax, 5 ; ret

// mov eax, 6 ; ret

// mov eax, 7 ; ret

// mov eax, dword ptr [eax] ; sub eax, dword ptr [edx] ; ret

// mov eax, dword ptr [ecx] ; mov dword ptr [edx], eax ; ret

// mov eax, ebx ; pop ebx ; ret

// mov eax, ecx ; ret

// mov eax, edx ; pop ebx ; ret

// mov eax, edx ; ret

// mov word ptr [edx], ax ; mov eax, edx ; ret

// mov word ptr [edx], cs ; ret

// pop eax ; ret
void gadget_10(){
	eax = pop();
	return;
}

// pop ebx ; add dword ptr [ecx], eax ; ret

// pop ebx ; add dword ptr [edx], ecx ; ret

// pop ebx ; add eax, edx ; ret

// pop ebx ; pop edx ; ret
void gadget_11(){
	ebx = pop();
	edx = pop();
	return;
}

// pop ebx ; ret

// pop ebx ; xor eax, eax ; ret
void gadget_12(){
	ebx = pop();
	eax = 0;
	return;
}

// pop ecx ; pop ebx ; ret
void gadget_13(){
	ecx = pop();
	ebx = pop();
	return;
}

// pop edx ; ret
void gadget_14(){
	edx = pop();
	return;
}

// ret

// sub eax, 1 ; pop ebx ; ret

// sub eax, dword ptr [edx] ; ret

// sub eax, ecx ; ret

// sub eax, edx ; ret

// xor eax, eax ; pop ebx ; ret
void gadget_15(){
	eax = 0;
	ebx = pop();
	return;
}

// xor eax, eax ; ret
void gadget_16(){
	eax = 0;
	return;
}

int main(){
	int choice = 0;

	//bounded
	for(int i =0; i< 10; i++){
		print_state();
		choice = nd();
		assume(choice>=0 && choice<17);

		if(choice==0){
			gadget_0();
		}
		if(choice==1){
			gadget_1();
		}
		if(choice==2){
			gadget_2();
		}
		if(choice==3){
			gadget_3();
		}
		if(choice==4){
			gadget_4();
		}
		if(choice==5){
			gadget_5();
		}
		if(choice==6){
			gadget_6();
		}
		if(choice==7){
			gadget_7();
		}
		if(choice==8){
			gadget_8();
		}
		if(choice==9){
			gadget_9();
		}
		if(choice==10){
			gadget_10();
		}
		if(choice==11){
			gadget_11();
		}
		if(choice==12){
			gadget_12();
		}
		if(choice==13){
			gadget_13();
		}
		if(choice==14){
			gadget_14();
		}
		if(choice==15){
			gadget_15();
		}
		if(choice==16){
			gadget_16();
		}

		print_state();
		sassert(s2!=4);
	}
 	return 0;
}
