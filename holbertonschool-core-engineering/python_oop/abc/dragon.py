#!/usr/bin/env python3
"""Mixin-based dragon example."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon with swimming and flying abilities."""

    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
