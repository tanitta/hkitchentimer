# Houdini Kitchen Timer
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/tanitta/hkitchentimer/blob/main/LICENSE)

Houdini Kitchen Timer is a lightweight Houdini package that notifies you with a sound when a long-running operation (such as cooking or saving) has finished.
It helps you catch the end of heavy processing without staring at the screen, allowing you to step away or multitask.

## Features

- Monitors Houdini's main event loop in real time.
- Automatically detects interruptions (e.g., cooking, file saving).
- Plays a system sound (notify.wav) as soon as Houdini becomes responsive again.

## Installation

1. Clone This Repository into your `$HOUDINI_PREF_DIR/packages`.
2. Copy and paste `hkitchentimer.json` in it into `$HOUDINI_PREF_DIR/packages`.

cf. [Houdini packages | Houdini help](https://www.sidefx.com/docs/houdini/ref/plugins.html)

## Behavior

- On every UI frame, it checks how much time has passed since the last update.
- If the delay exceeds `5.0` seconds (default threshold), it plays the sound file:
  ```
  C:\Windows\Media\notify.wav
  ```
- The sound is played asynchronously using `winsound.SND_ASYNC`, so it won’t block Houdini.

## Configuration

You can modify the threshold value in `pythonrc.py`:

```python
_kitchen_timer_instance = hkt.KitchenTimer(threshold=5.0)
```

You can also replace the sound file path in `__init__.py`:

```python
winsound.PlaySound("C:\\Windows\\Media\\notify.wav", ...)
```

## Notes

- Currently, the script is Windows-only due to the use of the `winsound` module.
- You can further extend it to support different OSs, send system notifications, or display pop-ups.

