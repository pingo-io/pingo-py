pingo-scripts
=============

Here some tools are found. They a designed to help our development.

If you use ``vim`` text editor, you can use the given ``vimrc`` to replace or
update something in your ``~/.vimrc`` file. Previously we had some problems
with TABs instead of spaces, as well as undesired trailing whitespaces.

The basic is to use expandtabs ``:set et``, which would avoid TABs by expanding
it to spaces. To ensure 4 spaces while keeping the indentation in new lines, a
it would be ``:set et ai ts=4 sw=4``. The ``vimrc`` here does that and also
several other useful configuration, like highlighting for the undesired
whitespaces.

In any case, to replace all tabs in a file to spaces using ``vim``, just type
``:ret``. For breaking text lines up to textwidth (79 chars in ``vimrc``,
following PEP8), type ``3gqj``, replacing the ``3`` by the number of lines that
makes one single paragraph (before the new line breaking). That's useful for
RST files (reStructuredText).

There is also a `purge_whitespace.sh` script. It fixes the white space issue in
all .py and .sh and  files of the project. So when adding new files that my not
the ok about whitespace, run this script.


-----------
Basic usage
-----------

.. code-block:: bash

    cp vimrc ~/.vimrc
    ./purge_whitespace.sh

