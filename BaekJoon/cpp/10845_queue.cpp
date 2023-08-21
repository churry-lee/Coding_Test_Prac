#include <iostream>
#include <vector>

struct MyQueue {
    std::vector<int> arr;

    MyQueue() = default;
    void push(int data);
    int pop();
    [[nodiscard]] size_t size() const;
    [[nodiscard]] bool empty() const;
    int front();
    int back();
};

void MyQueue::push(int data) {
    arr.push_back(data);
}

int MyQueue::pop() {
    if (arr.empty())
        return -1;
    int first = arr.front();
    arr.erase(arr.begin());
    return first;
}

size_t MyQueue::size() const {
    return arr.size();
}

bool MyQueue::empty() const {
    return arr.empty();
}

int MyQueue::front() {
    if (arr.empty())
        return -1;
    return arr.front();
}

int MyQueue::back() {
    if (arr.empty())
        return -1;
    return arr.back();
}

int main() {
    int n;
    std::cin >> n;

    auto * pMyQueue = new MyQueue();

    for (int iter = 0; iter < n; ++iter) {
        std::string status;
        int data;

        std::cin >> status;
        if (status == "push") {
            std::cin >> data;
            pMyQueue->push(data);
        }
        else if (status == "pop")
            std::cout << pMyQueue->pop() << std::endl;
        else if (status == "size")
            std::cout << pMyQueue->size() << std::endl;
        else if (status == "empty")
            std::cout << pMyQueue->empty() << std::endl;
        else if (status == "front")
            std::cout << pMyQueue->front() << std::endl;
        else if (status == "back")
            std::cout << pMyQueue->back() << std::endl;
    }

    return 0;
}
