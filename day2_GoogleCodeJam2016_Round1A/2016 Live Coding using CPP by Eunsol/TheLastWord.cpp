#include "stdafx.h"

#define _USE_MATH_DEFINES

#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>

#define forn(i, N) for(int i = 0; i < N; i ++)

using namespace std;

void solve() {
	string S;
	string target;
	cin >> S;
	for (char& s : S) {
		if (s >= target[0]) {
			target = s + target;
		}
		else {
			target = target + s;
		}
	}
	cout << target << endl;
}

int main()
{
	int T;
	cin >> T;

	forn(t, T) {

		cout << "Case #" << t + 1 << ": ";

		solve();
	}

	return 0;
}

