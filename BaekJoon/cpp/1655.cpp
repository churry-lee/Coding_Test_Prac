/*
 * 최대 힙, 최소 힙, 우선 순위 큐
 * 중앙 값을 찾기 위한 최대 힙, 최소 힙 구성 조건
 * 1. 최대 힙의 크기는 최소 힙의 크기 보다 하나 더 크거나 같아야 한다.
 * 2. 최대 힙의 최대 원소는 최소 힙의 최소 원소 보다 작거나 같아야 한다.
 */
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
