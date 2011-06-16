import objc as _objc
import sys, os
from os import path

LIBRARY=path.join("Library", "Frameworks", "LightAquaBlue.framework")
PREFIX="/"
if hasattr(sys, 'real_prefix'):
	print "Running in virtualenv"
	prefix=path.dirname(path.dirname(sys.prefix))
	target = path.join(prefix, LIBRARY)
	print "Checking if LightAquaBlue is in %s" % target
	if path.isdir(target):
		print "Found!"
		PREFIX=prefix
	else:
		print "Not Found!"

__bundle__ = _objc.initFrameworkWrapper("LightAquaBlue",
    frameworkIdentifier=None,
    frameworkPath=_objc.pathForFramework(path.join(PREFIX, LIBRARY)),
    globals=globals())
