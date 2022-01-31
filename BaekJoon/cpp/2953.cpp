// 2953.cpp
#include <iostream>

int main()
{
    using namespace std;

    const int ArSize = 4;
    int score[ArSize] = {};
    const int number_of_people = 5;  // 참가자수, 5명으로 고정
    int num = 0;
    int total = 0;

    for (int i = 0; i < number_of_people; i++)
    {
        int temp = 0;
        cin >> score[0] >> score[1] >> score[2] >> score[3];
        for (int j = 0; j < ArSize; j++)
            temp += score[j];

        if (temp > total)
        {
            num = i + 1;
            total = temp;
        }
    }
    std::cout << num << " " << total << std::endl;

    return 0;
}