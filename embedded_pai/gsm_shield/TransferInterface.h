


#ifndef TransferInterface_H
#define TransferInterface_H



#include "inttypes.h" 

//*****************************************************************************
//
// If building with a C++ compiler, make all of the definitions in this header
// have a C binding.
//
//*****************************************************************************
#ifdef __cplusplus
extern "C"
{
#endif

/*
#include "QuectelM10.h"
extern int Ccall_connectTCP(QuectelM10 *p, const char* server, int port);
extern int Ccall_disconnectTCP(QuectelM10 *p);
extern int Ccall_write(QuectelM10 *p, const uint8_t* buffer, size_t sz);
extern int Ccall_read(char* result, int resultlength);
*/

extern int GSM_connectTCP(const char* server, int port);
extern int GSM_disconnectTCP();
extern boolean GSM_closeGPRS();
extern int GSM_write(const uint8_t* buffer, size_t sz);
extern int GSM_read(char* result, int resultlength);
extern boolean GSM_dataAvailable(void);
extern boolean GSM_startupPrepare(void);
extern boolean GSM_sendFinish(void);

//*****************************************************************************
//
// Mark the end of the C bindings section for C++ compilers.
//
//*****************************************************************************
#ifdef __cplusplus
}
#endif

#endif
