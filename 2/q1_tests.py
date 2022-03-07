import unittest
from q1 import doc_to_html


class test_doc_to_html(unittest.TestCase):
    def test_m1(self):
        with open('m1_doc_actual.html', 'r') as f1:
            expected = f1.read()
        doc_to_html('homeworkmodule.py', 'm1_doc_expected.html')
        with open('m1_doc_expected.html', 'r') as f2:
            actual = f2.read()
        self.assertEqual(expected, actual)

    def test_m2(self):
        with open('m2_doc_actual.html', 'r') as f1:
            expected = f1.read()
        doc_to_html('anothermodule.py', 'm2_doc_expected.html')
        with open('m2_doc_expected.html', 'r') as f2:
            actual = f2.read()
        self.assertEqual(expected, actual)

