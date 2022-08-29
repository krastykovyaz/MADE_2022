#include <bits/stdc++.h>
#define int long long
#define endl "\n"
using namespace std;
int INF = 1e18;
template <class T>
ostream& operator << (ostream &out, vector <T>& a) {
    for (auto &el : a) out << el << " ";
    return out;
}

template <class T>
istream& operator >> (istream &in, vector <T> &a) {
    for (auto &el: a) in >> el;
    return in;
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, m, T;
    cin >> n >> m >> T;
    vector <int> a(n);
    cin >> a;
    sort(a.begin(), a.end());

    multiset <int> st;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (st.size() && *st.begin() < a[i]) {
            st.clear();
            ans += 1;
        }
        st.insert(a[i] + T);
        if (st.size() == m) {
            st.clear();
            ans += 1;
        }
    }

    ans += (st.size() > 0);
    cout << ans << endl;
}


