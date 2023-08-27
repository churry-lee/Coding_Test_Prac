import sys
input_ = sys.stdin.readline


mirror_char = {
	'b': 'd',
	'd': 'b',
	'i': 'i',
	'l': 'l',
	'm': 'm',
	'n': 'n',
	'o': 'o',
	'p': 'q',
	'q': 'p',
	's': 'z',
	'z': 's',
	'u': 'u',
	'v': 'v',
	'w': 'w',
	'x': 'x'
}


def is_mirror(s):
	if (s[0] not in mirror_char) or (mirror_char[s[0]] != s[-1]):
		return "Normal"
	
	m = ''
	for c in s:
		if c in mirror_char:
			c = mirror_char[c]
			
		m = c + m
		
	# print(f"s: {s}")
	# print(f"m: {m}")
	
	if s == m:
		return "Mirror"
	else:
		return "Normal"


if __name__ == '__main__':
	N = int(input_().strip())
	
	for _ in range(N):
		print(is_mirror(input_().strip()))
