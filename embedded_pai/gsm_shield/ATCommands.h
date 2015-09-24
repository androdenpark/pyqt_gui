
#ifndef ATCommands_H
#define ATCommands_H

#include "GSM.h"
#include "Streaming.h"
#include "LOG.h"

typedef enum{POWER_OFF, POWER_ON, SLEEP, RF_OFF, NORMAL_RUNNING}M10PowerState_e;

class ATCommands:public virtual GSM{
	private:
		const char GSM_COMMAND_TIMEOUT=0;
		const unsigned long GSM_TCP_TIMEOUT=300;
		boolean _transparentTranmit;


	protected:
		LOG logout;

	public:
		ATCommands();
		inline boolean checkResponse(char *string){
			//_tf.setTimeout(GSM_COMMAND_TIMEOUT);
	  		if(!_tf.find(string)){					
					logout.debugLog(string);
	    				return false;//if neccesary, send log out at here
	  		}
	  		else  
	    				return true;
		}
		inline void sendCommandString(char* string){	
			DelayNms(20);
	 		_cell.flush();
  	 		_cell << string << _BYTE(cr) << endl; 
  	 		//_cell << string << "\r"<< endl; 
		}


		inline boolean sendGenericCommand(char* command, char* expectedResponse){
			sendCommandString(command);
			return(checkResponse(expectedResponse));
		}

		inline void setTransmitMode(boolean mode){
			_transparentTranmit=mode;
		}

		inline boolean getTransmitMode(){
			return(_transparentTranmit);
		}

		inline boolean waitResponseCommand(char* command, char* response, char waitTimes){
			sendCommandString(command);
			for(int i=0; i<waitTimes; i++){
				if(checkResponse(response))
					return true;
			}
			return false;

		}

		inline boolean longtimeWaitCommand(char* command, char* response){
			return(waitResponseCommand(command, response, 50));
		}

		inline boolean shorttimeWaitCommand(char* command, char* response){
			return(waitResponseCommand(command, response, 10));
		}

		// after this, ip status will be IP INITIAL
		inline boolean deactivateGPRSContext(){
			return(shorttimeWaitCommand("AT+QIDEACT", "DEACT OK"));
		}


		char* toString(size_t num);

		boolean connectTCP(const char* server, int port);
		boolean disconnectTCP();// after this, ip status will be IP CLOSE
		boolean transparentTransmitConfig();

		void IpIntialConfig();

		boolean isSendFinished(size_t len);
		boolean isSendFinished();
		void sendData(const uint8_t *buf, size_t len);
		size_t readData(uint8_t *buf, size_t len);

		boolean PowerControl(M10PowerState_e powerControl);







		
		
		
		
};

#endif
