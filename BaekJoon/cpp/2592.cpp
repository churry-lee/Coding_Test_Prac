// 2592.cpp
#include <iostream>
#include <map>

int calculate_average(int * num_arr);
int find_mode(int * num_arr);

const int ArSize = 10;

int main()
{
    using std::cin;
    using std::cout;
    using std::endl;

    int num_arr[ArSize];
    for (int i = 0; i < ArSize; i++)
    {
        cin >> num_arr[i];
    }

    int avg = calculate_average(num_arr);
    // cout << "평균값: " << avg << endl;
    int mode = find_mode(num_arr);
    // cout << "최빈값: " << mode << endl;
    cout << avg << endl;
    cout << mode << endl;

    return 0;
}

int calculate_average(int * num_arr)
{
    int sum = 0;

    for (int i = 0; i < ArSize; i++)
        sum += num_arr[i];

    return sum / ArSize;
}

int find_mode(int * num_arr)
{
    std::map<int, int> modeMap;
    std::map<int, int>::iterator iter;

    for (int i = 0; i < ArSize; i++)
    {
        if (modeMap.find(num_arr[i]) != modeMap.end())
        {
            modeMap[num_arr[i]] += 1;
        }
        else {
            modeMap[num_arr[i]] = 1;
        }
    
        // std::cout << "key: " << num_arr[i] << ", "
        //           << "value: " << modeMap[num_arr[i]] << std::endl;
    }

    iter = modeMap.begin();
    int mode_key = iter->first;
    int mode_val = iter->second;

    // std::cout << "초기 mode key: " << iter->first << ", "
    //           << "초기 mode value: " << iter->second << std::endl;

    while (iter != modeMap.end()) 
    {
        // std::cout << "[" << iter->first << ", "
        //             << iter->second << "]\n";

        if (mode_val < iter->second) {
            mode_key = iter->first;
            mode_val = iter->second;
        }

        // std::cout << "mode key: " << mode_key << ", "
        //           << "mode val: " << mode_val << std::endl;

        ++iter;
    }

    return mode_key;
}