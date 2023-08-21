#include <iostream>
#include <vector>

template<class T> void chmax(T& a, T b) {
    if (a < b)
        a = b;
}

int main() {
    int N, K;
    std::cin >> N >> K;

    std::vector<int> W(N), V(N);
    for (int iter = 0; iter < N; ++iter) {
        std::cin >> W[iter] >> V[iter];
    }

    std::vector<std::vector<int>> dp(N + 1, std::vector<int>(K + 1, 0));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j <= K; ++j) {
            if (j - W[i] >= 0)
                chmax(dp[i + 1][j], dp[i][j - W[i]] + V[i]);

            chmax(dp[i + 1][j], dp[i][j]);
        }
    }

    std::cout << dp[N][K] << std::endl;

    return 0;
}
