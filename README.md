# KeebShot - Custom Keyboard Shortcut for Windows

KeebShot is a custom keyboard shortcut application developed using Python. It allows users to define and manage their own keyboard shortcuts for various tasks and actions on their computer. Whether you're a power user or simply want to streamline your workflow, KeebShot offers a simple and efficient way to enhance your productivity.


                                                            ![icon](/Screenshots/icon.jpg)

                ![settings](/Screenshots/settings.jpg)

## Requirements

- Python 3.x
- [keyboard](https://pypi.org/project/keyboard/) library
- [AppOpener](https://github.com/athrvvvv/AppOpener) library
- [infi.systray](https://github.com/Infinidat/infi.systray) library
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) library

## Installation

1. Clone the KeebShot repository:

```bash
git clone https://github.com/your-username/KeebShot.git
```

2. Goto cloned folder

```
cd KeebShot
```

3. Install the required dependencies using pip:

```bash
pip install requirements.txt
```

## Usage

1. Launch KeebShot by running the `runner-script.bat` file.

2. Right click on the system tray icon of KeebShot and click on settings

3. The GUI window will pop up, click on Edit JSON Use to create, edit, and manage your custom keyboard shortcuts. Specify the desired keyboard combination and the associated action for each shortcut.

4. Save your shortcuts, and hit Restart App to load the changes KeebShot will automatically start monitoring the keyboard for the defined combinations. When a shortcut is triggered, the associated action will be executed.

5. To exit KeebShot, simply right click on the system tray icon and select Quit.

## Contributing

Contributions to KeebShot are welcome! If you have any ideas, bug reports, or feature requests, please submit them through the GitHub repository. Make sure to follow the [contribution guidelines](CONTRIBUTING.md) when submitting your code.

## Acknowledgements

KeebShot was inspired by the need for customizable keyboard shortcuts and was developed as a personal project. We would like to thank the open-source community for their valuable contributions and the libraries used in building this application.

- [Python](https://www.python.org/)
- [keyboard](https://github.com/boppreh/keyboard)
- [AppOpener](https://github.com/athrvvvv/AppOpener)
- [infi.systray](https://github.com/Infinidat/infi.systray)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to the project maintainer at [saranshbhatnagar@proton.me](mailto:saranshbhatnagar@proton.me). We appreciate your interest in KeebShot!
