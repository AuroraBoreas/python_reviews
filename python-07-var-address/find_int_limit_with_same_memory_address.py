import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")

def test_limit(lbound: int) -> None:
    ubound: int = -250
    if lbound > ubound:
        raise ValueError("lbound must be < -250")
    for i in range(lbound, -250):
        a: int = i; b: int = i
        a_addr: str = hex(id(a))
        b_addr: str = hex(id(b))
        if a_addr != b_addr:
            logging.debug("hex(id(a)) = {}".format(a_addr))
            logging.debug("hex(id(b)) = {}".format(b_addr))
        else:
            logging.debug("found it! lower bound is {}".format(i)); break

if __name__ == "__main__":
    """
    this test is not working well.

    i had tested it via Python IDE manually.

    int limit [-5, 256], any var that has same value in this limit, shares the same memory address in Python IDE.
    """
    test_limit(250)