#include "QuectelM10.h"  
//#include "Streaming.h"

#include "hal.h"
#include "TimeDelay.h"



int QuectelM10::startup()
{
	  //GsmBoardEnable();
	//  setStatus(IDLE);
	   // Try 10 times to register in the network. Note this can take some time!
	  for(int i=0; i<100; i++){
					//DelayNms(20);
					if(sendGenericCommand("AT+CGREG?", "CGREG: 0,1")){ //chech gprs status
					//	setStatus(READY);

						logout.regularLog("QuectelM10:  startup now!\r\n");

						if(!transparentTransmitConfig()) {
							logout.errorLog("QuectelM10:  GPRS configured failed!\r\n");
							return false; //network config	
						}					
				//		setStatus(ATTACHED);

						logout.regularLog("QuectelM10:  GPRS configured successfully!\r\n");

						return true;
		            }

	  }		  
	  return false;
}

void QuectelM10::shutdown(){

	GsmBoardDisable();
	setStatus(IDLE);
	logout.warningLog("QuectelM10:  shutdown already!\r\n");

}    



boolean QuectelM10::ConnectServer(const char* server, int port){

/*	if(ATTACHED != getStatus()){
		logout.errorLog("QuectelM10:  status error when connect to server!\r\n");
		return false;
	}

*/

	if(!connectTCP(server, port)){
	//	logout.errorLog("QuectelM10:  connect to server failed!\r\n");
		return false;//connect to tcp server;
	}

//	setStatus(TCPCONNECTED); 

//	logout.regularLog("QuectelM10:  connect to server successfully!\r\n");
	
  	return true;
}

/*
int QuectelM10::connectTCP(const char* server, int port)
{
  //Status = ATTACHED.
  if (getStatus()!=ATTACHED) return false;

  _tf.setTimeout(GSM_COMMAND_TIMEOUT);
  //Visit the remote TCP server.
  _cell << "AT+QIOPEN=\"TCP\",\"" << server << "\"," << _DEC(port) <<  _BYTE(cr) << endl;

  if(!checkResponse("CONNECT")) return false;

  setStatus(TCPCONNECTED); 
  return true;
  
}

int QuectelM10::disconnectTCP()
{
  //Status = TCPCONNECTEDCLIENT or TCPCONNECTEDSERVER.
  if (getStatus()!=TCPCONNECTED) return false;

  //Switch to AT mode.
  sendCommandString("+++");  
  DelayNms(200);
  
  //Close TCP client and deact.
  sendCommandString("AT+QICLOSE");  
  setStatus(ATTACHED);

  return true;

}


*/

int QuectelM10::write(const uint8_t* buffer, size_t sz)
{
//   if((getStatus() != TCPCONNECTEDSERVER)&&(getStatus() != TCPCONNECTEDCLIENT))

/*    	if(getStatus() != TCPCONNECTED) {
			logout.debugLog("QuectelM10:  write operation forbiddoned, TCP status wrong!\r\n");
			return false;
    		}

*/
		
    
   	if(sz>1024)  return 0;
  
	sendData(buffer, sz);
    
  	return sz;  
}


int QuectelM10::read(char* result, int resultlength)//nonblocking
{
/*     	if(getStatus() != TCPCONNECTED) {
			logout.debugLog("QuectelM10:  write operation forbiddoned, TCP status wrong!\r\n");
			return false;
    	}
*/

  	return readData((uint8_t *)result, resultlength);
}



/*  
int QuectelM10::sendSMS(const char* to, const char* msg)
{

  //Status = READY or ATTACHED.
  if((getStatus() != READY)&&(getStatus() != ATTACHED))
    return 0;
      
  _tf.setTimeout(_GSM_DATA_TOUT_);	//Timeout for expecting modem responses.

  _cell.flush();

  //AT command to send a SMS. Destination telephone number 
  _cell << "AT+CMGS=\"" << to << "\"" <<_BYTE(cr) << endl; // Establecemos el destinatario

  //Expect for ">" character.
  if(!_tf.find(">")) return 0;

  //SMS text.
  _cell << msg << _BYTE(ctrlz) << _BYTE(cr) << endl; 

  //Expect "OK".
  if(!_tf.find("OK"))
    return 0;
  else  
    return 1;
}

*/


/*

int QuectelM10::dettachGPRS()
{
  if (getStatus()==IDLE) return 0;

  //GPRS dettachment.
  if(!sendGenericCommand("AT+CGATT=0", "OK")) return false; 
	
  setStatus(READY);
  return true;
  
}
*/



/*
int QuectelM10::connectTCPServer(int port)
{
  if (getStatus()!=ATTACHED)
     return 0;

  _tf.setTimeout(_GSM_CONNECTION_TOUT_);

  _cell.flush();

  // Set port
  _cell << "AT+QILPORT=\"TCP\"," << _DEC(port) << endl;
  if(!_tf.find("OK")) // Should we leave Status in ERROR?
    return 0;
    
  DelayNms(200);  
  
  //Read Local Port, if not read, server get error.
  _cell << "AT+QILOCIP" << endl;
    
  DelayNms(500);  
  
  // Open server
  _cell << "AT+QISERVER" << endl;
  if(_tf.find("OK"))
  {
    setStatus(TCPSERVERWAIT);
    return 1;
  }
  else
    return 0;
}

boolean QuectelM10::connectedClient()
{
  if (getStatus()!=TCPSERVERWAIT)
     return 0;
 
  // Alternative: AT+QISTAT, although it may be necessary to call an AT 
  // command every second,which is not wise
  _tf.setTimeout(1);
  if(_tf.find("CONNECT")) 
  {
    setStatus(TCPCONNECTEDSERVER);
    return true;
  }
  else
    return false;
 }
*/


/*
 int QuectelM10::readCellData(int &mcc, int &mnc, long &lac, long &cellid)
{
  if (getStatus()==IDLE)
    return 0;
    
   _tf.setTimeout(_GSM_DATA_TOUT_);
   _cell.flush();
  _cell << "AT+QENG=1,0" << endl; 
  _cell << "AT+QENG?" << endl; 
  if(!_tf.find("+QENG:"))
    return 0;

  mcc=_tf.getValue(); // The first one is 0
  mcc=_tf.getValue();
  mnc=_tf.getValue();
  lac=_tf.getValue();
  cellid=_tf.getValue();
  _tf.find("OK");
  _cell << "AT+QENG=1,0" << endl; 
  _tf.find("OK");
  return 1;
}


boolean QuectelM10::readSMS(char* msg, int msglength, char* number, int nlength)
{
  long index;

  if (getStatus()==IDLE)
    return false;
  
  _tf.setTimeout(_GSM_DATA_TOUT_);
  _cell.flush();
  _cell << "AT+CMGL=\"REC UNREAD\",1" << endl;
  if(_tf.find("+CMGL: "))
  {
    index=_tf.getValue();
    _tf.getString("\"+", "\"", number, nlength);
    _tf.getString("\n", "\nOK", msg, msglength);
    _cell << "AT+CMGD=" <<_DEC(index) << endl;
    _tf.find("OK");
    return true;
  };
  return false;
};


boolean QuectelM10::readCall(char* number, int nlength)
{
  int index;

  if (getStatus()==IDLE)
    return false;
  
  _tf.setTimeout(_GSM_DATA_TOUT_);

  if(_tf.find("+CLIP: \""))
  {
    _tf.getString("", "\"", number, nlength);
    _cell << "ATH" << endl;
    DelayNms(1000);
    _cell.flush();
    return true;
  };
  return false;
};

boolean QuectelM10::call(char* number, unsigned int milliseconds)
{ 
  if (getStatus()==IDLE)
    return false;
  
  _tf.setTimeout(_GSM_DATA_TOUT_);

  _cell << "ATD" << number << ";" << endl;
  DelayNms(milliseconds);
  _cell << "ATH" << endl;

  return true;
 
}

int QuectelM10::setPIN(char *pin)
{
  //Status = READY or ATTACHED.
  if((getStatus() != IDLE)) return 2;


      
  _tf.setTimeout(_GSM_DATA_TOUT_);	//Timeout for expecting modem responses.

  _cell.flush();

  //AT command to set PIN.
  _cell << "AT+CPIN=" << pin <<  _BYTE(cr) << endl; // Establecemos el pin

  //Expect "OK".
  if(!_tf.find("OK"))
    return 0;
  else  
    return 1;
}

/*
int QuectelM10::write(uint8_t c)
{
  if (getStatus() == TCPCONNECTED)
    return write(&c, 1);
  else
    return 0;
}



int QuectelM10::write(const char* str)
{
  if (getStatus() == TCPCONNECTED)
      return write((const uint8_t*)str, strlen(str));
  else
      return 0;
}


/*
int QuectelM10::changeNSIPmode(char mode) ///SYVV
{
    _tf.setTimeout(_TCP_CONNECTION_TOUT_);
    
    //if (getStatus()!=ATTACHED)
    //    return 0;

    _cell.flush();

    _cell << "AT+QIDNSIP=" << _BYTE(mode) <<_BYTE(cr) << endl;

    if(!_tf.find("OK")) return 0;
    
    return 1;
}

int QuectelM10::getCCI(char *cci)
{
  //Status must be READY
  if((getStatus() != READY))
    return 2;
      
  _tf.setTimeout(_GSM_DATA_TOUT_);	//Timeout for expecting modem responses.

  _cell.flush();

  //AT command to get CCID.
  _cell << "AT+QCCID" << _BYTE(cr) << endl; // Establecemos el pin
  
  //Read response from modem
  _tf.getString("AT+QCCID\r\r\r\n","\r\n",cci, 21);
  
  //Expect "OK".
  if(!_tf.find("OK"))
    return 0;
  else  
    return 1;
}

  
int QuectelM10::getIMEI(char *imei)
{
      
  _tf.setTimeout(_GSM_DATA_TOUT_);	//Timeout for expecting modem responses.

  _cell.flush();

  //AT command to get IMEI.
  _cell << "AT+GSN" << _BYTE(cr) << endl; 
  
  //Read response from modem
  _tf.getString("AT+GSN\r\r\r\n","\r\n",imei, 15);
  
  //Expect "OK".
  if(!_tf.find("OK"))
    return 0;
  else  
    return 1;
}

uint8_t QuectelM10::read()
{
  return _cell.read();
}








/*

int Ccall_connectTCP(QuectelM10 *p, const char* server, int port){
	
	return p->connectTCP(  server,  port);
}



int Ccall_disconnectTCP(QuectelM10 *p){
 	return p->disconnectTCP();
}


int Ccall_write(QuectelM10 *p, const uint8_t* buffer, size_t sz){
	return p->write(buffer, sz);
}


int Ccall_read(QuectelM10 *p, char* result, int resultlength){
	return p->read( result,  resultlength);
}


*/



