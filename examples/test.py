#!/usr/bin/python

import sealang

import clang
from clang import cindex

buf = """
#define VALUE_ONE 1

int test(int argc)
{
  return argc > VALUE_ONE;
}
"""

clang.cindex.Config.set_library_file("/usr/lib/llvm-6.0/lib/libclang.so")
idx = cindex.Index.create()
tu = idx.parse(path="t.c", unsaved_files=[("t.c", buf)])

# Get the function
f = list(tu.cursor.get_children())[0]
# Get the compound statement
l = list(f.get_children())
# Get the return statement
children = list(l[1].get_children())
# Get the binary operator
op = list(children[0].get_children())[0]
# Print the kind
print("Binary operator?", op.binary_operator)
# Get the literal
int_value = list(op.get_children())[1]
# And print the literal value for it
print("Literal?", int_value.literal)
