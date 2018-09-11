import os
import subprocess
from subprocess import PIPE
from subprocess import run

"""
Copyright (C) 2018 Stella Zevio
stella.zevio@lipn.univ-paris13.fr

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

def PDFParser(file):
    """ Parse PDF file with Apache Tika parser in order to get its textual content
    Parameter :
    textfile -- file to parse
    Return :
    content -- file content
    """
    localpath = os.path.dirname(os.path.realpath(__file__))+'/' # local path
    tikapath = localpath+'tika-app-1.18.jar' # path to Apache Tika jar file
    command = ['java', '-jar', tikapath, '-t', file] # command line for Apache Tika parser
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True) # run command
    content = result.stdout # get command line output as file content
    return content
