pypelinin'
==========

It's just experimentation for now. The idea is to create a simple (without
parallelism) pipeline to process text.

You pass the filenames and plugins want to use, so the pipeline will be created
and the plugins will work within that filenames.

If do you want to conver all your `.markdown` files to HTML, for example, so you
need this code:

    import pypelinin
    pypelinin.process(plugins=['glob', 'markdown'], parameters=['*.markdown'])

Further Develpment
==================

- There are a lot of plugins missing (now we have just two), like some kind of
  templating, support to other markup language, filters etc.
- If do you want to contribute, please use [Test-Driven
  Development](http://en.wikipedia.org/wiki/Test-driven_development).
