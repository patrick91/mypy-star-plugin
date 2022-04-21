from typing import Tuple, Union, TypeVar, Type


class User:
    name: str


class Error:
    message: str


class AnotherError:
    message: str


UserErrors = (
    Error,
    AnotherError,
)

# Ideally this should be a TypeVarTuple, but it doesn't seem to be supported by mypy
Types = TypeVar("Types", bound=Type)


def fake_union(name: str, types: Tuple[Types, ...]) -> Union[Types]:
    ...


Response = fake_union(types=(User, *UserErrors), name="Response")
