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
