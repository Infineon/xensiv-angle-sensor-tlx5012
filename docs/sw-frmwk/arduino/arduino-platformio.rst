.. _arduino-platformio:

Arduino & PlatformIO
====================

Introduction
------------
If you are new to PlatformIO, download and install Visual Studio Code first and then the PlatformIO plugin. Please follow the 
instructions on the `official website`_. Then go through `this tutorial`_ to get started with PlatformIO in VSCode and create a new project.


Library Installation
--------------------
With the project created, now the library and its dependencies can be configured in the Platform.ini Project File. This file, 
located in the project root folder, includes one (or several) building environments ``[env:__]``.

In the environment section, the platform, board, and framework are specified. PlatformIO will take care of downloading and installing the dependencies.

In the following example, we use ...

.. code-block::
    
    [env:uno]
    platform = atmelavr
    board = uno
    framework = arduino

    lib_deps=
    # Using a library name
    arduino-xensiv-tlx5012b-angle-sensor

    # Using the repository URL
    https://github.com/Infineon/arduino-xensiv-tlx5012b-angle-sensor

You can also simply take the ``platform.ini`` file from the `arduino-xensiv-tlx5012b-angle-sensor repo`_. This file includes all settings 
for using this library with different platforms.


.. note::
    PlatformIO is a professional collaborative platform for embedded development. It is an alternative to the Arduino IDE and is compatible with the Arduino ecosystem.
    PlatformIO is not officially supported by Infineon Technologies AG.


.. _`official website`: https://docs.platformio.org/en/latest/
.. _`this tutorial`: https://docs.platformio.org/en/stable/integration/ide/vscode.html
.. _`arduino-high-side-switch repo`: https://github.com/Infineon/arduino-xensiv-tlx5012b-angle-sensor
