'''Wrapper for edk.h

Generated with:
J:\home\eperfa\Synetiq\ctypesgen\ctypesgen.py -a -l edk.dll -o edk.py edk.h edkErrorCode.h EmoStateDLL.h glut.h

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["edk.dll"] = load_library("edk.dll")

# 1 libraries
# End libraries

# No modules

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 36
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memchr'):
        continue
    memchr = _lib.memchr
    memchr.argtypes = [POINTER(None), c_int, c_size_t]
    memchr.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 37
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memcmp'):
        continue
    memcmp = _lib.memcmp
    memcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 38
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memcpy'):
        continue
    memcpy = _lib.memcpy
    memcpy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcpy.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 39
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memmove'):
        continue
    memmove = _lib.memmove
    memmove.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memmove.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 40
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memset'):
        continue
    memset = _lib.memset
    memset.argtypes = [POINTER(None), c_int, c_size_t]
    memset.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 41
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcat'):
        continue
    strcat = _lib.strcat
    strcat.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strcat.restype = ReturnString
    else:
        strcat.restype = String
        strcat.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 42
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strchr'):
        continue
    strchr = _lib.strchr
    strchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strchr.restype = ReturnString
    else:
        strchr.restype = String
        strchr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 43
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcmp'):
        continue
    strcmp = _lib.strcmp
    strcmp.argtypes = [String, String]
    strcmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 44
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcoll'):
        continue
    strcoll = _lib.strcoll
    strcoll.argtypes = [String, String]
    strcoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 45
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcpy'):
        continue
    strcpy = _lib.strcpy
    strcpy.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strcpy.restype = ReturnString
    else:
        strcpy.restype = String
        strcpy.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 46
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcspn'):
        continue
    strcspn = _lib.strcspn
    strcspn.argtypes = [String, String]
    strcspn.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 47
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strerror'):
        continue
    strerror = _lib.strerror
    strerror.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strerror.restype = ReturnString
    else:
        strerror.restype = String
        strerror.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 49
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strlen'):
        continue
    strlen = _lib.strlen
    strlen.argtypes = [String]
    strlen.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 50
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strncat'):
        continue
    strncat = _lib.strncat
    strncat.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strncat.restype = ReturnString
    else:
        strncat.restype = String
        strncat.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 51
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strncmp'):
        continue
    strncmp = _lib.strncmp
    strncmp.argtypes = [String, String, c_size_t]
    strncmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 52
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strncpy'):
        continue
    strncpy = _lib.strncpy
    strncpy.argtypes = [String, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strncpy.restype = ReturnString
    else:
        strncpy.restype = String
        strncpy.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 53
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strpbrk'):
        continue
    strpbrk = _lib.strpbrk
    strpbrk.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strpbrk.restype = ReturnString
    else:
        strpbrk.restype = String
        strpbrk.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 54
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strrchr'):
        continue
    strrchr = _lib.strrchr
    strrchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strrchr.restype = ReturnString
    else:
        strrchr.restype = String
        strrchr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 55
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strspn'):
        continue
    strspn = _lib.strspn
    strspn.argtypes = [String, String]
    strspn.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 56
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strstr'):
        continue
    strstr = _lib.strstr
    strstr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strstr.restype = ReturnString
    else:
        strstr.restype = String
        strstr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 57
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strtok'):
        continue
    strtok = _lib.strtok
    strtok.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strtok.restype = ReturnString
    else:
        strtok.restype = String
        strtok.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 58
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strxfrm'):
        continue
    strxfrm = _lib.strxfrm
    strxfrm.argtypes = [String, String, c_size_t]
    strxfrm.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 64
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strerror'):
        continue
    _strerror = _lib._strerror
    _strerror.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        _strerror.restype = ReturnString
    else:
        _strerror.restype = String
        _strerror.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 65
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_memccpy'):
        continue
    _memccpy = _lib._memccpy
    _memccpy.argtypes = [POINTER(None), POINTER(None), c_int, c_size_t]
    _memccpy.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 66
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_memicmp'):
        continue
    _memicmp = _lib._memicmp
    _memicmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    _memicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 67
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strdup'):
        continue
    _strdup = _lib._strdup
    _strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        _strdup.restype = ReturnString
    else:
        _strdup.restype = String
        _strdup.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 68
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strcmpi'):
        continue
    _strcmpi = _lib._strcmpi
    _strcmpi.argtypes = [String, String]
    _strcmpi.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 69
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_stricmp'):
        continue
    _stricmp = _lib._stricmp
    _stricmp.argtypes = [String, String]
    _stricmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 70
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_stricoll'):
        continue
    _stricoll = _lib._stricoll
    _stricoll.argtypes = [String, String]
    _stricoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 71
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strlwr'):
        continue
    _strlwr = _lib._strlwr
    _strlwr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        _strlwr.restype = ReturnString
    else:
        _strlwr.restype = String
        _strlwr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 72
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strnicmp'):
        continue
    _strnicmp = _lib._strnicmp
    _strnicmp.argtypes = [String, String, c_size_t]
    _strnicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 73
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strnset'):
        continue
    _strnset = _lib._strnset
    _strnset.argtypes = [String, c_int, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        _strnset.restype = ReturnString
    else:
        _strnset.restype = String
        _strnset.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 74
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strrev'):
        continue
    _strrev = _lib._strrev
    _strrev.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        _strrev.restype = ReturnString
    else:
        _strrev.restype = String
        _strrev.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 75
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strset'):
        continue
    _strset = _lib._strset
    _strset.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        _strset.restype = ReturnString
    else:
        _strset.restype = String
        _strset.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 76
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strupr'):
        continue
    _strupr = _lib._strupr
    _strupr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        _strupr.restype = ReturnString
    else:
        _strupr.restype = String
        _strupr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 77
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_swab'):
        continue
    _swab = _lib._swab
    _swab.argtypes = [String, String, c_size_t]
    _swab.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 80
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strncoll'):
        continue
    _strncoll = _lib._strncoll
    _strncoll.argtypes = [String, String, c_size_t]
    _strncoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 81
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_strnicoll'):
        continue
    _strnicoll = _lib._strnicoll
    _strnicoll.argtypes = [String, String, c_size_t]
    _strnicoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 90
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memccpy'):
        continue
    memccpy = _lib.memccpy
    memccpy.argtypes = [POINTER(None), POINTER(None), c_int, c_size_t]
    memccpy.restype = POINTER(None)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 91
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'memicmp'):
        continue
    memicmp = _lib.memicmp
    memicmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 92
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strdup'):
        continue
    strdup = _lib.strdup
    strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strdup.restype = ReturnString
    else:
        strdup.restype = String
        strdup.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 93
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcmpi'):
        continue
    strcmpi = _lib.strcmpi
    strcmpi.argtypes = [String, String]
    strcmpi.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 94
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'stricmp'):
        continue
    stricmp = _lib.stricmp
    stricmp.argtypes = [String, String]
    stricmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 95
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strcasecmp'):
        continue
    strcasecmp = _lib.strcasecmp
    strcasecmp.argtypes = [String, String]
    strcasecmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 101
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'stricoll'):
        continue
    stricoll = _lib.stricoll
    stricoll.argtypes = [String, String]
    stricoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 102
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strlwr'):
        continue
    strlwr = _lib.strlwr
    strlwr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strlwr.restype = ReturnString
    else:
        strlwr.restype = String
        strlwr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strnicmp'):
        continue
    strnicmp = _lib.strnicmp
    strnicmp.argtypes = [String, String, c_size_t]
    strnicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 104
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strncasecmp'):
        continue
    strncasecmp = _lib.strncasecmp
    strncasecmp.argtypes = [String, String, c_size_t]
    strncasecmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 110
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strnset'):
        continue
    strnset = _lib.strnset
    strnset.argtypes = [String, c_int, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strnset.restype = ReturnString
    else:
        strnset.restype = String
        strnset.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strrev'):
        continue
    strrev = _lib.strrev
    strrev.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strrev.restype = ReturnString
    else:
        strrev.restype = String
        strrev.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 112
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strset'):
        continue
    strset = _lib.strset
    strset.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strset.restype = ReturnString
    else:
        strset.restype = String
        strset.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 113
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'strupr'):
        continue
    strupr = _lib.strupr
    strupr.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strupr.restype = ReturnString
    else:
        strupr.restype = String
        strupr.errcheck = ReturnString
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 115
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'swab'):
        continue
    swab = _lib.swab
    swab.argtypes = [String, String, c_size_t]
    swab.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscat'):
        continue
    wcscat = _lib.wcscat
    wcscat.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscat.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcschr'):
        continue
    wcschr = _lib.wcschr
    wcschr.argtypes = [POINTER(c_wchar), c_wchar]
    wcschr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 128
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscmp'):
        continue
    wcscmp = _lib.wcscmp
    wcscmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 129
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscoll'):
        continue
    wcscoll = _lib.wcscoll
    wcscoll.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 130
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscpy'):
        continue
    wcscpy = _lib.wcscpy
    wcscpy.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscpy.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 131
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscspn'):
        continue
    wcscspn = _lib.wcscspn
    wcscspn.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscspn.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 133
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcslen'):
        continue
    wcslen = _lib.wcslen
    wcslen.argtypes = [POINTER(c_wchar)]
    wcslen.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 134
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsncat'):
        continue
    wcsncat = _lib.wcsncat
    wcsncat.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    wcsncat.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 135
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsncmp'):
        continue
    wcsncmp = _lib.wcsncmp
    wcsncmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    wcsncmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 136
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsncpy'):
        continue
    wcsncpy = _lib.wcsncpy
    wcsncpy.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    wcsncpy.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 137
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcspbrk'):
        continue
    wcspbrk = _lib.wcspbrk
    wcspbrk.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcspbrk.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 138
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsrchr'):
        continue
    wcsrchr = _lib.wcsrchr
    wcsrchr.argtypes = [POINTER(c_wchar), c_wchar]
    wcsrchr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 139
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsspn'):
        continue
    wcsspn = _lib.wcsspn
    wcsspn.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcsspn.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 140
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsstr'):
        continue
    wcsstr = _lib.wcsstr
    wcsstr.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcsstr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 141
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcstok'):
        continue
    wcstok = _lib.wcstok
    wcstok.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcstok.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 142
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsxfrm'):
        continue
    wcsxfrm = _lib.wcsxfrm
    wcsxfrm.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    wcsxfrm.restype = c_size_t
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 152
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsdup'):
        continue
    _wcsdup = _lib._wcsdup
    _wcsdup.argtypes = [POINTER(c_wchar)]
    _wcsdup.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 153
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsicmp'):
        continue
    _wcsicmp = _lib._wcsicmp
    _wcsicmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    _wcsicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 154
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsicoll'):
        continue
    _wcsicoll = _lib._wcsicoll
    _wcsicoll.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    _wcsicoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 155
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcslwr'):
        continue
    _wcslwr = _lib._wcslwr
    _wcslwr.argtypes = [POINTER(c_wchar)]
    _wcslwr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 156
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsnicmp'):
        continue
    _wcsnicmp = _lib._wcsnicmp
    _wcsnicmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    _wcsnicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 157
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsnset'):
        continue
    _wcsnset = _lib._wcsnset
    _wcsnset.argtypes = [POINTER(c_wchar), c_wchar, c_size_t]
    _wcsnset.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 158
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsrev'):
        continue
    _wcsrev = _lib._wcsrev
    _wcsrev.argtypes = [POINTER(c_wchar)]
    _wcsrev.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 159
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsset'):
        continue
    _wcsset = _lib._wcsset
    _wcsset.argtypes = [POINTER(c_wchar), c_wchar]
    _wcsset.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 160
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsupr'):
        continue
    _wcsupr = _lib._wcsupr
    _wcsupr.argtypes = [POINTER(c_wchar)]
    _wcsupr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 163
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsncoll'):
        continue
    _wcsncoll = _lib._wcsncoll
    _wcsncoll.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    _wcsncoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 164
for _lib in _libs.itervalues():
    if not hasattr(_lib, '_wcsnicoll'):
        continue
    _wcsnicoll = _lib._wcsnicoll
    _wcsnicoll.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    _wcsnicoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 173
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcscmpi'):
        continue
    wcscmpi = _lib.wcscmpi
    wcscmpi.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcscmpi.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 179
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsdup'):
        continue
    wcsdup = _lib.wcsdup
    wcsdup.argtypes = [POINTER(c_wchar)]
    wcsdup.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 180
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsicmp'):
        continue
    wcsicmp = _lib.wcsicmp
    wcsicmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcsicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 181
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsicoll'):
        continue
    wcsicoll = _lib.wcsicoll
    wcsicoll.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
    wcsicoll.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 182
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcslwr'):
        continue
    wcslwr = _lib.wcslwr
    wcslwr.argtypes = [POINTER(c_wchar)]
    wcslwr.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 183
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsnicmp'):
        continue
    wcsnicmp = _lib.wcsnicmp
    wcsnicmp.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_size_t]
    wcsnicmp.restype = c_int
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 184
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsnset'):
        continue
    wcsnset = _lib.wcsnset
    wcsnset.argtypes = [POINTER(c_wchar), c_wchar, c_size_t]
    wcsnset.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 185
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsrev'):
        continue
    wcsrev = _lib.wcsrev
    wcsrev.argtypes = [POINTER(c_wchar)]
    wcsrev.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 186
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsset'):
        continue
    wcsset = _lib.wcsset
    wcsset.argtypes = [POINTER(c_wchar), c_wchar]
    wcsset.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 187
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'wcsupr'):
        continue
    wcsupr = _lib.wcsupr
    wcsupr.argtypes = [POINTER(c_wchar)]
    wcsupr.restype = POINTER(c_wchar)
    break

_off_t = c_long # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 52

off_t = _off_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 55

_dev_t = c_uint # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 63

dev_t = _dev_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 69

_ino_t = c_short # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 76

ino_t = _ino_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 79

_pid_t = c_int # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 86

pid_t = _pid_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 89

_mode_t = c_ushort # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 96

mode_t = _mode_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 99

_sigset_t = c_int # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 106

sigset_t = _sigset_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 109

_ssize_t = c_long # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 115

ssize_t = _ssize_t # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 118

fpos64_t = c_longlong # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 124

off64_t = c_longlong # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 129

useconds_t = c_uint # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/sys/types.h: 133

EmoStateHandle = POINTER(None) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 42

enum_EE_EmotivSuite_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 53

EE_EXPRESSIV = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 53

EE_AFFECTIV = (EE_EXPRESSIV + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 53

EE_COGNITIV = (EE_AFFECTIV + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 53

EE_EmotivSuite_t = enum_EE_EmotivSuite_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 53

enum_EE_ExpressivAlgo_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_NEUTRAL = 1 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_BLINK = 2 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_WINK_LEFT = 4 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_WINK_RIGHT = 8 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_HORIEYE = 16 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_EYEBROW = 32 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_FURROW = 64 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_SMILE = 128 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_CLENCH = 256 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_LAUGH = 512 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_SMIRK_LEFT = 1024 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EXP_SMIRK_RIGHT = 2048 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

EE_ExpressivAlgo_t = enum_EE_ExpressivAlgo_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 73

enum_EE_AffectivAlgo_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

AFF_EXCITEMENT = 1 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

AFF_MEDITATION = 2 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

AFF_FRUSTRATION = 4 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

AFF_ENGAGEMENT_BOREDOM = 8 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

EE_AffectivAlgo_t = enum_EE_AffectivAlgo_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 85

enum_EE_CognitivAction_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_NEUTRAL = 1 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_PUSH = 2 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_PULL = 4 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_LIFT = 8 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_DROP = 16 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_LEFT = 32 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_RIGHT = 64 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_LEFT = 128 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_RIGHT = 256 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_CLOCKWISE = 512 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_COUNTER_CLOCKWISE = 1024 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_FORWARDS = 2048 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_ROTATE_REVERSE = 4096 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

COG_DISAPPEAR = 8192 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

EE_CognitivAction_t = enum_EE_CognitivAction_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 107

enum_EE_SignalStrength_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 116

NO_SIGNAL = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 116

BAD_SIGNAL = (NO_SIGNAL + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 116

GOOD_SIGNAL = (BAD_SIGNAL + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 116

EE_SignalStrength_t = enum_EE_SignalStrength_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 116

enum_EE_InputChannels_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_CMS = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_DRL = (EE_CHAN_CMS + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_FP1 = (EE_CHAN_DRL + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_AF3 = (EE_CHAN_FP1 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_F7 = (EE_CHAN_AF3 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_F3 = (EE_CHAN_F7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_FC5 = (EE_CHAN_F3 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_T7 = (EE_CHAN_FC5 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_P7 = (EE_CHAN_T7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_O1 = (EE_CHAN_P7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_O2 = (EE_CHAN_O1 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_P8 = (EE_CHAN_O2 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_T8 = (EE_CHAN_P8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_FC6 = (EE_CHAN_T8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_F4 = (EE_CHAN_FC6 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_F8 = (EE_CHAN_F4 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_AF4 = (EE_CHAN_F8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_CHAN_FP2 = (EE_CHAN_AF4 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

EE_InputChannels_t = enum_EE_InputChannels_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 128

enum_EE_EEG_ContactQuality_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EEG_CQ_NO_SIGNAL = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EEG_CQ_VERY_BAD = (EEG_CQ_NO_SIGNAL + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EEG_CQ_POOR = (EEG_CQ_VERY_BAD + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EEG_CQ_FAIR = (EEG_CQ_POOR + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EEG_CQ_GOOD = (EEG_CQ_FAIR + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

EE_EEG_ContactQuality_t = enum_EE_EEG_ContactQuality_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 138

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 151
if hasattr(_libs['edk.dll'], 'ES_Create'):
    ES_Create = _libs['edk.dll'].ES_Create
    ES_Create.argtypes = []
    ES_Create.restype = EmoStateHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 161
if hasattr(_libs['edk.dll'], 'ES_Free'):
    ES_Free = _libs['edk.dll'].ES_Free
    ES_Free.argtypes = [EmoStateHandle]
    ES_Free.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 169
if hasattr(_libs['edk.dll'], 'ES_Init'):
    ES_Init = _libs['edk.dll'].ES_Init
    ES_Init.argtypes = [EmoStateHandle]
    ES_Init.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 181
if hasattr(_libs['edk.dll'], 'ES_GetTimeFromStart'):
    ES_GetTimeFromStart = _libs['edk.dll'].ES_GetTimeFromStart
    ES_GetTimeFromStart.argtypes = [EmoStateHandle]
    ES_GetTimeFromStart.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 192
if hasattr(_libs['edk.dll'], 'ES_GetHeadsetOn'):
    ES_GetHeadsetOn = _libs['edk.dll'].ES_GetHeadsetOn
    ES_GetHeadsetOn.argtypes = [EmoStateHandle]
    ES_GetHeadsetOn.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 201
if hasattr(_libs['edk.dll'], 'ES_GetNumContactQualityChannels'):
    ES_GetNumContactQualityChannels = _libs['edk.dll'].ES_GetNumContactQualityChannels
    ES_GetNumContactQualityChannels.argtypes = [EmoStateHandle]
    ES_GetNumContactQualityChannels.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 212
if hasattr(_libs['edk.dll'], 'ES_GetContactQuality'):
    ES_GetContactQuality = _libs['edk.dll'].ES_GetContactQuality
    ES_GetContactQuality.argtypes = [EmoStateHandle, c_int]
    ES_GetContactQuality.restype = EE_EEG_ContactQuality_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 232
if hasattr(_libs['edk.dll'], 'ES_GetContactQualityFromAllChannels'):
    ES_GetContactQualityFromAllChannels = _libs['edk.dll'].ES_GetContactQualityFromAllChannels
    ES_GetContactQualityFromAllChannels.argtypes = [EmoStateHandle, POINTER(EE_EEG_ContactQuality_t), c_size_t]
    ES_GetContactQualityFromAllChannels.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 241
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsBlink'):
    ES_ExpressivIsBlink = _libs['edk.dll'].ES_ExpressivIsBlink
    ES_ExpressivIsBlink.argtypes = [EmoStateHandle]
    ES_ExpressivIsBlink.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 251
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLeftWink'):
    ES_ExpressivIsLeftWink = _libs['edk.dll'].ES_ExpressivIsLeftWink
    ES_ExpressivIsLeftWink.argtypes = [EmoStateHandle]
    ES_ExpressivIsLeftWink.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 261
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsRightWink'):
    ES_ExpressivIsRightWink = _libs['edk.dll'].ES_ExpressivIsRightWink
    ES_ExpressivIsRightWink.argtypes = [EmoStateHandle]
    ES_ExpressivIsRightWink.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 270
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsEyesOpen'):
    ES_ExpressivIsEyesOpen = _libs['edk.dll'].ES_ExpressivIsEyesOpen
    ES_ExpressivIsEyesOpen.argtypes = [EmoStateHandle]
    ES_ExpressivIsEyesOpen.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 280
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingUp'):
    ES_ExpressivIsLookingUp = _libs['edk.dll'].ES_ExpressivIsLookingUp
    ES_ExpressivIsLookingUp.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingUp.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 290
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingDown'):
    ES_ExpressivIsLookingDown = _libs['edk.dll'].ES_ExpressivIsLookingDown
    ES_ExpressivIsLookingDown.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingDown.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 300
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingLeft'):
    ES_ExpressivIsLookingLeft = _libs['edk.dll'].ES_ExpressivIsLookingLeft
    ES_ExpressivIsLookingLeft.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingLeft.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 310
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingRight'):
    ES_ExpressivIsLookingRight = _libs['edk.dll'].ES_ExpressivIsLookingRight
    ES_ExpressivIsLookingRight.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingRight.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 324
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyelidState'):
    ES_ExpressivGetEyelidState = _libs['edk.dll'].ES_ExpressivGetEyelidState
    ES_ExpressivGetEyelidState.argtypes = [EmoStateHandle, POINTER(c_float), POINTER(c_float)]
    ES_ExpressivGetEyelidState.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 345
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyeLocation'):
    ES_ExpressivGetEyeLocation = _libs['edk.dll'].ES_ExpressivGetEyeLocation
    ES_ExpressivGetEyeLocation.argtypes = [EmoStateHandle, POINTER(c_float), POINTER(c_float)]
    ES_ExpressivGetEyeLocation.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 355
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyebrowExtent'):
    ES_ExpressivGetEyebrowExtent = _libs['edk.dll'].ES_ExpressivGetEyebrowExtent
    ES_ExpressivGetEyebrowExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetEyebrowExtent.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 365
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetSmileExtent'):
    ES_ExpressivGetSmileExtent = _libs['edk.dll'].ES_ExpressivGetSmileExtent
    ES_ExpressivGetSmileExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetSmileExtent.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 375
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetClenchExtent'):
    ES_ExpressivGetClenchExtent = _libs['edk.dll'].ES_ExpressivGetClenchExtent
    ES_ExpressivGetClenchExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetClenchExtent.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 386
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetUpperFaceAction'):
    ES_ExpressivGetUpperFaceAction = _libs['edk.dll'].ES_ExpressivGetUpperFaceAction
    ES_ExpressivGetUpperFaceAction.argtypes = [EmoStateHandle]
    ES_ExpressivGetUpperFaceAction.restype = EE_ExpressivAlgo_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 396
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetUpperFaceActionPower'):
    ES_ExpressivGetUpperFaceActionPower = _libs['edk.dll'].ES_ExpressivGetUpperFaceActionPower
    ES_ExpressivGetUpperFaceActionPower.argtypes = [EmoStateHandle]
    ES_ExpressivGetUpperFaceActionPower.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 406
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetLowerFaceAction'):
    ES_ExpressivGetLowerFaceAction = _libs['edk.dll'].ES_ExpressivGetLowerFaceAction
    ES_ExpressivGetLowerFaceAction.argtypes = [EmoStateHandle]
    ES_ExpressivGetLowerFaceAction.restype = EE_ExpressivAlgo_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 416
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetLowerFaceActionPower'):
    ES_ExpressivGetLowerFaceActionPower = _libs['edk.dll'].ES_ExpressivGetLowerFaceActionPower
    ES_ExpressivGetLowerFaceActionPower.argtypes = [EmoStateHandle]
    ES_ExpressivGetLowerFaceActionPower.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 427
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsActive'):
    ES_ExpressivIsActive = _libs['edk.dll'].ES_ExpressivIsActive
    ES_ExpressivIsActive.argtypes = [EmoStateHandle, EE_ExpressivAlgo_t]
    ES_ExpressivIsActive.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 437
if hasattr(_libs['edk.dll'], 'ES_AffectivGetExcitementLongTermScore'):
    ES_AffectivGetExcitementLongTermScore = _libs['edk.dll'].ES_AffectivGetExcitementLongTermScore
    ES_AffectivGetExcitementLongTermScore.argtypes = [EmoStateHandle]
    ES_AffectivGetExcitementLongTermScore.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 447
if hasattr(_libs['edk.dll'], 'ES_AffectivGetExcitementShortTermScore'):
    ES_AffectivGetExcitementShortTermScore = _libs['edk.dll'].ES_AffectivGetExcitementShortTermScore
    ES_AffectivGetExcitementShortTermScore.argtypes = [EmoStateHandle]
    ES_AffectivGetExcitementShortTermScore.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 458
if hasattr(_libs['edk.dll'], 'ES_AffectivIsActive'):
    ES_AffectivIsActive = _libs['edk.dll'].ES_AffectivIsActive
    ES_AffectivIsActive.argtypes = [EmoStateHandle, EE_AffectivAlgo_t]
    ES_AffectivIsActive.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 466
if hasattr(_libs['edk.dll'], 'ES_AffectivGetMeditationScore'):
    ES_AffectivGetMeditationScore = _libs['edk.dll'].ES_AffectivGetMeditationScore
    ES_AffectivGetMeditationScore.argtypes = [EmoStateHandle]
    ES_AffectivGetMeditationScore.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 474
if hasattr(_libs['edk.dll'], 'ES_AffectivGetFrustrationScore'):
    ES_AffectivGetFrustrationScore = _libs['edk.dll'].ES_AffectivGetFrustrationScore
    ES_AffectivGetFrustrationScore.argtypes = [EmoStateHandle]
    ES_AffectivGetFrustrationScore.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 482
if hasattr(_libs['edk.dll'], 'ES_AffectivGetEngagementBoredomScore'):
    ES_AffectivGetEngagementBoredomScore = _libs['edk.dll'].ES_AffectivGetEngagementBoredomScore
    ES_AffectivGetEngagementBoredomScore.argtypes = [EmoStateHandle]
    ES_AffectivGetEngagementBoredomScore.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 493
if hasattr(_libs['edk.dll'], 'ES_CognitivGetCurrentAction'):
    ES_CognitivGetCurrentAction = _libs['edk.dll'].ES_CognitivGetCurrentAction
    ES_CognitivGetCurrentAction.argtypes = [EmoStateHandle]
    ES_CognitivGetCurrentAction.restype = EE_CognitivAction_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 503
if hasattr(_libs['edk.dll'], 'ES_CognitivGetCurrentActionPower'):
    ES_CognitivGetCurrentActionPower = _libs['edk.dll'].ES_CognitivGetCurrentActionPower
    ES_CognitivGetCurrentActionPower.argtypes = [EmoStateHandle]
    ES_CognitivGetCurrentActionPower.restype = c_float

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 511
if hasattr(_libs['edk.dll'], 'ES_CognitivIsActive'):
    ES_CognitivIsActive = _libs['edk.dll'].ES_CognitivIsActive
    ES_CognitivIsActive.argtypes = [EmoStateHandle]
    ES_CognitivIsActive.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 522
if hasattr(_libs['edk.dll'], 'ES_GetWirelessSignalStatus'):
    ES_GetWirelessSignalStatus = _libs['edk.dll'].ES_GetWirelessSignalStatus
    ES_GetWirelessSignalStatus.argtypes = [EmoStateHandle]
    ES_GetWirelessSignalStatus.restype = EE_SignalStrength_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 531
if hasattr(_libs['edk.dll'], 'ES_Copy'):
    ES_Copy = _libs['edk.dll'].ES_Copy
    ES_Copy.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_Copy.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 542
if hasattr(_libs['edk.dll'], 'ES_AffectivEqual'):
    ES_AffectivEqual = _libs['edk.dll'].ES_AffectivEqual
    ES_AffectivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_AffectivEqual.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 553
if hasattr(_libs['edk.dll'], 'ES_ExpressivEqual'):
    ES_ExpressivEqual = _libs['edk.dll'].ES_ExpressivEqual
    ES_ExpressivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_ExpressivEqual.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 564
if hasattr(_libs['edk.dll'], 'ES_CognitivEqual'):
    ES_CognitivEqual = _libs['edk.dll'].ES_CognitivEqual
    ES_CognitivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_CognitivEqual.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 578
if hasattr(_libs['edk.dll'], 'ES_EmoEngineEqual'):
    ES_EmoEngineEqual = _libs['edk.dll'].ES_EmoEngineEqual
    ES_EmoEngineEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_EmoEngineEqual.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 589
if hasattr(_libs['edk.dll'], 'ES_Equal'):
    ES_Equal = _libs['edk.dll'].ES_Equal
    ES_Equal.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_Equal.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 598
if hasattr(_libs['edk.dll'], 'ES_GetBatteryChargeLevel'):
    ES_GetBatteryChargeLevel = _libs['edk.dll'].ES_GetBatteryChargeLevel
    ES_GetBatteryChargeLevel.argtypes = [EmoStateHandle, POINTER(c_int), POINTER(c_int)]
    ES_GetBatteryChargeLevel.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 607
if hasattr(_libs['edk.dll'], 'ES_AffectivGetExcitementShortTermModelParams'):
    ES_AffectivGetExcitementShortTermModelParams = _libs['edk.dll'].ES_AffectivGetExcitementShortTermModelParams
    ES_AffectivGetExcitementShortTermModelParams.argtypes = [EmoStateHandle, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    ES_AffectivGetExcitementShortTermModelParams.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 616
if hasattr(_libs['edk.dll'], 'ES_AffectivGetMeditationModelParams'):
    ES_AffectivGetMeditationModelParams = _libs['edk.dll'].ES_AffectivGetMeditationModelParams
    ES_AffectivGetMeditationModelParams.argtypes = [EmoStateHandle, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    ES_AffectivGetMeditationModelParams.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 625
if hasattr(_libs['edk.dll'], 'ES_AffectivGetEngagementBoredomModelParams'):
    ES_AffectivGetEngagementBoredomModelParams = _libs['edk.dll'].ES_AffectivGetEngagementBoredomModelParams
    ES_AffectivGetEngagementBoredomModelParams.argtypes = [EmoStateHandle, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    ES_AffectivGetEngagementBoredomModelParams.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/EmoStateDLL.h: 634
if hasattr(_libs['edk.dll'], 'ES_AffectivGetFrustrationModelParams'):
    ES_AffectivGetFrustrationModelParams = _libs['edk.dll'].ES_AffectivGetFrustrationModelParams
    ES_AffectivGetFrustrationModelParams.argtypes = [EmoStateHandle, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    ES_AffectivGetFrustrationModelParams.restype = None

enum_EE_ExpressivThreshold_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 51

EXP_SENSITIVITY = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 51

EE_ExpressivThreshold_t = enum_EE_ExpressivThreshold_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 51

enum_EE_ExpressivTrainingControl_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_NONE = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_START = (EXP_NONE + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_ACCEPT = (EXP_START + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_REJECT = (EXP_ACCEPT + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_ERASE = (EXP_REJECT + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EXP_RESET = (EXP_ERASE + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

EE_ExpressivTrainingControl_t = enum_EE_ExpressivTrainingControl_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 56

enum_EE_ExpressivSignature_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 61

EXP_SIG_UNIVERSAL = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 61

EXP_SIG_TRAINED = (EXP_SIG_UNIVERSAL + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 61

EE_ExpressivSignature_t = enum_EE_ExpressivSignature_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 61

enum_EE_CognitivTrainingControl_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_NONE = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_START = (COG_NONE + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_ACCEPT = (COG_START + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_REJECT = (COG_ACCEPT + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_ERASE = (COG_REJECT + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

COG_RESET = (COG_ERASE + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

EE_CognitivTrainingControl_t = enum_EE_CognitivTrainingControl_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 66

EmoEngineEventHandle = POINTER(None) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 73

OptimizationParamHandle = POINTER(None) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 76

DataHandle = POINTER(None) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 78

enum_EE_Event_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_UnknownEvent = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_EmulatorError = 1 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_ReservedEvent = 2 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_UserAdded = 16 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_UserRemoved = 32 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_EmoStateUpdated = 64 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_ProfileEvent = 128 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_CognitivEvent = 256 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_ExpressivEvent = 512 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_InternalStateChanged = 1024 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_AllEvent = ((((((EE_UserAdded | EE_UserRemoved) | EE_EmoStateUpdated) | EE_ProfileEvent) | EE_CognitivEvent) | EE_ExpressivEvent) | EE_InternalStateChanged) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

EE_Event_t = enum_EE_Event_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 94

enum_EE_ExpressivEvent_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivNoEvent = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingStarted = (EE_ExpressivNoEvent + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingSucceeded = (EE_ExpressivTrainingStarted + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingFailed = (EE_ExpressivTrainingSucceeded + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingCompleted = (EE_ExpressivTrainingFailed + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingDataErased = (EE_ExpressivTrainingCompleted + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingRejected = (EE_ExpressivTrainingDataErased + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivTrainingReset = (EE_ExpressivTrainingRejected + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

EE_ExpressivEvent_t = enum_EE_ExpressivEvent_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 101

enum_EE_CognitivEvent_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivNoEvent = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingStarted = (EE_CognitivNoEvent + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingSucceeded = (EE_CognitivTrainingStarted + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingFailed = (EE_CognitivTrainingSucceeded + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingCompleted = (EE_CognitivTrainingFailed + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingDataErased = (EE_CognitivTrainingCompleted + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingRejected = (EE_CognitivTrainingDataErased + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivTrainingReset = (EE_CognitivTrainingRejected + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivAutoSamplingNeutralCompleted = (EE_CognitivTrainingReset + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivSignatureUpdated = (EE_CognitivAutoSamplingNeutralCompleted + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

EE_CognitivEvent_t = enum_EE_CognitivEvent_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 109

enum_EE_DataChannels_enum = c_int # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_COUNTER = 0 # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_INTERPOLATED = (ED_COUNTER + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_RAW_CQ = (ED_INTERPOLATED + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_AF3 = (ED_RAW_CQ + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_F7 = (ED_AF3 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_F3 = (ED_F7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_FC5 = (ED_F3 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_T7 = (ED_FC5 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_P7 = (ED_T7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_O1 = (ED_P7 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_O2 = (ED_O1 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_P8 = (ED_O2 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_T8 = (ED_P8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_FC6 = (ED_T8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_F4 = (ED_FC6 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_F8 = (ED_F4 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_AF4 = (ED_F8 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_GYROX = (ED_AF4 + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_GYROY = (ED_GYROX + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_TIMESTAMP = (ED_GYROY + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_ES_TIMESTAMP = (ED_TIMESTAMP + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_FUNC_ID = (ED_ES_TIMESTAMP + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_FUNC_VALUE = (ED_FUNC_ID + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_MARKER = (ED_FUNC_VALUE + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

ED_SYNC_SIGNAL = (ED_MARKER + 1) # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

EE_DataChannel_t = enum_EE_DataChannels_enum # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 118

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 128
class struct_InputSensorDescriptor_struct(Structure):
    pass

struct_InputSensorDescriptor_struct.__slots__ = [
    'channelId',
    'fExists',
    'pszLabel',
    'xLoc',
    'yLoc',
    'zLoc',
]
struct_InputSensorDescriptor_struct._fields_ = [
    ('channelId', EE_InputChannels_t),
    ('fExists', c_int),
    ('pszLabel', String),
    ('xLoc', c_double),
    ('yLoc', c_double),
    ('zLoc', c_double),
]

InputSensorDescriptor_t = struct_InputSensorDescriptor_struct # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 128

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 139
if hasattr(_libs['edk.dll'], 'EE_EngineConnect'):
    EE_EngineConnect = _libs['edk.dll'].EE_EngineConnect
    EE_EngineConnect.argtypes = [String]
    EE_EngineConnect.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 157
if hasattr(_libs['edk.dll'], 'EE_EngineRemoteConnect'):
    EE_EngineRemoteConnect = _libs['edk.dll'].EE_EngineRemoteConnect
    EE_EngineRemoteConnect.argtypes = [String, c_ushort]
    EE_EngineRemoteConnect.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 168
if hasattr(_libs['edk.dll'], 'EE_EngineDisconnect'):
    EE_EngineDisconnect = _libs['edk.dll'].EE_EngineDisconnect
    EE_EngineDisconnect.argtypes = []
    EE_EngineDisconnect.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 182
if hasattr(_libs['edk.dll'], 'EE_EnableDiagnostics'):
    EE_EnableDiagnostics = _libs['edk.dll'].EE_EnableDiagnostics
    EE_EnableDiagnostics.argtypes = [String, c_int, c_int]
    EE_EnableDiagnostics.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 190
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventCreate'):
    EE_EmoEngineEventCreate = _libs['edk.dll'].EE_EmoEngineEventCreate
    EE_EmoEngineEventCreate.argtypes = []
    EE_EmoEngineEventCreate.restype = EmoEngineEventHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 198
if hasattr(_libs['edk.dll'], 'EE_ProfileEventCreate'):
    EE_ProfileEventCreate = _libs['edk.dll'].EE_ProfileEventCreate
    EE_ProfileEventCreate.argtypes = []
    EE_ProfileEventCreate.restype = EmoEngineEventHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 206
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventFree'):
    EE_EmoEngineEventFree = _libs['edk.dll'].EE_EmoEngineEventFree
    EE_EmoEngineEventFree.argtypes = [EmoEngineEventHandle]
    EE_EmoEngineEventFree.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 214
if hasattr(_libs['edk.dll'], 'EE_EmoStateCreate'):
    EE_EmoStateCreate = _libs['edk.dll'].EE_EmoStateCreate
    EE_EmoStateCreate.argtypes = []
    EE_EmoStateCreate.restype = EmoStateHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 222
if hasattr(_libs['edk.dll'], 'EE_EmoStateFree'):
    EE_EmoStateFree = _libs['edk.dll'].EE_EmoStateFree
    EE_EmoStateFree.argtypes = [EmoStateHandle]
    EE_EmoStateFree.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 232
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetType'):
    EE_EmoEngineEventGetType = _libs['edk.dll'].EE_EmoEngineEventGetType
    EE_EmoEngineEventGetType.argtypes = [EmoEngineEventHandle]
    EE_EmoEngineEventGetType.restype = EE_Event_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 242
if hasattr(_libs['edk.dll'], 'EE_CognitivEventGetType'):
    EE_CognitivEventGetType = _libs['edk.dll'].EE_CognitivEventGetType
    EE_CognitivEventGetType.argtypes = [EmoEngineEventHandle]
    EE_CognitivEventGetType.restype = EE_CognitivEvent_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 252
if hasattr(_libs['edk.dll'], 'EE_ExpressivEventGetType'):
    EE_ExpressivEventGetType = _libs['edk.dll'].EE_ExpressivEventGetType
    EE_ExpressivEventGetType.argtypes = [EmoEngineEventHandle]
    EE_ExpressivEventGetType.restype = EE_ExpressivEvent_t

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 266
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetUserId'):
    EE_EmoEngineEventGetUserId = _libs['edk.dll'].EE_EmoEngineEventGetUserId
    EE_EmoEngineEventGetUserId.argtypes = [EmoEngineEventHandle, POINTER(c_uint)]
    EE_EmoEngineEventGetUserId.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 280
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetEmoState'):
    EE_EmoEngineEventGetEmoState = _libs['edk.dll'].EE_EmoEngineEventGetEmoState
    EE_EmoEngineEventGetEmoState.argtypes = [EmoEngineEventHandle, EmoStateHandle]
    EE_EmoEngineEventGetEmoState.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 298
if hasattr(_libs['edk.dll'], 'EE_EngineGetNextEvent'):
    EE_EngineGetNextEvent = _libs['edk.dll'].EE_EngineGetNextEvent
    EE_EngineGetNextEvent.argtypes = [EmoEngineEventHandle]
    EE_EngineGetNextEvent.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 314
if hasattr(_libs['edk.dll'], 'EE_EngineClearEventQueue'):
    EE_EngineClearEventQueue = _libs['edk.dll'].EE_EngineClearEventQueue
    EE_EngineClearEventQueue.argtypes = [c_int]
    EE_EngineClearEventQueue.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 327
if hasattr(_libs['edk.dll'], 'EE_EngineGetNumUser'):
    EE_EngineGetNumUser = _libs['edk.dll'].EE_EngineGetNumUser
    EE_EngineGetNumUser.argtypes = [POINTER(c_uint)]
    EE_EngineGetNumUser.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 340
if hasattr(_libs['edk.dll'], 'EE_SetHardwarePlayerDisplay'):
    EE_SetHardwarePlayerDisplay = _libs['edk.dll'].EE_SetHardwarePlayerDisplay
    EE_SetHardwarePlayerDisplay.argtypes = [c_uint, c_uint]
    EE_SetHardwarePlayerDisplay.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 355
if hasattr(_libs['edk.dll'], 'EE_SetUserProfile'):
    EE_SetUserProfile = _libs['edk.dll'].EE_SetUserProfile
    EE_SetUserProfile.argtypes = [c_uint, POINTER(c_ubyte), c_uint]
    EE_SetUserProfile.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 372
if hasattr(_libs['edk.dll'], 'EE_GetUserProfile'):
    EE_GetUserProfile = _libs['edk.dll'].EE_GetUserProfile
    EE_GetUserProfile.argtypes = [c_uint, EmoEngineEventHandle]
    EE_GetUserProfile.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 388
if hasattr(_libs['edk.dll'], 'EE_GetBaseProfile'):
    EE_GetBaseProfile = _libs['edk.dll'].EE_GetBaseProfile
    EE_GetBaseProfile.argtypes = [EmoEngineEventHandle]
    EE_GetBaseProfile.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 402
if hasattr(_libs['edk.dll'], 'EE_GetUserProfileSize'):
    EE_GetUserProfileSize = _libs['edk.dll'].EE_GetUserProfileSize
    EE_GetUserProfileSize.argtypes = [EmoEngineEventHandle, POINTER(c_uint)]
    EE_GetUserProfileSize.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 417
if hasattr(_libs['edk.dll'], 'EE_GetUserProfileBytes'):
    EE_GetUserProfileBytes = _libs['edk.dll'].EE_GetUserProfileBytes
    EE_GetUserProfileBytes.argtypes = [EmoEngineEventHandle, POINTER(c_ubyte), c_uint]
    EE_GetUserProfileBytes.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 430
if hasattr(_libs['edk.dll'], 'EE_LoadUserProfile'):
    EE_LoadUserProfile = _libs['edk.dll'].EE_LoadUserProfile
    EE_LoadUserProfile.argtypes = [c_uint, String]
    EE_LoadUserProfile.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 443
if hasattr(_libs['edk.dll'], 'EE_SaveUserProfile'):
    EE_SaveUserProfile = _libs['edk.dll'].EE_SaveUserProfile
    EE_SaveUserProfile.argtypes = [c_uint, String]
    EE_SaveUserProfile.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 458
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetThreshold'):
    EE_ExpressivSetThreshold = _libs['edk.dll'].EE_ExpressivSetThreshold
    EE_ExpressivSetThreshold.argtypes = [c_uint, EE_ExpressivAlgo_t, EE_ExpressivThreshold_t, c_int]
    EE_ExpressivSetThreshold.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 474
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetThreshold'):
    EE_ExpressivGetThreshold = _libs['edk.dll'].EE_ExpressivGetThreshold
    EE_ExpressivGetThreshold.argtypes = [c_uint, EE_ExpressivAlgo_t, EE_ExpressivThreshold_t, POINTER(c_int)]
    EE_ExpressivGetThreshold.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 489
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetTrainingAction'):
    EE_ExpressivSetTrainingAction = _libs['edk.dll'].EE_ExpressivSetTrainingAction
    EE_ExpressivSetTrainingAction.argtypes = [c_uint, EE_ExpressivAlgo_t]
    EE_ExpressivSetTrainingAction.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 504
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetTrainingControl'):
    EE_ExpressivSetTrainingControl = _libs['edk.dll'].EE_ExpressivSetTrainingControl
    EE_ExpressivSetTrainingControl.argtypes = [c_uint, EE_ExpressivTrainingControl_t]
    EE_ExpressivSetTrainingControl.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 519
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainingAction'):
    EE_ExpressivGetTrainingAction = _libs['edk.dll'].EE_ExpressivGetTrainingAction
    EE_ExpressivGetTrainingAction.argtypes = [c_uint, POINTER(EE_ExpressivAlgo_t)]
    EE_ExpressivGetTrainingAction.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 533
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainingTime'):
    EE_ExpressivGetTrainingTime = _libs['edk.dll'].EE_ExpressivGetTrainingTime
    EE_ExpressivGetTrainingTime.argtypes = [c_uint, POINTER(c_uint)]
    EE_ExpressivGetTrainingTime.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 548
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainedSignatureActions'):
    EE_ExpressivGetTrainedSignatureActions = _libs['edk.dll'].EE_ExpressivGetTrainedSignatureActions
    EE_ExpressivGetTrainedSignatureActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_ExpressivGetTrainedSignatureActions.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 566
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainedSignatureAvailable'):
    EE_ExpressivGetTrainedSignatureAvailable = _libs['edk.dll'].EE_ExpressivGetTrainedSignatureAvailable
    EE_ExpressivGetTrainedSignatureAvailable.argtypes = [c_uint, POINTER(c_int)]
    EE_ExpressivGetTrainedSignatureAvailable.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 582
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetSignatureType'):
    EE_ExpressivSetSignatureType = _libs['edk.dll'].EE_ExpressivSetSignatureType
    EE_ExpressivSetSignatureType.argtypes = [c_uint, EE_ExpressivSignature_t]
    EE_ExpressivSetSignatureType.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 596
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetSignatureType'):
    EE_ExpressivGetSignatureType = _libs['edk.dll'].EE_ExpressivGetSignatureType
    EE_ExpressivGetSignatureType.argtypes = [c_uint, POINTER(EE_ExpressivSignature_t)]
    EE_ExpressivGetSignatureType.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 612
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActiveActions'):
    EE_CognitivSetActiveActions = _libs['edk.dll'].EE_CognitivSetActiveActions
    EE_CognitivSetActiveActions.argtypes = [c_uint, c_ulong]
    EE_CognitivSetActiveActions.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 626
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActiveActions'):
    EE_CognitivGetActiveActions = _libs['edk.dll'].EE_CognitivGetActiveActions
    EE_CognitivGetActiveActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_CognitivGetActiveActions.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 640
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainingTime'):
    EE_CognitivGetTrainingTime = _libs['edk.dll'].EE_CognitivGetTrainingTime
    EE_CognitivGetTrainingTime.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetTrainingTime.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 654
if hasattr(_libs['edk.dll'], 'EE_CognitivSetTrainingControl'):
    EE_CognitivSetTrainingControl = _libs['edk.dll'].EE_CognitivSetTrainingControl
    EE_CognitivSetTrainingControl.argtypes = [c_uint, EE_CognitivTrainingControl_t]
    EE_CognitivSetTrainingControl.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 668
if hasattr(_libs['edk.dll'], 'EE_CognitivSetTrainingAction'):
    EE_CognitivSetTrainingAction = _libs['edk.dll'].EE_CognitivSetTrainingAction
    EE_CognitivSetTrainingAction.argtypes = [c_uint, EE_CognitivAction_t]
    EE_CognitivSetTrainingAction.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 682
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainingAction'):
    EE_CognitivGetTrainingAction = _libs['edk.dll'].EE_CognitivGetTrainingAction
    EE_CognitivGetTrainingAction.argtypes = [c_uint, POINTER(EE_CognitivAction_t)]
    EE_CognitivGetTrainingAction.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 698
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainedSignatureActions'):
    EE_CognitivGetTrainedSignatureActions = _libs['edk.dll'].EE_CognitivGetTrainedSignatureActions
    EE_CognitivGetTrainedSignatureActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_CognitivGetTrainedSignatureActions.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 714
if hasattr(_libs['edk.dll'], 'EE_CognitivGetOverallSkillRating'):
    EE_CognitivGetOverallSkillRating = _libs['edk.dll'].EE_CognitivGetOverallSkillRating
    EE_CognitivGetOverallSkillRating.argtypes = [c_uint, POINTER(c_float)]
    EE_CognitivGetOverallSkillRating.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 731
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActionSkillRating'):
    EE_CognitivGetActionSkillRating = _libs['edk.dll'].EE_CognitivGetActionSkillRating
    EE_CognitivGetActionSkillRating.argtypes = [c_uint, EE_CognitivAction_t, POINTER(c_float)]
    EE_CognitivGetActionSkillRating.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 745
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActivationLevel'):
    EE_CognitivSetActivationLevel = _libs['edk.dll'].EE_CognitivSetActivationLevel
    EE_CognitivSetActivationLevel.argtypes = [c_uint, c_int]
    EE_CognitivSetActivationLevel.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 762
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActionSensitivity'):
    EE_CognitivSetActionSensitivity = _libs['edk.dll'].EE_CognitivSetActionSensitivity
    EE_CognitivSetActionSensitivity.argtypes = [c_uint, c_int, c_int, c_int, c_int]
    EE_CognitivSetActionSensitivity.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 778
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActivationLevel'):
    EE_CognitivGetActivationLevel = _libs['edk.dll'].EE_CognitivGetActivationLevel
    EE_CognitivGetActivationLevel.argtypes = [c_uint, POINTER(c_int)]
    EE_CognitivGetActivationLevel.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 795
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActionSensitivity'):
    EE_CognitivGetActionSensitivity = _libs['edk.dll'].EE_CognitivGetActionSensitivity
    EE_CognitivGetActionSensitivity.argtypes = [c_uint, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    EE_CognitivGetActionSensitivity.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 810
if hasattr(_libs['edk.dll'], 'EE_CognitivStartSamplingNeutral'):
    EE_CognitivStartSamplingNeutral = _libs['edk.dll'].EE_CognitivStartSamplingNeutral
    EE_CognitivStartSamplingNeutral.argtypes = [c_uint]
    EE_CognitivStartSamplingNeutral.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 823
if hasattr(_libs['edk.dll'], 'EE_CognitivStopSamplingNeutral'):
    EE_CognitivStopSamplingNeutral = _libs['edk.dll'].EE_CognitivStopSamplingNeutral
    EE_CognitivStopSamplingNeutral.argtypes = [c_uint]
    EE_CognitivStopSamplingNeutral.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 837
if hasattr(_libs['edk.dll'], 'EE_CognitivSetSignatureCaching'):
    EE_CognitivSetSignatureCaching = _libs['edk.dll'].EE_CognitivSetSignatureCaching
    EE_CognitivSetSignatureCaching.argtypes = [c_uint, c_uint]
    EE_CognitivSetSignatureCaching.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 851
if hasattr(_libs['edk.dll'], 'EE_CognitivGetSignatureCaching'):
    EE_CognitivGetSignatureCaching = _libs['edk.dll'].EE_CognitivGetSignatureCaching
    EE_CognitivGetSignatureCaching.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetSignatureCaching.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 865
if hasattr(_libs['edk.dll'], 'EE_CognitivSetSignatureCacheSize'):
    EE_CognitivSetSignatureCacheSize = _libs['edk.dll'].EE_CognitivSetSignatureCacheSize
    EE_CognitivSetSignatureCacheSize.argtypes = [c_uint, c_uint]
    EE_CognitivSetSignatureCacheSize.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 879
if hasattr(_libs['edk.dll'], 'EE_CognitivGetSignatureCacheSize'):
    EE_CognitivGetSignatureCacheSize = _libs['edk.dll'].EE_CognitivGetSignatureCacheSize
    EE_CognitivGetSignatureCacheSize.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetSignatureCacheSize.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 893
if hasattr(_libs['edk.dll'], 'EE_HeadsetGetSensorDetails'):
    EE_HeadsetGetSensorDetails = _libs['edk.dll'].EE_HeadsetGetSensorDetails
    EE_HeadsetGetSensorDetails.argtypes = [EE_InputChannels_t, POINTER(InputSensorDescriptor_t)]
    EE_HeadsetGetSensorDetails.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 907
if hasattr(_libs['edk.dll'], 'EE_HardwareGetVersion'):
    EE_HardwareGetVersion = _libs['edk.dll'].EE_HardwareGetVersion
    EE_HardwareGetVersion.argtypes = [c_uint, POINTER(c_ulong)]
    EE_HardwareGetVersion.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 921
if hasattr(_libs['edk.dll'], 'EE_SoftwareGetVersion'):
    EE_SoftwareGetVersion = _libs['edk.dll'].EE_SoftwareGetVersion
    EE_SoftwareGetVersion.argtypes = [String, c_uint, POINTER(c_ulong)]
    EE_SoftwareGetVersion.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 936
if hasattr(_libs['edk.dll'], 'EE_HeadsetGetGyroDelta'):
    EE_HeadsetGetGyroDelta = _libs['edk.dll'].EE_HeadsetGetGyroDelta
    EE_HeadsetGetGyroDelta.argtypes = [c_uint, POINTER(c_int), POINTER(c_int)]
    EE_HeadsetGetGyroDelta.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 949
if hasattr(_libs['edk.dll'], 'EE_HeadsetGyroRezero'):
    EE_HeadsetGyroRezero = _libs['edk.dll'].EE_HeadsetGyroRezero
    EE_HeadsetGyroRezero.argtypes = [c_uint]
    EE_HeadsetGyroRezero.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 956
if hasattr(_libs['edk.dll'], 'EE_OptimizationParamCreate'):
    EE_OptimizationParamCreate = _libs['edk.dll'].EE_OptimizationParamCreate
    EE_OptimizationParamCreate.argtypes = []
    EE_OptimizationParamCreate.restype = OptimizationParamHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 963
if hasattr(_libs['edk.dll'], 'EE_OptimizationParamFree'):
    EE_OptimizationParamFree = _libs['edk.dll'].EE_OptimizationParamFree
    EE_OptimizationParamFree.argtypes = [OptimizationParamHandle]
    EE_OptimizationParamFree.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 972
if hasattr(_libs['edk.dll'], 'EE_OptimizationEnable'):
    EE_OptimizationEnable = _libs['edk.dll'].EE_OptimizationEnable
    EE_OptimizationEnable.argtypes = [OptimizationParamHandle]
    EE_OptimizationEnable.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 981
if hasattr(_libs['edk.dll'], 'EE_OptimizationIsEnabled'):
    EE_OptimizationIsEnabled = _libs['edk.dll'].EE_OptimizationIsEnabled
    EE_OptimizationIsEnabled.argtypes = [POINTER(c_bool)]
    EE_OptimizationIsEnabled.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 989
if hasattr(_libs['edk.dll'], 'EE_OptimizationDisable'):
    EE_OptimizationDisable = _libs['edk.dll'].EE_OptimizationDisable
    EE_OptimizationDisable.argtypes = []
    EE_OptimizationDisable.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 998
if hasattr(_libs['edk.dll'], 'EE_OptimizationGetParam'):
    EE_OptimizationGetParam = _libs['edk.dll'].EE_OptimizationGetParam
    EE_OptimizationGetParam.argtypes = [OptimizationParamHandle]
    EE_OptimizationGetParam.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1009
if hasattr(_libs['edk.dll'], 'EE_OptimizationGetVitalAlgorithm'):
    EE_OptimizationGetVitalAlgorithm = _libs['edk.dll'].EE_OptimizationGetVitalAlgorithm
    EE_OptimizationGetVitalAlgorithm.argtypes = [OptimizationParamHandle, EE_EmotivSuite_t, POINTER(c_uint)]
    EE_OptimizationGetVitalAlgorithm.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1020
if hasattr(_libs['edk.dll'], 'EE_OptimizationSetVitalAlgorithm'):
    EE_OptimizationSetVitalAlgorithm = _libs['edk.dll'].EE_OptimizationSetVitalAlgorithm
    EE_OptimizationSetVitalAlgorithm.argtypes = [OptimizationParamHandle, EE_EmotivSuite_t, c_uint]
    EE_OptimizationSetVitalAlgorithm.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1030
if hasattr(_libs['edk.dll'], 'EE_ResetDetection'):
    EE_ResetDetection = _libs['edk.dll'].EE_ResetDetection
    EE_ResetDetection.argtypes = [c_uint, EE_EmotivSuite_t, c_uint]
    EE_ResetDetection.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1034
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'EE_GetSecurityCode'):
        continue
    EE_GetSecurityCode = _lib.EE_GetSecurityCode
    EE_GetSecurityCode.argtypes = []
    EE_GetSecurityCode.restype = c_double
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1035
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'EE_CheckSecurityCode'):
        continue
    EE_CheckSecurityCode = _lib.EE_CheckSecurityCode
    EE_CheckSecurityCode.argtypes = [c_double]
    EE_CheckSecurityCode.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1048
if hasattr(_libs['edk.dll'], 'EE_EngineLocalConnect'):
    EE_EngineLocalConnect = _libs['edk.dll'].EE_EngineLocalConnect
    EE_EngineLocalConnect.argtypes = [String]
    EE_EngineLocalConnect.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1054
if hasattr(_libs['edk.dll'], 'EE_DataCreate'):
    EE_DataCreate = _libs['edk.dll'].EE_DataCreate
    EE_DataCreate.argtypes = []
    EE_DataCreate.restype = DataHandle

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1060
if hasattr(_libs['edk.dll'], 'EE_DataFree'):
    EE_DataFree = _libs['edk.dll'].EE_DataFree
    EE_DataFree.argtypes = [DataHandle]
    EE_DataFree.restype = None

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1069
if hasattr(_libs['edk.dll'], 'EE_DataUpdateHandle'):
    EE_DataUpdateHandle = _libs['edk.dll'].EE_DataUpdateHandle
    EE_DataUpdateHandle.argtypes = [c_uint, DataHandle]
    EE_DataUpdateHandle.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1080
if hasattr(_libs['edk.dll'], 'EE_DataGet'):
    EE_DataGet = _libs['edk.dll'].EE_DataGet
    EE_DataGet.argtypes = [DataHandle, EE_DataChannel_t, POINTER(c_double), c_uint]
    EE_DataGet.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1092
if hasattr(_libs['edk.dll'], 'EE_DataGetMultiChannels'):
    EE_DataGetMultiChannels = _libs['edk.dll'].EE_DataGetMultiChannels
    EE_DataGetMultiChannels.argtypes = [DataHandle, POINTER(EE_DataChannel_t), c_uint, POINTER(POINTER(c_double)), c_uint]
    EE_DataGetMultiChannels.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1101
if hasattr(_libs['edk.dll'], 'EE_DataGetNumberOfSample'):
    EE_DataGetNumberOfSample = _libs['edk.dll'].EE_DataGetNumberOfSample
    EE_DataGetNumberOfSample.argtypes = [DataHandle, POINTER(c_uint)]
    EE_DataGetNumberOfSample.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1109
if hasattr(_libs['edk.dll'], 'EE_DataSetBufferSizeInSec'):
    EE_DataSetBufferSizeInSec = _libs['edk.dll'].EE_DataSetBufferSizeInSec
    EE_DataSetBufferSizeInSec.argtypes = [c_float]
    EE_DataSetBufferSizeInSec.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1117
if hasattr(_libs['edk.dll'], 'EE_DataGetBufferSizeInSec'):
    EE_DataGetBufferSizeInSec = _libs['edk.dll'].EE_DataGetBufferSizeInSec
    EE_DataGetBufferSizeInSec.argtypes = [POINTER(c_float)]
    EE_DataGetBufferSizeInSec.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1127
if hasattr(_libs['edk.dll'], 'EE_DataAcquisitionEnable'):
    EE_DataAcquisitionEnable = _libs['edk.dll'].EE_DataAcquisitionEnable
    EE_DataAcquisitionEnable.argtypes = [c_uint, c_bool]
    EE_DataAcquisitionEnable.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1136
if hasattr(_libs['edk.dll'], 'EE_DataAcquisitionIsEnabled'):
    EE_DataAcquisitionIsEnabled = _libs['edk.dll'].EE_DataAcquisitionIsEnabled
    EE_DataAcquisitionIsEnabled.argtypes = [c_uint, POINTER(c_bool)]
    EE_DataAcquisitionIsEnabled.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1145
if hasattr(_libs['edk.dll'], 'EE_DataSetSychronizationSignal'):
    EE_DataSetSychronizationSignal = _libs['edk.dll'].EE_DataSetSychronizationSignal
    EE_DataSetSychronizationSignal.argtypes = [c_uint, c_int]
    EE_DataSetSychronizationSignal.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1154
if hasattr(_libs['edk.dll'], 'EE_DataSetMarker'):
    EE_DataSetMarker = _libs['edk.dll'].EE_DataSetMarker
    EE_DataSetMarker.argtypes = [c_uint, c_int]
    EE_DataSetMarker.restype = c_int

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 1163
if hasattr(_libs['edk.dll'], 'EE_DataGetSamplingRate'):
    EE_DataGetSamplingRate = _libs['edk.dll'].EE_DataGetSamplingRate
    EE_DataGetSamplingRate.argtypes = [c_uint, POINTER(c_uint)]
    EE_DataGetSamplingRate.restype = c_int

GLenum = c_uint # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 112

GLboolean = c_ubyte # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 113

GLbitfield = c_uint # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 114

GLvoid = None # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 115

GLbyte = c_char # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 116

GLshort = c_short # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 117

GLint = c_int # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 118

GLubyte = c_ubyte # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 119

GLushort = c_ushort # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 120

GLuint = c_uint # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 121

GLsizei = c_int # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 122

GLfloat = c_float # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 123

GLclampf = c_float # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 124

GLdouble = c_double # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 125

GLclampd = c_double # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 126

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 983
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClearIndex'):
        continue
    glClearIndex = _lib.glClearIndex
    glClearIndex.argtypes = [GLfloat]
    glClearIndex.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 984
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClearColor'):
        continue
    glClearColor = _lib.glClearColor
    glClearColor.argtypes = [GLclampf, GLclampf, GLclampf, GLclampf]
    glClearColor.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 985
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClear'):
        continue
    glClear = _lib.glClear
    glClear.argtypes = [GLbitfield]
    glClear.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 986
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexMask'):
        continue
    glIndexMask = _lib.glIndexMask
    glIndexMask.argtypes = [GLuint]
    glIndexMask.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 987
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColorMask'):
        continue
    glColorMask = _lib.glColorMask
    glColorMask.argtypes = [GLboolean, GLboolean, GLboolean, GLboolean]
    glColorMask.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 988
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glAlphaFunc'):
        continue
    glAlphaFunc = _lib.glAlphaFunc
    glAlphaFunc.argtypes = [GLenum, GLclampf]
    glAlphaFunc.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 989
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glBlendFunc'):
        continue
    glBlendFunc = _lib.glBlendFunc
    glBlendFunc.argtypes = [GLenum, GLenum]
    glBlendFunc.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 990
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLogicOp'):
        continue
    glLogicOp = _lib.glLogicOp
    glLogicOp.argtypes = [GLenum]
    glLogicOp.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 991
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCullFace'):
        continue
    glCullFace = _lib.glCullFace
    glCullFace.argtypes = [GLenum]
    glCullFace.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 992
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFrontFace'):
        continue
    glFrontFace = _lib.glFrontFace
    glFrontFace.argtypes = [GLenum]
    glFrontFace.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 993
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPointSize'):
        continue
    glPointSize = _lib.glPointSize
    glPointSize.argtypes = [GLfloat]
    glPointSize.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 994
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLineWidth'):
        continue
    glLineWidth = _lib.glLineWidth
    glLineWidth.argtypes = [GLfloat]
    glLineWidth.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 995
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLineStipple'):
        continue
    glLineStipple = _lib.glLineStipple
    glLineStipple.argtypes = [GLint, GLushort]
    glLineStipple.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 996
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPolygonMode'):
        continue
    glPolygonMode = _lib.glPolygonMode
    glPolygonMode.argtypes = [GLenum, GLenum]
    glPolygonMode.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 997
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPolygonOffset'):
        continue
    glPolygonOffset = _lib.glPolygonOffset
    glPolygonOffset.argtypes = [GLfloat, GLfloat]
    glPolygonOffset.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 998
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPolygonStipple'):
        continue
    glPolygonStipple = _lib.glPolygonStipple
    glPolygonStipple.argtypes = [POINTER(GLubyte)]
    glPolygonStipple.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 999
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetPolygonStipple'):
        continue
    glGetPolygonStipple = _lib.glGetPolygonStipple
    glGetPolygonStipple.argtypes = [POINTER(GLubyte)]
    glGetPolygonStipple.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1000
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEdgeFlag'):
        continue
    glEdgeFlag = _lib.glEdgeFlag
    glEdgeFlag.argtypes = [GLboolean]
    glEdgeFlag.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1001
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEdgeFlagv'):
        continue
    glEdgeFlagv = _lib.glEdgeFlagv
    glEdgeFlagv.argtypes = [POINTER(GLboolean)]
    glEdgeFlagv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1002
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glScissor'):
        continue
    glScissor = _lib.glScissor
    glScissor.argtypes = [GLint, GLint, GLsizei, GLsizei]
    glScissor.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1003
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClipPlane'):
        continue
    glClipPlane = _lib.glClipPlane
    glClipPlane.argtypes = [GLenum, POINTER(GLdouble)]
    glClipPlane.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1004
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetClipPlane'):
        continue
    glGetClipPlane = _lib.glGetClipPlane
    glGetClipPlane.argtypes = [GLenum, POINTER(GLdouble)]
    glGetClipPlane.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1005
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDrawBuffer'):
        continue
    glDrawBuffer = _lib.glDrawBuffer
    glDrawBuffer.argtypes = [GLenum]
    glDrawBuffer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1006
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glReadBuffer'):
        continue
    glReadBuffer = _lib.glReadBuffer
    glReadBuffer.argtypes = [GLenum]
    glReadBuffer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1007
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEnable'):
        continue
    glEnable = _lib.glEnable
    glEnable.argtypes = [GLenum]
    glEnable.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1008
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDisable'):
        continue
    glDisable = _lib.glDisable
    glDisable.argtypes = [GLenum]
    glDisable.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1009
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIsEnabled'):
        continue
    glIsEnabled = _lib.glIsEnabled
    glIsEnabled.argtypes = [GLenum]
    glIsEnabled.restype = GLboolean
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1010
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEnableClientState'):
        continue
    glEnableClientState = _lib.glEnableClientState
    glEnableClientState.argtypes = [GLenum]
    glEnableClientState.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1011
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDisableClientState'):
        continue
    glDisableClientState = _lib.glDisableClientState
    glDisableClientState.argtypes = [GLenum]
    glDisableClientState.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1012
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetBooleanv'):
        continue
    glGetBooleanv = _lib.glGetBooleanv
    glGetBooleanv.argtypes = [GLenum, POINTER(GLboolean)]
    glGetBooleanv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1013
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetDoublev'):
        continue
    glGetDoublev = _lib.glGetDoublev
    glGetDoublev.argtypes = [GLenum, POINTER(GLdouble)]
    glGetDoublev.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1014
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetFloatv'):
        continue
    glGetFloatv = _lib.glGetFloatv
    glGetFloatv.argtypes = [GLenum, POINTER(GLfloat)]
    glGetFloatv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1015
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetIntegerv'):
        continue
    glGetIntegerv = _lib.glGetIntegerv
    glGetIntegerv.argtypes = [GLenum, POINTER(GLint)]
    glGetIntegerv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1016
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPushAttrib'):
        continue
    glPushAttrib = _lib.glPushAttrib
    glPushAttrib.argtypes = [GLbitfield]
    glPushAttrib.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1017
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPopAttrib'):
        continue
    glPopAttrib = _lib.glPopAttrib
    glPopAttrib.argtypes = []
    glPopAttrib.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1018
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPushClientAttrib'):
        continue
    glPushClientAttrib = _lib.glPushClientAttrib
    glPushClientAttrib.argtypes = [GLbitfield]
    glPushClientAttrib.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1019
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPopClientAttrib'):
        continue
    glPopClientAttrib = _lib.glPopClientAttrib
    glPopClientAttrib.argtypes = []
    glPopClientAttrib.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1020
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRenderMode'):
        continue
    glRenderMode = _lib.glRenderMode
    glRenderMode.argtypes = [GLenum]
    glRenderMode.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1021
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetError'):
        continue
    glGetError = _lib.glGetError
    glGetError.argtypes = []
    glGetError.restype = GLenum
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1022
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetString'):
        continue
    glGetString = _lib.glGetString
    glGetString.argtypes = [GLenum]
    glGetString.restype = POINTER(GLubyte)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1023
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFinish'):
        continue
    glFinish = _lib.glFinish
    glFinish.argtypes = []
    glFinish.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1024
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFlush'):
        continue
    glFlush = _lib.glFlush
    glFlush.argtypes = []
    glFlush.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1025
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glHint'):
        continue
    glHint = _lib.glHint
    glHint.argtypes = [GLenum, GLenum]
    glHint.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1028
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClearDepth'):
        continue
    glClearDepth = _lib.glClearDepth
    glClearDepth.argtypes = [GLclampd]
    glClearDepth.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1029
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDepthFunc'):
        continue
    glDepthFunc = _lib.glDepthFunc
    glDepthFunc.argtypes = [GLenum]
    glDepthFunc.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1030
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDepthMask'):
        continue
    glDepthMask = _lib.glDepthMask
    glDepthMask.argtypes = [GLboolean]
    glDepthMask.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1031
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDepthRange'):
        continue
    glDepthRange = _lib.glDepthRange
    glDepthRange.argtypes = [GLclampd, GLclampd]
    glDepthRange.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1034
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClearAccum'):
        continue
    glClearAccum = _lib.glClearAccum
    glClearAccum.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glClearAccum.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1035
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glAccum'):
        continue
    glAccum = _lib.glAccum
    glAccum.argtypes = [GLenum, GLfloat]
    glAccum.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1038
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMatrixMode'):
        continue
    glMatrixMode = _lib.glMatrixMode
    glMatrixMode.argtypes = [GLenum]
    glMatrixMode.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1039
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glOrtho'):
        continue
    glOrtho = _lib.glOrtho
    glOrtho.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]
    glOrtho.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1040
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFrustum'):
        continue
    glFrustum = _lib.glFrustum
    glFrustum.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]
    glFrustum.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1041
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glViewport'):
        continue
    glViewport = _lib.glViewport
    glViewport.argtypes = [GLint, GLint, GLsizei, GLsizei]
    glViewport.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1042
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPushMatrix'):
        continue
    glPushMatrix = _lib.glPushMatrix
    glPushMatrix.argtypes = []
    glPushMatrix.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1043
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPopMatrix'):
        continue
    glPopMatrix = _lib.glPopMatrix
    glPopMatrix.argtypes = []
    glPopMatrix.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1044
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLoadIdentity'):
        continue
    glLoadIdentity = _lib.glLoadIdentity
    glLoadIdentity.argtypes = []
    glLoadIdentity.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1045
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLoadMatrixd'):
        continue
    glLoadMatrixd = _lib.glLoadMatrixd
    glLoadMatrixd.argtypes = [POINTER(GLdouble)]
    glLoadMatrixd.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1046
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLoadMatrixf'):
        continue
    glLoadMatrixf = _lib.glLoadMatrixf
    glLoadMatrixf.argtypes = [POINTER(GLfloat)]
    glLoadMatrixf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1047
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMultMatrixd'):
        continue
    glMultMatrixd = _lib.glMultMatrixd
    glMultMatrixd.argtypes = [POINTER(GLdouble)]
    glMultMatrixd.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1048
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMultMatrixf'):
        continue
    glMultMatrixf = _lib.glMultMatrixf
    glMultMatrixf.argtypes = [POINTER(GLfloat)]
    glMultMatrixf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1049
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRotated'):
        continue
    glRotated = _lib.glRotated
    glRotated.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glRotated.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1050
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRotatef'):
        continue
    glRotatef = _lib.glRotatef
    glRotatef.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glRotatef.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1051
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glScaled'):
        continue
    glScaled = _lib.glScaled
    glScaled.argtypes = [GLdouble, GLdouble, GLdouble]
    glScaled.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1052
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glScalef'):
        continue
    glScalef = _lib.glScalef
    glScalef.argtypes = [GLfloat, GLfloat, GLfloat]
    glScalef.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1053
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTranslated'):
        continue
    glTranslated = _lib.glTranslated
    glTranslated.argtypes = [GLdouble, GLdouble, GLdouble]
    glTranslated.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1054
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTranslatef'):
        continue
    glTranslatef = _lib.glTranslatef
    glTranslatef.argtypes = [GLfloat, GLfloat, GLfloat]
    glTranslatef.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1057
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIsList'):
        continue
    glIsList = _lib.glIsList
    glIsList.argtypes = [GLuint]
    glIsList.restype = GLboolean
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1058
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDeleteLists'):
        continue
    glDeleteLists = _lib.glDeleteLists
    glDeleteLists.argtypes = [GLuint, GLsizei]
    glDeleteLists.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1059
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGenLists'):
        continue
    glGenLists = _lib.glGenLists
    glGenLists.argtypes = [GLsizei]
    glGenLists.restype = GLuint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1060
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNewList'):
        continue
    glNewList = _lib.glNewList
    glNewList.argtypes = [GLuint, GLenum]
    glNewList.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1061
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEndList'):
        continue
    glEndList = _lib.glEndList
    glEndList.argtypes = []
    glEndList.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1062
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCallList'):
        continue
    glCallList = _lib.glCallList
    glCallList.argtypes = [GLuint]
    glCallList.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1063
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCallLists'):
        continue
    glCallLists = _lib.glCallLists
    glCallLists.argtypes = [GLsizei, GLenum, POINTER(GLvoid)]
    glCallLists.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1064
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glListBase'):
        continue
    glListBase = _lib.glListBase
    glListBase.argtypes = [GLuint]
    glListBase.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1067
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glBegin'):
        continue
    glBegin = _lib.glBegin
    glBegin.argtypes = [GLenum]
    glBegin.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1068
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEnd'):
        continue
    glEnd = _lib.glEnd
    glEnd.argtypes = []
    glEnd.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1069
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2d'):
        continue
    glVertex2d = _lib.glVertex2d
    glVertex2d.argtypes = [GLdouble, GLdouble]
    glVertex2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1070
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2f'):
        continue
    glVertex2f = _lib.glVertex2f
    glVertex2f.argtypes = [GLfloat, GLfloat]
    glVertex2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1071
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2i'):
        continue
    glVertex2i = _lib.glVertex2i
    glVertex2i.argtypes = [GLint, GLint]
    glVertex2i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1072
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2s'):
        continue
    glVertex2s = _lib.glVertex2s
    glVertex2s.argtypes = [GLshort, GLshort]
    glVertex2s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1073
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3d'):
        continue
    glVertex3d = _lib.glVertex3d
    glVertex3d.argtypes = [GLdouble, GLdouble, GLdouble]
    glVertex3d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1074
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3f'):
        continue
    glVertex3f = _lib.glVertex3f
    glVertex3f.argtypes = [GLfloat, GLfloat, GLfloat]
    glVertex3f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1075
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3i'):
        continue
    glVertex3i = _lib.glVertex3i
    glVertex3i.argtypes = [GLint, GLint, GLint]
    glVertex3i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1076
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3s'):
        continue
    glVertex3s = _lib.glVertex3s
    glVertex3s.argtypes = [GLshort, GLshort, GLshort]
    glVertex3s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1077
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4d'):
        continue
    glVertex4d = _lib.glVertex4d
    glVertex4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glVertex4d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1078
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4f'):
        continue
    glVertex4f = _lib.glVertex4f
    glVertex4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glVertex4f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1079
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4i'):
        continue
    glVertex4i = _lib.glVertex4i
    glVertex4i.argtypes = [GLint, GLint, GLint, GLint]
    glVertex4i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1080
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4s'):
        continue
    glVertex4s = _lib.glVertex4s
    glVertex4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
    glVertex4s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1081
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2dv'):
        continue
    glVertex2dv = _lib.glVertex2dv
    glVertex2dv.argtypes = [POINTER(GLdouble)]
    glVertex2dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1082
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2fv'):
        continue
    glVertex2fv = _lib.glVertex2fv
    glVertex2fv.argtypes = [POINTER(GLfloat)]
    glVertex2fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1083
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2iv'):
        continue
    glVertex2iv = _lib.glVertex2iv
    glVertex2iv.argtypes = [POINTER(GLint)]
    glVertex2iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1084
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex2sv'):
        continue
    glVertex2sv = _lib.glVertex2sv
    glVertex2sv.argtypes = [POINTER(GLshort)]
    glVertex2sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1085
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3dv'):
        continue
    glVertex3dv = _lib.glVertex3dv
    glVertex3dv.argtypes = [POINTER(GLdouble)]
    glVertex3dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1086
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3fv'):
        continue
    glVertex3fv = _lib.glVertex3fv
    glVertex3fv.argtypes = [POINTER(GLfloat)]
    glVertex3fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1087
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3iv'):
        continue
    glVertex3iv = _lib.glVertex3iv
    glVertex3iv.argtypes = [POINTER(GLint)]
    glVertex3iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1088
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex3sv'):
        continue
    glVertex3sv = _lib.glVertex3sv
    glVertex3sv.argtypes = [POINTER(GLshort)]
    glVertex3sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1089
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4dv'):
        continue
    glVertex4dv = _lib.glVertex4dv
    glVertex4dv.argtypes = [POINTER(GLdouble)]
    glVertex4dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1090
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4fv'):
        continue
    glVertex4fv = _lib.glVertex4fv
    glVertex4fv.argtypes = [POINTER(GLfloat)]
    glVertex4fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1091
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4iv'):
        continue
    glVertex4iv = _lib.glVertex4iv
    glVertex4iv.argtypes = [POINTER(GLint)]
    glVertex4iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1092
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertex4sv'):
        continue
    glVertex4sv = _lib.glVertex4sv
    glVertex4sv.argtypes = [POINTER(GLshort)]
    glVertex4sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1093
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3b'):
        continue
    glNormal3b = _lib.glNormal3b
    glNormal3b.argtypes = [GLbyte, GLbyte, GLbyte]
    glNormal3b.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1094
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3d'):
        continue
    glNormal3d = _lib.glNormal3d
    glNormal3d.argtypes = [GLdouble, GLdouble, GLdouble]
    glNormal3d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1095
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3f'):
        continue
    glNormal3f = _lib.glNormal3f
    glNormal3f.argtypes = [GLfloat, GLfloat, GLfloat]
    glNormal3f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1096
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3i'):
        continue
    glNormal3i = _lib.glNormal3i
    glNormal3i.argtypes = [GLint, GLint, GLint]
    glNormal3i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1097
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3s'):
        continue
    glNormal3s = _lib.glNormal3s
    glNormal3s.argtypes = [GLshort, GLshort, GLshort]
    glNormal3s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1098
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3bv'):
        continue
    glNormal3bv = _lib.glNormal3bv
    glNormal3bv.argtypes = [POINTER(GLbyte)]
    glNormal3bv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1099
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3dv'):
        continue
    glNormal3dv = _lib.glNormal3dv
    glNormal3dv.argtypes = [POINTER(GLdouble)]
    glNormal3dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1100
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3fv'):
        continue
    glNormal3fv = _lib.glNormal3fv
    glNormal3fv.argtypes = [POINTER(GLfloat)]
    glNormal3fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1101
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3iv'):
        continue
    glNormal3iv = _lib.glNormal3iv
    glNormal3iv.argtypes = [POINTER(GLint)]
    glNormal3iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1102
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormal3sv'):
        continue
    glNormal3sv = _lib.glNormal3sv
    glNormal3sv.argtypes = [POINTER(GLshort)]
    glNormal3sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexd'):
        continue
    glIndexd = _lib.glIndexd
    glIndexd.argtypes = [GLdouble]
    glIndexd.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1104
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexf'):
        continue
    glIndexf = _lib.glIndexf
    glIndexf.argtypes = [GLfloat]
    glIndexf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1105
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexi'):
        continue
    glIndexi = _lib.glIndexi
    glIndexi.argtypes = [GLint]
    glIndexi.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1106
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexs'):
        continue
    glIndexs = _lib.glIndexs
    glIndexs.argtypes = [GLshort]
    glIndexs.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1107
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexub'):
        continue
    glIndexub = _lib.glIndexub
    glIndexub.argtypes = [GLubyte]
    glIndexub.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1108
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexdv'):
        continue
    glIndexdv = _lib.glIndexdv
    glIndexdv.argtypes = [POINTER(GLdouble)]
    glIndexdv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1109
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexfv'):
        continue
    glIndexfv = _lib.glIndexfv
    glIndexfv.argtypes = [POINTER(GLfloat)]
    glIndexfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1110
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexiv'):
        continue
    glIndexiv = _lib.glIndexiv
    glIndexiv.argtypes = [POINTER(GLint)]
    glIndexiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1111
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexsv'):
        continue
    glIndexsv = _lib.glIndexsv
    glIndexsv.argtypes = [POINTER(GLshort)]
    glIndexsv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1112
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexubv'):
        continue
    glIndexubv = _lib.glIndexubv
    glIndexubv.argtypes = [POINTER(GLubyte)]
    glIndexubv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1113
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3b'):
        continue
    glColor3b = _lib.glColor3b
    glColor3b.argtypes = [GLbyte, GLbyte, GLbyte]
    glColor3b.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1114
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3d'):
        continue
    glColor3d = _lib.glColor3d
    glColor3d.argtypes = [GLdouble, GLdouble, GLdouble]
    glColor3d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1115
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3f'):
        continue
    glColor3f = _lib.glColor3f
    glColor3f.argtypes = [GLfloat, GLfloat, GLfloat]
    glColor3f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1116
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3i'):
        continue
    glColor3i = _lib.glColor3i
    glColor3i.argtypes = [GLint, GLint, GLint]
    glColor3i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1117
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3s'):
        continue
    glColor3s = _lib.glColor3s
    glColor3s.argtypes = [GLshort, GLshort, GLshort]
    glColor3s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1118
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3ub'):
        continue
    glColor3ub = _lib.glColor3ub
    glColor3ub.argtypes = [GLubyte, GLubyte, GLubyte]
    glColor3ub.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1119
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3ui'):
        continue
    glColor3ui = _lib.glColor3ui
    glColor3ui.argtypes = [GLuint, GLuint, GLuint]
    glColor3ui.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1120
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3us'):
        continue
    glColor3us = _lib.glColor3us
    glColor3us.argtypes = [GLushort, GLushort, GLushort]
    glColor3us.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1121
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4b'):
        continue
    glColor4b = _lib.glColor4b
    glColor4b.argtypes = [GLbyte, GLbyte, GLbyte, GLbyte]
    glColor4b.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1122
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4d'):
        continue
    glColor4d = _lib.glColor4d
    glColor4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glColor4d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1123
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4f'):
        continue
    glColor4f = _lib.glColor4f
    glColor4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glColor4f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1124
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4i'):
        continue
    glColor4i = _lib.glColor4i
    glColor4i.argtypes = [GLint, GLint, GLint, GLint]
    glColor4i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1125
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4s'):
        continue
    glColor4s = _lib.glColor4s
    glColor4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
    glColor4s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1126
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4ub'):
        continue
    glColor4ub = _lib.glColor4ub
    glColor4ub.argtypes = [GLubyte, GLubyte, GLubyte, GLubyte]
    glColor4ub.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1127
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4ui'):
        continue
    glColor4ui = _lib.glColor4ui
    glColor4ui.argtypes = [GLuint, GLuint, GLuint, GLuint]
    glColor4ui.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1128
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4us'):
        continue
    glColor4us = _lib.glColor4us
    glColor4us.argtypes = [GLushort, GLushort, GLushort, GLushort]
    glColor4us.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1129
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3bv'):
        continue
    glColor3bv = _lib.glColor3bv
    glColor3bv.argtypes = [POINTER(GLbyte)]
    glColor3bv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1130
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3dv'):
        continue
    glColor3dv = _lib.glColor3dv
    glColor3dv.argtypes = [POINTER(GLdouble)]
    glColor3dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1131
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3fv'):
        continue
    glColor3fv = _lib.glColor3fv
    glColor3fv.argtypes = [POINTER(GLfloat)]
    glColor3fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1132
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3iv'):
        continue
    glColor3iv = _lib.glColor3iv
    glColor3iv.argtypes = [POINTER(GLint)]
    glColor3iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1133
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3sv'):
        continue
    glColor3sv = _lib.glColor3sv
    glColor3sv.argtypes = [POINTER(GLshort)]
    glColor3sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1134
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3ubv'):
        continue
    glColor3ubv = _lib.glColor3ubv
    glColor3ubv.argtypes = [POINTER(GLubyte)]
    glColor3ubv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1135
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3uiv'):
        continue
    glColor3uiv = _lib.glColor3uiv
    glColor3uiv.argtypes = [POINTER(GLuint)]
    glColor3uiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1136
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor3usv'):
        continue
    glColor3usv = _lib.glColor3usv
    glColor3usv.argtypes = [POINTER(GLushort)]
    glColor3usv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1137
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4bv'):
        continue
    glColor4bv = _lib.glColor4bv
    glColor4bv.argtypes = [POINTER(GLbyte)]
    glColor4bv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1138
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4dv'):
        continue
    glColor4dv = _lib.glColor4dv
    glColor4dv.argtypes = [POINTER(GLdouble)]
    glColor4dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1139
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4fv'):
        continue
    glColor4fv = _lib.glColor4fv
    glColor4fv.argtypes = [POINTER(GLfloat)]
    glColor4fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1140
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4iv'):
        continue
    glColor4iv = _lib.glColor4iv
    glColor4iv.argtypes = [POINTER(GLint)]
    glColor4iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1141
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4sv'):
        continue
    glColor4sv = _lib.glColor4sv
    glColor4sv.argtypes = [POINTER(GLshort)]
    glColor4sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1142
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4ubv'):
        continue
    glColor4ubv = _lib.glColor4ubv
    glColor4ubv.argtypes = [POINTER(GLubyte)]
    glColor4ubv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1143
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4uiv'):
        continue
    glColor4uiv = _lib.glColor4uiv
    glColor4uiv.argtypes = [POINTER(GLuint)]
    glColor4uiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1144
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColor4usv'):
        continue
    glColor4usv = _lib.glColor4usv
    glColor4usv.argtypes = [POINTER(GLushort)]
    glColor4usv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1145
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1d'):
        continue
    glTexCoord1d = _lib.glTexCoord1d
    glTexCoord1d.argtypes = [GLdouble]
    glTexCoord1d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1146
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1f'):
        continue
    glTexCoord1f = _lib.glTexCoord1f
    glTexCoord1f.argtypes = [GLfloat]
    glTexCoord1f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1147
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1i'):
        continue
    glTexCoord1i = _lib.glTexCoord1i
    glTexCoord1i.argtypes = [GLint]
    glTexCoord1i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1148
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1s'):
        continue
    glTexCoord1s = _lib.glTexCoord1s
    glTexCoord1s.argtypes = [GLshort]
    glTexCoord1s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1149
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2d'):
        continue
    glTexCoord2d = _lib.glTexCoord2d
    glTexCoord2d.argtypes = [GLdouble, GLdouble]
    glTexCoord2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1150
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2f'):
        continue
    glTexCoord2f = _lib.glTexCoord2f
    glTexCoord2f.argtypes = [GLfloat, GLfloat]
    glTexCoord2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1151
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2i'):
        continue
    glTexCoord2i = _lib.glTexCoord2i
    glTexCoord2i.argtypes = [GLint, GLint]
    glTexCoord2i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1152
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2s'):
        continue
    glTexCoord2s = _lib.glTexCoord2s
    glTexCoord2s.argtypes = [GLshort, GLshort]
    glTexCoord2s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1153
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3d'):
        continue
    glTexCoord3d = _lib.glTexCoord3d
    glTexCoord3d.argtypes = [GLdouble, GLdouble, GLdouble]
    glTexCoord3d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1154
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3f'):
        continue
    glTexCoord3f = _lib.glTexCoord3f
    glTexCoord3f.argtypes = [GLfloat, GLfloat, GLfloat]
    glTexCoord3f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1155
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3i'):
        continue
    glTexCoord3i = _lib.glTexCoord3i
    glTexCoord3i.argtypes = [GLint, GLint, GLint]
    glTexCoord3i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1156
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3s'):
        continue
    glTexCoord3s = _lib.glTexCoord3s
    glTexCoord3s.argtypes = [GLshort, GLshort, GLshort]
    glTexCoord3s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1157
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4d'):
        continue
    glTexCoord4d = _lib.glTexCoord4d
    glTexCoord4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glTexCoord4d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1158
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4f'):
        continue
    glTexCoord4f = _lib.glTexCoord4f
    glTexCoord4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glTexCoord4f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1159
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4i'):
        continue
    glTexCoord4i = _lib.glTexCoord4i
    glTexCoord4i.argtypes = [GLint, GLint, GLint, GLint]
    glTexCoord4i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1160
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4s'):
        continue
    glTexCoord4s = _lib.glTexCoord4s
    glTexCoord4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
    glTexCoord4s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1161
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1dv'):
        continue
    glTexCoord1dv = _lib.glTexCoord1dv
    glTexCoord1dv.argtypes = [POINTER(GLdouble)]
    glTexCoord1dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1162
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1fv'):
        continue
    glTexCoord1fv = _lib.glTexCoord1fv
    glTexCoord1fv.argtypes = [POINTER(GLfloat)]
    glTexCoord1fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1163
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1iv'):
        continue
    glTexCoord1iv = _lib.glTexCoord1iv
    glTexCoord1iv.argtypes = [POINTER(GLint)]
    glTexCoord1iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1164
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord1sv'):
        continue
    glTexCoord1sv = _lib.glTexCoord1sv
    glTexCoord1sv.argtypes = [POINTER(GLshort)]
    glTexCoord1sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1165
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2dv'):
        continue
    glTexCoord2dv = _lib.glTexCoord2dv
    glTexCoord2dv.argtypes = [POINTER(GLdouble)]
    glTexCoord2dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1166
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2fv'):
        continue
    glTexCoord2fv = _lib.glTexCoord2fv
    glTexCoord2fv.argtypes = [POINTER(GLfloat)]
    glTexCoord2fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1167
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2iv'):
        continue
    glTexCoord2iv = _lib.glTexCoord2iv
    glTexCoord2iv.argtypes = [POINTER(GLint)]
    glTexCoord2iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1168
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord2sv'):
        continue
    glTexCoord2sv = _lib.glTexCoord2sv
    glTexCoord2sv.argtypes = [POINTER(GLshort)]
    glTexCoord2sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1169
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3dv'):
        continue
    glTexCoord3dv = _lib.glTexCoord3dv
    glTexCoord3dv.argtypes = [POINTER(GLdouble)]
    glTexCoord3dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1170
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3fv'):
        continue
    glTexCoord3fv = _lib.glTexCoord3fv
    glTexCoord3fv.argtypes = [POINTER(GLfloat)]
    glTexCoord3fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1171
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3iv'):
        continue
    glTexCoord3iv = _lib.glTexCoord3iv
    glTexCoord3iv.argtypes = [POINTER(GLint)]
    glTexCoord3iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1172
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord3sv'):
        continue
    glTexCoord3sv = _lib.glTexCoord3sv
    glTexCoord3sv.argtypes = [POINTER(GLshort)]
    glTexCoord3sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1173
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4dv'):
        continue
    glTexCoord4dv = _lib.glTexCoord4dv
    glTexCoord4dv.argtypes = [POINTER(GLdouble)]
    glTexCoord4dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1174
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4fv'):
        continue
    glTexCoord4fv = _lib.glTexCoord4fv
    glTexCoord4fv.argtypes = [POINTER(GLfloat)]
    glTexCoord4fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1175
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4iv'):
        continue
    glTexCoord4iv = _lib.glTexCoord4iv
    glTexCoord4iv.argtypes = [POINTER(GLint)]
    glTexCoord4iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1176
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoord4sv'):
        continue
    glTexCoord4sv = _lib.glTexCoord4sv
    glTexCoord4sv.argtypes = [POINTER(GLshort)]
    glTexCoord4sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1177
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2d'):
        continue
    glRasterPos2d = _lib.glRasterPos2d
    glRasterPos2d.argtypes = [GLdouble, GLdouble]
    glRasterPos2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1178
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2f'):
        continue
    glRasterPos2f = _lib.glRasterPos2f
    glRasterPos2f.argtypes = [GLfloat, GLfloat]
    glRasterPos2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1179
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2i'):
        continue
    glRasterPos2i = _lib.glRasterPos2i
    glRasterPos2i.argtypes = [GLint, GLint]
    glRasterPos2i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1180
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2s'):
        continue
    glRasterPos2s = _lib.glRasterPos2s
    glRasterPos2s.argtypes = [GLshort, GLshort]
    glRasterPos2s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1181
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3d'):
        continue
    glRasterPos3d = _lib.glRasterPos3d
    glRasterPos3d.argtypes = [GLdouble, GLdouble, GLdouble]
    glRasterPos3d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1182
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3f'):
        continue
    glRasterPos3f = _lib.glRasterPos3f
    glRasterPos3f.argtypes = [GLfloat, GLfloat, GLfloat]
    glRasterPos3f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1183
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3i'):
        continue
    glRasterPos3i = _lib.glRasterPos3i
    glRasterPos3i.argtypes = [GLint, GLint, GLint]
    glRasterPos3i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1184
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3s'):
        continue
    glRasterPos3s = _lib.glRasterPos3s
    glRasterPos3s.argtypes = [GLshort, GLshort, GLshort]
    glRasterPos3s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1185
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4d'):
        continue
    glRasterPos4d = _lib.glRasterPos4d
    glRasterPos4d.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glRasterPos4d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1186
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4f'):
        continue
    glRasterPos4f = _lib.glRasterPos4f
    glRasterPos4f.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glRasterPos4f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1187
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4i'):
        continue
    glRasterPos4i = _lib.glRasterPos4i
    glRasterPos4i.argtypes = [GLint, GLint, GLint, GLint]
    glRasterPos4i.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1188
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4s'):
        continue
    glRasterPos4s = _lib.glRasterPos4s
    glRasterPos4s.argtypes = [GLshort, GLshort, GLshort, GLshort]
    glRasterPos4s.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1189
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2dv'):
        continue
    glRasterPos2dv = _lib.glRasterPos2dv
    glRasterPos2dv.argtypes = [POINTER(GLdouble)]
    glRasterPos2dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1190
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2fv'):
        continue
    glRasterPos2fv = _lib.glRasterPos2fv
    glRasterPos2fv.argtypes = [POINTER(GLfloat)]
    glRasterPos2fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1191
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2iv'):
        continue
    glRasterPos2iv = _lib.glRasterPos2iv
    glRasterPos2iv.argtypes = [POINTER(GLint)]
    glRasterPos2iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1192
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos2sv'):
        continue
    glRasterPos2sv = _lib.glRasterPos2sv
    glRasterPos2sv.argtypes = [POINTER(GLshort)]
    glRasterPos2sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1193
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3dv'):
        continue
    glRasterPos3dv = _lib.glRasterPos3dv
    glRasterPos3dv.argtypes = [POINTER(GLdouble)]
    glRasterPos3dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1194
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3fv'):
        continue
    glRasterPos3fv = _lib.glRasterPos3fv
    glRasterPos3fv.argtypes = [POINTER(GLfloat)]
    glRasterPos3fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1195
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3iv'):
        continue
    glRasterPos3iv = _lib.glRasterPos3iv
    glRasterPos3iv.argtypes = [POINTER(GLint)]
    glRasterPos3iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1196
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos3sv'):
        continue
    glRasterPos3sv = _lib.glRasterPos3sv
    glRasterPos3sv.argtypes = [POINTER(GLshort)]
    glRasterPos3sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1197
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4dv'):
        continue
    glRasterPos4dv = _lib.glRasterPos4dv
    glRasterPos4dv.argtypes = [POINTER(GLdouble)]
    glRasterPos4dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1198
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4fv'):
        continue
    glRasterPos4fv = _lib.glRasterPos4fv
    glRasterPos4fv.argtypes = [POINTER(GLfloat)]
    glRasterPos4fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1199
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4iv'):
        continue
    glRasterPos4iv = _lib.glRasterPos4iv
    glRasterPos4iv.argtypes = [POINTER(GLint)]
    glRasterPos4iv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1200
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRasterPos4sv'):
        continue
    glRasterPos4sv = _lib.glRasterPos4sv
    glRasterPos4sv.argtypes = [POINTER(GLshort)]
    glRasterPos4sv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1201
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectd'):
        continue
    glRectd = _lib.glRectd
    glRectd.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    glRectd.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1202
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectf'):
        continue
    glRectf = _lib.glRectf
    glRectf.argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
    glRectf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1203
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRecti'):
        continue
    glRecti = _lib.glRecti
    glRecti.argtypes = [GLint, GLint, GLint, GLint]
    glRecti.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1204
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRects'):
        continue
    glRects = _lib.glRects
    glRects.argtypes = [GLshort, GLshort, GLshort, GLshort]
    glRects.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1205
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectdv'):
        continue
    glRectdv = _lib.glRectdv
    glRectdv.argtypes = [POINTER(GLdouble), POINTER(GLdouble)]
    glRectdv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1206
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectfv'):
        continue
    glRectfv = _lib.glRectfv
    glRectfv.argtypes = [POINTER(GLfloat), POINTER(GLfloat)]
    glRectfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1207
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectiv'):
        continue
    glRectiv = _lib.glRectiv
    glRectiv.argtypes = [POINTER(GLint), POINTER(GLint)]
    glRectiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1208
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glRectsv'):
        continue
    glRectsv = _lib.glRectsv
    glRectsv.argtypes = [POINTER(GLshort), POINTER(GLshort)]
    glRectsv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1211
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glShadeModel'):
        continue
    glShadeModel = _lib.glShadeModel
    glShadeModel.argtypes = [GLenum]
    glShadeModel.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1212
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightf'):
        continue
    glLightf = _lib.glLightf
    glLightf.argtypes = [GLenum, GLenum, GLfloat]
    glLightf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1213
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLighti'):
        continue
    glLighti = _lib.glLighti
    glLighti.argtypes = [GLenum, GLenum, GLint]
    glLighti.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1214
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightfv'):
        continue
    glLightfv = _lib.glLightfv
    glLightfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glLightfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1215
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightiv'):
        continue
    glLightiv = _lib.glLightiv
    glLightiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glLightiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1216
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetLightfv'):
        continue
    glGetLightfv = _lib.glGetLightfv
    glGetLightfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetLightfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1217
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetLightiv'):
        continue
    glGetLightiv = _lib.glGetLightiv
    glGetLightiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetLightiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1218
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightModelf'):
        continue
    glLightModelf = _lib.glLightModelf
    glLightModelf.argtypes = [GLenum, GLfloat]
    glLightModelf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1219
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightModeli'):
        continue
    glLightModeli = _lib.glLightModeli
    glLightModeli.argtypes = [GLenum, GLint]
    glLightModeli.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1220
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightModelfv'):
        continue
    glLightModelfv = _lib.glLightModelfv
    glLightModelfv.argtypes = [GLenum, POINTER(GLfloat)]
    glLightModelfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1221
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLightModeliv'):
        continue
    glLightModeliv = _lib.glLightModeliv
    glLightModeliv.argtypes = [GLenum, POINTER(GLint)]
    glLightModeliv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1222
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMaterialf'):
        continue
    glMaterialf = _lib.glMaterialf
    glMaterialf.argtypes = [GLenum, GLenum, GLfloat]
    glMaterialf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1223
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMateriali'):
        continue
    glMateriali = _lib.glMateriali
    glMateriali.argtypes = [GLenum, GLenum, GLint]
    glMateriali.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1224
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMaterialfv'):
        continue
    glMaterialfv = _lib.glMaterialfv
    glMaterialfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glMaterialfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1225
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMaterialiv'):
        continue
    glMaterialiv = _lib.glMaterialiv
    glMaterialiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glMaterialiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1226
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetMaterialfv'):
        continue
    glGetMaterialfv = _lib.glGetMaterialfv
    glGetMaterialfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetMaterialfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1227
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetMaterialiv'):
        continue
    glGetMaterialiv = _lib.glGetMaterialiv
    glGetMaterialiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetMaterialiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1228
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColorMaterial'):
        continue
    glColorMaterial = _lib.glColorMaterial
    glColorMaterial.argtypes = [GLenum, GLenum]
    glColorMaterial.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1231
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelZoom'):
        continue
    glPixelZoom = _lib.glPixelZoom
    glPixelZoom.argtypes = [GLfloat, GLfloat]
    glPixelZoom.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1232
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelStoref'):
        continue
    glPixelStoref = _lib.glPixelStoref
    glPixelStoref.argtypes = [GLenum, GLfloat]
    glPixelStoref.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1233
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelStorei'):
        continue
    glPixelStorei = _lib.glPixelStorei
    glPixelStorei.argtypes = [GLenum, GLint]
    glPixelStorei.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1234
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelTransferf'):
        continue
    glPixelTransferf = _lib.glPixelTransferf
    glPixelTransferf.argtypes = [GLenum, GLfloat]
    glPixelTransferf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1235
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelTransferi'):
        continue
    glPixelTransferi = _lib.glPixelTransferi
    glPixelTransferi.argtypes = [GLenum, GLint]
    glPixelTransferi.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1236
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelMapfv'):
        continue
    glPixelMapfv = _lib.glPixelMapfv
    glPixelMapfv.argtypes = [GLenum, GLint, POINTER(GLfloat)]
    glPixelMapfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1237
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelMapuiv'):
        continue
    glPixelMapuiv = _lib.glPixelMapuiv
    glPixelMapuiv.argtypes = [GLenum, GLint, POINTER(GLuint)]
    glPixelMapuiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1238
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPixelMapusv'):
        continue
    glPixelMapusv = _lib.glPixelMapusv
    glPixelMapusv.argtypes = [GLenum, GLint, POINTER(GLushort)]
    glPixelMapusv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1239
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetPixelMapfv'):
        continue
    glGetPixelMapfv = _lib.glGetPixelMapfv
    glGetPixelMapfv.argtypes = [GLenum, POINTER(GLfloat)]
    glGetPixelMapfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1240
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetPixelMapuiv'):
        continue
    glGetPixelMapuiv = _lib.glGetPixelMapuiv
    glGetPixelMapuiv.argtypes = [GLenum, POINTER(GLuint)]
    glGetPixelMapuiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1241
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetPixelMapusv'):
        continue
    glGetPixelMapusv = _lib.glGetPixelMapusv
    glGetPixelMapusv.argtypes = [GLenum, POINTER(GLushort)]
    glGetPixelMapusv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1242
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glBitmap'):
        continue
    glBitmap = _lib.glBitmap
    glBitmap.argtypes = [GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, POINTER(GLubyte)]
    glBitmap.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1243
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glReadPixels'):
        continue
    glReadPixels = _lib.glReadPixels
    glReadPixels.argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
    glReadPixels.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1244
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDrawPixels'):
        continue
    glDrawPixels = _lib.glDrawPixels
    glDrawPixels.argtypes = [GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
    glDrawPixels.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1245
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCopyPixels'):
        continue
    glCopyPixels = _lib.glCopyPixels
    glCopyPixels.argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum]
    glCopyPixels.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1248
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glStencilFunc'):
        continue
    glStencilFunc = _lib.glStencilFunc
    glStencilFunc.argtypes = [GLenum, GLint, GLuint]
    glStencilFunc.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1249
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glStencilMask'):
        continue
    glStencilMask = _lib.glStencilMask
    glStencilMask.argtypes = [GLuint]
    glStencilMask.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1250
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glStencilOp'):
        continue
    glStencilOp = _lib.glStencilOp
    glStencilOp.argtypes = [GLenum, GLenum, GLenum]
    glStencilOp.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1251
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glClearStencil'):
        continue
    glClearStencil = _lib.glClearStencil
    glClearStencil.argtypes = [GLint]
    glClearStencil.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1254
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGend'):
        continue
    glTexGend = _lib.glTexGend
    glTexGend.argtypes = [GLenum, GLenum, GLdouble]
    glTexGend.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1255
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGenf'):
        continue
    glTexGenf = _lib.glTexGenf
    glTexGenf.argtypes = [GLenum, GLenum, GLfloat]
    glTexGenf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1256
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGeni'):
        continue
    glTexGeni = _lib.glTexGeni
    glTexGeni.argtypes = [GLenum, GLenum, GLint]
    glTexGeni.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1257
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGendv'):
        continue
    glTexGendv = _lib.glTexGendv
    glTexGendv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
    glTexGendv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1258
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGenfv'):
        continue
    glTexGenfv = _lib.glTexGenfv
    glTexGenfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glTexGenfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1259
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexGeniv'):
        continue
    glTexGeniv = _lib.glTexGeniv
    glTexGeniv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glTexGeniv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1260
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexGendv'):
        continue
    glGetTexGendv = _lib.glGetTexGendv
    glGetTexGendv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
    glGetTexGendv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1261
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexGenfv'):
        continue
    glGetTexGenfv = _lib.glGetTexGenfv
    glGetTexGenfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetTexGenfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1262
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexGeniv'):
        continue
    glGetTexGeniv = _lib.glGetTexGeniv
    glGetTexGeniv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetTexGeniv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1263
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexEnvf'):
        continue
    glTexEnvf = _lib.glTexEnvf
    glTexEnvf.argtypes = [GLenum, GLenum, GLfloat]
    glTexEnvf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1264
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexEnvi'):
        continue
    glTexEnvi = _lib.glTexEnvi
    glTexEnvi.argtypes = [GLenum, GLenum, GLint]
    glTexEnvi.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1265
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexEnvfv'):
        continue
    glTexEnvfv = _lib.glTexEnvfv
    glTexEnvfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glTexEnvfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1266
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexEnviv'):
        continue
    glTexEnviv = _lib.glTexEnviv
    glTexEnviv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glTexEnviv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1267
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexEnvfv'):
        continue
    glGetTexEnvfv = _lib.glGetTexEnvfv
    glGetTexEnvfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetTexEnvfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1268
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexEnviv'):
        continue
    glGetTexEnviv = _lib.glGetTexEnviv
    glGetTexEnviv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetTexEnviv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1269
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexParameterf'):
        continue
    glTexParameterf = _lib.glTexParameterf
    glTexParameterf.argtypes = [GLenum, GLenum, GLfloat]
    glTexParameterf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1270
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexParameteri'):
        continue
    glTexParameteri = _lib.glTexParameteri
    glTexParameteri.argtypes = [GLenum, GLenum, GLint]
    glTexParameteri.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1271
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexParameterfv'):
        continue
    glTexParameterfv = _lib.glTexParameterfv
    glTexParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glTexParameterfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1272
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexParameteriv'):
        continue
    glTexParameteriv = _lib.glTexParameteriv
    glTexParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glTexParameteriv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1273
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexParameterfv'):
        continue
    glGetTexParameterfv = _lib.glGetTexParameterfv
    glGetTexParameterfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetTexParameterfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1274
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexParameteriv'):
        continue
    glGetTexParameteriv = _lib.glGetTexParameteriv
    glGetTexParameteriv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetTexParameteriv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1275
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexLevelParameterfv'):
        continue
    glGetTexLevelParameterfv = _lib.glGetTexLevelParameterfv
    glGetTexLevelParameterfv.argtypes = [GLenum, GLint, GLenum, POINTER(GLfloat)]
    glGetTexLevelParameterfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1276
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexLevelParameteriv'):
        continue
    glGetTexLevelParameteriv = _lib.glGetTexLevelParameteriv
    glGetTexLevelParameteriv.argtypes = [GLenum, GLint, GLenum, POINTER(GLint)]
    glGetTexLevelParameteriv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1277
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexImage1D'):
        continue
    glTexImage1D = _lib.glTexImage1D
    glTexImage1D.argtypes = [GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)]
    glTexImage1D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1278
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexImage2D'):
        continue
    glTexImage2D = _lib.glTexImage2D
    glTexImage2D.argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid)]
    glTexImage2D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1279
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetTexImage'):
        continue
    glGetTexImage = _lib.glGetTexImage
    glGetTexImage.argtypes = [GLenum, GLint, GLenum, GLenum, POINTER(GLvoid)]
    glGetTexImage.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1282
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMap1d'):
        continue
    glMap1d = _lib.glMap1d
    glMap1d.argtypes = [GLenum, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)]
    glMap1d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1283
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMap1f'):
        continue
    glMap1f = _lib.glMap1f
    glMap1f.argtypes = [GLenum, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)]
    glMap1f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1284
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMap2d'):
        continue
    glMap2d = _lib.glMap2d
    glMap2d.argtypes = [GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble)]
    glMap2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1285
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMap2f'):
        continue
    glMap2f = _lib.glMap2f
    glMap2f.argtypes = [GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat)]
    glMap2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1286
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetMapdv'):
        continue
    glGetMapdv = _lib.glGetMapdv
    glGetMapdv.argtypes = [GLenum, GLenum, POINTER(GLdouble)]
    glGetMapdv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1287
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetMapfv'):
        continue
    glGetMapfv = _lib.glGetMapfv
    glGetMapfv.argtypes = [GLenum, GLenum, POINTER(GLfloat)]
    glGetMapfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1288
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetMapiv'):
        continue
    glGetMapiv = _lib.glGetMapiv
    glGetMapiv.argtypes = [GLenum, GLenum, POINTER(GLint)]
    glGetMapiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1289
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord1d'):
        continue
    glEvalCoord1d = _lib.glEvalCoord1d
    glEvalCoord1d.argtypes = [GLdouble]
    glEvalCoord1d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1290
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord1f'):
        continue
    glEvalCoord1f = _lib.glEvalCoord1f
    glEvalCoord1f.argtypes = [GLfloat]
    glEvalCoord1f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1291
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord1dv'):
        continue
    glEvalCoord1dv = _lib.glEvalCoord1dv
    glEvalCoord1dv.argtypes = [POINTER(GLdouble)]
    glEvalCoord1dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1292
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord1fv'):
        continue
    glEvalCoord1fv = _lib.glEvalCoord1fv
    glEvalCoord1fv.argtypes = [POINTER(GLfloat)]
    glEvalCoord1fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1293
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord2d'):
        continue
    glEvalCoord2d = _lib.glEvalCoord2d
    glEvalCoord2d.argtypes = [GLdouble, GLdouble]
    glEvalCoord2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1294
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord2f'):
        continue
    glEvalCoord2f = _lib.glEvalCoord2f
    glEvalCoord2f.argtypes = [GLfloat, GLfloat]
    glEvalCoord2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1295
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord2dv'):
        continue
    glEvalCoord2dv = _lib.glEvalCoord2dv
    glEvalCoord2dv.argtypes = [POINTER(GLdouble)]
    glEvalCoord2dv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1296
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalCoord2fv'):
        continue
    glEvalCoord2fv = _lib.glEvalCoord2fv
    glEvalCoord2fv.argtypes = [POINTER(GLfloat)]
    glEvalCoord2fv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1297
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMapGrid1d'):
        continue
    glMapGrid1d = _lib.glMapGrid1d
    glMapGrid1d.argtypes = [GLint, GLdouble, GLdouble]
    glMapGrid1d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1298
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMapGrid1f'):
        continue
    glMapGrid1f = _lib.glMapGrid1f
    glMapGrid1f.argtypes = [GLint, GLfloat, GLfloat]
    glMapGrid1f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1299
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMapGrid2d'):
        continue
    glMapGrid2d = _lib.glMapGrid2d
    glMapGrid2d.argtypes = [GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble]
    glMapGrid2d.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1300
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glMapGrid2f'):
        continue
    glMapGrid2f = _lib.glMapGrid2f
    glMapGrid2f.argtypes = [GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat]
    glMapGrid2f.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1301
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalPoint1'):
        continue
    glEvalPoint1 = _lib.glEvalPoint1
    glEvalPoint1.argtypes = [GLint]
    glEvalPoint1.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1302
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalPoint2'):
        continue
    glEvalPoint2 = _lib.glEvalPoint2
    glEvalPoint2.argtypes = [GLint, GLint]
    glEvalPoint2.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1303
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalMesh1'):
        continue
    glEvalMesh1 = _lib.glEvalMesh1
    glEvalMesh1.argtypes = [GLenum, GLint, GLint]
    glEvalMesh1.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1304
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEvalMesh2'):
        continue
    glEvalMesh2 = _lib.glEvalMesh2
    glEvalMesh2.argtypes = [GLenum, GLint, GLint, GLint, GLint]
    glEvalMesh2.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1307
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFogf'):
        continue
    glFogf = _lib.glFogf
    glFogf.argtypes = [GLenum, GLfloat]
    glFogf.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1308
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFogi'):
        continue
    glFogi = _lib.glFogi
    glFogi.argtypes = [GLenum, GLint]
    glFogi.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1309
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFogfv'):
        continue
    glFogfv = _lib.glFogfv
    glFogfv.argtypes = [GLenum, POINTER(GLfloat)]
    glFogfv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1310
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFogiv'):
        continue
    glFogiv = _lib.glFogiv
    glFogiv.argtypes = [GLenum, POINTER(GLint)]
    glFogiv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1313
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glFeedbackBuffer'):
        continue
    glFeedbackBuffer = _lib.glFeedbackBuffer
    glFeedbackBuffer.argtypes = [GLsizei, GLenum, POINTER(GLfloat)]
    glFeedbackBuffer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1314
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPassThrough'):
        continue
    glPassThrough = _lib.glPassThrough
    glPassThrough.argtypes = [GLfloat]
    glPassThrough.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1315
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glSelectBuffer'):
        continue
    glSelectBuffer = _lib.glSelectBuffer
    glSelectBuffer.argtypes = [GLsizei, POINTER(GLuint)]
    glSelectBuffer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1316
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glInitNames'):
        continue
    glInitNames = _lib.glInitNames
    glInitNames.argtypes = []
    glInitNames.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1317
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glLoadName'):
        continue
    glLoadName = _lib.glLoadName
    glLoadName.argtypes = [GLuint]
    glLoadName.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1318
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPushName'):
        continue
    glPushName = _lib.glPushName
    glPushName.argtypes = [GLuint]
    glPushName.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1319
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPopName'):
        continue
    glPopName = _lib.glPopName
    glPopName.argtypes = []
    glPopName.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1324
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGenTextures'):
        continue
    glGenTextures = _lib.glGenTextures
    glGenTextures.argtypes = [GLsizei, POINTER(GLuint)]
    glGenTextures.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1325
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDeleteTextures'):
        continue
    glDeleteTextures = _lib.glDeleteTextures
    glDeleteTextures.argtypes = [GLsizei, POINTER(GLuint)]
    glDeleteTextures.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1326
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glBindTexture'):
        continue
    glBindTexture = _lib.glBindTexture
    glBindTexture.argtypes = [GLenum, GLuint]
    glBindTexture.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1327
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glPrioritizeTextures'):
        continue
    glPrioritizeTextures = _lib.glPrioritizeTextures
    glPrioritizeTextures.argtypes = [GLsizei, POINTER(GLuint), POINTER(GLclampf)]
    glPrioritizeTextures.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1328
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glAreTexturesResident'):
        continue
    glAreTexturesResident = _lib.glAreTexturesResident
    glAreTexturesResident.argtypes = [GLsizei, POINTER(GLuint), POINTER(GLboolean)]
    glAreTexturesResident.restype = GLboolean
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1329
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIsTexture'):
        continue
    glIsTexture = _lib.glIsTexture
    glIsTexture.argtypes = [GLuint]
    glIsTexture.restype = GLboolean
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1331
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexSubImage1D'):
        continue
    glTexSubImage1D = _lib.glTexSubImage1D
    glTexSubImage1D.argtypes = [GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
    glTexSubImage1D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1332
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexSubImage2D'):
        continue
    glTexSubImage2D = _lib.glTexSubImage2D
    glTexSubImage2D.argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid)]
    glTexSubImage2D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1333
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCopyTexImage1D'):
        continue
    glCopyTexImage1D = _lib.glCopyTexImage1D
    glCopyTexImage1D.argtypes = [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint]
    glCopyTexImage1D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1334
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCopyTexImage2D'):
        continue
    glCopyTexImage2D = _lib.glCopyTexImage2D
    glCopyTexImage2D.argtypes = [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint]
    glCopyTexImage2D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1335
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCopyTexSubImage1D'):
        continue
    glCopyTexSubImage1D = _lib.glCopyTexSubImage1D
    glCopyTexSubImage1D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei]
    glCopyTexSubImage1D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1336
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glCopyTexSubImage2D'):
        continue
    glCopyTexSubImage2D = _lib.glCopyTexSubImage2D
    glCopyTexSubImage2D.argtypes = [GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei]
    glCopyTexSubImage2D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1338
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glVertexPointer'):
        continue
    glVertexPointer = _lib.glVertexPointer
    glVertexPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
    glVertexPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1339
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glNormalPointer'):
        continue
    glNormalPointer = _lib.glNormalPointer
    glNormalPointer.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
    glNormalPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1340
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glColorPointer'):
        continue
    glColorPointer = _lib.glColorPointer
    glColorPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
    glColorPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glIndexPointer'):
        continue
    glIndexPointer = _lib.glIndexPointer
    glIndexPointer.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
    glIndexPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glTexCoordPointer'):
        continue
    glTexCoordPointer = _lib.glTexCoordPointer
    glTexCoordPointer.argtypes = [GLint, GLenum, GLsizei, POINTER(GLvoid)]
    glTexCoordPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glEdgeFlagPointer'):
        continue
    glEdgeFlagPointer = _lib.glEdgeFlagPointer
    glEdgeFlagPointer.argtypes = [GLsizei, POINTER(GLvoid)]
    glEdgeFlagPointer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1344
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glGetPointerv'):
        continue
    glGetPointerv = _lib.glGetPointerv
    glGetPointerv.argtypes = [GLenum, POINTER(POINTER(GLvoid))]
    glGetPointerv.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1345
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glArrayElement'):
        continue
    glArrayElement = _lib.glArrayElement
    glArrayElement.argtypes = [GLint]
    glArrayElement.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1346
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDrawArrays'):
        continue
    glDrawArrays = _lib.glDrawArrays
    glDrawArrays.argtypes = [GLenum, GLint, GLsizei]
    glDrawArrays.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1347
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glDrawElements'):
        continue
    glDrawElements = _lib.glDrawElements
    glDrawElements.argtypes = [GLenum, GLsizei, GLenum, POINTER(GLvoid)]
    glDrawElements.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 1348
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glInterleavedArrays'):
        continue
    glInterleavedArrays = _lib.glInterleavedArrays
    glInterleavedArrays.argtypes = [GLenum, GLsizei, POINTER(GLvoid)]
    glInterleavedArrays.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 210
class struct_GLUnurbs(Structure):
    pass

GLUnurbs = struct_GLUnurbs # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 210

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 211
class struct_GLUquadric(Structure):
    pass

GLUquadric = struct_GLUquadric # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 211

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 212
class struct_GLUtesselator(Structure):
    pass

GLUtesselator = struct_GLUtesselator # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 212

GLUnurbsObj = GLUnurbs # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 215

GLUquadricObj = GLUquadric # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 216

GLUtesselatorObj = GLUtesselator # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 217

GLUtriangulatorObj = GLUtesselator # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 218

_GLUfuncptr = CFUNCTYPE(UNCHECKED(None), ) # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 223

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 225
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBeginCurve'):
        continue
    gluBeginCurve = _lib.gluBeginCurve
    gluBeginCurve.argtypes = [POINTER(GLUnurbs)]
    gluBeginCurve.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 226
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBeginPolygon'):
        continue
    gluBeginPolygon = _lib.gluBeginPolygon
    gluBeginPolygon.argtypes = [POINTER(GLUtesselator)]
    gluBeginPolygon.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 227
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBeginSurface'):
        continue
    gluBeginSurface = _lib.gluBeginSurface
    gluBeginSurface.argtypes = [POINTER(GLUnurbs)]
    gluBeginSurface.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 228
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBeginTrim'):
        continue
    gluBeginTrim = _lib.gluBeginTrim
    gluBeginTrim.argtypes = [POINTER(GLUnurbs)]
    gluBeginTrim.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 229
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBuild1DMipmaps'):
        continue
    gluBuild1DMipmaps = _lib.gluBuild1DMipmaps
    gluBuild1DMipmaps.argtypes = [GLenum, GLint, GLsizei, GLenum, GLenum, POINTER(None)]
    gluBuild1DMipmaps.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 230
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluBuild2DMipmaps'):
        continue
    gluBuild2DMipmaps = _lib.gluBuild2DMipmaps
    gluBuild2DMipmaps.argtypes = [GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None)]
    gluBuild2DMipmaps.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 231
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluCylinder'):
        continue
    gluCylinder = _lib.gluCylinder
    gluCylinder.argtypes = [POINTER(GLUquadric), GLdouble, GLdouble, GLdouble, GLint, GLint]
    gluCylinder.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 232
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluDeleteNurbsRenderer'):
        continue
    gluDeleteNurbsRenderer = _lib.gluDeleteNurbsRenderer
    gluDeleteNurbsRenderer.argtypes = [POINTER(GLUnurbs)]
    gluDeleteNurbsRenderer.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 233
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluDeleteQuadric'):
        continue
    gluDeleteQuadric = _lib.gluDeleteQuadric
    gluDeleteQuadric.argtypes = [POINTER(GLUquadric)]
    gluDeleteQuadric.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 234
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluDeleteTess'):
        continue
    gluDeleteTess = _lib.gluDeleteTess
    gluDeleteTess.argtypes = [POINTER(GLUtesselator)]
    gluDeleteTess.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 235
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluDisk'):
        continue
    gluDisk = _lib.gluDisk
    gluDisk.argtypes = [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint]
    gluDisk.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 236
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluEndCurve'):
        continue
    gluEndCurve = _lib.gluEndCurve
    gluEndCurve.argtypes = [POINTER(GLUnurbs)]
    gluEndCurve.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 237
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluEndPolygon'):
        continue
    gluEndPolygon = _lib.gluEndPolygon
    gluEndPolygon.argtypes = [POINTER(GLUtesselator)]
    gluEndPolygon.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 238
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluEndSurface'):
        continue
    gluEndSurface = _lib.gluEndSurface
    gluEndSurface.argtypes = [POINTER(GLUnurbs)]
    gluEndSurface.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 239
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluEndTrim'):
        continue
    gluEndTrim = _lib.gluEndTrim
    gluEndTrim.argtypes = [POINTER(GLUnurbs)]
    gluEndTrim.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 240
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluErrorString'):
        continue
    gluErrorString = _lib.gluErrorString
    gluErrorString.argtypes = [GLenum]
    gluErrorString.restype = POINTER(GLubyte)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 241
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluErrorUnicodeStringEXT'):
        continue
    gluErrorUnicodeStringEXT = _lib.gluErrorUnicodeStringEXT
    gluErrorUnicodeStringEXT.argtypes = [GLenum]
    gluErrorUnicodeStringEXT.restype = POINTER(c_wchar)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 242
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluGetNurbsProperty'):
        continue
    gluGetNurbsProperty = _lib.gluGetNurbsProperty
    gluGetNurbsProperty.argtypes = [POINTER(GLUnurbs), GLenum, POINTER(GLfloat)]
    gluGetNurbsProperty.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 243
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluGetString'):
        continue
    gluGetString = _lib.gluGetString
    gluGetString.argtypes = [GLenum]
    gluGetString.restype = POINTER(GLubyte)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 244
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluGetTessProperty'):
        continue
    gluGetTessProperty = _lib.gluGetTessProperty
    gluGetTessProperty.argtypes = [POINTER(GLUtesselator), GLenum, POINTER(GLdouble)]
    gluGetTessProperty.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 245
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluLoadSamplingMatrices'):
        continue
    gluLoadSamplingMatrices = _lib.gluLoadSamplingMatrices
    gluLoadSamplingMatrices.argtypes = [POINTER(GLUnurbs), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLint)]
    gluLoadSamplingMatrices.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 246
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluLookAt'):
        continue
    gluLookAt = _lib.gluLookAt
    gluLookAt.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]
    gluLookAt.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 247
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNewNurbsRenderer'):
        continue
    gluNewNurbsRenderer = _lib.gluNewNurbsRenderer
    gluNewNurbsRenderer.argtypes = []
    gluNewNurbsRenderer.restype = POINTER(GLUnurbs)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 248
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNewQuadric'):
        continue
    gluNewQuadric = _lib.gluNewQuadric
    gluNewQuadric.argtypes = []
    gluNewQuadric.restype = POINTER(GLUquadric)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 249
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNewTess'):
        continue
    gluNewTess = _lib.gluNewTess
    gluNewTess.argtypes = []
    gluNewTess.restype = POINTER(GLUtesselator)
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 250
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNextContour'):
        continue
    gluNextContour = _lib.gluNextContour
    gluNextContour.argtypes = [POINTER(GLUtesselator), GLenum]
    gluNextContour.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 251
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNurbsCallback'):
        continue
    gluNurbsCallback = _lib.gluNurbsCallback
    gluNurbsCallback.argtypes = [POINTER(GLUnurbs), GLenum, _GLUfuncptr]
    gluNurbsCallback.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 252
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNurbsCurve'):
        continue
    gluNurbsCurve = _lib.gluNurbsCurve
    gluNurbsCurve.argtypes = [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLenum]
    gluNurbsCurve.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 253
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNurbsProperty'):
        continue
    gluNurbsProperty = _lib.gluNurbsProperty
    gluNurbsProperty.argtypes = [POINTER(GLUnurbs), GLenum, GLfloat]
    gluNurbsProperty.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 254
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluNurbsSurface'):
        continue
    gluNurbsSurface = _lib.gluNurbsSurface
    gluNurbsSurface.argtypes = [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLint, POINTER(GLfloat), GLint, GLint, GLenum]
    gluNurbsSurface.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 255
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluOrtho2D'):
        continue
    gluOrtho2D = _lib.gluOrtho2D
    gluOrtho2D.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    gluOrtho2D.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 256
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluPartialDisk'):
        continue
    gluPartialDisk = _lib.gluPartialDisk
    gluPartialDisk.argtypes = [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble]
    gluPartialDisk.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 257
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluPerspective'):
        continue
    gluPerspective = _lib.gluPerspective
    gluPerspective.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]
    gluPerspective.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 258
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluPickMatrix'):
        continue
    gluPickMatrix = _lib.gluPickMatrix
    gluPickMatrix.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLint)]
    gluPickMatrix.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 259
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluProject'):
        continue
    gluProject = _lib.gluProject
    gluProject.argtypes = [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)]
    gluProject.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 260
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluPwlCurve'):
        continue
    gluPwlCurve = _lib.gluPwlCurve
    gluPwlCurve.argtypes = [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, GLenum]
    gluPwlCurve.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 261
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluQuadricCallback'):
        continue
    gluQuadricCallback = _lib.gluQuadricCallback
    gluQuadricCallback.argtypes = [POINTER(GLUquadric), GLenum, _GLUfuncptr]
    gluQuadricCallback.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 262
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluQuadricDrawStyle'):
        continue
    gluQuadricDrawStyle = _lib.gluQuadricDrawStyle
    gluQuadricDrawStyle.argtypes = [POINTER(GLUquadric), GLenum]
    gluQuadricDrawStyle.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 263
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluQuadricNormals'):
        continue
    gluQuadricNormals = _lib.gluQuadricNormals
    gluQuadricNormals.argtypes = [POINTER(GLUquadric), GLenum]
    gluQuadricNormals.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 264
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluQuadricOrientation'):
        continue
    gluQuadricOrientation = _lib.gluQuadricOrientation
    gluQuadricOrientation.argtypes = [POINTER(GLUquadric), GLenum]
    gluQuadricOrientation.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 265
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluQuadricTexture'):
        continue
    gluQuadricTexture = _lib.gluQuadricTexture
    gluQuadricTexture.argtypes = [POINTER(GLUquadric), GLboolean]
    gluQuadricTexture.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 266
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluScaleImage'):
        continue
    gluScaleImage = _lib.gluScaleImage
    gluScaleImage.argtypes = [GLenum, GLsizei, GLsizei, GLenum, POINTER(None), GLsizei, GLsizei, GLenum, POINTER(GLvoid)]
    gluScaleImage.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 267
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluSphere'):
        continue
    gluSphere = _lib.gluSphere
    gluSphere.argtypes = [POINTER(GLUquadric), GLdouble, GLint, GLint]
    gluSphere.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 268
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessBeginContour'):
        continue
    gluTessBeginContour = _lib.gluTessBeginContour
    gluTessBeginContour.argtypes = [POINTER(GLUtesselator)]
    gluTessBeginContour.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 269
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessBeginPolygon'):
        continue
    gluTessBeginPolygon = _lib.gluTessBeginPolygon
    gluTessBeginPolygon.argtypes = [POINTER(GLUtesselator), POINTER(GLvoid)]
    gluTessBeginPolygon.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 270
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessCallback'):
        continue
    gluTessCallback = _lib.gluTessCallback
    gluTessCallback.argtypes = [POINTER(GLUtesselator), GLenum, _GLUfuncptr]
    gluTessCallback.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 271
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessEndContour'):
        continue
    gluTessEndContour = _lib.gluTessEndContour
    gluTessEndContour.argtypes = [POINTER(GLUtesselator)]
    gluTessEndContour.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 272
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessEndPolygon'):
        continue
    gluTessEndPolygon = _lib.gluTessEndPolygon
    gluTessEndPolygon.argtypes = [POINTER(GLUtesselator)]
    gluTessEndPolygon.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 273
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessNormal'):
        continue
    gluTessNormal = _lib.gluTessNormal
    gluTessNormal.argtypes = [POINTER(GLUtesselator), GLdouble, GLdouble, GLdouble]
    gluTessNormal.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 274
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessProperty'):
        continue
    gluTessProperty = _lib.gluTessProperty
    gluTessProperty.argtypes = [POINTER(GLUtesselator), GLenum, GLdouble]
    gluTessProperty.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 275
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluTessVertex'):
        continue
    gluTessVertex = _lib.gluTessVertex
    gluTessVertex.argtypes = [POINTER(GLUtesselator), POINTER(GLdouble), POINTER(GLvoid)]
    gluTessVertex.restype = None
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 276
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluUnProject'):
        continue
    gluUnProject = _lib.gluUnProject
    gluUnProject.argtypes = [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)]
    gluUnProject.restype = GLint
    break

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 277
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'gluUnProject4'):
        continue
    gluUnProject4 = _lib.gluUnProject4
    gluUnProject4.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)]
    gluUnProject4.restype = GLint
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 146
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'exit'):
        continue
    exit = _lib.exit
    exit.argtypes = [c_int]
    exit.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 482
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutInit'):
        continue
    glutInit = _lib.glutInit
    glutInit.argtypes = [POINTER(c_int), POINTER(POINTER(c_char))]
    glutInit.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 484
for _lib in _libs.itervalues():
    if not hasattr(_lib, '__glutInitWithExit'):
        continue
    __glutInitWithExit = _lib.__glutInitWithExit
    __glutInitWithExit.argtypes = [POINTER(c_int), POINTER(POINTER(c_char)), CFUNCTYPE(UNCHECKED(None), c_int)]
    __glutInitWithExit.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 490
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutInitDisplayMode'):
        continue
    glutInitDisplayMode = _lib.glutInitDisplayMode
    glutInitDisplayMode.argtypes = [c_uint]
    glutInitDisplayMode.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 492
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutInitDisplayString'):
        continue
    glutInitDisplayString = _lib.glutInitDisplayString
    glutInitDisplayString.argtypes = [String]
    glutInitDisplayString.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 494
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutInitWindowPosition'):
        continue
    glutInitWindowPosition = _lib.glutInitWindowPosition
    glutInitWindowPosition.argtypes = [c_int, c_int]
    glutInitWindowPosition.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 495
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutInitWindowSize'):
        continue
    glutInitWindowSize = _lib.glutInitWindowSize
    glutInitWindowSize.argtypes = [c_int, c_int]
    glutInitWindowSize.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 496
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutMainLoop'):
        continue
    glutMainLoop = _lib.glutMainLoop
    glutMainLoop.argtypes = []
    glutMainLoop.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 499
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutCreateWindow'):
        continue
    glutCreateWindow = _lib.glutCreateWindow
    glutCreateWindow.argtypes = [String]
    glutCreateWindow.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 501
for _lib in _libs.itervalues():
    if not hasattr(_lib, '__glutCreateWindowWithExit'):
        continue
    __glutCreateWindowWithExit = _lib.__glutCreateWindowWithExit
    __glutCreateWindowWithExit.argtypes = [String, CFUNCTYPE(UNCHECKED(None), c_int)]
    __glutCreateWindowWithExit.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 507
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutCreateSubWindow'):
        continue
    glutCreateSubWindow = _lib.glutCreateSubWindow
    glutCreateSubWindow.argtypes = [c_int, c_int, c_int, c_int, c_int]
    glutCreateSubWindow.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 508
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDestroyWindow'):
        continue
    glutDestroyWindow = _lib.glutDestroyWindow
    glutDestroyWindow.argtypes = [c_int]
    glutDestroyWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 509
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPostRedisplay'):
        continue
    glutPostRedisplay = _lib.glutPostRedisplay
    glutPostRedisplay.argtypes = []
    glutPostRedisplay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 511
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPostWindowRedisplay'):
        continue
    glutPostWindowRedisplay = _lib.glutPostWindowRedisplay
    glutPostWindowRedisplay.argtypes = [c_int]
    glutPostWindowRedisplay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 513
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSwapBuffers'):
        continue
    glutSwapBuffers = _lib.glutSwapBuffers
    glutSwapBuffers.argtypes = []
    glutSwapBuffers.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 514
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGetWindow'):
        continue
    glutGetWindow = _lib.glutGetWindow
    glutGetWindow.argtypes = []
    glutGetWindow.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 515
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetWindow'):
        continue
    glutSetWindow = _lib.glutSetWindow
    glutSetWindow.argtypes = [c_int]
    glutSetWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 516
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetWindowTitle'):
        continue
    glutSetWindowTitle = _lib.glutSetWindowTitle
    glutSetWindowTitle.argtypes = [String]
    glutSetWindowTitle.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 517
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetIconTitle'):
        continue
    glutSetIconTitle = _lib.glutSetIconTitle
    glutSetIconTitle.argtypes = [String]
    glutSetIconTitle.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 518
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPositionWindow'):
        continue
    glutPositionWindow = _lib.glutPositionWindow
    glutPositionWindow.argtypes = [c_int, c_int]
    glutPositionWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 519
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutReshapeWindow'):
        continue
    glutReshapeWindow = _lib.glutReshapeWindow
    glutReshapeWindow.argtypes = [c_int, c_int]
    glutReshapeWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 520
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPopWindow'):
        continue
    glutPopWindow = _lib.glutPopWindow
    glutPopWindow.argtypes = []
    glutPopWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 521
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPushWindow'):
        continue
    glutPushWindow = _lib.glutPushWindow
    glutPushWindow.argtypes = []
    glutPushWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 522
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutIconifyWindow'):
        continue
    glutIconifyWindow = _lib.glutIconifyWindow
    glutIconifyWindow.argtypes = []
    glutIconifyWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 523
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutShowWindow'):
        continue
    glutShowWindow = _lib.glutShowWindow
    glutShowWindow.argtypes = []
    glutShowWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 524
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutHideWindow'):
        continue
    glutHideWindow = _lib.glutHideWindow
    glutHideWindow.argtypes = []
    glutHideWindow.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 526
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutFullScreen'):
        continue
    glutFullScreen = _lib.glutFullScreen
    glutFullScreen.argtypes = []
    glutFullScreen.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 527
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetCursor'):
        continue
    glutSetCursor = _lib.glutSetCursor
    glutSetCursor.argtypes = [c_int]
    glutSetCursor.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 529
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWarpPointer'):
        continue
    glutWarpPointer = _lib.glutWarpPointer
    glutWarpPointer.argtypes = [c_int, c_int]
    glutWarpPointer.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 533
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutEstablishOverlay'):
        continue
    glutEstablishOverlay = _lib.glutEstablishOverlay
    glutEstablishOverlay.argtypes = []
    glutEstablishOverlay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 534
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutRemoveOverlay'):
        continue
    glutRemoveOverlay = _lib.glutRemoveOverlay
    glutRemoveOverlay.argtypes = []
    glutRemoveOverlay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 535
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutUseLayer'):
        continue
    glutUseLayer = _lib.glutUseLayer
    glutUseLayer.argtypes = [GLenum]
    glutUseLayer.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 536
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPostOverlayRedisplay'):
        continue
    glutPostOverlayRedisplay = _lib.glutPostOverlayRedisplay
    glutPostOverlayRedisplay.argtypes = []
    glutPostOverlayRedisplay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 538
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPostWindowOverlayRedisplay'):
        continue
    glutPostWindowOverlayRedisplay = _lib.glutPostWindowOverlayRedisplay
    glutPostWindowOverlayRedisplay.argtypes = [c_int]
    glutPostWindowOverlayRedisplay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 540
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutShowOverlay'):
        continue
    glutShowOverlay = _lib.glutShowOverlay
    glutShowOverlay.argtypes = []
    glutShowOverlay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 541
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutHideOverlay'):
        continue
    glutHideOverlay = _lib.glutHideOverlay
    glutHideOverlay.argtypes = []
    glutHideOverlay.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 545
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutCreateMenu'):
        continue
    glutCreateMenu = _lib.glutCreateMenu
    glutCreateMenu.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    glutCreateMenu.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 547
for _lib in _libs.itervalues():
    if not hasattr(_lib, '__glutCreateMenuWithExit'):
        continue
    __glutCreateMenuWithExit = _lib.__glutCreateMenuWithExit
    __glutCreateMenuWithExit.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int), CFUNCTYPE(UNCHECKED(None), c_int)]
    __glutCreateMenuWithExit.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 553
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDestroyMenu'):
        continue
    glutDestroyMenu = _lib.glutDestroyMenu
    glutDestroyMenu.argtypes = [c_int]
    glutDestroyMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 554
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGetMenu'):
        continue
    glutGetMenu = _lib.glutGetMenu
    glutGetMenu.argtypes = []
    glutGetMenu.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 555
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetMenu'):
        continue
    glutSetMenu = _lib.glutSetMenu
    glutSetMenu.argtypes = [c_int]
    glutSetMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 556
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutAddMenuEntry'):
        continue
    glutAddMenuEntry = _lib.glutAddMenuEntry
    glutAddMenuEntry.argtypes = [String, c_int]
    glutAddMenuEntry.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 557
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutAddSubMenu'):
        continue
    glutAddSubMenu = _lib.glutAddSubMenu
    glutAddSubMenu.argtypes = [String, c_int]
    glutAddSubMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 558
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutChangeToMenuEntry'):
        continue
    glutChangeToMenuEntry = _lib.glutChangeToMenuEntry
    glutChangeToMenuEntry.argtypes = [c_int, String, c_int]
    glutChangeToMenuEntry.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 559
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutChangeToSubMenu'):
        continue
    glutChangeToSubMenu = _lib.glutChangeToSubMenu
    glutChangeToSubMenu.argtypes = [c_int, String, c_int]
    glutChangeToSubMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 560
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutRemoveMenuItem'):
        continue
    glutRemoveMenuItem = _lib.glutRemoveMenuItem
    glutRemoveMenuItem.argtypes = [c_int]
    glutRemoveMenuItem.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 561
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutAttachMenu'):
        continue
    glutAttachMenu = _lib.glutAttachMenu
    glutAttachMenu.argtypes = [c_int]
    glutAttachMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 562
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDetachMenu'):
        continue
    glutDetachMenu = _lib.glutDetachMenu
    glutDetachMenu.argtypes = [c_int]
    glutDetachMenu.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 565
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDisplayFunc'):
        continue
    glutDisplayFunc = _lib.glutDisplayFunc
    glutDisplayFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    glutDisplayFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 566
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutReshapeFunc'):
        continue
    glutReshapeFunc = _lib.glutReshapeFunc
    glutReshapeFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutReshapeFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 567
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutKeyboardFunc'):
        continue
    glutKeyboardFunc = _lib.glutKeyboardFunc
    glutKeyboardFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_ubyte, c_int, c_int)]
    glutKeyboardFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 568
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutMouseFunc'):
        continue
    glutMouseFunc = _lib.glutMouseFunc
    glutMouseFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int, c_int)]
    glutMouseFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 569
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutMotionFunc'):
        continue
    glutMotionFunc = _lib.glutMotionFunc
    glutMotionFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutMotionFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 570
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutPassiveMotionFunc'):
        continue
    glutPassiveMotionFunc = _lib.glutPassiveMotionFunc
    glutPassiveMotionFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutPassiveMotionFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 571
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutEntryFunc'):
        continue
    glutEntryFunc = _lib.glutEntryFunc
    glutEntryFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    glutEntryFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 572
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutVisibilityFunc'):
        continue
    glutVisibilityFunc = _lib.glutVisibilityFunc
    glutVisibilityFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    glutVisibilityFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 573
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutIdleFunc'):
        continue
    glutIdleFunc = _lib.glutIdleFunc
    glutIdleFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    glutIdleFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 574
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutTimerFunc'):
        continue
    glutTimerFunc = _lib.glutTimerFunc
    glutTimerFunc.argtypes = [c_uint, CFUNCTYPE(UNCHECKED(None), c_int), c_int]
    glutTimerFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 575
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutMenuStateFunc'):
        continue
    glutMenuStateFunc = _lib.glutMenuStateFunc
    glutMenuStateFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    glutMenuStateFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 577
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSpecialFunc'):
        continue
    glutSpecialFunc = _lib.glutSpecialFunc
    glutSpecialFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int)]
    glutSpecialFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 578
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSpaceballMotionFunc'):
        continue
    glutSpaceballMotionFunc = _lib.glutSpaceballMotionFunc
    glutSpaceballMotionFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int)]
    glutSpaceballMotionFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 579
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSpaceballRotateFunc'):
        continue
    glutSpaceballRotateFunc = _lib.glutSpaceballRotateFunc
    glutSpaceballRotateFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int)]
    glutSpaceballRotateFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 580
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSpaceballButtonFunc'):
        continue
    glutSpaceballButtonFunc = _lib.glutSpaceballButtonFunc
    glutSpaceballButtonFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutSpaceballButtonFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 581
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutButtonBoxFunc'):
        continue
    glutButtonBoxFunc = _lib.glutButtonBoxFunc
    glutButtonBoxFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutButtonBoxFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 582
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDialsFunc'):
        continue
    glutDialsFunc = _lib.glutDialsFunc
    glutDialsFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutDialsFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 583
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutTabletMotionFunc'):
        continue
    glutTabletMotionFunc = _lib.glutTabletMotionFunc
    glutTabletMotionFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int)]
    glutTabletMotionFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 584
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutTabletButtonFunc'):
        continue
    glutTabletButtonFunc = _lib.glutTabletButtonFunc
    glutTabletButtonFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int, c_int)]
    glutTabletButtonFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 586
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutMenuStatusFunc'):
        continue
    glutMenuStatusFunc = _lib.glutMenuStatusFunc
    glutMenuStatusFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int)]
    glutMenuStatusFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 587
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutOverlayDisplayFunc'):
        continue
    glutOverlayDisplayFunc = _lib.glutOverlayDisplayFunc
    glutOverlayDisplayFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    glutOverlayDisplayFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 589
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWindowStatusFunc'):
        continue
    glutWindowStatusFunc = _lib.glutWindowStatusFunc
    glutWindowStatusFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int)]
    glutWindowStatusFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 592
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutKeyboardUpFunc'):
        continue
    glutKeyboardUpFunc = _lib.glutKeyboardUpFunc
    glutKeyboardUpFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_ubyte, c_int, c_int)]
    glutKeyboardUpFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 593
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSpecialUpFunc'):
        continue
    glutSpecialUpFunc = _lib.glutSpecialUpFunc
    glutSpecialUpFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, c_int, c_int)]
    glutSpecialUpFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 594
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutJoystickFunc'):
        continue
    glutJoystickFunc = _lib.glutJoystickFunc
    glutJoystickFunc.argtypes = [CFUNCTYPE(UNCHECKED(None), c_uint, c_int, c_int, c_int), c_int]
    glutJoystickFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 600
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetColor'):
        continue
    glutSetColor = _lib.glutSetColor
    glutSetColor.argtypes = [c_int, GLfloat, GLfloat, GLfloat]
    glutSetColor.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 601
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGetColor'):
        continue
    glutGetColor = _lib.glutGetColor
    glutGetColor.argtypes = [c_int, c_int]
    glutGetColor.restype = GLfloat
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 602
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutCopyColormap'):
        continue
    glutCopyColormap = _lib.glutCopyColormap
    glutCopyColormap.argtypes = [c_int]
    glutCopyColormap.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 605
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGet'):
        continue
    glutGet = _lib.glutGet
    glutGet.argtypes = [GLenum]
    glutGet.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 606
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutDeviceGet'):
        continue
    glutDeviceGet = _lib.glutDeviceGet
    glutDeviceGet.argtypes = [GLenum]
    glutDeviceGet.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 609
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutExtensionSupported'):
        continue
    glutExtensionSupported = _lib.glutExtensionSupported
    glutExtensionSupported.argtypes = [String]
    glutExtensionSupported.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 612
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGetModifiers'):
        continue
    glutGetModifiers = _lib.glutGetModifiers
    glutGetModifiers.argtypes = []
    glutGetModifiers.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 613
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutLayerGet'):
        continue
    glutLayerGet = _lib.glutLayerGet
    glutLayerGet.argtypes = [GLenum]
    glutLayerGet.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 617
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutBitmapCharacter'):
        continue
    glutBitmapCharacter = _lib.glutBitmapCharacter
    glutBitmapCharacter.argtypes = [POINTER(None), c_int]
    glutBitmapCharacter.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 618
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutBitmapWidth'):
        continue
    glutBitmapWidth = _lib.glutBitmapWidth
    glutBitmapWidth.argtypes = [POINTER(None), c_int]
    glutBitmapWidth.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 619
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutStrokeCharacter'):
        continue
    glutStrokeCharacter = _lib.glutStrokeCharacter
    glutStrokeCharacter.argtypes = [POINTER(None), c_int]
    glutStrokeCharacter.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 620
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutStrokeWidth'):
        continue
    glutStrokeWidth = _lib.glutStrokeWidth
    glutStrokeWidth.argtypes = [POINTER(None), c_int]
    glutStrokeWidth.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 622
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutBitmapLength'):
        continue
    glutBitmapLength = _lib.glutBitmapLength
    glutBitmapLength.argtypes = [POINTER(None), POINTER(c_ubyte)]
    glutBitmapLength.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 623
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutStrokeLength'):
        continue
    glutStrokeLength = _lib.glutStrokeLength
    glutStrokeLength.argtypes = [POINTER(None), POINTER(c_ubyte)]
    glutStrokeLength.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 627
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireSphere'):
        continue
    glutWireSphere = _lib.glutWireSphere
    glutWireSphere.argtypes = [GLdouble, GLint, GLint]
    glutWireSphere.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 628
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidSphere'):
        continue
    glutSolidSphere = _lib.glutSolidSphere
    glutSolidSphere.argtypes = [GLdouble, GLint, GLint]
    glutSolidSphere.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 629
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireCone'):
        continue
    glutWireCone = _lib.glutWireCone
    glutWireCone.argtypes = [GLdouble, GLdouble, GLint, GLint]
    glutWireCone.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 630
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidCone'):
        continue
    glutSolidCone = _lib.glutSolidCone
    glutSolidCone.argtypes = [GLdouble, GLdouble, GLint, GLint]
    glutSolidCone.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 631
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireCube'):
        continue
    glutWireCube = _lib.glutWireCube
    glutWireCube.argtypes = [GLdouble]
    glutWireCube.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 632
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidCube'):
        continue
    glutSolidCube = _lib.glutSolidCube
    glutSolidCube.argtypes = [GLdouble]
    glutSolidCube.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 633
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireTorus'):
        continue
    glutWireTorus = _lib.glutWireTorus
    glutWireTorus.argtypes = [GLdouble, GLdouble, GLint, GLint]
    glutWireTorus.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 634
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidTorus'):
        continue
    glutSolidTorus = _lib.glutSolidTorus
    glutSolidTorus.argtypes = [GLdouble, GLdouble, GLint, GLint]
    glutSolidTorus.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 635
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireDodecahedron'):
        continue
    glutWireDodecahedron = _lib.glutWireDodecahedron
    glutWireDodecahedron.argtypes = []
    glutWireDodecahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 636
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidDodecahedron'):
        continue
    glutSolidDodecahedron = _lib.glutSolidDodecahedron
    glutSolidDodecahedron.argtypes = []
    glutSolidDodecahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 637
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireTeapot'):
        continue
    glutWireTeapot = _lib.glutWireTeapot
    glutWireTeapot.argtypes = [GLdouble]
    glutWireTeapot.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 638
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidTeapot'):
        continue
    glutSolidTeapot = _lib.glutSolidTeapot
    glutSolidTeapot.argtypes = [GLdouble]
    glutSolidTeapot.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 639
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireOctahedron'):
        continue
    glutWireOctahedron = _lib.glutWireOctahedron
    glutWireOctahedron.argtypes = []
    glutWireOctahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 640
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidOctahedron'):
        continue
    glutSolidOctahedron = _lib.glutSolidOctahedron
    glutSolidOctahedron.argtypes = []
    glutSolidOctahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 641
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireTetrahedron'):
        continue
    glutWireTetrahedron = _lib.glutWireTetrahedron
    glutWireTetrahedron.argtypes = []
    glutWireTetrahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 642
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidTetrahedron'):
        continue
    glutSolidTetrahedron = _lib.glutSolidTetrahedron
    glutSolidTetrahedron.argtypes = []
    glutSolidTetrahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 643
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutWireIcosahedron'):
        continue
    glutWireIcosahedron = _lib.glutWireIcosahedron
    glutWireIcosahedron.argtypes = []
    glutWireIcosahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 644
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSolidIcosahedron'):
        continue
    glutSolidIcosahedron = _lib.glutSolidIcosahedron
    glutSolidIcosahedron.argtypes = []
    glutSolidIcosahedron.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 648
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutVideoResizeGet'):
        continue
    glutVideoResizeGet = _lib.glutVideoResizeGet
    glutVideoResizeGet.argtypes = [GLenum]
    glutVideoResizeGet.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 649
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetupVideoResizing'):
        continue
    glutSetupVideoResizing = _lib.glutSetupVideoResizing
    glutSetupVideoResizing.argtypes = []
    glutSetupVideoResizing.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 650
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutStopVideoResizing'):
        continue
    glutStopVideoResizing = _lib.glutStopVideoResizing
    glutStopVideoResizing.argtypes = []
    glutStopVideoResizing.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 651
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutVideoResize'):
        continue
    glutVideoResize = _lib.glutVideoResize
    glutVideoResize.argtypes = [c_int, c_int, c_int, c_int]
    glutVideoResize.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 652
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutVideoPan'):
        continue
    glutVideoPan = _lib.glutVideoPan
    glutVideoPan.argtypes = [c_int, c_int, c_int, c_int]
    glutVideoPan.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 655
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutReportErrors'):
        continue
    glutReportErrors = _lib.glutReportErrors
    glutReportErrors.argtypes = []
    glutReportErrors.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 671
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutIgnoreKeyRepeat'):
        continue
    glutIgnoreKeyRepeat = _lib.glutIgnoreKeyRepeat
    glutIgnoreKeyRepeat.argtypes = [c_int]
    glutIgnoreKeyRepeat.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 672
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutSetKeyRepeat'):
        continue
    glutSetKeyRepeat = _lib.glutSetKeyRepeat
    glutSetKeyRepeat.argtypes = [c_int]
    glutSetKeyRepeat.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 673
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutForceJoystickFunc'):
        continue
    glutForceJoystickFunc = _lib.glutForceJoystickFunc
    glutForceJoystickFunc.argtypes = []
    glutForceJoystickFunc.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 685
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGameModeString'):
        continue
    glutGameModeString = _lib.glutGameModeString
    glutGameModeString.argtypes = [String]
    glutGameModeString.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 686
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutEnterGameMode'):
        continue
    glutEnterGameMode = _lib.glutEnterGameMode
    glutEnterGameMode.argtypes = []
    glutEnterGameMode.restype = c_int
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 687
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutLeaveGameMode'):
        continue
    glutLeaveGameMode = _lib.glutLeaveGameMode
    glutLeaveGameMode.argtypes = []
    glutLeaveGameMode.restype = None
    break

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 688
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'glutGameModeGet'):
        continue
    glutGameModeGet = _lib.glutGameModeGet
    glutGameModeGet.argtypes = [GLenum]
    glutGameModeGet.restype = c_int
    break

__const = c_int # <command-line>: 5

# <command-line>: 8
try:
    CTYPESGEN = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 25
try:
    __MINGW32_VERSION = 3.18
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 26
try:
    __MINGW32_MAJOR_VERSION = 3
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 27
try:
    __MINGW32_MINOR_VERSION = 18
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 28
try:
    __MINGW32_PATCHLEVEL = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 67
try:
    __MINGW_ANSI_STDIO__ = 1L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 72
try:
    __MINGW_LC_EXTENSIONS__ = 80L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 73
try:
    __MINGW_LC_MESSAGES__ = 16L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 74
try:
    __MINGW_LC_ENVVARS__ = 64L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 185
def __MINGW_GNUC_PREREQ(major, minor):
    return 0

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 210
def __UNUSED_PARAM(x):
    return x

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/_mingw.h: 257
try:
    __MSVCRT_VERSION__ = 1536
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/string.h: 150
try:
    _wcscmpi = _wcsicmp
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 11
try:
    EDK_OK = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 13
try:
    EDK_UNKNOWN_ERROR = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 15
try:
    EDK_INVALID_DEV_ID_ERROR = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 17
try:
    EDK_INVALID_PROFILE_ARCHIVE = 257
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 19
try:
    EDK_NO_USER_FOR_BASEPROFILE = 258
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 22
try:
    EDK_CANNOT_ACQUIRE_DATA = 512
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 25
try:
    EDK_BUFFER_TOO_SMALL = 768
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 27
try:
    EDK_OUT_OF_RANGE = 769
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 29
try:
    EDK_INVALID_PARAMETER = 770
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 31
try:
    EDK_PARAMETER_LOCKED = 771
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 33
try:
    EDK_COG_INVALID_TRAINING_ACTION = 772
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 35
try:
    EDK_COG_INVALID_TRAINING_CONTROL = 773
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 37
try:
    EDK_COG_INVALID_ACTIVE_ACTION = 774
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 39
try:
    EDK_COG_EXCESS_MAX_ACTIONS = 775
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 41
try:
    EDK_EXP_NO_SIG_AVAILABLE = 776
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 43
try:
    EDK_FILESYSTEM_ERROR = 777
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 46
try:
    EDK_INVALID_USER_ID = 1024
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 49
try:
    EDK_EMOENGINE_UNINITIALIZED = 1280
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 51
try:
    EDK_EMOENGINE_DISCONNECTED = 1281
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 53
try:
    EDK_EMOENGINE_PROXY_ERROR = 1282
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 56
try:
    EDK_NO_EVENT = 1536
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 59
try:
    EDK_GYRO_NOT_CALIBRATED = 1792
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 62
try:
    EDK_OPTIMIZATION_IS_ON = 2048
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\/edkErrorCode.h: 65
try:
    EDK_RESERVED1 = 2304
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 95
try:
    GL_VERSION_1_1 = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 137
try:
    GL_FALSE = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 138
try:
    GL_TRUE = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 141
try:
    GL_BYTE = 5120
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 142
try:
    GL_UNSIGNED_BYTE = 5121
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 143
try:
    GL_SHORT = 5122
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 144
try:
    GL_UNSIGNED_SHORT = 5123
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 145
try:
    GL_INT = 5124
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 146
try:
    GL_UNSIGNED_INT = 5125
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 147
try:
    GL_FLOAT = 5126
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 148
try:
    GL_DOUBLE = 5130
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 149
try:
    GL_2_BYTES = 5127
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 150
try:
    GL_3_BYTES = 5128
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 151
try:
    GL_4_BYTES = 5129
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 154
try:
    GL_POINTS = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 155
try:
    GL_LINES = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 156
try:
    GL_LINE_LOOP = 2
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 157
try:
    GL_LINE_STRIP = 3
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 158
try:
    GL_TRIANGLES = 4
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 159
try:
    GL_TRIANGLE_STRIP = 5
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 160
try:
    GL_TRIANGLE_FAN = 6
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 161
try:
    GL_QUADS = 7
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 162
try:
    GL_QUAD_STRIP = 8
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 163
try:
    GL_POLYGON = 9
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 166
try:
    GL_VERTEX_ARRAY = 32884
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 167
try:
    GL_NORMAL_ARRAY = 32885
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 168
try:
    GL_COLOR_ARRAY = 32886
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 169
try:
    GL_INDEX_ARRAY = 32887
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 170
try:
    GL_TEXTURE_COORD_ARRAY = 32888
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 171
try:
    GL_EDGE_FLAG_ARRAY = 32889
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 172
try:
    GL_VERTEX_ARRAY_SIZE = 32890
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 173
try:
    GL_VERTEX_ARRAY_TYPE = 32891
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 174
try:
    GL_VERTEX_ARRAY_STRIDE = 32892
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 175
try:
    GL_NORMAL_ARRAY_TYPE = 32894
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 176
try:
    GL_NORMAL_ARRAY_STRIDE = 32895
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 177
try:
    GL_COLOR_ARRAY_SIZE = 32897
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 178
try:
    GL_COLOR_ARRAY_TYPE = 32898
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 179
try:
    GL_COLOR_ARRAY_STRIDE = 32899
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 180
try:
    GL_INDEX_ARRAY_TYPE = 32901
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 181
try:
    GL_INDEX_ARRAY_STRIDE = 32902
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 182
try:
    GL_TEXTURE_COORD_ARRAY_SIZE = 32904
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 183
try:
    GL_TEXTURE_COORD_ARRAY_TYPE = 32905
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 184
try:
    GL_TEXTURE_COORD_ARRAY_STRIDE = 32906
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 185
try:
    GL_EDGE_FLAG_ARRAY_STRIDE = 32908
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 186
try:
    GL_VERTEX_ARRAY_POINTER = 32910
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 187
try:
    GL_NORMAL_ARRAY_POINTER = 32911
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 188
try:
    GL_COLOR_ARRAY_POINTER = 32912
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 189
try:
    GL_INDEX_ARRAY_POINTER = 32913
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 190
try:
    GL_TEXTURE_COORD_ARRAY_POINTER = 32914
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 191
try:
    GL_EDGE_FLAG_ARRAY_POINTER = 32915
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 192
try:
    GL_V2F = 10784
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 193
try:
    GL_V3F = 10785
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 194
try:
    GL_C4UB_V2F = 10786
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 195
try:
    GL_C4UB_V3F = 10787
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 196
try:
    GL_C3F_V3F = 10788
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 197
try:
    GL_N3F_V3F = 10789
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 198
try:
    GL_C4F_N3F_V3F = 10790
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 199
try:
    GL_T2F_V3F = 10791
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 200
try:
    GL_T4F_V4F = 10792
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 201
try:
    GL_T2F_C4UB_V3F = 10793
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 202
try:
    GL_T2F_C3F_V3F = 10794
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 203
try:
    GL_T2F_N3F_V3F = 10795
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 204
try:
    GL_T2F_C4F_N3F_V3F = 10796
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 205
try:
    GL_T4F_C4F_N3F_V4F = 10797
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 208
try:
    GL_MATRIX_MODE = 2976
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 209
try:
    GL_MODELVIEW = 5888
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 210
try:
    GL_PROJECTION = 5889
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 211
try:
    GL_TEXTURE = 5890
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 214
try:
    GL_POINT_SMOOTH = 2832
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 215
try:
    GL_POINT_SIZE = 2833
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 216
try:
    GL_POINT_SIZE_GRANULARITY = 2835
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 217
try:
    GL_POINT_SIZE_RANGE = 2834
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 220
try:
    GL_LINE_SMOOTH = 2848
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 221
try:
    GL_LINE_STIPPLE = 2852
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 222
try:
    GL_LINE_STIPPLE_PATTERN = 2853
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 223
try:
    GL_LINE_STIPPLE_REPEAT = 2854
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 224
try:
    GL_LINE_WIDTH = 2849
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 225
try:
    GL_LINE_WIDTH_GRANULARITY = 2851
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 226
try:
    GL_LINE_WIDTH_RANGE = 2850
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 229
try:
    GL_POINT = 6912
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 230
try:
    GL_LINE = 6913
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 231
try:
    GL_FILL = 6914
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 232
try:
    GL_CW = 2304
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 233
try:
    GL_CCW = 2305
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 234
try:
    GL_FRONT = 1028
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 235
try:
    GL_BACK = 1029
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 236
try:
    GL_POLYGON_MODE = 2880
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 237
try:
    GL_POLYGON_SMOOTH = 2881
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 238
try:
    GL_POLYGON_STIPPLE = 2882
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 239
try:
    GL_EDGE_FLAG = 2883
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 240
try:
    GL_CULL_FACE = 2884
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 241
try:
    GL_CULL_FACE_MODE = 2885
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 242
try:
    GL_FRONT_FACE = 2886
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 243
try:
    GL_POLYGON_OFFSET_FACTOR = 32824
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 244
try:
    GL_POLYGON_OFFSET_UNITS = 10752
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 245
try:
    GL_POLYGON_OFFSET_POINT = 10753
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 246
try:
    GL_POLYGON_OFFSET_LINE = 10754
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 247
try:
    GL_POLYGON_OFFSET_FILL = 32823
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 250
try:
    GL_COMPILE = 4864
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 251
try:
    GL_COMPILE_AND_EXECUTE = 4865
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 252
try:
    GL_LIST_BASE = 2866
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 253
try:
    GL_LIST_INDEX = 2867
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 254
try:
    GL_LIST_MODE = 2864
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 257
try:
    GL_NEVER = 512
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 258
try:
    GL_LESS = 513
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 259
try:
    GL_EQUAL = 514
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 260
try:
    GL_LEQUAL = 515
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 261
try:
    GL_GREATER = 516
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 262
try:
    GL_NOTEQUAL = 517
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 263
try:
    GL_GEQUAL = 518
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 264
try:
    GL_ALWAYS = 519
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 265
try:
    GL_DEPTH_TEST = 2929
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 266
try:
    GL_DEPTH_BITS = 3414
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 267
try:
    GL_DEPTH_CLEAR_VALUE = 2931
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 268
try:
    GL_DEPTH_FUNC = 2932
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 269
try:
    GL_DEPTH_RANGE = 2928
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 270
try:
    GL_DEPTH_WRITEMASK = 2930
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 271
try:
    GL_DEPTH_COMPONENT = 6402
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 274
try:
    GL_LIGHTING = 2896
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 275
try:
    GL_LIGHT0 = 16384
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 276
try:
    GL_LIGHT1 = 16385
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 277
try:
    GL_LIGHT2 = 16386
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 278
try:
    GL_LIGHT3 = 16387
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 279
try:
    GL_LIGHT4 = 16388
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 280
try:
    GL_LIGHT5 = 16389
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 281
try:
    GL_LIGHT6 = 16390
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 282
try:
    GL_LIGHT7 = 16391
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 283
try:
    GL_SPOT_EXPONENT = 4613
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 284
try:
    GL_SPOT_CUTOFF = 4614
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 285
try:
    GL_CONSTANT_ATTENUATION = 4615
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 286
try:
    GL_LINEAR_ATTENUATION = 4616
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 287
try:
    GL_QUADRATIC_ATTENUATION = 4617
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 288
try:
    GL_AMBIENT = 4608
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 289
try:
    GL_DIFFUSE = 4609
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 290
try:
    GL_SPECULAR = 4610
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 291
try:
    GL_SHININESS = 5633
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 292
try:
    GL_EMISSION = 5632
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 293
try:
    GL_POSITION = 4611
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 294
try:
    GL_SPOT_DIRECTION = 4612
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 295
try:
    GL_AMBIENT_AND_DIFFUSE = 5634
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 296
try:
    GL_COLOR_INDEXES = 5635
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 297
try:
    GL_LIGHT_MODEL_TWO_SIDE = 2898
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 298
try:
    GL_LIGHT_MODEL_LOCAL_VIEWER = 2897
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 299
try:
    GL_LIGHT_MODEL_AMBIENT = 2899
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 300
try:
    GL_FRONT_AND_BACK = 1032
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 301
try:
    GL_SHADE_MODEL = 2900
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 302
try:
    GL_FLAT = 7424
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 303
try:
    GL_SMOOTH = 7425
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 304
try:
    GL_COLOR_MATERIAL = 2903
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 305
try:
    GL_COLOR_MATERIAL_FACE = 2901
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 306
try:
    GL_COLOR_MATERIAL_PARAMETER = 2902
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 307
try:
    GL_NORMALIZE = 2977
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 310
try:
    GL_CLIP_PLANE0 = 12288
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 311
try:
    GL_CLIP_PLANE1 = 12289
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 312
try:
    GL_CLIP_PLANE2 = 12290
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 313
try:
    GL_CLIP_PLANE3 = 12291
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 314
try:
    GL_CLIP_PLANE4 = 12292
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 315
try:
    GL_CLIP_PLANE5 = 12293
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 318
try:
    GL_ACCUM_RED_BITS = 3416
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 319
try:
    GL_ACCUM_GREEN_BITS = 3417
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 320
try:
    GL_ACCUM_BLUE_BITS = 3418
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 321
try:
    GL_ACCUM_ALPHA_BITS = 3419
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 322
try:
    GL_ACCUM_CLEAR_VALUE = 2944
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 323
try:
    GL_ACCUM = 256
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 324
try:
    GL_ADD = 260
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 325
try:
    GL_LOAD = 257
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 326
try:
    GL_MULT = 259
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 327
try:
    GL_RETURN = 258
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 330
try:
    GL_ALPHA_TEST = 3008
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 331
try:
    GL_ALPHA_TEST_REF = 3010
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 332
try:
    GL_ALPHA_TEST_FUNC = 3009
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 335
try:
    GL_BLEND = 3042
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 336
try:
    GL_BLEND_SRC = 3041
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 337
try:
    GL_BLEND_DST = 3040
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 338
try:
    GL_ZERO = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 339
try:
    GL_ONE = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 340
try:
    GL_SRC_COLOR = 768
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 341
try:
    GL_ONE_MINUS_SRC_COLOR = 769
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 342
try:
    GL_SRC_ALPHA = 770
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 343
try:
    GL_ONE_MINUS_SRC_ALPHA = 771
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 344
try:
    GL_DST_ALPHA = 772
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 345
try:
    GL_ONE_MINUS_DST_ALPHA = 773
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 346
try:
    GL_DST_COLOR = 774
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 347
try:
    GL_ONE_MINUS_DST_COLOR = 775
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 348
try:
    GL_SRC_ALPHA_SATURATE = 776
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 349
try:
    GL_CONSTANT_COLOR = 32769
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 350
try:
    GL_ONE_MINUS_CONSTANT_COLOR = 32770
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 351
try:
    GL_CONSTANT_ALPHA = 32771
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 352
try:
    GL_ONE_MINUS_CONSTANT_ALPHA = 32772
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 355
try:
    GL_FEEDBACK = 7169
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 356
try:
    GL_RENDER = 7168
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 357
try:
    GL_SELECT = 7170
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 360
try:
    GL_2D = 1536
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 361
try:
    GL_3D = 1537
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 362
try:
    GL_3D_COLOR = 1538
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 363
try:
    GL_3D_COLOR_TEXTURE = 1539
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 364
try:
    GL_4D_COLOR_TEXTURE = 1540
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 365
try:
    GL_POINT_TOKEN = 1793
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 366
try:
    GL_LINE_TOKEN = 1794
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 367
try:
    GL_LINE_RESET_TOKEN = 1799
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 368
try:
    GL_POLYGON_TOKEN = 1795
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 369
try:
    GL_BITMAP_TOKEN = 1796
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 370
try:
    GL_DRAW_PIXEL_TOKEN = 1797
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 371
try:
    GL_COPY_PIXEL_TOKEN = 1798
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 372
try:
    GL_PASS_THROUGH_TOKEN = 1792
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 373
try:
    GL_FEEDBACK_BUFFER_POINTER = 3568
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 374
try:
    GL_FEEDBACK_BUFFER_SIZE = 3569
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 375
try:
    GL_FEEDBACK_BUFFER_TYPE = 3570
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 378
try:
    GL_SELECTION_BUFFER_POINTER = 3571
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 379
try:
    GL_SELECTION_BUFFER_SIZE = 3572
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 382
try:
    GL_FOG = 2912
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 383
try:
    GL_FOG_MODE = 2917
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 384
try:
    GL_FOG_DENSITY = 2914
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 385
try:
    GL_FOG_COLOR = 2918
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 386
try:
    GL_FOG_INDEX = 2913
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 387
try:
    GL_FOG_START = 2915
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 388
try:
    GL_FOG_END = 2916
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 389
try:
    GL_LINEAR = 9729
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 390
try:
    GL_EXP = 2048
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 391
try:
    GL_EXP2 = 2049
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 394
try:
    GL_LOGIC_OP = 3057
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 395
try:
    GL_INDEX_LOGIC_OP = 3057
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 396
try:
    GL_COLOR_LOGIC_OP = 3058
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 397
try:
    GL_LOGIC_OP_MODE = 3056
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 398
try:
    GL_CLEAR = 5376
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 399
try:
    GL_SET = 5391
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 400
try:
    GL_COPY = 5379
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 401
try:
    GL_COPY_INVERTED = 5388
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 402
try:
    GL_NOOP = 5381
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 403
try:
    GL_INVERT = 5386
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 404
try:
    GL_AND = 5377
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 405
try:
    GL_NAND = 5390
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 406
try:
    GL_OR = 5383
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 407
try:
    GL_NOR = 5384
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 408
try:
    GL_XOR = 5382
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 409
try:
    GL_EQUIV = 5385
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 410
try:
    GL_AND_REVERSE = 5378
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 411
try:
    GL_AND_INVERTED = 5380
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 412
try:
    GL_OR_REVERSE = 5387
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 413
try:
    GL_OR_INVERTED = 5389
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 416
try:
    GL_STENCIL_TEST = 2960
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 417
try:
    GL_STENCIL_WRITEMASK = 2968
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 418
try:
    GL_STENCIL_BITS = 3415
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 419
try:
    GL_STENCIL_FUNC = 2962
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 420
try:
    GL_STENCIL_VALUE_MASK = 2963
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 421
try:
    GL_STENCIL_REF = 2967
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 422
try:
    GL_STENCIL_FAIL = 2964
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 423
try:
    GL_STENCIL_PASS_DEPTH_PASS = 2966
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 424
try:
    GL_STENCIL_PASS_DEPTH_FAIL = 2965
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 425
try:
    GL_STENCIL_CLEAR_VALUE = 2961
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 426
try:
    GL_STENCIL_INDEX = 6401
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 427
try:
    GL_KEEP = 7680
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 428
try:
    GL_REPLACE = 7681
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 429
try:
    GL_INCR = 7682
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 430
try:
    GL_DECR = 7683
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 433
try:
    GL_NONE = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 434
try:
    GL_LEFT = 1030
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 435
try:
    GL_RIGHT = 1031
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 439
try:
    GL_FRONT_LEFT = 1024
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 440
try:
    GL_FRONT_RIGHT = 1025
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 441
try:
    GL_BACK_LEFT = 1026
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 442
try:
    GL_BACK_RIGHT = 1027
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 443
try:
    GL_AUX0 = 1033
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 444
try:
    GL_AUX1 = 1034
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 445
try:
    GL_AUX2 = 1035
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 446
try:
    GL_AUX3 = 1036
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 447
try:
    GL_COLOR_INDEX = 6400
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 448
try:
    GL_RED = 6403
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 449
try:
    GL_GREEN = 6404
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 450
try:
    GL_BLUE = 6405
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 451
try:
    GL_ALPHA = 6406
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 452
try:
    GL_LUMINANCE = 6409
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 453
try:
    GL_LUMINANCE_ALPHA = 6410
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 454
try:
    GL_ALPHA_BITS = 3413
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 455
try:
    GL_RED_BITS = 3410
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 456
try:
    GL_GREEN_BITS = 3411
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 457
try:
    GL_BLUE_BITS = 3412
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 458
try:
    GL_INDEX_BITS = 3409
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 459
try:
    GL_SUBPIXEL_BITS = 3408
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 460
try:
    GL_AUX_BUFFERS = 3072
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 461
try:
    GL_READ_BUFFER = 3074
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 462
try:
    GL_DRAW_BUFFER = 3073
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 463
try:
    GL_DOUBLEBUFFER = 3122
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 464
try:
    GL_STEREO = 3123
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 465
try:
    GL_BITMAP = 6656
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 466
try:
    GL_COLOR = 6144
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 467
try:
    GL_DEPTH = 6145
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 468
try:
    GL_STENCIL = 6146
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 469
try:
    GL_DITHER = 3024
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 470
try:
    GL_RGB = 6407
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 471
try:
    GL_RGBA = 6408
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 474
try:
    GL_MAX_LIST_NESTING = 2865
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 475
try:
    GL_MAX_ATTRIB_STACK_DEPTH = 3381
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 476
try:
    GL_MAX_MODELVIEW_STACK_DEPTH = 3382
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 477
try:
    GL_MAX_NAME_STACK_DEPTH = 3383
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 478
try:
    GL_MAX_PROJECTION_STACK_DEPTH = 3384
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 479
try:
    GL_MAX_TEXTURE_STACK_DEPTH = 3385
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 480
try:
    GL_MAX_EVAL_ORDER = 3376
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 481
try:
    GL_MAX_LIGHTS = 3377
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 482
try:
    GL_MAX_CLIP_PLANES = 3378
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 483
try:
    GL_MAX_TEXTURE_SIZE = 3379
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 484
try:
    GL_MAX_PIXEL_MAP_TABLE = 3380
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 485
try:
    GL_MAX_VIEWPORT_DIMS = 3386
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 486
try:
    GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 489
try:
    GL_ATTRIB_STACK_DEPTH = 2992
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 490
try:
    GL_CLIENT_ATTRIB_STACK_DEPTH = 2993
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 491
try:
    GL_COLOR_CLEAR_VALUE = 3106
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 492
try:
    GL_COLOR_WRITEMASK = 3107
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 493
try:
    GL_CURRENT_INDEX = 2817
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 494
try:
    GL_CURRENT_COLOR = 2816
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 495
try:
    GL_CURRENT_NORMAL = 2818
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 496
try:
    GL_CURRENT_RASTER_COLOR = 2820
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 497
try:
    GL_CURRENT_RASTER_DISTANCE = 2825
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 498
try:
    GL_CURRENT_RASTER_INDEX = 2821
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 499
try:
    GL_CURRENT_RASTER_POSITION = 2823
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 500
try:
    GL_CURRENT_RASTER_TEXTURE_COORDS = 2822
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 501
try:
    GL_CURRENT_RASTER_POSITION_VALID = 2824
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 502
try:
    GL_CURRENT_TEXTURE_COORDS = 2819
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 503
try:
    GL_INDEX_CLEAR_VALUE = 3104
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 504
try:
    GL_INDEX_MODE = 3120
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 505
try:
    GL_INDEX_WRITEMASK = 3105
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 506
try:
    GL_MODELVIEW_MATRIX = 2982
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 507
try:
    GL_MODELVIEW_STACK_DEPTH = 2979
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 508
try:
    GL_NAME_STACK_DEPTH = 3440
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 509
try:
    GL_PROJECTION_MATRIX = 2983
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 510
try:
    GL_PROJECTION_STACK_DEPTH = 2980
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 511
try:
    GL_RENDER_MODE = 3136
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 512
try:
    GL_RGBA_MODE = 3121
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 513
try:
    GL_TEXTURE_MATRIX = 2984
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 514
try:
    GL_TEXTURE_STACK_DEPTH = 2981
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 515
try:
    GL_VIEWPORT = 2978
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 518
try:
    GL_AUTO_NORMAL = 3456
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 519
try:
    GL_MAP1_COLOR_4 = 3472
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 520
try:
    GL_MAP1_GRID_DOMAIN = 3536
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 521
try:
    GL_MAP1_GRID_SEGMENTS = 3537
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 522
try:
    GL_MAP1_INDEX = 3473
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 523
try:
    GL_MAP1_NORMAL = 3474
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 524
try:
    GL_MAP1_TEXTURE_COORD_1 = 3475
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 525
try:
    GL_MAP1_TEXTURE_COORD_2 = 3476
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 526
try:
    GL_MAP1_TEXTURE_COORD_3 = 3477
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 527
try:
    GL_MAP1_TEXTURE_COORD_4 = 3478
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 528
try:
    GL_MAP1_VERTEX_3 = 3479
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 529
try:
    GL_MAP1_VERTEX_4 = 3480
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 530
try:
    GL_MAP2_COLOR_4 = 3504
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 531
try:
    GL_MAP2_GRID_DOMAIN = 3538
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 532
try:
    GL_MAP2_GRID_SEGMENTS = 3539
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 533
try:
    GL_MAP2_INDEX = 3505
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 534
try:
    GL_MAP2_NORMAL = 3506
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 535
try:
    GL_MAP2_TEXTURE_COORD_1 = 3507
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 536
try:
    GL_MAP2_TEXTURE_COORD_2 = 3508
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 537
try:
    GL_MAP2_TEXTURE_COORD_3 = 3509
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 538
try:
    GL_MAP2_TEXTURE_COORD_4 = 3510
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 539
try:
    GL_MAP2_VERTEX_3 = 3511
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 540
try:
    GL_MAP2_VERTEX_4 = 3512
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 541
try:
    GL_COEFF = 2560
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 542
try:
    GL_DOMAIN = 2562
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 543
try:
    GL_ORDER = 2561
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 546
try:
    GL_FOG_HINT = 3156
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 547
try:
    GL_LINE_SMOOTH_HINT = 3154
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 548
try:
    GL_PERSPECTIVE_CORRECTION_HINT = 3152
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 549
try:
    GL_POINT_SMOOTH_HINT = 3153
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 550
try:
    GL_POLYGON_SMOOTH_HINT = 3155
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 551
try:
    GL_DONT_CARE = 4352
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 552
try:
    GL_FASTEST = 4353
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 553
try:
    GL_NICEST = 4354
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 556
try:
    GL_SCISSOR_TEST = 3089
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 557
try:
    GL_SCISSOR_BOX = 3088
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 560
try:
    GL_MAP_COLOR = 3344
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 561
try:
    GL_MAP_STENCIL = 3345
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 562
try:
    GL_INDEX_SHIFT = 3346
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 563
try:
    GL_INDEX_OFFSET = 3347
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 564
try:
    GL_RED_SCALE = 3348
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 565
try:
    GL_RED_BIAS = 3349
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 566
try:
    GL_GREEN_SCALE = 3352
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 567
try:
    GL_GREEN_BIAS = 3353
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 568
try:
    GL_BLUE_SCALE = 3354
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 569
try:
    GL_BLUE_BIAS = 3355
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 570
try:
    GL_ALPHA_SCALE = 3356
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 571
try:
    GL_ALPHA_BIAS = 3357
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 572
try:
    GL_DEPTH_SCALE = 3358
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 573
try:
    GL_DEPTH_BIAS = 3359
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 574
try:
    GL_PIXEL_MAP_S_TO_S_SIZE = 3249
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 575
try:
    GL_PIXEL_MAP_I_TO_I_SIZE = 3248
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 576
try:
    GL_PIXEL_MAP_I_TO_R_SIZE = 3250
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 577
try:
    GL_PIXEL_MAP_I_TO_G_SIZE = 3251
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 578
try:
    GL_PIXEL_MAP_I_TO_B_SIZE = 3252
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 579
try:
    GL_PIXEL_MAP_I_TO_A_SIZE = 3253
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 580
try:
    GL_PIXEL_MAP_R_TO_R_SIZE = 3254
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 581
try:
    GL_PIXEL_MAP_G_TO_G_SIZE = 3255
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 582
try:
    GL_PIXEL_MAP_B_TO_B_SIZE = 3256
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 583
try:
    GL_PIXEL_MAP_A_TO_A_SIZE = 3257
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 584
try:
    GL_PIXEL_MAP_S_TO_S = 3185
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 585
try:
    GL_PIXEL_MAP_I_TO_I = 3184
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 586
try:
    GL_PIXEL_MAP_I_TO_R = 3186
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 587
try:
    GL_PIXEL_MAP_I_TO_G = 3187
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 588
try:
    GL_PIXEL_MAP_I_TO_B = 3188
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 589
try:
    GL_PIXEL_MAP_I_TO_A = 3189
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 590
try:
    GL_PIXEL_MAP_R_TO_R = 3190
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 591
try:
    GL_PIXEL_MAP_G_TO_G = 3191
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 592
try:
    GL_PIXEL_MAP_B_TO_B = 3192
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 593
try:
    GL_PIXEL_MAP_A_TO_A = 3193
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 594
try:
    GL_PACK_ALIGNMENT = 3333
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 595
try:
    GL_PACK_LSB_FIRST = 3329
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 596
try:
    GL_PACK_ROW_LENGTH = 3330
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 597
try:
    GL_PACK_SKIP_PIXELS = 3332
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 598
try:
    GL_PACK_SKIP_ROWS = 3331
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 599
try:
    GL_PACK_SWAP_BYTES = 3328
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 600
try:
    GL_UNPACK_ALIGNMENT = 3317
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 601
try:
    GL_UNPACK_LSB_FIRST = 3313
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 602
try:
    GL_UNPACK_ROW_LENGTH = 3314
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 603
try:
    GL_UNPACK_SKIP_PIXELS = 3316
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 604
try:
    GL_UNPACK_SKIP_ROWS = 3315
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 605
try:
    GL_UNPACK_SWAP_BYTES = 3312
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 606
try:
    GL_ZOOM_X = 3350
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 607
try:
    GL_ZOOM_Y = 3351
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 610
try:
    GL_TEXTURE_ENV = 8960
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 611
try:
    GL_TEXTURE_ENV_MODE = 8704
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 612
try:
    GL_TEXTURE_1D = 3552
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 613
try:
    GL_TEXTURE_2D = 3553
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 614
try:
    GL_TEXTURE_WRAP_S = 10242
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 615
try:
    GL_TEXTURE_WRAP_T = 10243
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 616
try:
    GL_TEXTURE_MAG_FILTER = 10240
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 617
try:
    GL_TEXTURE_MIN_FILTER = 10241
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 618
try:
    GL_TEXTURE_ENV_COLOR = 8705
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 619
try:
    GL_TEXTURE_GEN_S = 3168
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 620
try:
    GL_TEXTURE_GEN_T = 3169
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 621
try:
    GL_TEXTURE_GEN_MODE = 9472
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 622
try:
    GL_TEXTURE_BORDER_COLOR = 4100
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 623
try:
    GL_TEXTURE_WIDTH = 4096
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 624
try:
    GL_TEXTURE_HEIGHT = 4097
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 625
try:
    GL_TEXTURE_BORDER = 4101
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 626
try:
    GL_TEXTURE_COMPONENTS = 4099
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 627
try:
    GL_TEXTURE_RED_SIZE = 32860
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 628
try:
    GL_TEXTURE_GREEN_SIZE = 32861
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 629
try:
    GL_TEXTURE_BLUE_SIZE = 32862
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 630
try:
    GL_TEXTURE_ALPHA_SIZE = 32863
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 631
try:
    GL_TEXTURE_LUMINANCE_SIZE = 32864
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 632
try:
    GL_TEXTURE_INTENSITY_SIZE = 32865
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 633
try:
    GL_NEAREST_MIPMAP_NEAREST = 9984
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 634
try:
    GL_NEAREST_MIPMAP_LINEAR = 9986
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 635
try:
    GL_LINEAR_MIPMAP_NEAREST = 9985
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 636
try:
    GL_LINEAR_MIPMAP_LINEAR = 9987
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 637
try:
    GL_OBJECT_LINEAR = 9217
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 638
try:
    GL_OBJECT_PLANE = 9473
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 639
try:
    GL_EYE_LINEAR = 9216
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 640
try:
    GL_EYE_PLANE = 9474
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 641
try:
    GL_SPHERE_MAP = 9218
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 642
try:
    GL_DECAL = 8449
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 643
try:
    GL_MODULATE = 8448
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 644
try:
    GL_NEAREST = 9728
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 645
try:
    GL_REPEAT = 10497
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 646
try:
    GL_CLAMP = 10496
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 647
try:
    GL_S = 8192
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 648
try:
    GL_T = 8193
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 649
try:
    GL_R = 8194
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 650
try:
    GL_Q = 8195
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 651
try:
    GL_TEXTURE_GEN_R = 3170
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 652
try:
    GL_TEXTURE_GEN_Q = 3171
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 655
try:
    GL_VENDOR = 7936
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 656
try:
    GL_RENDERER = 7937
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 657
try:
    GL_VERSION = 7938
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 658
try:
    GL_EXTENSIONS = 7939
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 661
try:
    GL_NO_ERROR = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 662
try:
    GL_INVALID_VALUE = 1281
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 663
try:
    GL_INVALID_ENUM = 1280
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 664
try:
    GL_INVALID_OPERATION = 1282
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 665
try:
    GL_STACK_OVERFLOW = 1283
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 666
try:
    GL_STACK_UNDERFLOW = 1284
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 667
try:
    GL_OUT_OF_MEMORY = 1285
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 670
try:
    GL_CURRENT_BIT = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 671
try:
    GL_POINT_BIT = 2
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 672
try:
    GL_LINE_BIT = 4
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 673
try:
    GL_POLYGON_BIT = 8
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 674
try:
    GL_POLYGON_STIPPLE_BIT = 16
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 675
try:
    GL_PIXEL_MODE_BIT = 32
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 676
try:
    GL_LIGHTING_BIT = 64
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 677
try:
    GL_FOG_BIT = 128
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 678
try:
    GL_DEPTH_BUFFER_BIT = 256
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 679
try:
    GL_ACCUM_BUFFER_BIT = 512
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 680
try:
    GL_STENCIL_BUFFER_BIT = 1024
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 681
try:
    GL_VIEWPORT_BIT = 2048
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 682
try:
    GL_TRANSFORM_BIT = 4096
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 683
try:
    GL_ENABLE_BIT = 8192
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 684
try:
    GL_COLOR_BUFFER_BIT = 16384
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 685
try:
    GL_HINT_BIT = 32768
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 686
try:
    GL_EVAL_BIT = 65536
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 687
try:
    GL_LIST_BIT = 131072
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 688
try:
    GL_TEXTURE_BIT = 262144
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 689
try:
    GL_SCISSOR_BIT = 524288
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 690
try:
    GL_ALL_ATTRIB_BITS = 1048575
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 694
try:
    GL_PROXY_TEXTURE_1D = 32867
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 695
try:
    GL_PROXY_TEXTURE_2D = 32868
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 696
try:
    GL_TEXTURE_PRIORITY = 32870
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 697
try:
    GL_TEXTURE_RESIDENT = 32871
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 698
try:
    GL_TEXTURE_BINDING_1D = 32872
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 699
try:
    GL_TEXTURE_BINDING_2D = 32873
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 700
try:
    GL_TEXTURE_INTERNAL_FORMAT = 4099
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 701
try:
    GL_ALPHA4 = 32827
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 702
try:
    GL_ALPHA8 = 32828
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 703
try:
    GL_ALPHA12 = 32829
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 704
try:
    GL_ALPHA16 = 32830
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 705
try:
    GL_LUMINANCE4 = 32831
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 706
try:
    GL_LUMINANCE8 = 32832
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 707
try:
    GL_LUMINANCE12 = 32833
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 708
try:
    GL_LUMINANCE16 = 32834
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 709
try:
    GL_LUMINANCE4_ALPHA4 = 32835
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 710
try:
    GL_LUMINANCE6_ALPHA2 = 32836
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 711
try:
    GL_LUMINANCE8_ALPHA8 = 32837
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 712
try:
    GL_LUMINANCE12_ALPHA4 = 32838
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 713
try:
    GL_LUMINANCE12_ALPHA12 = 32839
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 714
try:
    GL_LUMINANCE16_ALPHA16 = 32840
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 715
try:
    GL_INTENSITY = 32841
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 716
try:
    GL_INTENSITY4 = 32842
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 717
try:
    GL_INTENSITY8 = 32843
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 718
try:
    GL_INTENSITY12 = 32844
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 719
try:
    GL_INTENSITY16 = 32845
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 720
try:
    GL_R3_G3_B2 = 10768
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 721
try:
    GL_RGB4 = 32847
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 722
try:
    GL_RGB5 = 32848
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 723
try:
    GL_RGB8 = 32849
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 724
try:
    GL_RGB10 = 32850
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 725
try:
    GL_RGB12 = 32851
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 726
try:
    GL_RGB16 = 32852
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 727
try:
    GL_RGBA2 = 32853
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 728
try:
    GL_RGBA4 = 32854
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 729
try:
    GL_RGB5_A1 = 32855
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 730
try:
    GL_RGBA8 = 32856
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 731
try:
    GL_RGB10_A2 = 32857
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 732
try:
    GL_RGBA12 = 32858
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 733
try:
    GL_RGBA16 = 32859
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 734
try:
    GL_CLIENT_PIXEL_STORE_BIT = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 735
try:
    GL_CLIENT_VERTEX_ARRAY_BIT = 2
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 736
try:
    GL_ALL_CLIENT_ATTRIB_BITS = 4294967295L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/gl.h: 737
try:
    GL_CLIENT_ALL_ATTRIB_BITS = 4294967295L
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 47
try:
    GLU_FALSE = 0
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 48
try:
    GLU_TRUE = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 51
try:
    GLU_VERSION_1_1 = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 52
try:
    GLU_VERSION_1_2 = 1
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 55
try:
    GLU_VERSION = 100800
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 56
try:
    GLU_EXTENSIONS = 100801
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 59
try:
    GLU_INVALID_ENUM = 100900
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 60
try:
    GLU_INVALID_VALUE = 100901
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 61
try:
    GLU_OUT_OF_MEMORY = 100902
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 62
try:
    GLU_INVALID_OPERATION = 100904
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 66
try:
    GLU_OUTLINE_POLYGON = 100240
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 67
try:
    GLU_OUTLINE_PATCH = 100241
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 70
try:
    GLU_NURBS_ERROR1 = 100251
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 71
try:
    GLU_NURBS_ERROR2 = 100252
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 72
try:
    GLU_NURBS_ERROR3 = 100253
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 73
try:
    GLU_NURBS_ERROR4 = 100254
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 74
try:
    GLU_NURBS_ERROR5 = 100255
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 75
try:
    GLU_NURBS_ERROR6 = 100256
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 76
try:
    GLU_NURBS_ERROR7 = 100257
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 77
try:
    GLU_NURBS_ERROR8 = 100258
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 78
try:
    GLU_NURBS_ERROR9 = 100259
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 79
try:
    GLU_NURBS_ERROR10 = 100260
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 80
try:
    GLU_NURBS_ERROR11 = 100261
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 81
try:
    GLU_NURBS_ERROR12 = 100262
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 82
try:
    GLU_NURBS_ERROR13 = 100263
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 83
try:
    GLU_NURBS_ERROR14 = 100264
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 84
try:
    GLU_NURBS_ERROR15 = 100265
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 85
try:
    GLU_NURBS_ERROR16 = 100266
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 86
try:
    GLU_NURBS_ERROR17 = 100267
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 87
try:
    GLU_NURBS_ERROR18 = 100268
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 88
try:
    GLU_NURBS_ERROR19 = 100269
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 89
try:
    GLU_NURBS_ERROR20 = 100270
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 90
try:
    GLU_NURBS_ERROR21 = 100271
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 91
try:
    GLU_NURBS_ERROR22 = 100272
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 92
try:
    GLU_NURBS_ERROR23 = 100273
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 93
try:
    GLU_NURBS_ERROR24 = 100274
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 94
try:
    GLU_NURBS_ERROR25 = 100275
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 95
try:
    GLU_NURBS_ERROR26 = 100276
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 96
try:
    GLU_NURBS_ERROR27 = 100277
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 97
try:
    GLU_NURBS_ERROR28 = 100278
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 98
try:
    GLU_NURBS_ERROR29 = 100279
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 99
try:
    GLU_NURBS_ERROR30 = 100280
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 100
try:
    GLU_NURBS_ERROR31 = 100281
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 101
try:
    GLU_NURBS_ERROR32 = 100282
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 102
try:
    GLU_NURBS_ERROR33 = 100283
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 103
try:
    GLU_NURBS_ERROR34 = 100284
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 104
try:
    GLU_NURBS_ERROR35 = 100285
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 105
try:
    GLU_NURBS_ERROR36 = 100286
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 106
try:
    GLU_NURBS_ERROR37 = 100287
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 109
try:
    GLU_AUTO_LOAD_MATRIX = 100200
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 110
try:
    GLU_CULLING = 100201
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 111
try:
    GLU_SAMPLING_TOLERANCE = 100203
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 112
try:
    GLU_DISPLAY_MODE = 100204
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 113
try:
    GLU_PARAMETRIC_TOLERANCE = 100202
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 114
try:
    GLU_SAMPLING_METHOD = 100205
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 115
try:
    GLU_U_STEP = 100206
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 116
try:
    GLU_V_STEP = 100207
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 119
try:
    GLU_PATH_LENGTH = 100215
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 120
try:
    GLU_PARAMETRIC_ERROR = 100216
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 121
try:
    GLU_DOMAIN_DISTANCE = 100217
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 124
try:
    GLU_MAP1_TRIM_2 = 100210
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 125
try:
    GLU_MAP1_TRIM_3 = 100211
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 128
try:
    GLU_POINT = 100010
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 129
try:
    GLU_LINE = 100011
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 130
try:
    GLU_FILL = 100012
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 131
try:
    GLU_SILHOUETTE = 100013
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 134
try:
    GLU_ERROR = 100103
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 137
try:
    GLU_SMOOTH = 100000
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 138
try:
    GLU_FLAT = 100001
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 139
try:
    GLU_NONE = 100002
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 142
try:
    GLU_OUTSIDE = 100020
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 143
try:
    GLU_INSIDE = 100021
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 146
try:
    GLU_TESS_BEGIN = 100100
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 147
try:
    GLU_BEGIN = 100100
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 148
try:
    GLU_TESS_VERTEX = 100101
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 149
try:
    GLU_VERTEX = 100101
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 150
try:
    GLU_TESS_END = 100102
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 151
try:
    GLU_END = 100102
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 152
try:
    GLU_TESS_ERROR = 100103
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 153
try:
    GLU_TESS_EDGE_FLAG = 100104
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 154
try:
    GLU_EDGE_FLAG = 100104
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 155
try:
    GLU_TESS_COMBINE = 100105
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 156
try:
    GLU_TESS_BEGIN_DATA = 100106
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 157
try:
    GLU_TESS_VERTEX_DATA = 100107
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 158
try:
    GLU_TESS_END_DATA = 100108
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 159
try:
    GLU_TESS_ERROR_DATA = 100109
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 160
try:
    GLU_TESS_EDGE_FLAG_DATA = 100110
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 161
try:
    GLU_TESS_COMBINE_DATA = 100111
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 164
try:
    GLU_CW = 100120
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 165
try:
    GLU_CCW = 100121
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 166
try:
    GLU_INTERIOR = 100122
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 167
try:
    GLU_EXTERIOR = 100123
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 168
try:
    GLU_UNKNOWN = 100124
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 171
try:
    GLU_TESS_WINDING_RULE = 100140
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 172
try:
    GLU_TESS_BOUNDARY_ONLY = 100141
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 173
try:
    GLU_TESS_TOLERANCE = 100142
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 176
try:
    GLU_TESS_ERROR1 = 100151
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 177
try:
    GLU_TESS_ERROR2 = 100152
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 178
try:
    GLU_TESS_ERROR3 = 100153
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 179
try:
    GLU_TESS_ERROR4 = 100154
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 180
try:
    GLU_TESS_ERROR5 = 100155
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 181
try:
    GLU_TESS_ERROR6 = 100156
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 182
try:
    GLU_TESS_ERROR7 = 100157
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 183
try:
    GLU_TESS_ERROR8 = 100158
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 184
try:
    GLU_TESS_MISSING_BEGIN_POLYGON = 100151
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 185
try:
    GLU_TESS_MISSING_BEGIN_CONTOUR = 100152
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 186
try:
    GLU_TESS_MISSING_END_POLYGON = 100153
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 187
try:
    GLU_TESS_MISSING_END_CONTOUR = 100154
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 188
try:
    GLU_TESS_COORD_TOO_LARGE = 100155
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 189
try:
    GLU_TESS_NEED_COMBINE_CALLBACK = 100156
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 192
try:
    GLU_TESS_WINDING_ODD = 100130
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 193
try:
    GLU_TESS_WINDING_NONZERO = 100131
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 194
try:
    GLU_TESS_WINDING_POSITIVE = 100132
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 195
try:
    GLU_TESS_WINDING_NEGATIVE = 100133
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 196
try:
    GLU_TESS_WINDING_ABS_GEQ_TWO = 100134
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 199
try:
    GLU_INCOMPATIBLE_GL_VERSION = 100903
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 220
try:
    GLU_TESS_MAX_COORD = 1e+150
except:
    pass

# c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 282
try:
    gluErrorStringWIN = gluErrorString
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 183
try:
    GLUT_API_VERSION = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 223
try:
    GLUT_XLIB_IMPLEMENTATION = 15
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 227
try:
    GLUT_RGB = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 228
try:
    GLUT_RGBA = GLUT_RGB
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 229
try:
    GLUT_INDEX = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 230
try:
    GLUT_SINGLE = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 231
try:
    GLUT_DOUBLE = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 232
try:
    GLUT_ACCUM = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 233
try:
    GLUT_ALPHA = 8
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 234
try:
    GLUT_DEPTH = 16
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 235
try:
    GLUT_STENCIL = 32
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 237
try:
    GLUT_MULTISAMPLE = 128
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 238
try:
    GLUT_STEREO = 256
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 241
try:
    GLUT_LUMINANCE = 512
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 245
try:
    GLUT_LEFT_BUTTON = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 246
try:
    GLUT_MIDDLE_BUTTON = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 247
try:
    GLUT_RIGHT_BUTTON = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 250
try:
    GLUT_DOWN = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 251
try:
    GLUT_UP = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 255
try:
    GLUT_KEY_F1 = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 256
try:
    GLUT_KEY_F2 = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 257
try:
    GLUT_KEY_F3 = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 258
try:
    GLUT_KEY_F4 = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 259
try:
    GLUT_KEY_F5 = 5
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 260
try:
    GLUT_KEY_F6 = 6
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 261
try:
    GLUT_KEY_F7 = 7
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 262
try:
    GLUT_KEY_F8 = 8
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 263
try:
    GLUT_KEY_F9 = 9
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 264
try:
    GLUT_KEY_F10 = 10
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 265
try:
    GLUT_KEY_F11 = 11
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 266
try:
    GLUT_KEY_F12 = 12
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 268
try:
    GLUT_KEY_LEFT = 100
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 269
try:
    GLUT_KEY_UP = 101
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 270
try:
    GLUT_KEY_RIGHT = 102
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 271
try:
    GLUT_KEY_DOWN = 103
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 272
try:
    GLUT_KEY_PAGE_UP = 104
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 273
try:
    GLUT_KEY_PAGE_DOWN = 105
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 274
try:
    GLUT_KEY_HOME = 106
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 275
try:
    GLUT_KEY_END = 107
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 276
try:
    GLUT_KEY_INSERT = 108
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 280
try:
    GLUT_LEFT = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 281
try:
    GLUT_ENTERED = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 284
try:
    GLUT_MENU_NOT_IN_USE = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 285
try:
    GLUT_MENU_IN_USE = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 288
try:
    GLUT_NOT_VISIBLE = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 289
try:
    GLUT_VISIBLE = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 292
try:
    GLUT_HIDDEN = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 293
try:
    GLUT_FULLY_RETAINED = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 294
try:
    GLUT_PARTIALLY_RETAINED = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 295
try:
    GLUT_FULLY_COVERED = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 298
try:
    GLUT_RED = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 299
try:
    GLUT_GREEN = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 300
try:
    GLUT_BLUE = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 304
try:
    GLUT_STROKE_ROMAN = None
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 305
try:
    GLUT_STROKE_MONO_ROMAN = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 308
try:
    GLUT_BITMAP_9_BY_15 = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 309
try:
    GLUT_BITMAP_8_BY_13 = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 310
try:
    GLUT_BITMAP_TIMES_ROMAN_10 = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 311
try:
    GLUT_BITMAP_TIMES_ROMAN_24 = 5
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 313
try:
    GLUT_BITMAP_HELVETICA_10 = 6
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 314
try:
    GLUT_BITMAP_HELVETICA_12 = 7
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 315
try:
    GLUT_BITMAP_HELVETICA_18 = 8
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 348
try:
    GLUT_WINDOW_X = 100
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 349
try:
    GLUT_WINDOW_Y = 101
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 350
try:
    GLUT_WINDOW_WIDTH = 102
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 351
try:
    GLUT_WINDOW_HEIGHT = 103
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 352
try:
    GLUT_WINDOW_BUFFER_SIZE = 104
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 353
try:
    GLUT_WINDOW_STENCIL_SIZE = 105
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 354
try:
    GLUT_WINDOW_DEPTH_SIZE = 106
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 355
try:
    GLUT_WINDOW_RED_SIZE = 107
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 356
try:
    GLUT_WINDOW_GREEN_SIZE = 108
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 357
try:
    GLUT_WINDOW_BLUE_SIZE = 109
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 358
try:
    GLUT_WINDOW_ALPHA_SIZE = 110
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 359
try:
    GLUT_WINDOW_ACCUM_RED_SIZE = 111
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 360
try:
    GLUT_WINDOW_ACCUM_GREEN_SIZE = 112
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 361
try:
    GLUT_WINDOW_ACCUM_BLUE_SIZE = 113
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 362
try:
    GLUT_WINDOW_ACCUM_ALPHA_SIZE = 114
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 363
try:
    GLUT_WINDOW_DOUBLEBUFFER = 115
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 364
try:
    GLUT_WINDOW_RGBA = 116
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 365
try:
    GLUT_WINDOW_PARENT = 117
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 366
try:
    GLUT_WINDOW_NUM_CHILDREN = 118
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 367
try:
    GLUT_WINDOW_COLORMAP_SIZE = 119
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 369
try:
    GLUT_WINDOW_NUM_SAMPLES = 120
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 370
try:
    GLUT_WINDOW_STEREO = 121
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 373
try:
    GLUT_WINDOW_CURSOR = 122
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 375
try:
    GLUT_SCREEN_WIDTH = 200
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 376
try:
    GLUT_SCREEN_HEIGHT = 201
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 377
try:
    GLUT_SCREEN_WIDTH_MM = 202
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 378
try:
    GLUT_SCREEN_HEIGHT_MM = 203
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 379
try:
    GLUT_MENU_NUM_ITEMS = 300
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 380
try:
    GLUT_DISPLAY_MODE_POSSIBLE = 400
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 381
try:
    GLUT_INIT_WINDOW_X = 500
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 382
try:
    GLUT_INIT_WINDOW_Y = 501
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 383
try:
    GLUT_INIT_WINDOW_WIDTH = 502
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 384
try:
    GLUT_INIT_WINDOW_HEIGHT = 503
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 385
try:
    GLUT_INIT_DISPLAY_MODE = 504
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 387
try:
    GLUT_ELAPSED_TIME = 700
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 390
try:
    GLUT_WINDOW_FORMAT_ID = 123
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 395
try:
    GLUT_HAS_KEYBOARD = 600
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 396
try:
    GLUT_HAS_MOUSE = 601
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 397
try:
    GLUT_HAS_SPACEBALL = 602
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 398
try:
    GLUT_HAS_DIAL_AND_BUTTON_BOX = 603
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 399
try:
    GLUT_HAS_TABLET = 604
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 400
try:
    GLUT_NUM_MOUSE_BUTTONS = 605
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 401
try:
    GLUT_NUM_SPACEBALL_BUTTONS = 606
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 402
try:
    GLUT_NUM_BUTTON_BOX_BUTTONS = 607
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 403
try:
    GLUT_NUM_DIALS = 608
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 404
try:
    GLUT_NUM_TABLET_BUTTONS = 609
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 407
try:
    GLUT_DEVICE_IGNORE_KEY_REPEAT = 610
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 408
try:
    GLUT_DEVICE_KEY_REPEAT = 611
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 409
try:
    GLUT_HAS_JOYSTICK = 612
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 410
try:
    GLUT_OWNS_JOYSTICK = 613
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 411
try:
    GLUT_JOYSTICK_BUTTONS = 614
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 412
try:
    GLUT_JOYSTICK_AXES = 615
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 413
try:
    GLUT_JOYSTICK_POLL_RATE = 616
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 418
try:
    GLUT_OVERLAY_POSSIBLE = 800
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 419
try:
    GLUT_LAYER_IN_USE = 801
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 420
try:
    GLUT_HAS_OVERLAY = 802
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 421
try:
    GLUT_TRANSPARENT_INDEX = 803
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 422
try:
    GLUT_NORMAL_DAMAGED = 804
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 423
try:
    GLUT_OVERLAY_DAMAGED = 805
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 427
try:
    GLUT_VIDEO_RESIZE_POSSIBLE = 900
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 428
try:
    GLUT_VIDEO_RESIZE_IN_USE = 901
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 429
try:
    GLUT_VIDEO_RESIZE_X_DELTA = 902
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 430
try:
    GLUT_VIDEO_RESIZE_Y_DELTA = 903
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 431
try:
    GLUT_VIDEO_RESIZE_WIDTH_DELTA = 904
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 432
try:
    GLUT_VIDEO_RESIZE_HEIGHT_DELTA = 905
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 433
try:
    GLUT_VIDEO_RESIZE_X = 906
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 434
try:
    GLUT_VIDEO_RESIZE_Y = 907
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 435
try:
    GLUT_VIDEO_RESIZE_WIDTH = 908
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 436
try:
    GLUT_VIDEO_RESIZE_HEIGHT = 909
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 440
try:
    GLUT_NORMAL = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 441
try:
    GLUT_OVERLAY = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 444
try:
    GLUT_ACTIVE_SHIFT = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 445
try:
    GLUT_ACTIVE_CTRL = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 446
try:
    GLUT_ACTIVE_ALT = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 450
try:
    GLUT_CURSOR_RIGHT_ARROW = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 451
try:
    GLUT_CURSOR_LEFT_ARROW = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 453
try:
    GLUT_CURSOR_INFO = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 454
try:
    GLUT_CURSOR_DESTROY = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 455
try:
    GLUT_CURSOR_HELP = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 456
try:
    GLUT_CURSOR_CYCLE = 5
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 457
try:
    GLUT_CURSOR_SPRAY = 6
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 458
try:
    GLUT_CURSOR_WAIT = 7
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 459
try:
    GLUT_CURSOR_TEXT = 8
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 460
try:
    GLUT_CURSOR_CROSSHAIR = 9
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 462
try:
    GLUT_CURSOR_UP_DOWN = 10
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 463
try:
    GLUT_CURSOR_LEFT_RIGHT = 11
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 465
try:
    GLUT_CURSOR_TOP_SIDE = 12
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 466
try:
    GLUT_CURSOR_BOTTOM_SIDE = 13
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 467
try:
    GLUT_CURSOR_LEFT_SIDE = 14
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 468
try:
    GLUT_CURSOR_RIGHT_SIDE = 15
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 469
try:
    GLUT_CURSOR_TOP_LEFT_CORNER = 16
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 470
try:
    GLUT_CURSOR_TOP_RIGHT_CORNER = 17
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 471
try:
    GLUT_CURSOR_BOTTOM_RIGHT_CORNER = 18
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 472
try:
    GLUT_CURSOR_BOTTOM_LEFT_CORNER = 19
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 474
try:
    GLUT_CURSOR_INHERIT = 100
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 476
try:
    GLUT_CURSOR_NONE = 101
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 478
try:
    GLUT_CURSOR_FULL_CROSSHAIR = 102
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 661
try:
    GLUT_KEY_REPEAT_OFF = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 662
try:
    GLUT_KEY_REPEAT_ON = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 663
try:
    GLUT_KEY_REPEAT_DEFAULT = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 666
try:
    GLUT_JOYSTICK_BUTTON_A = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 667
try:
    GLUT_JOYSTICK_BUTTON_B = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 668
try:
    GLUT_JOYSTICK_BUTTON_C = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 669
try:
    GLUT_JOYSTICK_BUTTON_D = 8
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 677
try:
    GLUT_GAME_MODE_ACTIVE = 0
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 678
try:
    GLUT_GAME_MODE_POSSIBLE = 1
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 679
try:
    GLUT_GAME_MODE_WIDTH = 2
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 680
try:
    GLUT_GAME_MODE_HEIGHT = 3
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 681
try:
    GLUT_GAME_MODE_PIXEL_DEPTH = 4
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 682
try:
    GLUT_GAME_MODE_REFRESH_RATE = 5
except:
    pass

# J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\glut.h: 683
try:
    GLUT_GAME_MODE_DISPLAY_CHANGED = 6
except:
    pass

InputSensorDescriptor_struct = struct_InputSensorDescriptor_struct # J:\\home\\eperfa\\Synetiq\\emotiv_sdk2\\edk.h: 128

GLUnurbs = struct_GLUnurbs # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 210

GLUquadric = struct_GLUquadric # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 211

GLUtesselator = struct_GLUtesselator # c:\\mingw32-xy\\bin\\../lib/gcc/mingw32/4.5.2/../../../../include/GL/glu.h: 212

# No inserted files

