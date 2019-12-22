DashML - Functional HTML Generation
====================================

Create functions to build HTML in Python- inspired by the "component movement" in Javascript.

```python
>>> from dashtml import _, render
>>>
>>> render(_.p("Hello, world!"))
'<p>Hello, world!</p>'
```

## Why DashML?

Javascript frameworks like React or Vue took over the frontend landscape because of the ease of creating reusable components. React _especially_ thrives with the fact that components are _code_, and can be manipulated as such.

Meanwhile, server-side languages are stuck with difficult to compose template languages to generate HTML. It's hard to extract components out of Jinja2 or Django templates to re-use.

DashML expands on existing Python libraries to create an ergonomic way to generate HTML in Python.

* Built on `lxml` (built on C) for extreme speed- check out the benchmarks (or run them yourself!).
* `markupsafe` to prevent injection attacks (like React does!)
* A minimal API you can pick up in ~15 minutes.

## Get Started

## Special Thanks

## License

MIT
