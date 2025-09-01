# Technical Specification

## General guidelines

* The code should be as simple as possible to achieve the Product Specifications
* There should be some kind of end to end test
  * For the command line app, a markdown test plan for a human to follow will be sufficient
* There should be unit tests

## Architecture and Framework guidelines

* There should be facility to manage what version of Python is used
* Dependencies pulled from pypi.org should be managed with modern best practice dependency management framework for Python
* The web application and API should use the Flask framework
* We should use SQLite as a database for early development
  * We should use patterns or frameworks that will allow for changing to use Postgres in the future
