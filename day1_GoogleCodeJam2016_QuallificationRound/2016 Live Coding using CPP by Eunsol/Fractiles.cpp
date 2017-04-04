// Fractiles.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>

using namespace std;
int main()
{
	int T, K, C, S;

	unsigned long long int sum;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> K >> C >> S;
		cout << "Case #" << i + 1 << ": ";
		if (((int)(K - 1) / C) + 1 > S) {
			cout << "IMPOSSIBLE" << endl;

		}
		else {

			for (int j = 1; j <= K; j += C) {
				sum = 1;
				for (int k = 0; k < C && k + j <= K; k ++) {
					sum += (unsigned long long int)(j - 1 + k) * (unsigned long long int) powl(K, C - k - 1);
					
				}
				cout << sum << " ";
			}
			cout << endl;
		}
	}
    return 0;
}

