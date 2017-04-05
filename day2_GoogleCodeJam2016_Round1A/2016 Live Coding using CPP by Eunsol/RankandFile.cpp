#include "stdafx.h"

#define _USE_MATH_DEFINES

#include <iostream>
#include <math.h>
#include <algorithm>

#define forn(i, N) for(int i = 0; i < N; i ++)

using namespace std;

void solve() {
	int N;
	int number[5000];
	int an = 0;
	int count = 0;
	int now;
	cin >> N;
	forn(i, 2 * N - 1) {
		forn(j, N) {
			cin >> number[an++];
		}
	}
	sort(number, number + an);
	number[an] = number[an - 1] + 1;
	now = number[0];
	count = 1;
	for (int i = 1; i <= an; i++) {
		if (number[i] != now) {
			if (count % 2 == 1) {
				cout << now << " ";
			}
			now = number[i];

			count = 1;
		}
		else
		{
			count++;
		}
	}
	cout << endl;
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

