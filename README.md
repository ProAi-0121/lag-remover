# Lag Remover

A small Windows desktop tool that clears temporary files and refreshes the network
connection to help reduce lag. It's a single window with one button.

The window is built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
and packaged as an `.exe` with PyInstaller.

## What it does

Clicking **Fix** runs a few standard Windows maintenance commands and shows the
output in a console area inside the window:

- Deletes the current user's and Windows temporary files (`%temp%`, `%Windir%\Temp`)
- Clears the prefetch cache (`C:\WINDOWS\Prefetch`)
- Releases, flushes, and renews the DHCP lease / DNS cache (`ipconfig /release`,
  `ipconfig /flushdns`, `ipconfig /renew`)

When it finishes, the **Fix** button becomes **Quit**.

## Requirements

- Windows
- Python 3.x (only needed to run from source; the packaged `.exe` has none)

## Setup

```bash
pip install customtkinter
```

## Usage

Run it from the project folder:

```bash
python FIX.py
```

The cleanup and network commands need administrator rights to run reliably, so
open a terminal **as Administrator** before starting it.

## Building the .exe

```bash
pip install pyinstaller
pyinstaller Fix.spec
```

The executable is written to `dist/Fix.exe`. The `.spec` file points at `FIX.py`
and bundles `lag.ico` as the app icon.

## Project structure

```
lag-remover/
├── FIX.py        # the app itself
├── Fix.spec      # PyInstaller build config
├── lag.ico       # window icon
└── .gitignore
```

## Troubleshooting

- **Nothing happens when I click Fix.** Make sure you're running as Administrator.
- **The window icon doesn't show when running from source.** Run the script from
  the project folder so `lag.ico` is on the working path. The packaged `.exe`
  bundles the icon, so it isn't affected.