#include <iostream>
#define N 10
using namespace std;
int a_copy[N];

void insertSort(int a[], int len) {
	for (int i = 1; i < len; i++) {
		int tmp = a[i];
		int j = i - 1;
		while (j >= 0 && tmp < a[j]) {
			a[j + 1] = a[j];
			j--;
		}
		a[j + 1] = tmp;
	}
}

void bubbleSort(int a[], int len) {
	for (int i = 0; i < len-1; i++) {
		for (int j = i + 1; j < len; j++) {
			if (a[i] > a[j]) {
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
}

void selectSort(int a[], int len) {
	for (int i = 0; i < len; i++) {
		int min = i;
		for (int j = i + 1; j < len; j++) {
			if (a[min] > a[j]) {
				min = j;
			}
		}
		swap(a[min], a[i]);
	}
}

void merge(int a[], int l, int mid, int r) {
	int i = l, j = mid + 1, now = l;
	for (int k = l; k <= r; k++) {
		a_copy[k] = a[k];
	}
	while (i <= mid && j <= r) {
		if (a_copy[j] < a_copy[i]) {
			a[now] = a_copy[j];
			j++;
		}
		else {
			a[now] = a_copy[i];
			i++;
		}
		now++;
	}
	if (i <= mid) {
		for (; i <= mid; i++) {
			a[now] = a_copy[i];
			now++;
		}
	}
	else if (j <= r) {
		for (; j <= r; j++) {
			a[now] = a_copy[j];
			now++;
		}
	}
}

void mergeSort(int a[], int l, int r) {
	if (l < r) {
		int mid = (l + r) / 2;
		mergeSort(a, l, mid);
		mergeSort(a, mid + 1, r);
		merge(a, l, mid, r);
	}
}

int quick_partition(int a[], int l, int r) {
	int temp = a[l];
	int key = a[l];
	while (l < r) {
		while (l < r && a[r] >= key)
			--r;
		a[l] = a[r];
		while (l < r && a[l] <= key)
			++l;
		a[r] = a[l];
	}
	a[l] = temp;
	return l;
}
void quickSort(int a[], int l, int r) {
	if (l < r) {
		int mid = quick_partition(a, l, r);
		quickSort(a, l, mid - 1);
		quickSort(a, mid + 1, r);
	}
}

void heapAdjust(int a[], int start, int end) {
	int c = start;
	int temp = a[c];
	int l = 2 * c + 1;
	for (; l <= end; c=l,l = 2 *l+1) {
		if (l < end && a[l] < a[l + 1])
			++l;
		if (temp >= a[l])
			break;
		a[c] = a[l];
		a[l] = temp;
	}
}

void heapSort(int a[],int len) {
	// 从(n/2-1) --> 0逐次遍历。遍历之后，得到的数组实际上是一个(最大)二叉堆。
	for (int i = len / 2 -1 ; i > 0; --i) {
		heapAdjust(a, i, len-1);
	}
	for (int i = len-1; i > 0; i--) {
		int temp = a[i];
		a[i] = a[0];
		a[0] = temp;
		//交换a[0],a[1],a[i]最大
		heapAdjust(a, 0, i - 1);
		//使得a[0...i - 1]仍然是一个最大堆。
	}
}

int main()
{
	int a[10] = { 10,9,4,6,5,3,8,6,2,1};
	insertSort(a, 10);
	for (int i = 0; i < 10; i++) {
		cout << a[i] <<" ";
	}
	cout << endl;
	int a1[10] = { 10,9,4,6,5,3,8,6,2,1 };
	bubbleSort(a1, 10);
	for (int i = 0; i < 10; i++) {
		cout << a1[i] << " ";
	}
	cout << endl;
	int a2[10] = { 10,9,4,6,5,3,8,6,2,1 };
	selectSort(a2, 10);
	for (int i = 0; i < 10; i++) {
		cout << a2[i] << " ";
	}
	cout << endl;
	int a3[10] = { 10,9,4,6,5,3,8,6,2,1 };
	mergeSort(a3, 0, 9);
	for (int i = 0; i < 10; i++) {
		cout << a3[i] << " ";
	}
	cout << endl;
	int a4[10] = { 10,9,4,6,5,3,8,6,2,1 };
	quickSort(a4, 0, 9);
	for (int i = 0; i < 10; i++) {
		cout << a4[i] << " ";
	}
	cout << endl;
	int a5[10] = { 10,9,4,6,5,3,8,6,2,1};
	heapSort(a5, 10);
	for (int i = 0; i < 10; i++) {
		cout << a5[i] << " ";
	}
	cout << endl;
}
