
#ifndef NewSoftSerial_H
#define NewSoftSerial_H

#include "gsmSerialOut.h"
#include "inttypes.h"

//extern "C"{


//}


class NewSoftSerial:public Print{
	public :
//		NewSoftSerial();
//		~NewSoftSerial();
		boolean read(char &recaivedByte);
//		uint8_t available();
		
};

#endif
