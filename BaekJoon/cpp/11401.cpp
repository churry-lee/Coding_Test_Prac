#include <cstdio>
typedef long long ll;
const int MAX = 4000000;
const int MOD = 1000000007;
ll fac[MAX + 1], finv[MAX + 1], inv[MAX + 1];

// power 함수 구현 a^b를 계산하는 함수
ll power(ll a, ll b) {
	ll res = 1;
	while (b > 0) {
		if (b % 2) {
			res *= a;
			res %= MOD;
		}
		a *= a;
		a %= MOD;
		b /= 2;
	}
	return res;
}

// 합동식을 만족하는 팩토리얼 계산
void combinit() {
	fac[0] = fac[1] = 1;
	finv[0] = finv[1] = 1;
	inv[1] = 1;
	for (int i = 2; i <= MAX; i++) {
		fac[i] = fac[i - 1] * i % MOD;
		inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
		finv[i] = finv[i - 1] * inv[i] % MOD;
	}
}

ll comb(int n, int k) {
	if (n < k) return 0;
	if (n < 0 || k < 0) return 0;
	return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

int main() {
	combinit();
	int n, k;
	scanf("%d %d", &n, &k);
	printf("%lld\n", comb(n, k));
	return 0;
}
