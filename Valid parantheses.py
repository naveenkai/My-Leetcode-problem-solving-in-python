class Solution(object):
    def isValid(self, s):
        	l = list()
		d = {'(':')', '[':']', '{':'}'}

		for i in s:
			if i in d.keys():
				l.append(i)
			else:
				if len(l) != 0 and d[l[-1]] == i:
					l.pop()
				else:
					return False

		if len(l) == 0:
			return True
       
