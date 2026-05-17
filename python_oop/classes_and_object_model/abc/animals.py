#!/usr/bin/env python3
"""Abstract Animal class and concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
	"""Base abstract animal class."""

	@abstractmethod
	def sound(self):
		"""Return the animal sound."""


class Dog(Animal):
	"""Dog implementation of Animal."""

	def sound(self):
		return "Bark"


class Cat(Animal):
	"""Cat implementation of Animal."""

	def sound(self):
		return "Meow"
