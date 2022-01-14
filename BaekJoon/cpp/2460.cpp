// 2460.cpp
#include <iostream>

int cal_passenger_num(int cur, int out, int in);

int main()
{
    using std::cin;
    using std::cout;
    using std::endl;

    int curr_passenger = 0;
    int out, in;
    int temp = 0;

    for (int i = 0; i < 10; i++)
    {
        // cout << i+1 << "번역\n";
        cin >> out >> in;
        curr_passenger = cal_passenger_num(curr_passenger, out, in);
        if (curr_passenger > temp)
            temp = curr_passenger;
        // cout << "현재 승객 수: " << curr_passenger<< endl;
    }
    cout << temp << endl;
    return 0;
}

int cal_passenger_num(int cur, int out, int in)
{
    return cur - out + in;
}