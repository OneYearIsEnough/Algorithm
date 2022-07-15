[TOC]

# 快速排序

## [快速排序](https://www.acwing.com/problem/content/787/)

给定你一个长度为 n 的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

- 输入格式

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在 1∼10e9 范围内），表示整个数列。

- 输出格式

输出共一行，包含 n 个整数，表示排好序的数列。

- 数据范围

1≤n≤100000

- 输入样例：

```
5
3 1 2 4 5
```

- 输出样例：

```
1 2 3 4 5
```

==代码==

经典三路快排，不会可以原地去世了。

```c++
#include <iostream>
#include <ctime>
using namespace std;

const int N = 100010;
int nums[N];
int n;

void quickSort(int nums[], int l, int r) {
    if (l >= r) return;
    
    int rnd_idx = rand() % (r - l + 1) + l;
    swap(nums[l], nums[rnd_idx]);
    int e = nums[l];
    int lt = l, gt = r + 1;
    int i = l + 1;
    while (i < gt) {
        if (nums[i] < e) swap(nums[++lt], nums[i++]);
        else if (e < nums[i]) swap(nums[i], nums[--gt]);
        else ++i;
    }
    swap(nums[l], nums[lt]);
    quickSort(nums, l, lt - 1);
    quickSort(nums, gt, r);
}

int main() {
    srand(time(nullptr));
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> nums[i];
    
    quickSort(nums, 0, n - 1);

    for (int i = 0; i < n; ++i) cout << nums[i] << " ";
    return 0;
    
}
```

## [第k个数](https://www.acwing.com/problem/content/788/)

给定一个长度为 n 的整数数列，以及一个整数 k，请用快速选择算法求出数列从小到大排序后的第 k 个数。

- 输入格式

第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在 1∼109 范围内），表示整数数列。

- 输出格式

输出一个整数，表示数列的第 k 小数。

- 数据范围

1≤n≤100000,
1≤k≤n

- 输入样例：

```
5 3
2 4 1 5 3
```

- 输出样例：

```
3
```

==代码==

单路快排应用，算法名字叫快速选择

```c++
#include <iostream>
#include <ctime>
using namespace std;

const int N = 100010;
int nums[N];
int n, k;

int findKSmallest(int nums[], int l, int r) {
    if (l == r) return nums[l];  // 如果数据一定有效，是进不来这个条件的
    int rnd_idx = rand() % (r - l + 1) + l;
    swap(nums[l], nums[rnd_idx]);
    int e = nums[l];
    int lt = l;
    
    for (int i = l + 1; i <= r; ++i)
        if (nums[i] < e) swap(nums[++lt], nums[i]);
    swap(nums[l], nums[lt]);
    if (lt == k - 1) return nums[lt];
    else if (lt < k - 1) return findKSmallest(nums, lt + 1, r);
    return findKSmallest(nums, l, lt - 1);
}

int main() {
    srand(time(nullptr));
    cin >> n >> k;
    for (int i = 0; i < n; ++i) cin>> nums[i];
    
    cout << findKSmallest(nums, 0, n - 1) << endl;
    return 0;
}
```



# 归并排序

## [归并排序](https://www.acwing.com/problem/content/789/)

给定你一个长度为 n 的整数数列。

请你使用归并排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

- 输入格式

输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在 1∼109 范围内），表示整个数列。

- 输出格式

输出共一行，包含 n 个整数，表示排好序的数列。

- 数据范围

1≤n≤100000

- 输入样例：

```
5
3 1 2 4 5
```

- 输出样例：

```
1 2 3 4 5
```

==代码==

不会的同学可以选择原地去世

```c++
#include <iostream>
using namespace std;

const int N = 100010;
int nums[N], aux[N];
int n;

void merge(int nums[], int l, int m, int r) {
    for (int i = l; i <= r; ++i) aux[i] = nums[i];
    int i = l, j = m + 1;
    for (int k = l; k <= r; ++k) {
        if (i > m) nums[k] = aux[j++];
        else if (j > r) nums[k] = aux[i++];
        else if (aux[i] <= aux[j]) nums[k] = aux[i++];
        else nums[k] = aux[j++];
    }
}

void mergeSort(int nums[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(nums, l, m);
    mergeSort(nums, m + 1, r);
    merge(nums, l, m, r);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> nums[i];
    
    mergeSort(nums, 0, n - 1);
    
    for (int i = 0; i < n; ++i) cout << nums[i] << " ";
    cout << endl;
    return 0;
}
```

## [逆序对的数量](https://www.acwing.com/problem/content/790/)

给定一个长度为 n 的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i<j 且 a[i]>a[j]，则其为一个逆序对；否则不是。

- 输入格式

第一行包含整数 n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

- 输出格式

输出一个整数，表示逆序对的个数。

- 数据范围

1≤n≤100000，
数列中的元素的取值范围 [1,10e9]

- 输入样例：

```
6
2 3 4 5 6 1
```

- 输出样例：

```
5
```

==代码==

归并排序的应用，即当前状态下左侧数比右侧数大，那么他们是一个逆序对，而此时左侧数右边的所有数（不超过左侧数组）都可以和打钱右边的数成为一个逆序对（建立在归并排序在归并的过程中保证了子数组有序的特性），此时就减小了时间复杂度。

```C++
#include <iostream>
using namespace std;

const int N = 100010;
int nums[N], aux[N];
int n;
long long ret;  // 注意爆int

void merge(int nums[], int l, int m, int r) {
    for (int i = l; i <= r; ++i) aux[i] = nums[i];
    int i = l, j = m + 1;
    for (int k = l; k <= r; ++k) {
        if (i > m) nums[k] = aux[j++];
        else if (j > r) nums[k] = aux[i++];  // 不用维护ret，因为前面的操作已经把这些逆序对算过了，不用重复计算了
        else if (aux[i] <= aux[j]) nums[k] = aux[i++];
        else {
            ret += m - i + 1;
            nums[k] = aux[j++];
        }
    }
}

void mergeSort(int nums[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(nums, l, m);
    mergeSort(nums, m + 1, r);
    merge(nums, l, m, r);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> nums[i];
    
    mergeSort(nums, 0, n - 1);
    cout << ret << endl;
    return 0;
}
```

