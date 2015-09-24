#include "MQTTCommons.h"
#include "TransferInterface.h"
#include "WiFi.h"
#include "GlobalMacro.h"

typedef enum {
NoneTool,
isGSM,
isWIFI
}wirelessMeduim_t;

#ifdef _GSM_ENABLE_
static wirelessMeduim_t CTool  = isGSM;
#endif

#ifdef _WIFI_ENABLE_
static wirelessMeduim_t CTool  = isWIFI;
#endif


void TcpCallBackFunctionsRegister(TcpActivityAPI_t *TcpFuncAddr){
	if(CTool == isWIFI ){
		TcpFuncAddr->connectTCPServer = (connectTCPServer_p )WiFiClient_Connect;
		TcpFuncAddr->dataAvailable = (dataAvailable_p )WiFiClient_Available;
		TcpFuncAddr->disconnectWireless = (disconnectWireless_p )WiFi_Disconnect;
		TcpFuncAddr->recaiveDataIn = (recaiveDataIn_p)WiFiClient_ReadBlock;
		TcpFuncAddr->sendDataOut = (sendDataOut_p )WiFiClient_WriteBlock;
		TcpFuncAddr->isSendDataFinish = 0;
		}
	else if(CTool == isGSM ){
		TcpFuncAddr->connectTCPServer = (connectTCPServer_p )GSM_connectTCP;
		TcpFuncAddr->dataAvailable = (dataAvailable_p )GSM_dataAvailable;
		TcpFuncAddr->disconnectWireless = (disconnectWireless_p )GSM_disconnectTCP;
		TcpFuncAddr->recaiveDataIn = (recaiveDataIn_p)GSM_read;
		TcpFuncAddr->sendDataOut = (sendDataOut_p )GSM_write;
		TcpFuncAddr->isSendDataFinish = (isSendDataFinish_p)GSM_sendFinish;
		}
	
}









