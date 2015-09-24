/*
  LOG.cpp - Library for standard logging convention.
  Created by Meir Michanie, June 9, 2010.
  Released into the public domain.
  Version 0.1
*/

#include "LOG.h"
#include "stdio.h"
//#include "string.h"

LOG::LOG(int level)
{
  setLevel(level);
}


//LOG::~LOG(){}

void LOG::regularLog(const char* string)
{
	fprintf(stdout,string);

}

void LOG::errorLog(const char* string)
{

	char *errorHeader = "error: ";
	fprintf(stderr,errorHeader);
 	fprintf(stderr,string);
 	char *errorEnd = "\r\n";
	fprintf(stderr,errorEnd);

}

void LOG::warningLog(const char* string)
{
 if (_level>2){
	char *worningEnd = "\r\n";
	char *worningHeader = "warning: ";
 	fprintf(stdout,worningHeader);
 	fprintf(stdout,string);
	fprintf(stdout,worningEnd);
 }
}

void LOG::debugLog(const char* string)
{
 if (_level>4){

	 char *debugEnd = "\r\n";
	 char *debugHeader = "debug: ";

 	 fprintf(stdout,debugHeader);
 	 fprintf(stdout,string);
	 fprintf(stdout,debugEnd);
 }
}

