
 #ifndef INTTYPES_H
 #define  INTTYPES_H


typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
typedef unsigned char boolean;
typedef unsigned int size_t;

#define NULL 0
#define true 1
#define false 0

//#define  STDOUT_GSM (FILE *)5

typedef enum{
	wrongAnswer,
	noAnswer
}errorCode_t;

#endif
