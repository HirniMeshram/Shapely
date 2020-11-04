"""Load/dump geometries using the well-known text (WKT) format
"""

from shapely import geos

import pygeos


# Pickle-like convenience functions


def loads(data):
    """
    Load a geometry from a WKT string.

    Parameters
    ----------
    data : str
        A WKT string

    Returns
    -------
    Shapely geometry object
    """
    return pygeos.from_wkt(data)


def load(fp):
    """
    Load a geometry from an open file.

    Parameters
    ----------
    fp :
        A file-like object which implements a `read` method.

    Returns
    -------
    Shapely geometry object
    """
    data = fp.read()
    return loads(data)


def dumps(ob, trim=False, rounding_precision=-1, **kw):
    """
    Dump a WKT representation of a geometry to a string.

    Parameters
    ----------
    ob :
        A geometry object of any type to be dumped to WKT.
    trim : bool, default False
        Remove excess decimals from the WKT.
    rounding_precision (GEOS 3.3+) : int
        Round output to the specified number of digits.
        Default behavior returns full precision.
    output_dimension (GEOS 3.3+): int, default 3
        Force removal of dimensions above the one specified.

    Returns
    -------
    input geometry as WKT string
    """
    return pygeos.to_wkt(ob, trim=trim, rounding_precision=rounding_precision, **kw)


def dump(ob, fp, **settings):
    """
    Dump a geometry to an open file.

    Parameters
    ----------
    ob :
        A geometry object of any type to be dumped to WKT.
    fp :
        A file-like object which implements a `write` method.
    trim : bool, default False
        Remove excess decimals from the WKT.
    rounding_precision (GEOS 3.3+) : int
        Round output to the specified number of digits.
        Default behavior returns full precision.
    output_dimension (GEOS 3.3+): int, default 3
        Force removal of dimensions above the one specified.

    Returns
    -------
    None
    """
    fp.write(dumps(ob, **settings))
