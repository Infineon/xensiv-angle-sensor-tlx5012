.. _porting-guide:

Porting Guide
=============

Porting the library to a new software development framework and hardware
platform entails the implementation of the corresponding GPIO and SPI
PAL classes. In the following sections, some additional explanations and
hints are provided:

Framework PAL Implementation
----------------------------

Implement the abstract PAL interface for you framework. The **SPI
class** and **GPIO class** are mandatory.

The Doxygen comments in *"src/pal/tlx5012-pal-gpio.hpp"* and *"src/pal/tlx5012-pal-spic.hpp"*
describe the required behavior of each function
of the :ref:`PAL Interface <pal-intf>`.

Consider the existing framework implementations as reference examples
for your design: *“/src/framework/sample_fmwk/pal”*. Some of the
functions are optional, depending on your framework and intended usage of
the library.

This is the case for *init()* and *deinit()*, which take care of the
hardware peripherals init/deinitialization. If this is done in your main
application (or somewhere else outside the library), there is no need of
delegating such initialization to the `XENSIV™ TLx5012B`_ library. The definition
of these functions can just be a return with the success return code.


Framework API Wrapper
---------------------

The framework API wrapper implementation is optional, it is meant to
ease the usage. The main help it provides is avoiding the creation of the
GPIO and SPI object instances for the developer.

To illustrate this approach, it is easier to evaluate a concrete
implementation of the Arduino wrapper. For example the constructor of
the *Tle5012Ino* class, which can be found in the files *“src/framework/arduino/wrapper/tle5012-ino.cpp”*.

Adapt the constructor arguments to those used for the platform class
creation (GPIO and SPI) in the new framework, using the native
data types and structures. Hide what can be already defined for that
platform and provide as much abstraction and simplicity as possible.

For example, the core library of the base constructor is defined like
this:

.. code-block:: C
   
   Tle5012B();

is wrapped for Arduino like this:

.. code-block:: C

   Tle5012Ino();
   Tle5012Ino(uint8_t csPin, slaveNum slave=TLE5012B_S0);
   Tle5012Ino(SPIClass3W &bus, uint8_t csPin, uint8_t misoPin, uint8_t mosiPin, uint8_t sckPin, slaveNum slave=TLE5012B_S0);

While it does not seem to simplify much in number of arguments, an
Arduino developer can simply pass the pin number as argument, and
does not need to deal with the (probably unknown) GPIO classes,
neither specify further GPIO configuration like the mode (input,
output, pull-up..), positive/negative logic, etc.

As for the constructor, the same philosophy can apply to other
functions of the public API. In case of Arduino clarity and simplicity might prevail over
configurability and functionality. Therefore, the :ref:`wrapper API <arduino-api>` 
further hides, groups or eliminates certain functionalities.

For each ecosystem and framework, any other criteria can be chosen,
to match as well its code conventions, implementation
principles and paradigms.


.. _`XENSIV™ TLx5012B`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e1000_ms2go
