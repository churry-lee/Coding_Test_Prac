#include <iostream>
#include <vector>

struct MyStack {
    std::vector<int> arr;

    MyStack() = default;
    int top();
    void push(int data);
    int pop();
    [[nodiscard]] bool empty() const;
    [[nodiscard]] size_t size() const;
};

int MyStack::top() {
    if (arr.empty())
        return -1;
    return arr.back();
}

void MyStack::push(int data) {
    arr.push_back(data);
}

int MyStack::pop() {
    if (arr.empty())
        return -1;
    int last = arr.back();
    arr.pop_back();
    return last;
}

bool MyStack::empty() const {
    return arr.empty();
}

size_t MyStack::size() const {
    return arr.size();
}

int main() {
    int n;
    std::cin >> n;

    auto * stack = new MyStack();

    for (int iter = 0; iter < n; ++iter) {
        std::string status;
        int data;

        std::cin >> status;
        if (status == "top")
            std::cout << stack->top() << std::endl;
        else if (status == "push") {
            std::cin >> data;
            stack->push(data);
        }
        else if (status == "pop")
          std::cout << stack->pop() << std::endl;
        else if (status == "empty")
          std::cout << stack->empty() << std::endl;
        else if (status == "size")
          std::cout << stack->size() << std::endl;
    }

    return 0;
}
