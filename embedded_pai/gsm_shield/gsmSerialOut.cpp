#include "gsmSerialOut.h"
#include "xuart.h"

//#define USART_GSM             0x40004800  // same defines as USART3_BASE in xhw_memmap.h

void Print::print(const char *string){	
	fprintf(STDOUT_GSM, string);
}


void Print::print(char *string){
	fprintf(STDOUT_GSM, string);
}


void Print::print(long val, int base){

	switch(base){
		case BYTE:
		{
						
			xUARTCharPut(USART_GSM, (unsigned char)val);// we can not use fprintf() to send, because val may be 0x00;
			break;}
		case DEC:
		{
			char array[]={(val/1000+'0'), (val%1000/100+'0'), (val%100/10+'0'), val%10+'0', '\0'};
			int i;
			for(i=0; i<3; i++){
					if(array[i] > '0')
						//fprintf(STDOUT_GSM, array+i);
						break;					
			}
			fprintf(STDOUT_GSM, array+i);
			break;}
		default:
			break;
	}


}

void Print::println(){
			//char *endLine="\r";
			//fprintf(STDOUT_GSM, endLine);
			
			}
