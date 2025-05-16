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

You can customize the behavior of Kitchen Timer using environment variables in your houdini.env file.

### `HKITCHENTIMER_DURATION`
Type: float

Default: 5.0

Description:
Specifies the threshold (in seconds) after which the timer considers Houdini as "blocked."
If the delay exceeds this value, a sound will be played when Houdini becomes responsive again.

```
  HKITCHENTIMER_DURATION = 10
```

### `HKITCHENTIMER_SOUNDPATH`
Type: string (absolute file path to .wav)

Default: C:\Windows\Media\notify.wav

Description:
Path to the .wav file that will be played as a notification sound when the delay exceeds the threshold.

```
  HKITCHENTIMER_SOUNDPATH = "C:\Windows\Media\tada.wav"
```

### `HKITCHENTIMER_VOLUME`
Type: float

Default: 1.0

Description:
Gain multiplier for the notification sound. For example, 2.0 doubles the volume.

```
HKITCHENTIMER_VOLUME = 2.0
```

## Notes

- Currently, the script is Windows-only due to the use of the `winsound` module.
- You can further extend it to support different OSs, send system notifications, or display pop-ups.

