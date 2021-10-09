"""Win32 API function **SHChangeNotify**.
https://docs.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shchangenotify

Only required constants are defined.
"""

import ctypes

SHCNE_ASSOCCHANGED = 0x08000000
SHCNF_IDLIST = 0x0000

__all__ = ["notify_shell"]


def notify_shell():
    """Request the Windows shell to invalidate icon cache and rebuild it.
    See https://docs.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shchangenotify#remarks.
    """

    ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, 0, 0)
