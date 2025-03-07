.. XENSIV TLx5012B Angle Sensor documentation master file, created by
   sphinx-quickstart on Wed Sep 18 17:51:31 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

`XENSIV™ TLx5012B`_ Angle Sensor Documentation
==============================================

Welcome to the Infineon `XENSIV™ TLx5012B`_ magnetic angle sensor library docs!

.. list-table::
    :width: 100%
    :class: borderless

    * - .. image:: img/TLx5012B-Exxxx_Board_top-persp.jpg
            :width: 100%
            :align: center

      - .. image:: img/TLE5012B_breakout.png
            :width: 100%
            :align: center

      - .. image:: img/TLE_5012B_DSO-8-16_plain.png
            :width: 100%
            :align: center


Scope
=====

The `XENSIV™ TLx5012B`_ is a 360° angle sensor that detects the orientation of a magnetic field.
This is achieved by measuring sine and cosine angle components with monolithic integrated Giant Magneto Resistance (iGMR) elements.
These raw signals (sine and cosine) are digitally processed internally to calculate the angle orientation of the magnetic field (magnet). 
The `XENSIV™ TLx5012B`_ is a pre-calibrated sensor. The calibration parameters are stored in laser fuses. At start-up the values of
the fuses are written into flip-flops, where these values can be changed by the application-specific parameters. Further precision of the angle measurement 
over a wide temperature range and a long lifetime can be improved by enabling an optional internal auto calibration algorithm.
Data communication is achieved through a bi-directional Synchronous Serial Communication (SSC) interface that is SPI-compatible. The sensor configuration is stored in registers, 
which are accessible by the SSC interface. Additionally four other interfaces are available with the `XENSIV™ TLx5012B`_: Pulse-Width-Modulation (PWM) protocol, 
Short-PWM-Code (SPC) protocol,
Hall Switch Mode (HSM) and Incremental Interface (IIF). These interfaces can be used in parallel with SSC or alone. Pre-configured sensor derivates with
different interface settings are available.

This library provides a generic software framework for the `XENSIV™ TLx5012B`_ family. The library is designed to be used with different hardware platforms and software frameworks.

* `TLE5012B E1xxx 2GO Kits`_ with different predefined communication protocols
* `TLI5012B E1000 2GO Kit`_ with SSC and IIF communication protocol
* :ref:`TLx5012B Breakout Board` with different predefined communication protocols in push-pull or open-drain configuration
* `TLE5012B E1000`_  DSO-8-16 bulk chip with different predefined communication protocols (see :ref:`Interfaces and Variants`) in push-pull or open-drain configuration
* This library covers the SSC communication protocol for all variants

TLx5012B Family
===============

The TLx5012B family includes the following predefined communication protocols:

* SSC (Synchronous Serial Communication) or 3-wire SPI (Serial Peripheral Interface) which is implemented in all variants 
* IIF (Infineon Interface) which is implemented in the `TLE5012B E1000 2GO Kit`_ or the `TLI5012B E1000 2GO Kit`_
* PWM (Pulse Width Modulation) which is implemented in the `TLE5012B E5000 2GO Kit`_
* SPC (Single Pin Communication) which is implemented in the `TLE5012B E9000 2GO Kit`_

Beside the predefined protocols, all `XENSIV™ TLx5012B`_ variants can be configured to use any of these custom communication protocols.

License
=======

Please find the license file for this library `here <https://github.com/Infineon/arduino-xensiv-tlx5012b-angle-sensor/main/LICENSE>`_.

.. toctree::
   :maxdepth: 3
   :caption: Home
   :hidden:

   Introduction <self>

.. toctree::
   :maxdepth: 3
   :caption: Hardware Platforms
   :hidden:

   hw-platforms/hw-platforms

.. toctree::
   :maxdepth: 3
   :caption: Additional information
   :hidden:

   misc/index

.. toctree::
   :maxdepth: 3
   :caption: Software Frameworks
   :hidden:

   sw-frmwk/index

.. toctree::
   :maxdepth: 3
   :caption: Examples
   :hidden:

   examples/index

.. toctree::
   :maxdepth: 5
   :caption: API Reference
   :hidden:

   Modules     <api-reference/modules.rst>

.. toctree::
   :maxdepth: 3
   :caption: Library Details
   :hidden:

   Library Architecture <lib-details/library-architecture.rst>
   Porting Guide <lib-details/porting-guide.rst>

.. toctree::
   :maxdepth: 3
   :caption: Related Links
   :hidden:

   links


.. _`XENSIV™ TLx5012B`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e1000_ms2go
.. _`TLE5012B E1xxx 2GO Kits`: https://www.infineon.com/cms/en/product/promopages/sensors-2go/#angle-sensor-2go
.. _`TLE5012B E1000 2GO Kit`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e1000_ms2go/
.. _`TLI5012B E1000 2GO Kit`: https://www.infineon.com/cms/en/product/evaluation-boards/tli5012b_e1000_ms2go/
.. _`TLE5012B E5000 2GO Kit`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e5000_ms2go/
.. _`TLE5012B E9000 2GO Kit`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e9000_ms2go/
.. _`TLE5012B E1000`: https://www.infineon.com/cms/en/product/sensor/magnetic-sensors/magnetic-position-sensors/angle-sensors/tle5012b-e1000/
