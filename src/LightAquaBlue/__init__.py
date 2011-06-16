import objc as _objc
import sys, os
from os import path

LIBRARY=path.join("Library", "Frameworks", "LightAquaBlue.framework")
PREFIX="/"
if hasattr(sys, 'real_prefix'):
	print "Running in virtualenv"
	prefix=path.dirname(path.dirname(sys.prefix))
	print "Checking if LightAquaBlue is in %s" % PREFIX
	library = "Library/Python/LightAquaBlue.framework"
	if path.isdir(path.join(prefix, library)):
		print "Found!"
		PREFIX=prefix
		LIBRARY=library
	else:
		print "Not Found!"
		PREFIX="/"

__bundle__ = _objc.initFrameworkWrapper("LightAquaBlue",
    frameworkIdentifier="com.blammit.LightAquaBlue",
    frameworkPath=_objc.pathForFramework(path.join(PREFIX, LIBRARY)),
    globals=globals())
