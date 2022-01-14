// 2908.cpp
#include <iostream>
#include <string>

std::string reverse_num(std::string num);
void display_bigger_num(std::string x, std::string y);

int main()
{
    using std::cin;
    using std::cout;

    std::string x, y, result;
    std::string rev_x, rev_y;

    cin >> x >> y;

    rev_x = reverse_num(x);
    rev_y = reverse_num(y);

    display_bigger_num(rev_x, rev_y);

    return 0;
}

std::string reverse_num(std::string num)
{
    char temp;
    int i, j;

    for (j = 0, i = num.size() - 1; j < i; --i, ++j)
    {
        temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }
    return num;
}

void display_bigger_num(std::string x, std::string y)
{
    if (std::stoi(x) > std::stoi(y))
        std::cout << x << std::endl;
    else if (std::stoi(x) < std::stoi(y))
        std::cout << y << std::endl;
}