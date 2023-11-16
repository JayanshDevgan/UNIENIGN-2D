import pyuac
from output import UNI
from Hub import HUB


if not pyuac.isUserAdmin():
    UNI.Warn("\n\t\t\t Re-launching as admin!")
    pyuac.runAsAdmin()
else:
    HUB.initialize()