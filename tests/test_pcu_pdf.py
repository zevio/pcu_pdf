import unittest

from pcu_pdf.pcu_pdf import PDFParser

class test_pcu_pdf(unittest.TestCase):

	def test_PDFParser(self):
		self.assertIn('Apache Tika is a PDF parser', PDFParser("data/test.pdf"))

if __name__ == '__main__':
	unittest.main()