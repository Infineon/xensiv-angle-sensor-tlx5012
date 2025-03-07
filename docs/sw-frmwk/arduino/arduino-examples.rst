.. _arduino-examples:


Arduino Examples
----------------

You can find these examples also in the Arduino IDE by navigating to *File* -> *Examples* -> *XENSIV TLx5012B Angle Sensor*.

.. list-table::
    :header-rows: 1

    * - Example
      - Summary
    * - :code:`E9000SPC <example-E9000SPC.rst>`
      - * :ref:`example-E9000SPC`
    * - :code:`readAngleSpeedRevolutions <example-readAngleSpeedRevolutions.rst>`
      - * :ref:`example-readAngleSpeedRevolutions`
    * - :code:`readAngleTest <example-readAngleTest.rst>`
      - * :ref:`example-readAngleTest`
    * - :code:`readAngleValueProcessing <example-readAngleValueProcessing.rst>`
      - * :ref:`example-readAngleValueProcessing`
    * - :code:`readMultipleRegisters <example-readMultipleRegisters.rst>`
      - * :ref:`example-readMultipleRegisters`
    * - :code:`readSpeedProcessing <example-readSpeedProcessing.rst>`
      - * :ref:`example-readSpeedProcessing`
    * - :code:`sensorRegisters <example-sensorRegisters.rst>`
      - * :ref:`example-sensorRegisters`
    * - :code:`sensorType <example-sensorType.rst>`
      - * :ref:`example-sensorType`
    * - :code:`snapshotSensorValues <example-snapshotSensorValues.rst>`
      - * :ref:`example-snapshotSensorValues`
    * - :code:`useMultipleSPIChannels <example-useMultipleSPIChannels.rst>`
      - * :ref:`example-useMultipleSPIChannels`
    * - :code:`useMultipleSensors <example-useMultipleSensors.rst>`
      - * :ref:`example-useMultipleSensors`
    * - :code:`writeRegisters <example-writeRegisters.rst>`
      - * :ref:`example-writeRegisters`


Processing Examples
-------------------

There are also some programs based on the `Processing`_ language. These programs are using the serial communication
to the sensor either with the :ref:`example-readAngleValueProcessing` or the :ref:`example-readSpeedProcessing` example.

To run this games the needed Arduino example has to be uploaded to the `TLE5012B E1xxx 2GO Kits`_ and a special joystick with a magnet has to be used.

.. list-table::
    :header-rows: 1

    * - Example
      - Summary
    * - :code:`Ball_Bat <Ball_Bat.rst>`
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`Bouncing_Ball_Game <Bouncing_Ball_Game.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`Circle <Circle.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`Make_Spiral <Make_Spiral.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`Snake <Snake.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`Snake_Like_Game <Snake_Like_Game.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`pong <pong.rst>` 
      - * needs :ref:`example-readAngleValueProcessing`
    * - :code:`speed <speed.rst>` 
      - * needs :ref:`example-readSpeedProcessing`


.. _`Processing`: https://processing.org/
.. _`XENSIV™ TLx5012B`: https://www.infineon.com/cms/en/product/evaluation-boards/tle5012b_e1000_ms2go
.. _`TLE5012B E1xxx 2GO Kits`: https://www.infineon.com/cms/en/product/promopages/sensors-2go/#angle-sensor-2go