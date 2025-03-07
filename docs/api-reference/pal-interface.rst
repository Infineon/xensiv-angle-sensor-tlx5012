.. _pal-intf:

Platform Abstraction Layer Interface
------------------------------------

The `XENSIV™ TLx5012B`_ library requires SPIC and GPIO resources from the platform.
These are implemented in terms of the following abstract class APIs for each supported software framework:

- :ref:`SPIC PAL`
- :ref:`GPIO PAL`

Their member parameters and functions are described in this section.

.. _SPIC PAL:

SPIC PAL
""""""""

.. doxygenclass:: tle5012::SPICPAL
   :members:
   :allow-dot-graphs:

.. _GPIO PAL:

GPIO PAL
""""""""
.. doxygenclass:: tle5012::GPIOPAL
   :members:
   :allow-dot-graphs:

.. _`XENSIV™ TLx5012B`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e1000_ms2go