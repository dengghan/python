def d2(arg1, arg2):
	def _d2(func):
		@functools.wraps(func)
		def __d2(arg3, arg4):
			print("before test", arg1, arg2)
			return func(arg3, arg4)
		return __d2
	return _d2

@d2('c', 'd')
def test(arg1,arg2):
	print('test', arg1, arg2)

print(test.__name__)