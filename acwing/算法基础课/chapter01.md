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

# 二分

## [数的范围](https://www.acwing.com/problem/content/791/)

给定一个按照升序排列的长度为 n 的整数数组，以及 q 个查询。

对于每个查询，返回一个元素 k 的起始位置和终止位置（位置从 0 开始计数）。

如果数组中不存在该元素，则返回 `-1`。

- 输入格式

第一行包含整数 n 和 q，表示数组长度和询问个数。

第二行包含 n 个整数（均在 1∼10000 范围内），表示完整数组。

接下来 q 行，每行包含一个整数 k，表示一个询问元素。

- 输出格式

共 q 行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回 `-1`。

- 数据范围

1≤n≤100000
1≤q≤10000
1≤k≤10000

- 输入样例：

```
6 3
1 2 2 3 3 4
3
4
5
```

- 输出样例：

```
3 4
5 5
-1 -1
```

==代码==

二分查找模板还是不太熟练呀，写了挺长时间。。

```c++
# define PII pair<int, int>

#include <iostream>
#include <utility>
using namespace std;

const int N = 100010;
int nums[N];
int n, q;

PII find(int nums[], int _l, int _r, int num) {
    // 找左边界
    int l = _l, r = _r;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (nums[m] < num) l = m + 1;
        else r = m;
    }
    // 无效
    if (nums[l] != num) return {-1, -1};
    int l_res = l;
    // 找右边界
    l = _l, r = _r;
    while (l < r) {
        int m = l + (r - l + 1) / 2;
        if (num < nums[m]) r = m - 1;
        else l = m;
    }
    return {l_res, l};
}

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; ++i) cin >> nums[i];
    for (int i = 0; i < q; ++i) {
        int num;
        cin >> num;
        PII res = find(nums, 0, n - 1, num);
        cout << res.first << " " << res.second << endl;
    }
    return 0;
}
```

## [数的三次方根✅](https://www.acwing.com/problem/content/792/)

给定一个浮点数 n，求它的三次方根。

- 输入格式

共一行，包含一个浮点数 n。

- 输出格式

共一行，包含一个浮点数，表示问题的解。

注意，结果保留 6 位小数。

- 数据范围

−10000≤n≤10000

- 输入样例：

```
1000.00
```

- 输出样例：

```
10.000000
```

==代码==

```c++
#include <iostream>
using namespace std;

double n;

int main() {
    cin >> n;
    double l = -10000, r = 10000;
    while (r - l >= 10e-8) {  // 注意精度是放在while循环条件里的，并且要/100保证精度稳妥
        double m = (r + l) / 2;
        if (m * m * m <= n) l = m;
        else r = m;
    }
    printf("%lf", l);
    return 0;
}
```

# 高精度

## [高精度加法](https://www.acwing.com/problem/content/793/)

给定两个正整数（不含前导 0），计算它们的和。

- 输入格式

共两行，每行包含一个整数。

- 输出格式

共一行，包含所求的和。

- 数据范围

1≤整数长度≤100000

- 输入样例：

```
12
23
```

- 输出样例：

```
35
```

==代码==

```c++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string a, b;

string add(const string& a, const string& b) {
    string res;
    int i = a.size() - 1, j = b.size() - 1, c = 0;
    while (i >= 0 || j >= 0 || c > 0) {
        if (i >= 0) c += a[i--] - '0';
        if (j >= 0) c += b[j--] - '0';
        res += c % 10 + '0';
        c /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    cin >> a >> b;
    
    cout << add(a, b) << endl;
    return 0;
}
```

## [高精度减法](https://www.acwing.com/problem/content/794/)

给定两个正整数（不含前导 0），计算它们的差，计算结果可能为负数。

- 输入格式

共两行，每行包含一个整数。

- 输出格式

共一行，包含所求的差。

- 数据范围

1≤整数长度≤10e5

- 输入样例：

```
32
11
```

- 输出样例：

```
21
```

==代码==

```c++
#include <iostream>
#include <string>
#include <algorithm>
#include "math.h"
using namespace std;

string s1, s2;

bool cmp(const string& s1, const string& s2) {
    // 保证s1>=s2，着重理解里面的逻辑，而不是s1>s2，要不然下面'-'的逻辑就给错了
    int n1 = s1.size(), n2 = s2.size();
    if (n1 != n2) return n1 > n2;
    for (int i = 0; i < n1; ++i)
        if (s1[i] != s2[i]) return s1[i] > s2[i];
    return true;
}

string sub(const string& s1, const string& s2) {
    string res;
    int n1 = s1.size(), n2 = s2.size();
    int i = n1 - 1, j = n2 - 1, c = 0;
    while (i >= 0) {
        c = s1[i--] - '0' - c;
        if (j >= 0) c -= s2[j--] - '0';  // s2有可能已经遍历完了
        res += (c + 10) % 10 + '0';  // c为负数，那么+10取模为当前位的结果，如果为正，则是本身，因此(c+10)%10可以同时conver两种情况
        c = c < 0 ? 1 : 0;
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    cin >> s1 >> s2;
    if (!cmp(s1, s2)) {
        cout << "-" + sub(s2, s1) << endl;
    }
    else cout << sub(s1, s2) << endl;
    return 0;
}
```

## [高精度乘法](https://www.acwing.com/problem/content/795/)

给定两个非负整数（不含前导 0） A 和 B，请你计算 A×B 的值。

- 输入格式

共两行，第一行包含整数 A，第二行包含整数 B。

- 输出格式

共一行，包含 A×B 的值。

- 数据范围

1≤A的长度≤100000,
0≤B≤10000

- 输入样例：

```
2
3
```

- 输出样例：

```
6
```

==代码==

```c++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string a;
int b;

string mul(const string& a, int b) {
    string res;
    int n = a.size();
    int i = n - 1, c = 0;
    while (i >= 0 || c != 0) {
        if (i >= 0) c = (a[i--] - '0') * b + c;
        res += c % 10 + '0';
        c = c / 10;
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    cin >> a >> b;
    cout << mul(a, b) << endl;
    return 0;
}
```

## [高精度除法✅](https://www.acwing.com/problem/content/796/)

给定两个非负整数（不含前导 0） A，B，请你计算 A/B 的商和余数。

- 输入格式

共两行，第一行包含整数 A，第二行包含整数 B。

- 输出格式

共两行，第一行输出所求的商，第二行输出所求余数。

- 数据范围

1≤A的长度≤100000,
1≤B≤10000,
B 一定不为 0

- 输入样例：

```
7
2
```

- 输出样例：

```
3
1
```

==代码==

```c++
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string a;
int b;

string div(const string& a, int b, int& r) {
    // 除法是从最高位开始的
    string res;
    int n = a.size();
    for (int i = 0; i < n; ++i) {
        r = r * 10 + a[i] - '0';
        res += (r / b) + '0';
        r = r % b;
    }
    // 去除前导0
    reverse(res.begin(), res.end());
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
} 

int main() {
    cin >> a >> b;
    int r = 0;  // 余数
    string res = div(a, b, r);
    cout << res << endl << r << endl;
    return 0;
}
```



# 前缀和差分

## [前缀和](https://www.acwing.com/problem/content/797/)

输入一个长度为 n 的整数序列。

接下来再输入 m 个询问，每个询问输入一对 l,r。

对于每个询问，输出原序列中从第 l 个数到第 r 个数的和。

- 输入格式

第一行包含两个整数 n 和 m。

第二行包含 n 个整数，表示整数数列。

接下来 m 行，每行包含两个整数 l 和 r，表示一个询问的区间范围。

- 输出格式

共 m 行，每行输出一个询问的结果。

- 数据范围

1≤l≤r≤n,
1≤n,m≤100000,
−1000≤数列中元素的值≤1000

- 输入样例：

```
5 3
2 1 3 6 4
1 2
1 3
2 4
```

- 输出样例：

```
3
6
10
```

==代码==

```c++
// 前缀和的基本应用

#include <iostream>
using namespace std;

const int N = 100010;
int nums[N], pre_sum[N];
int n, m;

int query(int l, int r) {
    // 左闭右闭
    return pre_sum[r] - pre_sum[l - 1];
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) cin >> nums[i];
    for (int i = 1; i <= n; ++i) pre_sum[i] = pre_sum[i - 1] + nums[i];
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        cout << query(l, r) << endl;
    }
    return 0;
}
```

## [子矩阵的和](https://www.acwing.com/problem/content/798/)

输入一个 n 行 m 列的整数矩阵，再输入 q 个询问，每个询问包含四个整数 x1,y1,x2,y2，表示一个子矩阵的左上角坐标和右下角坐标。

对于每个询问输出子矩阵中所有数的和。

- 输入格式

第一行包含三个整数 n，m，q。

接下来 n 行，每行包含 m 个整数，表示整数矩阵。

接下来 q 行，每行包含四个整数 x1,y1,x2,y2，表示一组询问。

- 输出格式

共 q 行，每行输出一个询问的结果。

- 数据范围

1≤n,m≤1000,
1≤q≤200000,
1≤x1≤x2≤n,
1≤y1≤y2≤m,
−1000≤矩阵内元素的值≤1000

- 输入样例：

```
3 4 3
1 7 2 4
3 6 2 8
2 1 2 3
1 1 2 2
2 1 3 4
1 3 3 4
```

- 输出样例：

```
17
27
21
```

==代码==

```c++
// 2d前缀和的简单应用

#include <iostream>
using namespace std;

const int N = 1010;
int nums[N][N], pre_sum[N][N];
int n, m, q;

int query(int x1, int y1, int x2, int y2) {
    return pre_sum[x2][y2] - pre_sum[x1 - 1][y2] - pre_sum[x2][y1 - 1] + pre_sum[x1 - 1][y1 - 1];
}

int main() {
    cin >> n >> m >> q;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            cin >> nums[i][j];
    // 维护前缀和数组
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + nums[i][j];
    // 查询
    for (int i = 0; i < q; ++i) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << query(x1, y1, x2, y2) << endl;
    }
    return 0;
}
```

## [差分](https://www.acwing.com/problem/content/799/)

输入一个长度为 n 的整数序列。

接下来输入 m 个操作，每个操作包含三个整数 l,r,c，表示将序列中 [l,r] 之间的每个数加上 c。

请你输出进行完所有操作后的序列。

- 输入格式

第一行包含两个整数 n 和 m。

第二行包含 n 个整数，表示整数序列。

接下来 m 行，每行包含三个整数 l，r，c，表示一个操作。

- 输出格式

共一行，包含 n 个整数，表示最终序列。

- 数据范围

1≤n,m≤100000,
1≤l≤r≤n,
−1000≤c≤1000,
−1000≤整数序列中元素的值≤1000

- 输入样例：

```
6 3
1 2 2 1 2 1
1 3 1
3 5 1
1 6 1
```

- 输出样例：

```
3 4 5 3 4 2
```

==代码==

```c++
#include <iostream>
using namespace std;

const int N = 100010;
int nums[N], diff[N];
int n, m;

void op(int l, int r, int c) {
    diff[l] += c;
    diff[r + 1] -= c;
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) cin >> nums[i];
    for (int i = 1; i <= n; ++i) op(i, i, nums[i]);  // 用op来维护差分数组
    for (int i = 0; i < m; ++i) {
        int l, r, c;
        cin >> l >> r >> c;
        op(l, r, c);
    }
    // 查分数组前缀和为原数组
    for (int i = 1; i <= n; ++i) {
        diff[i] += diff[i - 1];
        cout << diff[i] << " ";
    }
    cout << endl;
    return 0;
}
```

## [差分矩阵](https://www.acwing.com/problem/content/800/)

输入一个 n 行 m 列的整数矩阵，再输入 q 个操作，每个操作包含五个整数 x1,y1,x2,y2,c，其中 (x1,y1) 和 (x2,y2) 表示一个子矩阵的左上角坐标和右下角坐标。

每个操作都要将选中的子矩阵中的每个元素的值加上 c。

请你将进行完所有操作后的矩阵输出。

- 输入格式

第一行包含整数 n,m,q。

接下来 n 行，每行包含 m 个整数，表示整数矩阵。

接下来 q 行，每行包含 5 个整数 x1,y1,x2,y2,c，表示一个操作。

- 输出格式

共 n 行，每行 m 个整数，表示所有操作进行完毕后的最终矩阵。

- 数据范围

1≤n,m≤1000,
1≤q≤100000,
1≤x1≤x2≤n,
1≤y1≤y2≤m,
−1000≤c≤1000,
−1000≤矩阵内元素的值≤1000

- 输入样例：

```
3 4 3
1 2 2 1
3 2 2 1
1 1 1 1
1 1 2 2 1
1 3 2 3 2
3 1 3 4 1
```

- 输出样例：

```
2 3 4 1
4 3 4 1
2 2 2 2
```

==代码==

```c++
// 二维差分基本应用，看出来了cin(cout)确实比scanf(printf)慢将近一倍啊！

#include <iostream>
using namespace std;

const int N = 1010;
int nums[N][N], diff[N][N];
int n, m, q;

void op(int x1, int y1, int x2, int y2, int c) {
    diff[x1][y1] += c;
    diff[x2 + 1][y1] -= c;
    diff[x1][y2 + 1] -= c;
    diff[x2 + 1][y2 + 1] += c;
}

int main() {
    cin >> n >> m >> q;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            cin >> nums[i][j];
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            op(i, j, i, j, nums[i][j]);  // 通过op方法来维护差分矩阵
    // 执行query
    for (int i = 0; i < q; ++i) {
        int x1, y1, x2, y2, c;
        cin >> x1 >> y1 >> x2 >> y2 >> c;
        op(x1, y1, x2, y2, c);
    }
    // 求差分矩阵的前缀和矩阵即为原数组矩阵
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
            cout << diff[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```



# 双指针算法

## [最长连续不重复子序列](https://www.acwing.com/problem/content/801/)

给定一个长度为 n 的整数序列，请找出最长的不包含重复的数的连续区间，输出它的长度。

- 输入格式

第一行包含整数 n。

第二行包含 n 个整数（均在 0∼10e5 范围内），表示整数序列。

- 输出格式

共一行，包含一个整数，表示最长的不包含重复的数的连续区间的长度。

- 数据范围

1≤n≤10e5

- 输入样例：

```
5
1 2 2 3 5
```

- 输出样例：

```
3
```

==代码==

```c++
#include <iostream>
using namespace std;

const int N = 100010;
int nums[N], record[N];
int n;

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> nums[i];
    
    int j = 0;
    int res = 0;
    for (int i = 0; i < n; ++i) {
        ++record[nums[i]];
        while (record[nums[i]] > 1) --record[nums[j++]];
        res = max(res, i - j + 1);
    }
    cout << res << endl;
    return 0;
}
```

## [数组元素的目标和](https://www.acwing.com/problem/content/802/)

给定两个升序排序的有序数组 A 和 B，以及一个目标值 x。

数组下标从 0 开始。

请你求出满足 A[i]+B[j]=x 的数对 (i,j)。

数据保证有唯一解。

- 输入格式

第一行包含三个整数 n,m,x，分别表示 A 的长度，B 的长度以及目标值 x。

第二行包含 n 个整数，表示数组 A。

第三行包含 m 个整数，表示数组 B。

- 输出格式

共一行，包含两个整数 i 和 j。

- 数据范围

数组长度不超过 10e5。
同一数组内元素各不相同。
1≤数组元素≤10e9

- 输入样例：

```
4 5 6
1 2 4 7
3 4 6 8 9
```

- 输出样例：

```
1 1
```

==代码==

```c++
// 双指针注意方向互斥就好了

#include <iostream>
using namespace std;

const int N = 100010;
int A[N], B[N];
int n, m, x;

int main() {
    cin >> n >> m >> x;
    for (int i = 0; i < n; ++i) cin >> A[i];
    for (int i = 0; i < m; ++i) cin >> B[i];
    
    int l = 0, r = m - 1;
    while (A[l] + B[r] != x) {
        if (A[l] + B[r] < x) ++l;
        else --r;
    }
    cout << l << " " << r << endl;
    return 0;
}
```

## [判断子序列✅](https://www.acwing.com/problem/content/2818/)

给定一个长度为 nn 的整数序列 a1,a2,…,an 以及一个长度为 m 的整数序列 b1,b2,…,bm。

请你判断 a 序列是否为 b 序列的子序列。

子序列指序列的一部分项按**原有次序排列**而得的序列，例如序列 {a1,a3,a5 是序列 {a1,a2,a3,a4,a5 的一个子序列。

- 输入格式

第一行包含两个整数 n,m。

第二行包含 n 个整数，表示 a1,a2,…,ana。

第三行包含 m 个整数，表示 b1,b2,…,bm。

- 输出格式

如果 a 序列是 b 序列的子序列，输出一行 `Yes`。

否则，输出 `No`。

- 数据范围

1≤n≤m≤10e5,
−10e9≤ai,bi≤10e9

- 输入样例：

```
3 5
1 3 5
1 2 3 4 5
```

- 输出样例：

```
Yes
```

==代码==

```c++
#include <iostream>
using namespace std;

const int N = 100010;
int A[N], B[N];
int n, m;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> A[i];
    for (int i = 0; i < m; ++i) cin >> B[i];
    
    // 经典双指针，双指针一定能够保证有解
    int i = 0, j = 0;
    while (i < n && j < m) {
        if (A[i] == B[j]) ++i;
        ++j;  // 无论是否匹配成功，j都要往后走一次
    }
    cout << (i == n ? "Yes" : "No") << endl;
    return 0;
}
```

