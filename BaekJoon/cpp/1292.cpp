// 1292.cpp
#include <iostream>

void make_sequence(int * arr);
int calculate_result(int, int, int * arr);
const int ArSize = 1000;

int main()
{
    using namespace std;

    int A, B;
    cin >> A >> B;

    int arr[ArSize];

    make_sequence(arr);
    // std::cout << "배열 출력" << std::endl;
    // for (int i = 0; i < ArSize; i++)
    // {
    //     std::cout << i << ": " << arr[i] << std::endl;
    // }
    int answer = calculate_result(A, B, arr);
    std::cout << answer << std::endl; 

    return 0;
}

void make_sequence(int * arr)
{
    int count = 1;
    int index = 0;

    while ( index < 1000 )
    {
        for (int i = 0; i < count; i++)
        {
            arr[index] = count;
            index++;
            if (index > 999)
                break;
            std::cout << index << std::endl;
        }
        count++;
    }
}

int calculate_result(int A, int B, int * arr)
{
    int answer = 0;

    for (int i = A - 1; i < B; i++)
    {
        answer = answer + arr[i];
    }

    return answer;
}