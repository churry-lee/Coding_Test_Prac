#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int solution(vector<int> array)
{
	map<int, int> myMap;

	for (auto & num : array)
		if (!myMap.count(num))
			myMap.insert(make_pair(num, 1));
		else
			myMap[num] += 1;
	int max_value = 0;
	for(auto iter = myMap.begin(); iter != myMap.end(); iter++)
	{
		cout << iter->first << " : " << iter->second << endl;
		if (iter->second >= max_value)
			max_value = iter->second;
	}
	cout << "max value = " << max_value << endl;

	vector<int> answer;
	for(auto iter = myMap.begin(); iter != myMap.end(); iter++)
		if (iter->second == max_value)
			answer.push_back(iter->first);

	if (answer.size() >= 2)
		return -1;
	else
		return answer[0];
}

int main()
{
	vector<int> array{1, 2, 3, 3, 3, 4};
	cout << solution(array) << endl;

	return 0;
}
