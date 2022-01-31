// 2711.cpp
#include <iostream>

void result(int, char *);

const int ArSize = 80;
int main()
{
    using namespace std;
    int number_of_testcase;   // 테스트 케이스의 개수
    int wrong_index;          // 단어에서 틀린 위치
    char word[ArSize];        // 입력된 단어

    cin >> number_of_testcase;

    for (int i = 0; i < number_of_testcase; i++)
    {
        cin >> wrong_index >> word;
        result(wrong_index, word);
    }
    return 0;
}

void result(int wrong_index, char * word)
{
    int count = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        if (count != wrong_index - 1)
            std::cout << word[i];
        count++;
    }
    std::cout << std::endl;
}