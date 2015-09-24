#ifndef gsmSerialOut_h
#define gsmSerialOut_h

#include <stdio.h>


enum{
	HEX,
	DEC,
	OCT,
	BIN,
	BYTE
};


class Print{
	public:
//		Print();
//		~Print();
		void print(const char *string);
		void print(char *string);
		void print(long val, int base);
		void println();
		inline void flush(){};
	protected:
		const unsigned long USART_GSM=0x40004800;

};
#endif
