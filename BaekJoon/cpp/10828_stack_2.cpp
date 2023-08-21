#include <iostream>

//const int maxSize = 10000;

struct MyStack {
    int maxSize;
    int top;
    int* stackArr;

    explicit MyStack(int size) : maxSize(size), top(-1), stackArr(new int[size]) {}

    void push(int data);
    int pop();
    [[nodiscard]] int getTop() const;
    [[nodiscard]] bool isEmpty() const;
    [[nodiscard]] int size() const;
};

void MyStack::push(int data) {
    if (top >= (maxSize - 1)) {
        std::cout << "Stack overflow. Can't push!" << std::endl;
        return;
    }
    stackArr[++top] = data;
}

int MyStack::pop() {
    if (top < 0) {
//        std::cout << "Stack underflow. Can't pop!" << std::endl;
        return -1;
    }
    int pop_data = stackArr[top];
    --top;
    return pop_data;
}

int MyStack::getTop() const {
    if (top < 0) {
//        std::cout << "Stack is empty!" << std::endl;
        return -1;
    }
    return stackArr[top];
}

bool MyStack::isEmpty() const {
    return (top < 0);
}

int MyStack::size() const {
    return (top + 1);
}

int main() {
    int n;
    std::cin >> n;

    auto * stack = new MyStack(n);

    for (int iter = 0; iter < n; ++iter) {
        std::string status;
        int data;

        std::cin >> status;
        if (status == "top")
            std::cout << stack->getTop() << std::endl;
        else if (status == "push") {
            std::cin >> data;
            stack->push(data);
        }
        else if (status == "pop")
            std::cout << stack->pop() << std::endl;
        else if (status == "empty")
            std::cout << stack->isEmpty() << std::endl;
        else if (status == "size")
            std::cout << stack->size() << std::endl;
    }

    return 0;
}
