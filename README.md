# pcu_pdf (Apache Tika parser for PCU project)

PDF parser component (Apache Tika) for PCU project.
From the path of a PDF file, get its textual content.

[Check PCU project][pcu].

[pcu]: https://github.com/zevio/pcu_core

----

## Usage in another project

If you wish to import this module in another Python project, please install it :

`pip install pcu-pdf`

Then, add this import line at the beginning of your Python file :

`from pcu_pdf import pcu_pdf`

You can now use pcu_pdf's functions, for example :

`pcu_pdf.PDFParser("path/to/pdf/file")`

## Test

To test your installation, go to pcu_pdf/ directory and execute the Makefile with the following command line : 

`make test`
