#include <iostream>
#define MAX 10

using namespace std;

class stack {
	private: 
		int data[MAX];
		int top;
	public:
		void initStack();
		bool stackFull();
		bool stackEmpty();
		void push(int x);
		int pop();
		void traverse();
		int stackTop();
};

void stack::initStack() {
	top = 0;
}

bool stack::stackFull() {
	if (top == 11)
		return true;
	return false;
}
bool stack::stackEmpty() {
	if (top == 0)
		return true;
	return false;
}
void stack::push(int x) {
	if (stackFull())
		cout << "栈满了" << endl;
	else {
		data[top] = x;
		top++;
	}
}
int stack::pop() {
	if (stackEmpty())
		cout << "栈为空" << endl;
	else {
		int elem = data[top-1];
		top--;
		return elem;
	}
}
void stack::traverse() {
	for (int i = 0; i < top; i++) {
		cout << data[i] << " ";
	}
}
int stack::stackTop() {
	return data[top-1];
}
int main()
{
	stack stack1 = stack();
	stack1.initStack();
	if (stack1.stackEmpty()) cout << "栈为空" << endl;
	stack1.push(2);
	stack1.push(3);
	stack1.push(4);
	cout<<stack1.stackTop();
	cout << "\n";
	stack1.traverse();
	cout << "\n";
	cout<<stack1.pop();
}
