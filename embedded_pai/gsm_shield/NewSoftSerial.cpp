#include "NewSoftSerial.h"
#include "xuart.h"


//#define USART_GSM             0x40004800  // same defines as USART3_BASE in xhw_memmap.h
//#define USART3_BASE             0x40004800  // USART3

//#define USART1_BASE             0x40013800  // USART1

boolean NewSoftSerial::read(char &recaivedByte){

	int result =UARTCharGetNonBlocking(USART_GSM);
	if(result == -1)
		return  0;
	else{
		//UARTCharPut(USART1_BASE, r);
		//recaivedByte =r;
		recaivedByte=(char)result;
		return 1;
	}
}

//NewSoftSerial::NewSoftSerial(){}

//NewSoftSerial::~NewSoftSerial(){}
