.. DashML documentation master file, created by
   sphinx-quickstart on Sun Dec 22 15:43:03 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DashML Docs
===========

DashML is a library for creating HTML components- directly in Python. You can define HTML components as functions, for reuse, composability, and rendering. ::

    from dashml import render, _

    def my_greeter(subject: str):
        return _.p(f"Hello {name}!")

    render(my_greeter("world"))

While template languages like Django or Jinja have reusability and componentizing problems, DashML is built specifically for a great API for authoring components.

DashML is built as an extension to document creation on top of lxml. This gives DashML awesome speed, and native interop with lxml functions and methods.

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart.md
   dashml.rst

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
