.. image:: https://img.shields.io/badge/IRC-%23hackerfleet%20on%20freenode-blue.svg
    :target: http://webchat.freenode.net/?randomnick=1&channels=hackerfleet&uio=d4>
    :alt: IRC Channel

.. image:: https://img.shields.io/badge/dynamic/json.svg?url=https://pypistats.org/api/packages/hfos/recent?mirrors=false&label=downloads&query=$.data.last_month&suffix=/month
    :target: https://pypistats.org/packages/hfos

Please be wary of bugs and report strange things, thank you!

HFOS - The Hackerfleet Operating System
=======================================

**A collaborative and modular vessel board computer system.**

* **Geo Information** Use a sophisticated map to annotate and review geographical information
* **Vehicle support** Attach a sailyacht, your camper or pack one in your backpack
* **Project planning** Issue tracking for collaborative teams
* **Modular** Expandable with integrated modules, build your own
* **Cloud independent** Run nodes on your own infrastructure

Installation
============

This is a (dependency) module to install an `Isomer instance <https://github.com/isomeric/isomer>`__
with all non-experimental Hackerfleet modules.

There is more than one way of installing Isomer, `see the detailed instructions for those
<http://isomer.readthedocs.io/en/latest/start/quick.html>`__.

After installing Isomer, use the management tool to install this package:

.. code-block:: sh

    sudo iso instance install-module https://github.com/hackerfleet/hfos

Or if you already downloaded the repository:

.. code-block:: sh

    sudo iso instance install-module -i -s git /path/to/hfos-repo

Modules
=======

We primarily focused on navigation tools, so these are currently the 'more usable' modules.
They are far from complete, see the WiP list below.

*Obligatory Warning*: **Do not use for navigational purposes!**
*Always have up to date paper maps and know how to use them!*

============== ==============================================================
  Name           Description
============== ==============================================================
alert          User alerting and notification system
anchor         Automatic anchor safety watcher
busrepeater    Tool to repeat navigation data bus frames to other media
comms          Communication package
dashboard      Dashboard information system
equipment      Equipment management
logbook        Displaying and manual logging of important (nautical) events
maps           (Offline) moving maps with shareable views/layers
mesh           Mesh networking
navdata        Navigational data module
nmea           NMEA-0183 Navigation and AIS data bus parser
nodestate      Node wide status system
robot          RC remote control unit
switchboard    Virtual switchboard
webguides      Importer for skipperguide.de wiki content into the map
============== ==============================================================

Work in progress
----------------

-  Full GDAL based vector chart support (Currently only raster charts)
-  Dynamic Logbook
-  GRIB data (in charts)
-  Navigation aides, planning
-  Datalog, automated navigational data exchange
-  Crew management, more safety tools
-  wireless crew network and general communications

Bugs & Discussion
=================

Please research any bugs you find via our `Github issue tracker for
Isomer <https://github.com/hackerfleet/hfos/issues>`__ and report them,
if they're still unknown.

You can also find us here:

* `github.com/Hackerfleet <https://github.com/Hackerfleet>`__
* `reddit <https://reddit.com/r/hackerfleet>`__
* `Hackerfleet Twitter <https://twitter.com/hackerfleet>`__
* `Isomer Twitter <https://twitter.com/isomerframework>`__
* `Facebook <https://www.facebook.com/Hackerfleet>`__
* `soup.io <http://hackerfleet.soup.io/>`__
* `G+ <https://plus.google.com/105528689027070271173>`__
* `irc #hackerfleet on freenode <http://webchat.freenode.net/?randomnick=1&channels=hackerfleet&uio=d4>`__

.. note:: Please be patient when using IRC, responses might take a few hours!

Contributors
============

Code
----

-  Heiko 'riot' Weinen riot@c-base.org
-  Johannes 'ijon' Rundfeldt ijon@c-base.org
-  Martin Ling
-  River 'anm' MacLeod
-  Sascha 'c_ascha' Behrendt c_ascha@c-base.org
-  `You? <mailto:riot@c-base.org?subject=Isomer Contributor Request>`_

Assets
------

-  Fabulous icons by iconmonstr.com, the noun project and Hackerfleet contributors

Support
-------

-  `c-base e.V. <https://c-base.org>`__ our home base, the spacestation below Berlin Mitte
-  Lassulus for hosting and nix expertise
-  `Jetbrains s.r.o <https://jetbrains.com>`__ for the opensource license of their ultimate IDE
-  `Github <https://github.com>`__ for hosting our code
-  `Gitlab <https://gitlab.com>`__ for hosting our code ;)
-  `Travis.CI <https://travis-ci.org>`__ for continuous integration services
-  `BrowserStack <https://browserstack.com>`__ for cross device testing capabilities

License
=======

Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


-- :boat: :+1:
