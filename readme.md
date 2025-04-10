
Title
-----

The evolution of a configuration system for UAV actuator monitoring: a refactoring case study


About
-----

Daniel is working with custom sensor systems, monitoring applications and mission critical embedded systems developed for research UAVs. As part of a flight testing team, he is one of the first tester, user and critic of his own work. He enjoys working on software related problems, helping others, reading and making coffee.


Abstract
--------

With this talk, I invite you to look at the evolution of the configuration management implementation of a UAV actuator monitoring system. The system has an SD card slot with a file system, a USB port and an I2C connection for additional sensors. Over time, we evolved the system from purely compile-time configuration to mixed compile-time and run-time configurations. The latest iteration of the configuration system allows some parameter and feature flag changes at run-time and can update the local configuration file with actual values. 

During the talk, we will highlight the main differences between the two design. We will explore the influence of some literature, the and usage of language elements like static_assert, templates and lambda functions and idioms like RAII and YAGNI. At the end of the talk, we will compare the usability and memory consumption of each design and collect some lessons learned. 

[Live Link](https://htmlpreview.github.io/?https://github.com/dTeubl/acmu_refactoring_casestudy/blob/main/refactoring.html#)
