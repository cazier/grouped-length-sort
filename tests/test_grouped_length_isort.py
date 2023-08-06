import isort
from ward import test


@test("test length sort can group by package")  # type: ignore[misc]
def _() -> None:
    assert (
        isort.code(
            """
import a.b.cc
import b.aa.d
import b.a.d

from a.b.c import d
from aa.bb.cc import dd
from aa.b.c import e
from a.bb.cc import d
from aaaa.b import c
""",
            group_by_package=True,
            length_sort=True,
            sort_order="grouped_length",
        )
        == """
import a.b.cc
import b.a.d
import b.aa.d
from a.b.c import d
from a.bb.cc import d
from aa.b.c import e
from aa.bb.cc import dd
from aaaa.b import c
"""
    )


@test("include stdlib")  # type: ignore[misc]
def _() -> None:
    assert (
        isort.code(
            """
from a.b.c import d
from aa.bb.cc import dd
from aa.b.cc import dd
from multiprocessing.pool import ApplyResult
from multiprocessing.heap import Arena
from multiprocessing.dummy import DummyProcess
import multiprocessing.forkserver
""",
            group_by_package=True,
            length_sort=True,
            sort_order="grouped_length",
        )
        == """
import multiprocessing.forkserver
from multiprocessing.heap import Arena
from multiprocessing.pool import ApplyResult
from multiprocessing.dummy import DummyProcess

from a.b.c import d
from aa.b.cc import dd
from aa.bb.cc import dd
"""
    )


@test("include 3rd party")  # type: ignore[misc]
def _() -> None:
    assert (
        isort.code(
            """
from ward import test
from isort.api import sort_file
from isort.stdlibs.py2 import stdlib
from isort.stdlibs.py3 import stdlib, py310

from isort.files import find
from isort.hooks import get_lines
from a.b.c import d
from aa.bb.cc import dd
from aa.b.cc import dd
""",
            group_by_package=True,
            length_sort=True,
            sort_order="grouped_length",
            known_third_party=["ward", "isort"],
            known_first_party=["a", "aa"],
        )
        == """
from ward import test
from isort.api import sort_file
from isort.files import find
from isort.hooks import get_lines
from isort.stdlibs.py2 import stdlib
from isort.stdlibs.py3 import py310, stdlib

from a.b.c import d
from aa.b.cc import dd
from aa.bb.cc import dd
"""
    )
