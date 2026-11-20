# Light mode for laptops with little memory (viewer: "failed after 1.5 h, low memory", 20 Nov).
# On when CLIPPER_LIGHT=1, or automatically under 12 GB of RAM (CLIPPER_LIGHT=0 turns it off).
# Light = 1 Short at a time, 30 fps renders, only the first hour of very long streams, audio downloads deleted once transcribed.
import ctypes, os, shutil, sys

def ram_gb():
    try:
        if os.name == "nt":
            class M(ctypes.Structure): _fields_ = [("l", ctypes.c_ulong), ("load", ctypes.c_ulong), ("total", ctypes.c_ulonglong), ("avail", ctypes.c_ulonglong)] + [(f"x{i}", ctypes.c_ulonglong) for i in range(5)]
            m = M(); m.l = ctypes.sizeof(M); ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)); return m.total / 2 ** 30
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2 ** 30
    except Exception: return 16.0  # unknown: assume enough

def light():
    v = os.environ.get("CLIPPER_LIGHT", "")
    return v == "1" if v in ("0", "1") else ram_gb() < 12

def disk_ok(path=".", need_gb=3.0):
    """Stop early with a clear message instead of failing after an hour: a run needs a few GB for downloads and renders."""
    free = shutil.disk_usage(os.path.abspath(path)).free / 2 ** 30
    if free < need_gb:
        sys.exit(f"Only {free:.1f} GB free on this disk; a run needs about {need_gb:.0f} GB. Free some space "
                 "(in the app: Settings > Disk space > Delete downloads), then run again.")
    return free

def note():
    return f"Light mode on ({ram_gb():.0f} GB RAM): 1 Short at a time, 30 fps, first hour of long streams." if light() else ""

if __name__ == "__main__":
    os.environ["CLIPPER_LIGHT"] = "1"; assert light(); os.environ["CLIPPER_LIGHT"] = "0"; assert not light()
    assert ram_gb() > 0 and disk_ok(".", 0.0) > 0
    print("selftest ok", round(ram_gb(), 1), "GB RAM")
