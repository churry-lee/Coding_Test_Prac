// 2577.cpp
#include <iostream>

int multiply_input_nums(int A, int B, int C);
void counting_elements(int num);
void display_result(int * result);

int main()
{
    using std::cin;
    using std::cout;
    using std::endl;

    int A, B, C;

    int answer = multiply_input_nums(A, B, C);
    counting_elements(answer);

    return 0;
}

int multiply_input_nums(int A, int B, int C)
{
    using std::cin;

    cin >> A >> B >> C;

    return A * B * C;
}

void counting_elements(int num)
{
    int result[10] = {};

    while ( num / 10 != 0)
    {
        int temp = num % 10;
        num = num / 10;
        // std::cout << temp << ", " << num << std::endl;

        result[temp] += 1;
    }

    result[num] += 1;

    display_result(result);
}

void display_result(int * result)
{
    for (int i = 0; i < 10; i++)
        {
            std::cout << result[i] << std::endl;
        }
}
