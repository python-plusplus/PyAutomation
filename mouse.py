while True:
    from ctypes import windll, Structure, c_long, byref
    import time


    class POINT(Structure):
        _fields_ = [("x", c_long), ("y", c_long)]



    def queryMousePosition():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        windll.user32.
        return {"x": pt.x * 1.5, "y": pt.y * 1.5}


    pos = queryMousePosition()
    time.sleep(2)
    print(pos)