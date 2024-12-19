import subprocess
import cairocffi
import sys

id = 54525966


def geticon(wm_class, path=""):
    out = subprocess.check_output(
        ["xprop", "-id", str(id), "-notype", "32c", "_NET_WM_ICON"]
    )
    outlist = [int(o.strip()) for o in out.decode("utf-8").split("=")[1].split(",")]

    width = outlist.pop(0)
    height = outlist.pop(0)

    imgdata = bytearray()
    for o in outlist:
        imgdata.extend(o.to_bytes(4, sys.byteorder))

    surf = cairocffi.ImageSurface(cairocffi.FORMAT_ARGB32, width, height, data=imgdata)
    surf.write_to_png(f"../resources/icons/{id}.png")
