
#include "QuectelM10.h"
#include "TransferInterface.h"

//#include "stdio.h"

static QuectelM10 p;

int GSM_connectTCP(const char* server, int port){
//	QuectelM10 p;
//	printf("ifQuectelM10 p; != getStatus()){!\r\n");
	return p.ConnectServer(server,  port);
}



int GSM_disconnectTCP(){
//	QuectelM10 p;
 	return p.disconnectTCP();
}


int GSM_write(const uint8_t* buffer, size_t sz){
//	QuectelM10 p;
	return p.write(buffer, sz);
}


int GSM_read(char* result, int resultlength){
//	QuectelM10 p;
	return p.read( result,  resultlength);
}


boolean GSM_dataAvailable(void){
	return 1;
}


boolean GSM_startupPrepare(void){
	return(p.startup());
}


boolean GSM_sendFinish(void){
	return(p.isSendFinished());
}


boolean GSM_closeGPRS(){
		return p.deactivateGPRSContext();
}
