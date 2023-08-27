#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <utility>

using namespace std;

struct BankAccount {
	int balance;
	queue<int> q_reservation;
	
	BankAccount(int balance_);
	~BankAccount() = default;
	
	void deposit(int amount);
	void pay(int amount);
	void reservation(int amount);
	void process_reservations();
};

BankAccount::BankAccount(int balance_) : balance(balance_)
{}

void BankAccount::deposit(int amount) {
	balance += amount;
}

void BankAccount::pay(int amount) {
	if (balance >= amount)
		balance -= amount;
}

void BankAccount::process_reservations() {
	while (!q_reservation.empty()) {
		if(balance >= q_reservation.front()){
			balance -= q_reservation.front();
			q_reservation.pop();
		} else {
			break;
		}
	}
}

void BankAccount::reservation(int amount) {
	if (balance >= amount && q_reservation.empty())
		balance -= amount;
	else
		q_reservation.push(amount);
}

void parse_transaction(BankAccount& account, vector<pair<string, int>> transactions) {
	for (auto & transaction : transactions) {
		string operation = transaction.first;
		int amount = transaction.second;
		if (operation == "deposit")
			account.deposit(amount);
		else if (operation == "pay")
			account.pay(amount);
		else if (operation == "reservation")
			account.reservation(amount);
		account.process_reservations();
	}
	cout << account.balance << endl;
}

int main() {
	int N, M;
	cin >> N >> M;
	
	BankAccount account(N);
	
	vector<pair<string, int>> transactions;
	transactions.clear();
	
	for (int i = 0; i < M; ++i) {
		string operation;
		int amount;
		cin >> operation >> amount;
		transactions.emplace_back(operation, amount);
	}
	
	parse_transaction(account, transactions);
	
	return 0;
}
