import hou
import hkitchentimer as hkt

def is_callback_registered(callback_fn):
    return callback_fn in hou.ui.eventLoopCallbacks()

_kitchen_timer_instance = None

def start_kitchen_timer():
    global _kitchen_timer_instance
    if _kitchen_timer_instance is None:
        try:
            threshold = float(hou.getenv("HKITCHENTIMER_DURATION", "5.0"))
        except ValueError:
            threshold = 5.0  # fallback
        sound_path = hou.getenv(
            "HKITCHENTIMER_SOUNDPATH",
            "C:\\Windows\\Media\\notify.wav"
        )
        _kitchen_timer_instance = hkt.KitchenTimer(sound_path, threshold)

    if not is_callback_registered(_kitchen_timer_instance.update):
        hou.ui.addEventLoopCallback(_kitchen_timer_instance.update)
        print("KitchenTimer registered.")
    else:
        print("KitchenTimer already registered.")

start_kitchen_timer()
