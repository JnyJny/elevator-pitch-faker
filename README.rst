Elevator Pitch Faker
====================

|pypi| |license| |python|

**elevator_pitch_faker** is a provider for the `Faker`_ Python package
which creates a humorous elevator pitch for your next novel/movie. Inspiration drawn from this `article`_.

Install
-------

Install with pip:

.. code:: bash
	  
 $ pip install elevator-pitch-faker


Or install with setup.py:

.. code:: bash
	  
 $ git clone https://github.com/jnyjny/elevator-pitch-faker.git
 $ cd elevator-pitch-faker && python3 setup.py install

Uninstall with pip:

.. code:: bash

	  $ pip uninstall elevator-pitch-faker

Usage
-----

Add the ``StoryPitchProvider`` to your ``Faker`` instance:

.. code:: python

	  from faker import Faker
	  from elevator_pitch_faker import StoryPitchProvider
	  
	  fake = Faker()
	  fake.add_provider(StoryPitchProvider)
	  
          print(fake.story_pitch())


View the methods defined by ElevatorPitchProvider:

.. code:: bash
	  
  $ pydoc3 elevator_pitch.StoryPitchProvider


.. |pypi| image:: https://img.shields.io/pypi/v/elevator-pitch-faker.svg?style=flat-square&label=version
    :target: https://pypi.org/pypi/elevator-pitch-faker
    :alt: Latest version released on PyPi

.. |python| image:: https://img.shields.io/pypi/pyversions/elevator-pitch-faker.svg?style=flat-square
   :target: https://pypi.org/project/elevator-pitch-faker/
   :alt: Python Versions	  

.. |license| image:: https://img.shields.io/badge/license-apache-blue.svg?style=flat-square
    :target: https://github.com/jnyjny/elevator-pitch-faker/blob/master/LICENSE
    :alt: Apache license version 2.0  

.. _Faker: https://github.com/joke2k/faker

.. _Elevator Pitch: https://github.com/jnyjny/elevator-pitch-faker

.. _article: https://electricliterature.com/how-to-write-elevator-pitch-novel-publicity-infographic-a8ec74ecf7ce
    

