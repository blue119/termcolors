# Foreground colors

tf = ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'white']
tfl = ['lblack', 'lred', 'lgreen', 'lyellow', 'lblue', 'lpink', 'lcyan', 'lwhite']
tb = ['blackb', 'redb', 'greenb', 'yellowb', 'blueb', 'pinkb', 'cyanb', 'whiteb']
total = tf + tfl + tb

cc = {
	'black':'30m', 	'red':'31m', 	'green':'32m', 	'yellow':'33m',
	'blue':'34m', 	'pink':'35m', 	'cyan':'36m', 	'white':'37m',

	'lblack':'1;30m', 'lred':'1;31m', 'lgreen':'1;32m', 'lyellow':'1;33m',
	'lblue':'1;34m', 'lpink':'1;35m', 'lcyan':'1;36m', 'lwhite':'1;37m',

	'blackb':'40m', 'redb':'41m', 'greenb':'42m', 'yellowb':'43m',
	'blueb':'44m', 'pinkb':'45m', 'cyanb':'46m', 'whiteb':'47m'
	}

code_temp = '''
def %(func)s(s):
	if s.endswith('\033[0m'): s = s[:-4]
	return '\033[%(cc)s' + s + '\033[0m'
'''
for i in total: exec code_temp % {'func': i, 'cc': cc.get(i)} in globals()
# for i in total: print code_temp % {'func': i, 'cc': cc.get(i)}

