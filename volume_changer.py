# volume changer library

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# function which return the volume interface
def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

# function which increase the volume
def increase_volume(step=0.1):
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + step, 1.0), None)

# function which decreases the volume
def decrease_volume(step=0.1):
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - step, 0.0), None)

# function to mute volume
def mute_volume():
    volume = get_volume_interface()
    volume.SetMute(1, None)

# function to unmute the volume
def unmute_volume():
    volume = get_volume_interface()
    volume.SetMute(0, None)
