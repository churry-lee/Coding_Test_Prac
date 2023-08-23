def cal_martian_math(formulas):
	results = []
	for formula in formulas:
		result = formula[0]
		for op in formula[1:]:
			if op == '@':
				result *= 3
			elif op == '%':
				result += 5
			elif op == '#':
				result -= 7
		results.append(result)
	return results


T = int(input())

formulas = []
for _ in range(T):
	formula = input().split()
	formula[0] = float(formula[0])
	formulas.append(formula)

results = cal_martian_math(formulas)

for result in results:
	print(f"{result:.2f}")
