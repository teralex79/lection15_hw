#!/usr/bin/python3.6

import logging
#from datetime import datetime

logger = logging.getLogger("hw15_extra")
sh = logging.StreamHandler()
fh = logging.FileHandler('sample.log', 'w')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s', datefmt = '%Y.%m.%d %H:%M:%S')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)
logger.addHandler(fh)
logger.debug("Program started logger.debug")
logger.info("Program started logger.info")
logger.warning("Program started logger.warning")


#print(datetime.now())

#logging.basicConfig(filename="sample.log", level=logging.INFO)
# Сообщение отладочное
#logging.debug( 'This is a debug message' )
# Сообщение информационное
#logging.info( 'This is an info message' )
# Сообщение предупреждение
#logging.warning( 'This is a warning' )
# Сообщение ошибки
#logging.error( 'This is an error message' )
# Сообщение критическое
#logging.critical( 'FATAL!!!' )

#logger = logging.getLogger("exampleApp")
#logger.setLevel(logging.INFO)
#logger2 = logging.getLogger("exampleApp2")
#logger2.setLevel(logging.INFO)
# create the logging file handler
#fh = logging.FileHandler("sample.log")
#fh2 = logging.FileHandler("sample.log")

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#formatter2 = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s  - %(message)s')
#fh.setFormatter(formatter)
#fh2.setFormatter(formatter2)
    
# add handler to logger object
#logger.addHandler(fh)
#logger2.addHandler(fh2)
    
#logger.info("Program started")
#logger2.info("Program started 2")
#logging.info("Program started")
# result = otherMod2.add(7, 8)
#logger.info("Done!")
#logger2.info("Done! 2")
 

