from decimal import Decimal
from typing import Callable, Optional

from mypy.nodes import NameExpr, StarExpr, TupleExpr
from mypy.plugin import DynamicClassDefContext, Plugin


def union_hook(ctx: DynamicClassDefContext) -> None:
    types_expr = ctx.call.args[ctx.call.arg_names.index("types")]

    assert isinstance(types_expr, TupleExpr)

    for type_ in types_expr.items:
        if isinstance(type_, StarExpr):
            assert isinstance(type_.expr, NameExpr)
            name = type_.expr.name

            # breakpoint()
            var_node = ctx.api.lookup_current_scope(name)
            print(dir(var_node))
            print(var_node.type)

            # how can I find the value of this expr?
            print(name)


class MypyVersion:
    """Stores the mypy version to be used by the plugin"""

    VERSION: Decimal


class ExamplePlugin(Plugin):
    def get_dynamic_class_hook(
        self, fullname: str
    ) -> Optional[Callable[[DynamicClassDefContext], None]]:
        if fullname == "app.fake_union":
            return union_hook

        return None


def plugin(version: str):
    # Save the version to be used by the plugin.
    MypyVersion.VERSION = Decimal(version)

    return ExamplePlugin
