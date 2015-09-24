/*
  LOG.h - Library for standard logging convention.
  Created by Meir Michanie, June 9, 2010.
  Released into the public domain.
  Version 0.1
*/

#ifndef LOG_h
#define LOG_h
//#include "WProgram.h"

class LOG
{
 public:
	LOG(int level);
//	~LOG();
	void regularLog(const char* string);
	void errorLog(const char* string);
	void warningLog(const char* string);
	void debugLog(const char* string);

  inline int  getLevel(void)      { return _level ;  }
  inline void setLevel(int level) { _level = level; }
	
 private:
	int _level ;
	
};

#endif
