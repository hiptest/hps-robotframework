# hps-robotframework
[![Build Status](https://travis-ci.org/hiptest/hps-robotframework.svg?branch=master)](https://travis-ci.org/hiptest/hps-robotframework)

Hiptest publisher samples with Robot framework

In this repository you'll find tests generated in Robot framework format from [Hiptest](https://hiptest.com), using [Hiptest publisher](https://github.com/hiptest/hiptest-publisher).

The goals are:

 * to show how tests are exported in Robot framework.
 * to check exports work out of the box (well, with implemented actionwords)

System under test
------------------

The SUT is a (not that much) simple coffee machine. You start it, you ask for a coffee and you get it, sometimes. But most of times you have to add water or beans, empty the grounds. You have an automatic expresso machine at work or at home? So you know how it goes :-)

Update tests
-------------


To update the tests:

    hiptest-publisher -c robotframework.conf --only=tests

The tests are generated in the [``tests``](https://github.com/hiptest/hps-robotframework/tree/master/tests) directory.

Run tests
---------


To build the project and run the tests, use the following command:

    pybot -P src:tests tests/*.txt
Or 
    robot -P src:tests tests/*.robot


The SUT implementation can be seen in [``src/coffee_machine.py``](https://github.com/hiptest/hps-robotframework/blob/master/src/coffee_machine.py)

The test report is generated in ```output.xml```

