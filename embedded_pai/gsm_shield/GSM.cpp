#include "GSM.h"
#include <string.h>


GSM::GSM():_cell(),_tf(_cell, 0),_status(IDLE){;}

/*
int GSM::isIP(const char* cadena)
{
    int i;
    for (i=0; i<strlen(cadena); i++)
        if (!(cadena[i]=='.' || ( cadena[i]>=48 && cadena[i] <=57)))
            return 0;
    return 1;
}
*/

//int GSM::startup(char* pin){return 0;};
int GSM::startup(void){return 0;};
void GSM::shutdown(){;};
//int GSM::sendSMS(const char* to, const char* msg){return 0;};
//int GSM::attachGPRS(char* domain, char* dom1, char* dom2){return 0;};
//int GSM::dettachGPRS(){return 0;};
//int GSM::connectTCP(const char* server, int port){return 0;};
//int GSM::disconnectTCP(){return 0;};
//int GSM::connectTCPServer(int port){return 0;};
//boolean GSM::connectedClient(){return false;};
//int GSM::readCellData(int &mcc, int &mnc, long &lac, long &cellid){return 0;};
//int GSM::write(const char* str){ return 0;}
int GSM::write(const uint8_t* buffer, size_t sz){return 0;};
//boolean GSM::availableSMS(){return false;};
//boolean GSM::readSMS(char* msg, int msglength, char* number, int nlength){return false;};
//boolean GSM::readCall(char* number, int nlength){return false;};
//boolean GSM::call(char* number, unsigned int milliseconds){return false;};
//int GSM::setPIN(char *pin){return 0;};
//int GSM::getCCI(char* cci){return 0;};
//int GSM::getIMEI(char* imei){return 0;};
int GSM::read(char* result, int resultlength){return 0;};
//uint8_t GSM::read(){return 0;};







