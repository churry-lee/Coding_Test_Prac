#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	priority_queue<int, vector<int>, less<>> maxHeap;
	priority_queue<int, vector<int>, greater<>> minHeap;
	
	int N, num;
	cin >> N;
	
	for (int iter = 0; iter < N; ++iter) {
		cin >> num;
		
		if (maxHeap.size() == minHeap.size())
			maxHeap.push(num);
		else
			minHeap.push(num);
		
		if (!maxHeap.empty() && !minHeap.empty() && maxHeap.top() > minHeap.top()) {
			int maxTop = maxHeap.top(), minTop = minHeap.top();
			maxHeap.pop(); minHeap.pop();
			maxHeap.push(minTop); minHeap.push(maxTop);
		}
		printf("%d\n", maxHeap.top());
	}
	
	return 0;
}
