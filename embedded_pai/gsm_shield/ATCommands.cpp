#include "ATCommands.h"
#include <string.h>

/*void memcpy_diy(char* des, const char*src){
	char* des_t= des;
	char* src_t= src;
	if(des==0 || src==0)
		return;
	while(*(des_t++));
	while(*(des++) = *(src_t++) );
}*/


ATCommands::ATCommands():logout(3){_transparentTranmit=false;}

boolean ATCommands::transparentTransmitConfig(){


	   if(!sendGenericCommand("AT+QISTAT", "IP INITIAL")){
		   logout.warningLog("QuectelM10:  it has been configured already, please notice!\r\n");
		   return true; // ip status wrong!!!!!!!!!
	   }


	   IpIntialConfig();//

	   //Register the TCP/IP stack.// after this command, the IP status will be IP START
	   sendCommandString("AT+QIREGAPP");//
	   // if(!sendGenericCommand("AT+QIREGAPP", "OK")) return false;
	   // DelayNms(20);

	   //Activate FGCNT.// after this command, the IP status will be IP GPRSACT
	   //if(!sendGenericCommand("AT+QIACT", "OK")) return false; //if the ip status is not IP START, it will respond error.
	   sendCommandString("AT+QIACT");//

	   // query the local IP address.
	   //AT+QILOCIP


	   /******it may take several seconds to wait ,so delate it ********/
	   //if(!sendGenericCommand("AT+QISTAT", "IP GPRSACT"))
		//	  return false; // ip status wrong!!!!!!!!!

	   //attach gprs service
	   //if(!sendGenericCommand("AT+CGATT=1", "OK")) return false; 
	   //sendCommandString("AT+CGATT=1");
	  
	  //Use domain name as the address to stablish a TCP session.
	  // if(!sendGenericCommand("AT+QIDNSIP=0", "OK")) return false; //TCP server  is dotted decimal ip addr,like:xxxx.xxxx.xxxx.xxxx
		// sendCommandString("AT+QIDNSIP=0");
	  //  _cell << "AT+QIDNSIP=1" <<  _BYTE(cr) << endl;// TCP server is domain name: like:www.baidu.com
	 //_cell << "AT+QIDNSIP=0" <<  _BYTE(cr) << endl;//TCP server  is dotted decimal ip addr,like:xxxx.xxxx.xxxx.xxxx
	    
	  return true;// config success.
	
}

/*
 * It is strongly recommended to implement the former commands after SIM PIN is unlocked.
 *  And all these commands should be implemented in the state IP INITIAL which can be queried by the command ¡°AT+QISTAT¡±.
 */
void ATCommands::IpIntialConfig(){
	   //Set the context 0 as FGCNT.
	   //The command ¡°AT+QIFGCNT¡± is used to select FGCNT. It is recommended to implement this command before other TCP/UDP operations
	   sendCommandString("AT+QIFGCNT=0");

	   //Set bearer type as GPRS and the APN is ¡°CMNET¡±
	   sendCommandString("AT+QICSGP=1,\"CMNET\"");

	   //Disable the function of MUXIP.//Control Whether or Not to Enable Multiple TCPIP Session;
	   //if(!sendGenericCommand("AT+QIMUX=0", "OK")) return false;
	   sendCommandString("AT+QIMUX=0");// if it's already set to 0, response error

	   if(_transparentTranmit){
		   //Set the session mode as transparent.
		   // if(!sendGenericCommand("AT+QIMODE=1", "OK")) return false;
		   sendCommandString("AT+QIMODE=1");// if it's already set to 1, response error

		   /*
		    * 3 means to set the retry times to resend as 3, this is a internal process, which doesn¡¯t have an obvious affection.
		    * 2 means to set wait interval as 100ms, which means system will wait for 200 ms before send the data in the buffer when the data in the buffer is less than 512.
		    * 512 means that once the length of the data in the buffer reaches 512, the data will be sent out.
		    * 1 means to enable escape data mode with ¡°+++¡±.
		    */
		   sendCommandString("AT+QITCFG=3,2,512,1");
	   }


	   //Use domain name as the address to stablish a TCP session.
	   // if(!sendGenericCommand("AT+QIDNSIP=0", "OK")) return false; //TCP server  is dotted decimal ip addr,like:xxxx.xxxx.xxxx.xxxx
	   sendCommandString("AT+QIDNSIP=0");
		  //  _cell << "AT+QIDNSIP=1" <<  _BYTE(cr) << endl;// TCP server is domain name: like:www.baidu.com
		 //_cell << "AT+QIDNSIP=0" <<  _BYTE(cr) << endl;//TCP server  is dotted decimal ip addr,like:xxxx.xxxx.xxxx.xxxx


	   /*recaive data formate config*/
	//   sendCommandString("AT+QISHOWLA=0");// do not add the local address
	//   sendCommandString("AT+QIHEAD=0");// do not add the header information.
	//   sendCommandString("AT+QISHOWPT=0");// do not add the transmission layer protocol type.

	//   sendCommandString("AT+QISHOWRA=1");// // add the address and port of the remote server before the received data.






}




boolean ATCommands::connectTCP(const char* server, int port){
	//"AT+QIOPEN="TCP","9.186.57.23","8001"
	 //Visit the remote TCP server.

	if(sendGenericCommand("AT+QISTAT", "CONNECT OK"))
				return true;

	//AT+QIOPEN="TCP","202.108.130.41","6082"
	//
  	_cell << "AT+QIOPEN=\"TCP\",\""<< server <<"\",\""<< _DEC(port)<< "\"" <<_BYTE(cr) << endl;
	//_cell << "AT+QIOPEN=\"TCP\",\""<< server <<"\",\""<< array+i<< "\"" <<_BYTE(cr) << endl;
	//sendCommandString("AT+QIOPEN=\"TCP\",\"202.108.130.41\",\"6082\"");

	for(int i = 0; i <100; i++){	// tcp connect time will be 75s deponds on the network status
			if(checkResponse("CONNECT"))
				return true;
	}
	
	 return false;
}


boolean ATCommands::disconnectTCP(){
	//back off to command context from data transmit context
	if(_transparentTranmit)
			sendCommandString("+++");
	//Close TCP client and deact.
  	sendCommandString("AT+QICLOSE");
  	logout.debugLog("QuectelM10:  tcp connection closed !\r\n");
}


void ATCommands::sendData(const uint8_t *buf, size_t len){

	if(!_transparentTranmit){

		if(!sendGenericCommand("AT+QISTAT", "CONNECT OK")){
			logout.errorLog("QuectelM10:  tcp not connected when send data!\r\n");
			return;
		}


		char maxLen=strlen("AT+QISEND=1024");
		char* mallocBuf= (char *)malloc(maxLen);
		memset(mallocBuf,'\0',maxLen);
		/***************************************************
		we can not use command AT+QISEND that doesn't give certain length info, because data sent may contain CTRL+Z, AT+QISEND=25 command 
		will take every character as data until set length reached.	
		*******************************************************/
		memcpy(mallocBuf, "AT+QISEND=", strlen("AT+QISEND="));
		strcat(mallocBuf, toString(len));

	//	logout.debugLog(mallocBuf);

		if(!sendGenericCommand(mallocBuf, ">")){
			free(mallocBuf);
			//logout.errorLog("QuectelM10:  AT+QISEND response error!\r\n");
			return ;
		}


		free(mallocBuf);

//		logout.debugLog("QuectelM10:  AT+QISEND response ok\r\n");


/*		if(!shorttimeWaitCommand("AT+QISEND", ">")){
			logout.errorLog("QuectelM10:  AT+QISEND response error!\r\n");
						return ;
		}*/

	}



	for(int i=0; i<len; i++){
		//unsigned char sendByte=*(buf+i);
		//_cell<<_BYTE(*(buf+i));
		//
		_cell<<_BYTE(*(buf+i));
		//_cell<<toString(*(buf+i));

		//logout.errorLog(toString(*(buf+i)));

	}

		//_cell<<_BYTE(0x10);




//	_cell<<"aaaaaaaaaaaaaaaaaaaaaaaaaaaa";
	
	if(!_transparentTranmit){

		_cell <<_BYTE(ctrlz)<<_BYTE(cr) << endl;

		while(!checkResponse("SEND OK\r\n"));

//		while(sendGenericCommand("AT+QISTAT", "CONNECT OK")){
//			logout.errorLog("QuectelM10:  CONNECT OK!\r\n");
//		}

		//for(len=1; len<50; len++)
//		isSendFinished(len);

/*		char sendByte;
		char bbbb[40]={0};
		int i=0;

		for(int a=150; a>0; a--)
			if(_tf.read(sendByte))
						if(i<39){
								bbbb[i]=sendByte+1;
								i++;
						}else
							break;
//			if((sendByte == '\n') || (sendByte == '\r')){
//					sendByte=0;
//					logout.errorLog(bbbb);
//			}



		logout.errorLog(bbbb);

 *///OUTPUT THE RECAIVE DATA


//		if(!sendGenericCommand("AT+QISTAT", "CONNECT OK"));




	}


}

/*
+QIRD:9.186.57.23:7070,TCP,36<CR><LF>
1234567890qwertyuiopasdfghjklzxcvbnm

*/
size_t ATCommands::readData(uint8_t *buf, size_t len){

//	while(!checkResponse("RECV FROM"));

/*	if(!_tf.find("\r\n")){
		logout.debugLog("QuectelM10:  read AT+QIRD failed!\r\n");
		return 0;
	}
*///DATA RECAIVED HAS NO HEAD

	char recaivedByte;
	size_t recaived_len=0;
	for(int i =0; i<GSM_TCP_TIMEOUT; i++){
		if(recaived_len<len){
				if(_tf.read(recaivedByte)){
				*(buf+recaived_len)=(uint8_t)recaivedByte;
				recaived_len++;
				}
		}else{
			//for(int c=0; c<len; c++)
			//	logout.debugLog(toString(*(buf+c)));

			return 	len;
		}

	}

	//logout.debugLog("QuectelM10:  read data timeout!\r\n");
	return 0;
}









boolean ATCommands::isSendFinished(size_t len){

/*	char array[]={(len/1000+'0'), (len%1000/100+'0'), (len%100/10+'0'), len%10+'0', '\0'};
	int nonZeroStart;
	for(nonZeroStart=0; nonZeroStart<3; nonZeroStart++){
			if(array[nonZeroStart] > '0')
				//fprintf(STDOUT_GSM, array+i);
				break;
	}
*/
	if(!len)
		return true;

	//response formate:172, 172, 0
	char maxLen=strlen("1024, 1024, 0");
	char *buf=(char *) malloc(maxLen);
	memset(buf, '\0', maxLen);
	memcpy(buf, toString(len),strlen(toString(len)));
	strcat(buf, ", ");
	strcat(buf, toString(len));
//	strcat(buf, ", 0");

	//logout.debugLog(buf);
	char dataSendBasicTimes = 10;

	for(int i =0; i < dataSendBasicTimes + (len); i++)
		if(sendGenericCommand("AT+QISACK", buf)){
			free(buf);
			logout.debugLog("QuectelM10:  send finished\r\n");
			return true;
	}

	logout.errorLog("QuectelM10:  data send error!\r\n");
	free(buf);
	return false;

}


boolean ATCommands::isSendFinished(){


	uint16_t MaxSendTimes = 1024;


	for(int i =0; i < MaxSendTimes; i++)
		if(sendGenericCommand("AT+QISACK", ","))
				if(checkResponse(", 0") && sendGenericCommand("AT+QISTAT", "CONNECT OK"))
						return true;

	logout.debugLog("QuectelM10:  data send error!\r\n");
	return false;

}




char* ATCommands::toString(size_t len){
	static char array[]={0};

	array[0]=len/1000+'0';
	array[1]=len%1000/100+'0';
	array[2]=len%100/10+'0';
	array[3]=len%10+'0';

	int nonZeroStart;
	for(nonZeroStart=0; nonZeroStart<3; nonZeroStart++){
			if(array[nonZeroStart] > '0')
				//fprintf(STDOUT_GSM, array+i);
				break;
	}

	return array+nonZeroStart;

}


boolean ATCommands::PowerControl(M10PowerState_e powerControl){
	switch(powerControl){
	case POWER_OFF:
		return sendGenericCommand("AT+QPOWD=0","OK");//shutdown immediately!
	case RF_OFF:
		break;
	case NORMAL_RUNNING:
		break;
	case SLEEP:
		break;
	default:
		break;
	}

}




