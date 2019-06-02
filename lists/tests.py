#testes de unidade são aqueles que testam o sistema do lado do programador

from django.test import TestCase

class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.assertEqual(1+1,3)
