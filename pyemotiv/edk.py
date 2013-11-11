'''
This file was hand-modified after being auto-generated.

bool parameters in functions weren't recognized properly, so they were commented out
in the original c code and added by hand to the python code 

'''

'''Wrapper for edk.h

Generated with:
C:\Users\eperfa\Documents\Synetiq\ctypesgen\ctypesgen.py -a -l edk.dll -o edk.py edk.h edkErrorCode.h EmoStateDLL.h

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
            
            for path in self.other_dirs:
                if os.path.exists(path):
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
    name_formats = ["%s", "%s.dll", "lib%s.dll", "%slib.dll"]

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

# FIXME eperfa
#add_library_search_dirs(["C:\\Program Files\\Emotiv Research Edition SDK v2.0.0.20\\dll\\32 bits\\"])
add_library_search_dirs(["C:\\Progra~1\\Emotiv~1.20\\dll\\32bit~1\\"])

# Begin libraries

_libs["edk.dll"] = load_library("edk.dll")

# 1 libraries
# End libraries

# No modules

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

EmoStateHandle = POINTER(None) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 27

enum_EE_EmotivSuite_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 36

EE_EXPRESSIV = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 36

EE_AFFECTIV = (EE_EXPRESSIV + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 36

EE_COGNITIV = (EE_AFFECTIV + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 36

EE_EmotivSuite_t = enum_EE_EmotivSuite_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 36

enum_EE_ExpressivAlgo_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_NEUTRAL = 1 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_BLINK = 2 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_WINK_LEFT = 4 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_WINK_RIGHT = 8 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_HORIEYE = 16 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_EYEBROW = 32 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_FURROW = 64 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_SMILE = 128 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_CLENCH = 256 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_LAUGH = 512 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_SMIRK_LEFT = 1024 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EXP_SMIRK_RIGHT = 2048 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

EE_ExpressivAlgo_t = enum_EE_ExpressivAlgo_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 56

enum_EE_AffectivAlgo_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

AFF_EXCITEMENT = 1 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

AFF_MEDITATION = 2 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

AFF_FRUSTRATION = 4 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

AFF_ENGAGEMENT_BOREDOM = 8 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

EE_AffectivAlgo_t = enum_EE_AffectivAlgo_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 68

enum_EE_CognitivAction_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_NEUTRAL = 1 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_PUSH = 2 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_PULL = 4 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_LIFT = 8 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_DROP = 16 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_LEFT = 32 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_RIGHT = 64 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_LEFT = 128 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_RIGHT = 256 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_CLOCKWISE = 512 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_COUNTER_CLOCKWISE = 1024 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_FORWARDS = 2048 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_ROTATE_REVERSE = 4096 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

COG_DISAPPEAR = 8192 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

EE_CognitivAction_t = enum_EE_CognitivAction_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 90

enum_EE_SignalStrength_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 99

NO_SIGNAL = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 99

BAD_SIGNAL = (NO_SIGNAL + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 99

GOOD_SIGNAL = (BAD_SIGNAL + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 99

EE_SignalStrength_t = enum_EE_SignalStrength_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 99

enum_EE_InputChannels_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_CMS = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_DRL = (EE_CHAN_CMS + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_FP1 = (EE_CHAN_DRL + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_AF3 = (EE_CHAN_FP1 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_F7 = (EE_CHAN_AF3 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_F3 = (EE_CHAN_F7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_FC5 = (EE_CHAN_F3 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_T7 = (EE_CHAN_FC5 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_P7 = (EE_CHAN_T7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_O1 = (EE_CHAN_P7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_O2 = (EE_CHAN_O1 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_P8 = (EE_CHAN_O2 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_T8 = (EE_CHAN_P8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_FC6 = (EE_CHAN_T8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_F4 = (EE_CHAN_FC6 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_F8 = (EE_CHAN_F4 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_AF4 = (EE_CHAN_F8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_CHAN_FP2 = (EE_CHAN_AF4 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

EE_InputChannels_t = enum_EE_InputChannels_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 111

enum_EE_EEG_ContactQuality_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EEG_CQ_NO_SIGNAL = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EEG_CQ_VERY_BAD = (EEG_CQ_NO_SIGNAL + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EEG_CQ_POOR = (EEG_CQ_VERY_BAD + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EEG_CQ_FAIR = (EEG_CQ_POOR + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EEG_CQ_GOOD = (EEG_CQ_FAIR + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

EE_EEG_ContactQuality_t = enum_EE_EEG_ContactQuality_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 121

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 134
if hasattr(_libs['edk.dll'], 'ES_Create'):
    ES_Create = _libs['edk.dll'].ES_Create
    ES_Create.argtypes = []
    ES_Create.restype = EmoStateHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 144
if hasattr(_libs['edk.dll'], 'ES_Free'):
    ES_Free = _libs['edk.dll'].ES_Free
    ES_Free.argtypes = [EmoStateHandle]
    ES_Free.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 152
if hasattr(_libs['edk.dll'], 'ES_Init'):
    ES_Init = _libs['edk.dll'].ES_Init
    ES_Init.argtypes = [EmoStateHandle]
    ES_Init.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 164
if hasattr(_libs['edk.dll'], 'ES_GetTimeFromStart'):
    ES_GetTimeFromStart = _libs['edk.dll'].ES_GetTimeFromStart
    ES_GetTimeFromStart.argtypes = [EmoStateHandle]
    ES_GetTimeFromStart.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 175
if hasattr(_libs['edk.dll'], 'ES_GetHeadsetOn'):
    ES_GetHeadsetOn = _libs['edk.dll'].ES_GetHeadsetOn
    ES_GetHeadsetOn.argtypes = [EmoStateHandle]
    ES_GetHeadsetOn.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 184
if hasattr(_libs['edk.dll'], 'ES_GetNumContactQualityChannels'):
    ES_GetNumContactQualityChannels = _libs['edk.dll'].ES_GetNumContactQualityChannels
    ES_GetNumContactQualityChannels.argtypes = [EmoStateHandle]
    ES_GetNumContactQualityChannels.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 195
if hasattr(_libs['edk.dll'], 'ES_GetContactQuality'):
    ES_GetContactQuality = _libs['edk.dll'].ES_GetContactQuality
    ES_GetContactQuality.argtypes = [EmoStateHandle, c_int]
    ES_GetContactQuality.restype = EE_EEG_ContactQuality_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 215
if hasattr(_libs['edk.dll'], 'ES_GetContactQualityFromAllChannels'):
    ES_GetContactQualityFromAllChannels = _libs['edk.dll'].ES_GetContactQualityFromAllChannels
    ES_GetContactQualityFromAllChannels.argtypes = [EmoStateHandle, POINTER(EE_EEG_ContactQuality_t), c_size_t]
    ES_GetContactQualityFromAllChannels.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 224
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsBlink'):
    ES_ExpressivIsBlink = _libs['edk.dll'].ES_ExpressivIsBlink
    ES_ExpressivIsBlink.argtypes = [EmoStateHandle]
    ES_ExpressivIsBlink.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 234
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLeftWink'):
    ES_ExpressivIsLeftWink = _libs['edk.dll'].ES_ExpressivIsLeftWink
    ES_ExpressivIsLeftWink.argtypes = [EmoStateHandle]
    ES_ExpressivIsLeftWink.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 244
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsRightWink'):
    ES_ExpressivIsRightWink = _libs['edk.dll'].ES_ExpressivIsRightWink
    ES_ExpressivIsRightWink.argtypes = [EmoStateHandle]
    ES_ExpressivIsRightWink.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 253
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsEyesOpen'):
    ES_ExpressivIsEyesOpen = _libs['edk.dll'].ES_ExpressivIsEyesOpen
    ES_ExpressivIsEyesOpen.argtypes = [EmoStateHandle]
    ES_ExpressivIsEyesOpen.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 263
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingUp'):
    ES_ExpressivIsLookingUp = _libs['edk.dll'].ES_ExpressivIsLookingUp
    ES_ExpressivIsLookingUp.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingUp.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 273
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingDown'):
    ES_ExpressivIsLookingDown = _libs['edk.dll'].ES_ExpressivIsLookingDown
    ES_ExpressivIsLookingDown.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingDown.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 283
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingLeft'):
    ES_ExpressivIsLookingLeft = _libs['edk.dll'].ES_ExpressivIsLookingLeft
    ES_ExpressivIsLookingLeft.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingLeft.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 293
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsLookingRight'):
    ES_ExpressivIsLookingRight = _libs['edk.dll'].ES_ExpressivIsLookingRight
    ES_ExpressivIsLookingRight.argtypes = [EmoStateHandle]
    ES_ExpressivIsLookingRight.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 307
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyelidState'):
    ES_ExpressivGetEyelidState = _libs['edk.dll'].ES_ExpressivGetEyelidState
    ES_ExpressivGetEyelidState.argtypes = [EmoStateHandle, POINTER(c_float), POINTER(c_float)]
    ES_ExpressivGetEyelidState.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 328
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyeLocation'):
    ES_ExpressivGetEyeLocation = _libs['edk.dll'].ES_ExpressivGetEyeLocation
    ES_ExpressivGetEyeLocation.argtypes = [EmoStateHandle, POINTER(c_float), POINTER(c_float)]
    ES_ExpressivGetEyeLocation.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 338
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetEyebrowExtent'):
    ES_ExpressivGetEyebrowExtent = _libs['edk.dll'].ES_ExpressivGetEyebrowExtent
    ES_ExpressivGetEyebrowExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetEyebrowExtent.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 348
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetSmileExtent'):
    ES_ExpressivGetSmileExtent = _libs['edk.dll'].ES_ExpressivGetSmileExtent
    ES_ExpressivGetSmileExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetSmileExtent.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 358
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetClenchExtent'):
    ES_ExpressivGetClenchExtent = _libs['edk.dll'].ES_ExpressivGetClenchExtent
    ES_ExpressivGetClenchExtent.argtypes = [EmoStateHandle]
    ES_ExpressivGetClenchExtent.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 369
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetUpperFaceAction'):
    ES_ExpressivGetUpperFaceAction = _libs['edk.dll'].ES_ExpressivGetUpperFaceAction
    ES_ExpressivGetUpperFaceAction.argtypes = [EmoStateHandle]
    ES_ExpressivGetUpperFaceAction.restype = EE_ExpressivAlgo_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 379
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetUpperFaceActionPower'):
    ES_ExpressivGetUpperFaceActionPower = _libs['edk.dll'].ES_ExpressivGetUpperFaceActionPower
    ES_ExpressivGetUpperFaceActionPower.argtypes = [EmoStateHandle]
    ES_ExpressivGetUpperFaceActionPower.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 389
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetLowerFaceAction'):
    ES_ExpressivGetLowerFaceAction = _libs['edk.dll'].ES_ExpressivGetLowerFaceAction
    ES_ExpressivGetLowerFaceAction.argtypes = [EmoStateHandle]
    ES_ExpressivGetLowerFaceAction.restype = EE_ExpressivAlgo_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 399
if hasattr(_libs['edk.dll'], 'ES_ExpressivGetLowerFaceActionPower'):
    ES_ExpressivGetLowerFaceActionPower = _libs['edk.dll'].ES_ExpressivGetLowerFaceActionPower
    ES_ExpressivGetLowerFaceActionPower.argtypes = [EmoStateHandle]
    ES_ExpressivGetLowerFaceActionPower.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 410
if hasattr(_libs['edk.dll'], 'ES_ExpressivIsActive'):
    ES_ExpressivIsActive = _libs['edk.dll'].ES_ExpressivIsActive
    ES_ExpressivIsActive.argtypes = [EmoStateHandle, EE_ExpressivAlgo_t]
    ES_ExpressivIsActive.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 420
if hasattr(_libs['edk.dll'], 'ES_AffectivGetExcitementLongTermScore'):
    ES_AffectivGetExcitementLongTermScore = _libs['edk.dll'].ES_AffectivGetExcitementLongTermScore
    ES_AffectivGetExcitementLongTermScore.argtypes = [EmoStateHandle]
    ES_AffectivGetExcitementLongTermScore.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 430
if hasattr(_libs['edk.dll'], 'ES_AffectivGetExcitementShortTermScore'):
    ES_AffectivGetExcitementShortTermScore = _libs['edk.dll'].ES_AffectivGetExcitementShortTermScore
    ES_AffectivGetExcitementShortTermScore.argtypes = [EmoStateHandle]
    ES_AffectivGetExcitementShortTermScore.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 441
if hasattr(_libs['edk.dll'], 'ES_AffectivIsActive'):
    ES_AffectivIsActive = _libs['edk.dll'].ES_AffectivIsActive
    ES_AffectivIsActive.argtypes = [EmoStateHandle, EE_AffectivAlgo_t]
    ES_AffectivIsActive.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 449
if hasattr(_libs['edk.dll'], 'ES_AffectivGetMeditationScore'):
    ES_AffectivGetMeditationScore = _libs['edk.dll'].ES_AffectivGetMeditationScore
    ES_AffectivGetMeditationScore.argtypes = [EmoStateHandle]
    ES_AffectivGetMeditationScore.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 457
if hasattr(_libs['edk.dll'], 'ES_AffectivGetFrustrationScore'):
    ES_AffectivGetFrustrationScore = _libs['edk.dll'].ES_AffectivGetFrustrationScore
    ES_AffectivGetFrustrationScore.argtypes = [EmoStateHandle]
    ES_AffectivGetFrustrationScore.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 465
if hasattr(_libs['edk.dll'], 'ES_AffectivGetEngagementBoredomScore'):
    ES_AffectivGetEngagementBoredomScore = _libs['edk.dll'].ES_AffectivGetEngagementBoredomScore
    ES_AffectivGetEngagementBoredomScore.argtypes = [EmoStateHandle]
    ES_AffectivGetEngagementBoredomScore.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 475
if hasattr(_libs['edk.dll'], 'ES_CognitivGetCurrentAction'):
    ES_CognitivGetCurrentAction = _libs['edk.dll'].ES_CognitivGetCurrentAction
    ES_CognitivGetCurrentAction.argtypes = [EmoStateHandle]
    ES_CognitivGetCurrentAction.restype = EE_CognitivAction_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 485
if hasattr(_libs['edk.dll'], 'ES_CognitivGetCurrentActionPower'):
    ES_CognitivGetCurrentActionPower = _libs['edk.dll'].ES_CognitivGetCurrentActionPower
    ES_CognitivGetCurrentActionPower.argtypes = [EmoStateHandle]
    ES_CognitivGetCurrentActionPower.restype = c_float

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 493
if hasattr(_libs['edk.dll'], 'ES_CognitivIsActive'):
    ES_CognitivIsActive = _libs['edk.dll'].ES_CognitivIsActive
    ES_CognitivIsActive.argtypes = [EmoStateHandle]
    ES_CognitivIsActive.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 504
if hasattr(_libs['edk.dll'], 'ES_GetWirelessSignalStatus'):
    ES_GetWirelessSignalStatus = _libs['edk.dll'].ES_GetWirelessSignalStatus
    ES_GetWirelessSignalStatus.argtypes = [EmoStateHandle]
    ES_GetWirelessSignalStatus.restype = EE_SignalStrength_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 513
if hasattr(_libs['edk.dll'], 'ES_Copy'):
    ES_Copy = _libs['edk.dll'].ES_Copy
    ES_Copy.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_Copy.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 524
if hasattr(_libs['edk.dll'], 'ES_AffectivEqual'):
    ES_AffectivEqual = _libs['edk.dll'].ES_AffectivEqual
    ES_AffectivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_AffectivEqual.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 535
if hasattr(_libs['edk.dll'], 'ES_ExpressivEqual'):
    ES_ExpressivEqual = _libs['edk.dll'].ES_ExpressivEqual
    ES_ExpressivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_ExpressivEqual.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 546
if hasattr(_libs['edk.dll'], 'ES_CognitivEqual'):
    ES_CognitivEqual = _libs['edk.dll'].ES_CognitivEqual
    ES_CognitivEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_CognitivEqual.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 560
if hasattr(_libs['edk.dll'], 'ES_EmoEngineEqual'):
    ES_EmoEngineEqual = _libs['edk.dll'].ES_EmoEngineEqual
    ES_EmoEngineEqual.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_EmoEngineEqual.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 571
if hasattr(_libs['edk.dll'], 'ES_Equal'):
    ES_Equal = _libs['edk.dll'].ES_Equal
    ES_Equal.argtypes = [EmoStateHandle, EmoStateHandle]
    ES_Equal.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/EmoStateDLL.h: 580
if hasattr(_libs['edk.dll'], 'ES_GetBatteryChargeLevel'):
    ES_GetBatteryChargeLevel = _libs['edk.dll'].ES_GetBatteryChargeLevel
    ES_GetBatteryChargeLevel.argtypes = [EmoStateHandle, POINTER(c_int), POINTER(c_int)]
    ES_GetBatteryChargeLevel.restype = None

enum_EE_ExpressivThreshold_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 27

EXP_SENSITIVITY = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 27

EE_ExpressivThreshold_t = enum_EE_ExpressivThreshold_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 27

enum_EE_ExpressivTrainingControl_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_NONE = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_START = (EXP_NONE + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_ACCEPT = (EXP_START + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_REJECT = (EXP_ACCEPT + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_ERASE = (EXP_REJECT + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EXP_RESET = (EXP_ERASE + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

EE_ExpressivTrainingControl_t = enum_EE_ExpressivTrainingControl_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 32

enum_EE_ExpressivSignature_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 37

EXP_SIG_UNIVERSAL = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 37

EXP_SIG_TRAINED = (EXP_SIG_UNIVERSAL + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 37

EE_ExpressivSignature_t = enum_EE_ExpressivSignature_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 37

enum_EE_CognitivTrainingControl_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_NONE = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_START = (COG_NONE + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_ACCEPT = (COG_START + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_REJECT = (COG_ACCEPT + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_ERASE = (COG_REJECT + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

COG_RESET = (COG_ERASE + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

EE_CognitivTrainingControl_t = enum_EE_CognitivTrainingControl_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 42

EmoEngineEventHandle = POINTER(None) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 49

OptimizationParamHandle = POINTER(None) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 52

DataHandle = POINTER(None) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 54

enum_EE_Event_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_UnknownEvent = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_EmulatorError = 1 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_ReservedEvent = 2 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_UserAdded = 16 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_UserRemoved = 32 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_EmoStateUpdated = 64 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_ProfileEvent = 128 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_CognitivEvent = 256 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_ExpressivEvent = 512 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_InternalStateChanged = 1024 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_AllEvent = ((((((EE_UserAdded | EE_UserRemoved) | EE_EmoStateUpdated) | EE_ProfileEvent) | EE_CognitivEvent) | EE_ExpressivEvent) | EE_InternalStateChanged) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

EE_Event_t = enum_EE_Event_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 70

enum_EE_ExpressivEvent_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivNoEvent = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingStarted = (EE_ExpressivNoEvent + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingSucceeded = (EE_ExpressivTrainingStarted + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingFailed = (EE_ExpressivTrainingSucceeded + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingCompleted = (EE_ExpressivTrainingFailed + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingDataErased = (EE_ExpressivTrainingCompleted + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingRejected = (EE_ExpressivTrainingDataErased + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivTrainingReset = (EE_ExpressivTrainingRejected + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

EE_ExpressivEvent_t = enum_EE_ExpressivEvent_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 77

enum_EE_CognitivEvent_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivNoEvent = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingStarted = (EE_CognitivNoEvent + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingSucceeded = (EE_CognitivTrainingStarted + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingFailed = (EE_CognitivTrainingSucceeded + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingCompleted = (EE_CognitivTrainingFailed + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingDataErased = (EE_CognitivTrainingCompleted + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingRejected = (EE_CognitivTrainingDataErased + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivTrainingReset = (EE_CognitivTrainingRejected + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivAutoSamplingNeutralCompleted = (EE_CognitivTrainingReset + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivSignatureUpdated = (EE_CognitivAutoSamplingNeutralCompleted + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

EE_CognitivEvent_t = enum_EE_CognitivEvent_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 85

enum_EE_DataChannels_enum = c_int # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_COUNTER = 0 # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_INTERPOLATED = (ED_COUNTER + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_RAW_CQ = (ED_INTERPOLATED + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_AF3 = (ED_RAW_CQ + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_F7 = (ED_AF3 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_F3 = (ED_F7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_FC5 = (ED_F3 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_T7 = (ED_FC5 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_P7 = (ED_T7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_O1 = (ED_P7 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_O2 = (ED_O1 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_P8 = (ED_O2 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_T8 = (ED_P8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_FC6 = (ED_T8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_F4 = (ED_FC6 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_F8 = (ED_F4 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_AF4 = (ED_F8 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_GYROX = (ED_AF4 + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_GYROY = (ED_GYROX + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_TIMESTAMP = (ED_GYROY + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_ES_TIMESTAMP = (ED_TIMESTAMP + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_FUNC_ID = (ED_ES_TIMESTAMP + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_FUNC_VALUE = (ED_FUNC_ID + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_MARKER = (ED_FUNC_VALUE + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

ED_SYNC_SIGNAL = (ED_MARKER + 1) # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

EE_DataChannel_t = enum_EE_DataChannels_enum # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 94

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 104
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

InputSensorDescriptor_t = struct_InputSensorDescriptor_struct # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 104

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 115
if hasattr(_libs['edk.dll'], 'EE_EngineConnect'):
    EE_EngineConnect = _libs['edk.dll'].EE_EngineConnect
    EE_EngineConnect.argtypes = [String]
    EE_EngineConnect.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 133
if hasattr(_libs['edk.dll'], 'EE_EngineRemoteConnect'):
    EE_EngineRemoteConnect = _libs['edk.dll'].EE_EngineRemoteConnect
    EE_EngineRemoteConnect.argtypes = [String, c_ushort, String]
    EE_EngineRemoteConnect.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 144
if hasattr(_libs['edk.dll'], 'EE_EngineDisconnect'):
    EE_EngineDisconnect = _libs['edk.dll'].EE_EngineDisconnect
    EE_EngineDisconnect.argtypes = []
    EE_EngineDisconnect.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 158
if hasattr(_libs['edk.dll'], 'EE_EnableDiagnostics'):
    EE_EnableDiagnostics = _libs['edk.dll'].EE_EnableDiagnostics
    EE_EnableDiagnostics.argtypes = [String, c_int, c_int]
    EE_EnableDiagnostics.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 166
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventCreate'):
    EE_EmoEngineEventCreate = _libs['edk.dll'].EE_EmoEngineEventCreate
    EE_EmoEngineEventCreate.argtypes = []
    EE_EmoEngineEventCreate.restype = EmoEngineEventHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 174
if hasattr(_libs['edk.dll'], 'EE_ProfileEventCreate'):
    EE_ProfileEventCreate = _libs['edk.dll'].EE_ProfileEventCreate
    EE_ProfileEventCreate.argtypes = []
    EE_ProfileEventCreate.restype = EmoEngineEventHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 182
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventFree'):
    EE_EmoEngineEventFree = _libs['edk.dll'].EE_EmoEngineEventFree
    EE_EmoEngineEventFree.argtypes = [EmoEngineEventHandle]
    EE_EmoEngineEventFree.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 190
if hasattr(_libs['edk.dll'], 'EE_EmoStateCreate'):
    EE_EmoStateCreate = _libs['edk.dll'].EE_EmoStateCreate
    EE_EmoStateCreate.argtypes = []
    EE_EmoStateCreate.restype = EmoStateHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 198
if hasattr(_libs['edk.dll'], 'EE_EmoStateFree'):
    EE_EmoStateFree = _libs['edk.dll'].EE_EmoStateFree
    EE_EmoStateFree.argtypes = [EmoStateHandle]
    EE_EmoStateFree.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 208
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetType'):
    EE_EmoEngineEventGetType = _libs['edk.dll'].EE_EmoEngineEventGetType
    EE_EmoEngineEventGetType.argtypes = [EmoEngineEventHandle]
    EE_EmoEngineEventGetType.restype = EE_Event_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 218
if hasattr(_libs['edk.dll'], 'EE_CognitivEventGetType'):
    EE_CognitivEventGetType = _libs['edk.dll'].EE_CognitivEventGetType
    EE_CognitivEventGetType.argtypes = [EmoEngineEventHandle]
    EE_CognitivEventGetType.restype = EE_CognitivEvent_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 228
if hasattr(_libs['edk.dll'], 'EE_ExpressivEventGetType'):
    EE_ExpressivEventGetType = _libs['edk.dll'].EE_ExpressivEventGetType
    EE_ExpressivEventGetType.argtypes = [EmoEngineEventHandle]
    EE_ExpressivEventGetType.restype = EE_ExpressivEvent_t

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 242
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetUserId'):
    EE_EmoEngineEventGetUserId = _libs['edk.dll'].EE_EmoEngineEventGetUserId
    EE_EmoEngineEventGetUserId.argtypes = [EmoEngineEventHandle, POINTER(c_uint)]
    EE_EmoEngineEventGetUserId.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 256
if hasattr(_libs['edk.dll'], 'EE_EmoEngineEventGetEmoState'):
    EE_EmoEngineEventGetEmoState = _libs['edk.dll'].EE_EmoEngineEventGetEmoState
    EE_EmoEngineEventGetEmoState.argtypes = [EmoEngineEventHandle, EmoStateHandle]
    EE_EmoEngineEventGetEmoState.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 274
if hasattr(_libs['edk.dll'], 'EE_EngineGetNextEvent'):
    EE_EngineGetNextEvent = _libs['edk.dll'].EE_EngineGetNextEvent
    EE_EngineGetNextEvent.argtypes = [EmoEngineEventHandle]
    EE_EngineGetNextEvent.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 290
if hasattr(_libs['edk.dll'], 'EE_EngineClearEventQueue'):
    EE_EngineClearEventQueue = _libs['edk.dll'].EE_EngineClearEventQueue
    EE_EngineClearEventQueue.argtypes = [c_int]
    EE_EngineClearEventQueue.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 303
if hasattr(_libs['edk.dll'], 'EE_EngineGetNumUser'):
    EE_EngineGetNumUser = _libs['edk.dll'].EE_EngineGetNumUser
    EE_EngineGetNumUser.argtypes = [POINTER(c_uint)]
    EE_EngineGetNumUser.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 316
if hasattr(_libs['edk.dll'], 'EE_SetHardwarePlayerDisplay'):
    EE_SetHardwarePlayerDisplay = _libs['edk.dll'].EE_SetHardwarePlayerDisplay
    EE_SetHardwarePlayerDisplay.argtypes = [c_uint, c_uint]
    EE_SetHardwarePlayerDisplay.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 331
if hasattr(_libs['edk.dll'], 'EE_SetUserProfile'):
    EE_SetUserProfile = _libs['edk.dll'].EE_SetUserProfile
    EE_SetUserProfile.argtypes = [c_uint, POINTER(c_ubyte), c_uint]
    EE_SetUserProfile.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 348
if hasattr(_libs['edk.dll'], 'EE_GetUserProfile'):
    EE_GetUserProfile = _libs['edk.dll'].EE_GetUserProfile
    EE_GetUserProfile.argtypes = [c_uint, EmoEngineEventHandle]
    EE_GetUserProfile.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 364
if hasattr(_libs['edk.dll'], 'EE_GetBaseProfile'):
    EE_GetBaseProfile = _libs['edk.dll'].EE_GetBaseProfile
    EE_GetBaseProfile.argtypes = [EmoEngineEventHandle]
    EE_GetBaseProfile.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 378
if hasattr(_libs['edk.dll'], 'EE_GetUserProfileSize'):
    EE_GetUserProfileSize = _libs['edk.dll'].EE_GetUserProfileSize
    EE_GetUserProfileSize.argtypes = [EmoEngineEventHandle, POINTER(c_uint)]
    EE_GetUserProfileSize.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 393
if hasattr(_libs['edk.dll'], 'EE_GetUserProfileBytes'):
    EE_GetUserProfileBytes = _libs['edk.dll'].EE_GetUserProfileBytes
    EE_GetUserProfileBytes.argtypes = [EmoEngineEventHandle, POINTER(c_ubyte), c_uint]
    EE_GetUserProfileBytes.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 406
if hasattr(_libs['edk.dll'], 'EE_LoadUserProfile'):
    EE_LoadUserProfile = _libs['edk.dll'].EE_LoadUserProfile
    EE_LoadUserProfile.argtypes = [c_uint, String]
    EE_LoadUserProfile.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 419
if hasattr(_libs['edk.dll'], 'EE_SaveUserProfile'):
    EE_SaveUserProfile = _libs['edk.dll'].EE_SaveUserProfile
    EE_SaveUserProfile.argtypes = [c_uint, String]
    EE_SaveUserProfile.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 434
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetThreshold'):
    EE_ExpressivSetThreshold = _libs['edk.dll'].EE_ExpressivSetThreshold
    EE_ExpressivSetThreshold.argtypes = [c_uint, EE_ExpressivAlgo_t, EE_ExpressivThreshold_t, c_int]
    EE_ExpressivSetThreshold.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 450
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetThreshold'):
    EE_ExpressivGetThreshold = _libs['edk.dll'].EE_ExpressivGetThreshold
    EE_ExpressivGetThreshold.argtypes = [c_uint, EE_ExpressivAlgo_t, EE_ExpressivThreshold_t, POINTER(c_int)]
    EE_ExpressivGetThreshold.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 465
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetTrainingAction'):
    EE_ExpressivSetTrainingAction = _libs['edk.dll'].EE_ExpressivSetTrainingAction
    EE_ExpressivSetTrainingAction.argtypes = [c_uint, EE_ExpressivAlgo_t]
    EE_ExpressivSetTrainingAction.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 480
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetTrainingControl'):
    EE_ExpressivSetTrainingControl = _libs['edk.dll'].EE_ExpressivSetTrainingControl
    EE_ExpressivSetTrainingControl.argtypes = [c_uint, EE_ExpressivTrainingControl_t]
    EE_ExpressivSetTrainingControl.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 495
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainingAction'):
    EE_ExpressivGetTrainingAction = _libs['edk.dll'].EE_ExpressivGetTrainingAction
    EE_ExpressivGetTrainingAction.argtypes = [c_uint, POINTER(EE_ExpressivAlgo_t)]
    EE_ExpressivGetTrainingAction.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 509
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainingTime'):
    EE_ExpressivGetTrainingTime = _libs['edk.dll'].EE_ExpressivGetTrainingTime
    EE_ExpressivGetTrainingTime.argtypes = [c_uint, POINTER(c_uint)]
    EE_ExpressivGetTrainingTime.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 524
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainedSignatureActions'):
    EE_ExpressivGetTrainedSignatureActions = _libs['edk.dll'].EE_ExpressivGetTrainedSignatureActions
    EE_ExpressivGetTrainedSignatureActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_ExpressivGetTrainedSignatureActions.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 542
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetTrainedSignatureAvailable'):
    EE_ExpressivGetTrainedSignatureAvailable = _libs['edk.dll'].EE_ExpressivGetTrainedSignatureAvailable
    EE_ExpressivGetTrainedSignatureAvailable.argtypes = [c_uint, POINTER(c_int)]
    EE_ExpressivGetTrainedSignatureAvailable.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 558
if hasattr(_libs['edk.dll'], 'EE_ExpressivSetSignatureType'):
    EE_ExpressivSetSignatureType = _libs['edk.dll'].EE_ExpressivSetSignatureType
    EE_ExpressivSetSignatureType.argtypes = [c_uint, EE_ExpressivSignature_t]
    EE_ExpressivSetSignatureType.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 572
if hasattr(_libs['edk.dll'], 'EE_ExpressivGetSignatureType'):
    EE_ExpressivGetSignatureType = _libs['edk.dll'].EE_ExpressivGetSignatureType
    EE_ExpressivGetSignatureType.argtypes = [c_uint, POINTER(EE_ExpressivSignature_t)]
    EE_ExpressivGetSignatureType.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 588
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActiveActions'):
    EE_CognitivSetActiveActions = _libs['edk.dll'].EE_CognitivSetActiveActions
    EE_CognitivSetActiveActions.argtypes = [c_uint, c_ulong]
    EE_CognitivSetActiveActions.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 602
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActiveActions'):
    EE_CognitivGetActiveActions = _libs['edk.dll'].EE_CognitivGetActiveActions
    EE_CognitivGetActiveActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_CognitivGetActiveActions.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 616
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainingTime'):
    EE_CognitivGetTrainingTime = _libs['edk.dll'].EE_CognitivGetTrainingTime
    EE_CognitivGetTrainingTime.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetTrainingTime.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 630
if hasattr(_libs['edk.dll'], 'EE_CognitivSetTrainingControl'):
    EE_CognitivSetTrainingControl = _libs['edk.dll'].EE_CognitivSetTrainingControl
    EE_CognitivSetTrainingControl.argtypes = [c_uint, EE_CognitivTrainingControl_t]
    EE_CognitivSetTrainingControl.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 644
if hasattr(_libs['edk.dll'], 'EE_CognitivSetTrainingAction'):
    EE_CognitivSetTrainingAction = _libs['edk.dll'].EE_CognitivSetTrainingAction
    EE_CognitivSetTrainingAction.argtypes = [c_uint, EE_CognitivAction_t]
    EE_CognitivSetTrainingAction.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 658
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainingAction'):
    EE_CognitivGetTrainingAction = _libs['edk.dll'].EE_CognitivGetTrainingAction
    EE_CognitivGetTrainingAction.argtypes = [c_uint, POINTER(EE_CognitivAction_t)]
    EE_CognitivGetTrainingAction.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 674
if hasattr(_libs['edk.dll'], 'EE_CognitivGetTrainedSignatureActions'):
    EE_CognitivGetTrainedSignatureActions = _libs['edk.dll'].EE_CognitivGetTrainedSignatureActions
    EE_CognitivGetTrainedSignatureActions.argtypes = [c_uint, POINTER(c_ulong)]
    EE_CognitivGetTrainedSignatureActions.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 690
if hasattr(_libs['edk.dll'], 'EE_CognitivGetOverallSkillRating'):
    EE_CognitivGetOverallSkillRating = _libs['edk.dll'].EE_CognitivGetOverallSkillRating
    EE_CognitivGetOverallSkillRating.argtypes = [c_uint, POINTER(c_float)]
    EE_CognitivGetOverallSkillRating.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 707
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActionSkillRating'):
    EE_CognitivGetActionSkillRating = _libs['edk.dll'].EE_CognitivGetActionSkillRating
    EE_CognitivGetActionSkillRating.argtypes = [c_uint, EE_CognitivAction_t, POINTER(c_float)]
    EE_CognitivGetActionSkillRating.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 721
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActivationLevel'):
    EE_CognitivSetActivationLevel = _libs['edk.dll'].EE_CognitivSetActivationLevel
    EE_CognitivSetActivationLevel.argtypes = [c_uint, c_int]
    EE_CognitivSetActivationLevel.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 738
if hasattr(_libs['edk.dll'], 'EE_CognitivSetActionSensitivity'):
    EE_CognitivSetActionSensitivity = _libs['edk.dll'].EE_CognitivSetActionSensitivity
    EE_CognitivSetActionSensitivity.argtypes = [c_uint, c_int, c_int, c_int, c_int]
    EE_CognitivSetActionSensitivity.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 754
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActivationLevel'):
    EE_CognitivGetActivationLevel = _libs['edk.dll'].EE_CognitivGetActivationLevel
    EE_CognitivGetActivationLevel.argtypes = [c_uint, POINTER(c_int)]
    EE_CognitivGetActivationLevel.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 771
if hasattr(_libs['edk.dll'], 'EE_CognitivGetActionSensitivity'):
    EE_CognitivGetActionSensitivity = _libs['edk.dll'].EE_CognitivGetActionSensitivity
    EE_CognitivGetActionSensitivity.argtypes = [c_uint, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    EE_CognitivGetActionSensitivity.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 786
if hasattr(_libs['edk.dll'], 'EE_CognitivStartSamplingNeutral'):
    EE_CognitivStartSamplingNeutral = _libs['edk.dll'].EE_CognitivStartSamplingNeutral
    EE_CognitivStartSamplingNeutral.argtypes = [c_uint]
    EE_CognitivStartSamplingNeutral.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 799
if hasattr(_libs['edk.dll'], 'EE_CognitivStopSamplingNeutral'):
    EE_CognitivStopSamplingNeutral = _libs['edk.dll'].EE_CognitivStopSamplingNeutral
    EE_CognitivStopSamplingNeutral.argtypes = [c_uint]
    EE_CognitivStopSamplingNeutral.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 813
if hasattr(_libs['edk.dll'], 'EE_CognitivSetSignatureCaching'):
    EE_CognitivSetSignatureCaching = _libs['edk.dll'].EE_CognitivSetSignatureCaching
    EE_CognitivSetSignatureCaching.argtypes = [c_uint, c_uint]
    EE_CognitivSetSignatureCaching.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 827
if hasattr(_libs['edk.dll'], 'EE_CognitivGetSignatureCaching'):
    EE_CognitivGetSignatureCaching = _libs['edk.dll'].EE_CognitivGetSignatureCaching
    EE_CognitivGetSignatureCaching.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetSignatureCaching.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 841
if hasattr(_libs['edk.dll'], 'EE_CognitivSetSignatureCacheSize'):
    EE_CognitivSetSignatureCacheSize = _libs['edk.dll'].EE_CognitivSetSignatureCacheSize
    EE_CognitivSetSignatureCacheSize.argtypes = [c_uint, c_uint]
    EE_CognitivSetSignatureCacheSize.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 855
if hasattr(_libs['edk.dll'], 'EE_CognitivGetSignatureCacheSize'):
    EE_CognitivGetSignatureCacheSize = _libs['edk.dll'].EE_CognitivGetSignatureCacheSize
    EE_CognitivGetSignatureCacheSize.argtypes = [c_uint, POINTER(c_uint)]
    EE_CognitivGetSignatureCacheSize.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 869
if hasattr(_libs['edk.dll'], 'EE_HeadsetGetSensorDetails'):
    EE_HeadsetGetSensorDetails = _libs['edk.dll'].EE_HeadsetGetSensorDetails
    EE_HeadsetGetSensorDetails.argtypes = [EE_InputChannels_t, POINTER(InputSensorDescriptor_t)]
    EE_HeadsetGetSensorDetails.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 883
if hasattr(_libs['edk.dll'], 'EE_HardwareGetVersion'):
    EE_HardwareGetVersion = _libs['edk.dll'].EE_HardwareGetVersion
    EE_HardwareGetVersion.argtypes = [c_uint, POINTER(c_ulong)]
    EE_HardwareGetVersion.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 897
if hasattr(_libs['edk.dll'], 'EE_SoftwareGetVersion'):
    EE_SoftwareGetVersion = _libs['edk.dll'].EE_SoftwareGetVersion
    EE_SoftwareGetVersion.argtypes = [String, c_uint, POINTER(c_ulong)]
    EE_SoftwareGetVersion.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 912
if hasattr(_libs['edk.dll'], 'EE_HeadsetGetGyroDelta'):
    EE_HeadsetGetGyroDelta = _libs['edk.dll'].EE_HeadsetGetGyroDelta
    EE_HeadsetGetGyroDelta.argtypes = [c_uint, POINTER(c_int), POINTER(c_int)]
    EE_HeadsetGetGyroDelta.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 925
if hasattr(_libs['edk.dll'], 'EE_HeadsetGyroRezero'):
    EE_HeadsetGyroRezero = _libs['edk.dll'].EE_HeadsetGyroRezero
    EE_HeadsetGyroRezero.argtypes = [c_uint]
    EE_HeadsetGyroRezero.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 932
if hasattr(_libs['edk.dll'], 'EE_OptimizationParamCreate'):
    EE_OptimizationParamCreate = _libs['edk.dll'].EE_OptimizationParamCreate
    EE_OptimizationParamCreate.argtypes = []
    EE_OptimizationParamCreate.restype = OptimizationParamHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 939
if hasattr(_libs['edk.dll'], 'EE_OptimizationParamFree'):
    EE_OptimizationParamFree = _libs['edk.dll'].EE_OptimizationParamFree
    EE_OptimizationParamFree.argtypes = [OptimizationParamHandle]
    EE_OptimizationParamFree.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 948
if hasattr(_libs['edk.dll'], 'EE_OptimizationEnable'):
    EE_OptimizationEnable = _libs['edk.dll'].EE_OptimizationEnable
    EE_OptimizationEnable.argtypes = [OptimizationParamHandle]
    EE_OptimizationEnable.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 957
if hasattr(_libs['edk.dll'], 'EE_OptimizationIsEnabled'):
    EE_OptimizationIsEnabled = _libs['edk.dll'].EE_OptimizationIsEnabled
    EE_OptimizationIsEnabled.argtypes = [POINTER(c_bool)]
    EE_OptimizationIsEnabled.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 965
if hasattr(_libs['edk.dll'], 'EE_OptimizationDisable'):
    EE_OptimizationDisable = _libs['edk.dll'].EE_OptimizationDisable
    EE_OptimizationDisable.argtypes = []
    EE_OptimizationDisable.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 974
if hasattr(_libs['edk.dll'], 'EE_OptimizationGetParam'):
    EE_OptimizationGetParam = _libs['edk.dll'].EE_OptimizationGetParam
    EE_OptimizationGetParam.argtypes = [OptimizationParamHandle]
    EE_OptimizationGetParam.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 985
if hasattr(_libs['edk.dll'], 'EE_OptimizationGetVitalAlgorithm'):
    EE_OptimizationGetVitalAlgorithm = _libs['edk.dll'].EE_OptimizationGetVitalAlgorithm
    EE_OptimizationGetVitalAlgorithm.argtypes = [OptimizationParamHandle, EE_EmotivSuite_t, POINTER(c_uint)]
    EE_OptimizationGetVitalAlgorithm.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 996
if hasattr(_libs['edk.dll'], 'EE_OptimizationSetVitalAlgorithm'):
    EE_OptimizationSetVitalAlgorithm = _libs['edk.dll'].EE_OptimizationSetVitalAlgorithm
    EE_OptimizationSetVitalAlgorithm.argtypes = [OptimizationParamHandle, EE_EmotivSuite_t, c_uint]
    EE_OptimizationSetVitalAlgorithm.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1006
if hasattr(_libs['edk.dll'], 'EE_ResetDetection'):
    EE_ResetDetection = _libs['edk.dll'].EE_ResetDetection
    EE_ResetDetection.argtypes = [c_uint, EE_EmotivSuite_t, c_uint]
    EE_ResetDetection.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1010
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'EE_GetSecurityCode'):
        continue
    EE_GetSecurityCode = _lib.EE_GetSecurityCode
    EE_GetSecurityCode.argtypes = []
    EE_GetSecurityCode.restype = c_double
    break

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1017
if hasattr(_libs['edk.dll'], 'EE_DataCreate'):
    EE_DataCreate = _libs['edk.dll'].EE_DataCreate
    EE_DataCreate.argtypes = []
    EE_DataCreate.restype = DataHandle

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1023
if hasattr(_libs['edk.dll'], 'EE_DataFree'):
    EE_DataFree = _libs['edk.dll'].EE_DataFree
    EE_DataFree.argtypes = [DataHandle]
    EE_DataFree.restype = None

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1032
if hasattr(_libs['edk.dll'], 'EE_DataUpdateHandle'):
    EE_DataUpdateHandle = _libs['edk.dll'].EE_DataUpdateHandle
    EE_DataUpdateHandle.argtypes = [c_uint, DataHandle]
    EE_DataUpdateHandle.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1043
if hasattr(_libs['edk.dll'], 'EE_DataGet'):
    EE_DataGet = _libs['edk.dll'].EE_DataGet
    EE_DataGet.argtypes = [DataHandle, EE_DataChannel_t, POINTER(c_double), c_uint]
    EE_DataGet.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1052
if hasattr(_libs['edk.dll'], 'EE_DataGetNumberOfSample'):
    EE_DataGetNumberOfSample = _libs['edk.dll'].EE_DataGetNumberOfSample
    EE_DataGetNumberOfSample.argtypes = [DataHandle, POINTER(c_uint)]
    EE_DataGetNumberOfSample.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1060
if hasattr(_libs['edk.dll'], 'EE_DataSetBufferSizeInSec'):
    EE_DataSetBufferSizeInSec = _libs['edk.dll'].EE_DataSetBufferSizeInSec
    EE_DataSetBufferSizeInSec.argtypes = [c_float]
    EE_DataSetBufferSizeInSec.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1068
if hasattr(_libs['edk.dll'], 'EE_DataGetBufferSizeInSec'):
    EE_DataGetBufferSizeInSec = _libs['edk.dll'].EE_DataGetBufferSizeInSec
    EE_DataGetBufferSizeInSec.argtypes = [POINTER(c_float)]
    EE_DataGetBufferSizeInSec.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1078
if hasattr(_libs['edk.dll'], 'EE_DataAcquisitionEnable'):
    EE_DataAcquisitionEnable = _libs['edk.dll'].EE_DataAcquisitionEnable
    EE_DataAcquisitionEnable.argtypes = [c_uint, c_bool]
    EE_DataAcquisitionEnable.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1087
if hasattr(_libs['edk.dll'], 'EE_DataAcquisitionIsEnabled'):
    EE_DataAcquisitionIsEnabled = _libs['edk.dll'].EE_DataAcquisitionIsEnabled
    EE_DataAcquisitionIsEnabled.argtypes = [c_uint, POINTER(c_bool)]
    EE_DataAcquisitionIsEnabled.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1096
if hasattr(_libs['edk.dll'], 'EE_DataSetSychronizationSignal'):
    EE_DataSetSychronizationSignal = _libs['edk.dll'].EE_DataSetSychronizationSignal
    EE_DataSetSychronizationSignal.argtypes = [c_uint, c_int]
    EE_DataSetSychronizationSignal.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1105
if hasattr(_libs['edk.dll'], 'EE_DataSetMarker'):
    EE_DataSetMarker = _libs['edk.dll'].EE_DataSetMarker
    EE_DataSetMarker.argtypes = [c_uint, c_int]
    EE_DataSetMarker.restype = c_int

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 1114
if hasattr(_libs['edk.dll'], 'EE_DataGetSamplingRate'):
    EE_DataGetSamplingRate = _libs['edk.dll'].EE_DataGetSamplingRate
    EE_DataGetSamplingRate.argtypes = [c_uint, POINTER(c_uint)]
    EE_DataGetSamplingRate.restype = c_int

__const = c_int # <command-line>: 5

# <command-line>: 8
try:
    CTYPESGEN = 1
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 11
try:
    EDK_OK = 0
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 13
try:
    EDK_UNKNOWN_ERROR = 1
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 15
try:
    EDK_INVALID_DEV_ID_ERROR = 2
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 17
try:
    EDK_INVALID_PROFILE_ARCHIVE = 257
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 19
try:
    EDK_NO_USER_FOR_BASEPROFILE = 258
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 22
try:
    EDK_CANNOT_ACQUIRE_DATA = 512
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 25
try:
    EDK_BUFFER_TOO_SMALL = 768
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 27
try:
    EDK_OUT_OF_RANGE = 769
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 29
try:
    EDK_INVALID_PARAMETER = 770
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 31
try:
    EDK_PARAMETER_LOCKED = 771
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 33
try:
    EDK_COG_INVALID_TRAINING_ACTION = 772
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 35
try:
    EDK_COG_INVALID_TRAINING_CONTROL = 773
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 37
try:
    EDK_COG_INVALID_ACTIVE_ACTION = 774
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 39
try:
    EDK_COG_EXCESS_MAX_ACTIONS = 775
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 41
try:
    EDK_EXP_NO_SIG_AVAILABLE = 776
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 43
try:
    EDK_FILESYSTEM_ERROR = 777
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 46
try:
    EDK_INVALID_USER_ID = 1024
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 49
try:
    EDK_EMOENGINE_UNINITIALIZED = 1280
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 51
try:
    EDK_EMOENGINE_DISCONNECTED = 1281
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 53
try:
    EDK_EMOENGINE_PROXY_ERROR = 1282
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 56
try:
    EDK_NO_EVENT = 1536
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 59
try:
    EDK_GYRO_NOT_CALIBRATED = 1792
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 62
try:
    EDK_OPTIMIZATION_IS_ON = 2048
except:
    pass

# C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\/edkErrorCode.h: 65
try:
    EDK_RESERVED1 = 2304
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

InputSensorDescriptor_struct = struct_InputSensorDescriptor_struct # C:\\Users\\eperfa\\Documents\\Synetiq\\emotiv_sdk\\edk.h: 104

# No inserted files

