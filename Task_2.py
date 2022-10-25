def python_art(thinkness: int):
    symbol = "H"
    for i in range(int(1.5*thinkness)):
        print(symbol*thinkness+" "*2*thinkness+symbol*thinkness)
    for i in range(int(thinkness/2)+1):
        print(symbol*4*thinkness)
    for i in range(int(1.5*thinkness)):
        print(symbol*thinkness+" "*2*thinkness+symbol*thinkness)
