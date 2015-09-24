#ifndef QUECTELM10_H
#define QUECTELM10_H
#include "NewSoftSerial.h"
#include "ATCommands.h"





class QuectelM10:public ATCommands{

  private:
  	//int setPIN(char *pin);//
	//    int configandwait(char* pin);// 	
	 //   int changeNSIPmode(char);//

  public:
	    //QuectelM10();//
	    //~QuectelM10();//    
	   // int startup(char* pin=0);//
    int startup();//
    void shutdown();//        
    int write(const uint8_t* buffer, size_t sz);//
    int read(char* result, int resultlength);//
    boolean ConnectServer(const char* server, int port);
 //   int connectTCP(const char* server, int port);//
 //   int disconnectTCP();//
  //  int dettachGPRS();//
  //  int attachGPRS(char* domain, char* dom1, char* dom2);//
    //int restart(char* pin=0);//
    //int getCCI(char* cci);//
    //int getIMEI(char* imei);//
    //int sendSMS(const char* to, const char* msg);//    
    //boolean readSMS(char* msg, int msglength, char* number, int nlength);//
    //boolean readCall(char* number, int nlength);//
    //boolean call(char* number, unsigned int milliseconds);//
    //int connectTCPServer(int port);//
    //boolean connectedClient();//	
    //int write(uint8_t c);//
 //   int write(const char* str);//    
    //uint8_t read();//
   // int readCellData(int &mcc, int &mnc, long &lac, long &cellid);//
  
};

//extern QuectelM10 gsm;

/*
extern "C" int Ccall_connectTCP(QuectelM10 *p, const char* server, int port);
extern "C" int Ccall_disconnectTCP(QuectelM10 *p);
extern "C" int Ccall_write(QuectelM10 *p, const uint8_t* buffer, size_t sz);
extern "C" int Ccall_read(char* result, int resultlength);

*/


#endif

