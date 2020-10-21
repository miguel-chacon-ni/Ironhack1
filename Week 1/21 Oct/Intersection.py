#!/usr/bin/env python
# coding: utf-8

# ## Functions

# A function is a 'device' that groups a set of statements so they can be run more than once in a program.
# 
# They let us specify parameters (arguments) as inputs.
# 
# **Why use functions?**
# 
# - _Maximizing code re-use and minimizing redundancy:_
# 
# Functions allow us to group operations in a single place (with a single name) and call it many times, we have to write less code. 'Packing' your code into functions is generally a way to make it more useful, portable and easy to automatize and re-use.
# 
# - _Procedural decomposition:_
# 
# Functions help you split programs into parts that have a meaning of their own. The same way making a pizza can be splitted into 'making the dough', 'adding topings', 'baking', your programs should be split into chunks (functions), each one with its sub-tasks.

# Important: 
# 
# - diference between 'print' and 'return' in a function.
# 
# - scope rules
# 
# - argument passing
# 

# ### Coding functions
# 
# - **def** is executable code. We have to execute the code for the function to exist. def creates an object and assigns it to a name. A new function object is created and assigned to the function's name.
# 
# - **lambda** creates an object but returns it as a result. With lambda expressions we can create functions and obtain their output in a single line.
# 
# - **return** sends a result back to the caller
# 
# - **global** and **non-local** adjust the scope of variables. By default, all names assigned in a function are local to that function and exist only while the function runs. To assign a name in the enclosing module, functions need to list it in a global statement. More generally, names are always looked up in scopes—places where variables are stored —and assignments bind names to scopes.
# 
# - **arguments** are passed by position, unless you specify otherwise
# 
# 

# #### def Statement
# 
# `def name(arg1, arg2, ... argN):
#     ...
#     return value`

# Because function definition happens at runtime, there’s nothing special about the function name. What’s important is the object to which it refers:
# 
# 
# `def func():            # Define func this way
# othername = func           # Assign function object
# othername()                # Call func again`
# 

# #### Defining a function to divide 2 numbers:

# In[11]:





# #### Calling the function
# 
# Unless specified otherwise, arguments are passed in order

# In[12]:





# Switch the order of the arguments:

# In[ ]:





# Set a default value for an argument:

# In[5]:


# an argument with a default doesn't need to be passed


# Arguments are not restricted to an object type (we never declare the types od variables, arguments or return values)

# In[ ]:





# What if we really want to constrain the function to only integers

# In[ ]:





# Testing for types is not a common practice. Embrace python's flexibility!

# What if we use print instead of return?

# In[29]:


def intersect(seq1, seq2):
    str(seq1) + str(seq2)
    print(str(seq1) +"_"+ str(seq2))
intersect(1,2)
list=str(seq1) + "_"+ str(seq2)


# #### Build a function to return the intersection of two sets

# In[49]:


# Build a function to return the intersection of two sets
def intersect(seq1, seq2):
    list=[]
    for x in seq1:
        if x in seq2:
            list.append(x)
    return(list)
        


# In[50]:


# test your function
small_primes = (1, 2, 3, 5, 7, 11, 13)
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
intersect(small_primes, fibonacci)


# In[8]:


# Should work with strings as well
Javi = "Javi"
Avión = "Avión"


# ### Modules
# 
# Convert this function into a module and import it from another notebook.

# ### Scopes
# 
# #### where's the variable res?
# 
# It is a local variable: a name that is visible only to code inside the function def and that exists only while the function runs. In fact, because all names assigned in any way inside a function are classified as local variables by default, nearly all the names in intersect are local variables:
# 
# - res is obviously assigned, so it is a local variable.
# 
# - Arguments are passed by assignment, so seq1 and seq2 are, too.
# 
# - The for loop assigns items to a variable, so the name x is also local.
# 
# When you use a name in a program, Python creates, changes, or looks up the name in what is known as a namespace—a place where names live. When we talk about the search for a name’s value in relation to code, the term scope refers to a namespace: that is, the location of a name’s assignment in your source code determines the scope of the name’s visibility to your code.
# 
# The place where you assign a name in your source code determines the namespace it will live in, and hence its scope of visibility.
# 
# - Names assigned inside a def can only be seen by the code within that def. You cannot even refer to such names from outside the function.
# 
# - Names assigned inside a def do not clash with variables outside the def, even if the same names are used elsewhere. A name X assigned outside a given def (i.e., in a different def or at the top level of a module file) is a completely different variable from a name X assigned inside that def.

# In[28]:


x = 1990

def func():
    x = 2020
    print(x)
    
print(x)
func()


# - If you need to assign a name that lives at the top level of the module enclosing the function, you can do so by declaring it in a global statement inside the function. 
# 
# - If you need to assign a name that lives in an enclosing def, as of Python 3.X you can do so by declaring it in a nonlocal statement.

# Type of assignment within a function classifies a name as local. This includes = statements, module names in import, function names in def, function argument names, and so on. If you assign a name in any way within a def, it will become a local to that function by default.
# 
# In-place changes to objects do not classify names as locals; only actual name assignments do. 
# 
# For instance, if the name L is assigned to a list at the top level of a module, a statement L = X within a function will classify L as a local, but L.append(X) will not. In the latter case, we are changing the list object that L references, not L itself—L is found in the global scope as usual, and Python happily modifies it without requiring a global (or nonlocal) declaration. As usual, it helps to keep the distinction between names and objects clear: changing an object is not an assignment to a name.

# In[19]:


L = [1, 2, 3]

def append4():
    L.append(4)
    return L

append4()


# In[20]:


L


# In[11]:


L = [1, 2, 3]

def transform_L_into_X():
    X = "This is X"
    L = X
    return L

transform_L_into_X()


# In[22]:


L


# #### The global statement

# In[82]:


X = 88                         # Global X

def func():
    global X
    X = 99                     # Global X: outside def

func()
print(X)                       # Prints 99


# Minimize globals! What is the value of x here? It depends on where you ask during running time, and that's confusing and prone to errors.

# Some more tips for using functions:
# 
# - each function should have a single, unified purpose.
# 
# - each function should be relatively small

# ### Lambda functions

# The lambda tends to intimidate people more than it should. This reaction seems to stem from the name “lambda” itself—a name that comes from the Lisp language, which got it from lambda calculus, which is a form of symbolic logic. 
# 
# It's an **anonymous function**. It's an expression that creates a function, but does not assign it to any name.
# 
# It can only contain a single expression, not a block of statements.
# 

# 
