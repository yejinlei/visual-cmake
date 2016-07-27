#coding:UTF-8
from pyparsing import *

#保留字
key_endfunction = Keyword("endfunction",caseless=True)
key_function = Keyword("function",caseless=True)
key_elseif =  Keyword("elseif",caseless=True)
key_else = Keyword("else",caseless=True)
key_endif =  Keyword("endif",caseless=True)
key_if =  Keyword("if",caseless=True)
key_endmacro = Keyword("endmacro",caseless=True)
key_macro =  Keyword("macro",caseless=True)
key_endforeach =  Keyword("endforeach",caseless=True)
key_foreach =  Keyword("foreach",caseless=True)
key_endwhile =  Keyword("endwhile",caseless=True)
key_while =  Keyword("while",caseless=True)