from typing import Any, Callable, Iterable, List, Tuple, Union


def _split(from_imports: Iterable[str], key: Callable[[str], str]) -> List[List[Union[str, Tuple[int, str]]]]:
    return [
        [key(package)[0]] + [(len(subpackage), subpackage) for subpackage in package.split(".")]
        for package in from_imports
    ]


def _merge(imports: List[List[Any]]) -> List[str]:
    return [".".join(package for _, package in _import) for _, *_import in imports]


def grouped_length(to_sort: Iterable[str], key: Callable[[str], str], reverse: bool = False) -> List[str]:
    return _merge(sorted(_split(to_sort, key), reverse=reverse))
