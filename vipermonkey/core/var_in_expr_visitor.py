"""
ViperMonkey: Visitor for collecting the names declared variables.

ViperMonkey is a specialized engine to parse, analyze and interpret Microsoft
VBA macros (Visual Basic for Applications), mainly for malware analysis.

Author: Philippe Lagadec - http://www.decalage.info
License: BSD, see source code or documentation

Project Repository:
https://github.com/decalage2/ViperMonkey
"""

# === LICENSE ==================================================================

# ViperMonkey is copyright (c) 2015-2016 Philippe Lagadec (http://www.decalage.info)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from visitor import *
from statements import *

class var_in_expr_visitor(visitor):
    """
    Get the names of all variables that appear in an expression.
    """

    def __init__(self, context=None):
        self.variables = set()
        self.visited = set()
        self.context = context
    
    def visit(self, item):
        from expressions import SimpleNameExpression
        from expressions import Function_Call
        from vba_object import VbaLibraryFunc
        from vba_object import VBA_Object

        # Already looked at this?
        if (item in self.visited):
            return False
        self.visited.add(item)

        # Simple variable?
        if (isinstance(item, SimpleNameExpression)):
            self.variables.add(str(item.name))

        # Array access?
        if (("Function_Call" in str(type(item))) and (self.context is not None)):

            # Is this an array or function?
            if (self.context.contains(item.name)):
                ref = self.context.get(item.name)
                if (isinstance(ref, list) or isinstance(ref, str)):
                    self.variables.add(str(item.name))
                    
        return True
