# KitchenTimer

**KitchenTimer** is a lightweight Houdini package that alerts you with a sound whenever the UI event loop has been blocked for more than a specified duration (e.g., due to a long cook or save operation).  
It's designed to help you stay aware of heavy operations and long waits during Houdini sessions.

## 🔧 Features

- Monitors Houdini's main event loop in real time.
- Automatically detects interruptions (e.g., cooking, file saving).
- Plays a system sound (e.g., `notify.wav`) if the delay exceeds a threshold.
- Easy to install — just drop it into your Houdini packages folder.

## 🛠️ Installation

1. Place the `hkitchentimer` folder in your Houdini `packages` directory:
   ```
   $HOUDINI_USER_PREF_DIR/packages/
   ```

2. Make sure the following files exist:
   ```
   hkitchentimer/
   ├── hkitchentimer.json
   ├── __init__.py
   └── pythonrc.py
   ```

3. Launch Houdini — the timer will automatically activate on startup.

## 🔔 Behavior

- On every UI frame, it checks how much time has passed since the last update.
- If the delay exceeds `5.0` seconds (default threshold), it plays the sound file:
  ```
  C:\Windows\Media\notify.wav
  ```
- The sound is played asynchronously using `winsound.SND_ASYNC`, so it won’t block Houdini.

## ⚙️ Configuration

You can modify the threshold value in `pythonrc.py`:

```python
_kitchen_timer_instance = hkt.KitchenTimer(threshold=5.0)
```

You can also replace the sound file path in `__init__.py`:

```python
winsound.PlaySound("C:\\Windows\\Media\\notify.wav", ...)
```

## 🧠 Notes

- Currently, the script is Windows-only due to the use of the `winsound` module.
- You can further extend it to support different OSs, send system notifications, or display pop-ups.
- Useful for debugging or background batch work detection.

## 📄 License

MIT License or your own custom terms — feel free to modify and use as needed.
