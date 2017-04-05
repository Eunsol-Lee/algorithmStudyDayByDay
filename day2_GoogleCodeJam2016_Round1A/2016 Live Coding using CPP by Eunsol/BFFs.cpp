#include "stdafx.h"

#define _USE_MATH_DEFINES

#include <iostream>
#include <math.h>
#include <algorithm>

#define forn(i, N) for(int i = 0; i < N; i ++)

using namespace std;

void solve() {
	int N;
	int F[1001];
	int seed[1001] = { 0 };
	int distance[1001] = { 0 };
	int result = 0;
	int seedcount = 0;
	cin >> N;
	forn(i, N) {
		cin >> F[i];
	}

	forn(i, N) {
		if (F[F[i] - 1] == i + 1) {
			seed[i] = 1;
		}
	}

	forn(i, N) {
		if (!distance[i] && !seed[i]) {
			int now = i;
			int count = 1;
			forn(j, N) {
				distance[now] = count;
				now = F[now] - 1;
				if (seed[now]) {
 					distance[now] = max(distance[now], count);
					break;
				}
				count++;
			}
		}
	}
	forn(i, N) {
		if (seed[i]) {
			seedcount += 1 + distance[i];
		}
	}


	forn(i, N) {
		int now, count = 1;
		now = i + 1;
		forn(j, N) {
			count++;
			now = F[now - 1];
			if (now == i + 1) {
				result = max(result, count - 1);
				break;
			}
		}
	}

	cout << max(result, seedcount) << endl;
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

