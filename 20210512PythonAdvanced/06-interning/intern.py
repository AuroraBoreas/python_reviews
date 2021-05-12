"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

a = 140971
b = 140971
logging.debug(id(a))
logging.debug(id(b))
logging.debug(a is b)

a = "Zhang Liang"
b = "Zhang Liang"
logging.debug(a is b)

a = "T" * 4096
b = "T" * 4096
logging.debug(a is b)

a = "T" * 4097
b = "T" * 4097
logging.debug(a is b)

import sys
a = sys.intern('T' * 8194)
b = sys.intern('T' * 8194)
logging.debug(a is b)