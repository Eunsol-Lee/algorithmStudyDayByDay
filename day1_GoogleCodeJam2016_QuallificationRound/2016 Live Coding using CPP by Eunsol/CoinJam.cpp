// CoinJam.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;
int main()
{

	
	int T, N, J;
	string result;
	int count = 0;
	cin >> T;
	cin >> N >> J;
	cout << "Case #1:" << endl;
	for (int a1 = 1; a1 < N - 1; a1 += 2) {
		for (int a2 = a1 + 2; a2 < N - 1; a2 += 2) {
			for (int a3 = 2; a3 < N - 1; a3 += 2) {
				for (int a4 = a3 + 2; a4 < N - 1; a4 += 2) {
					result.assign(N, '0');
					result[0] = '1';
					result[N - 1] = '1';
					result[a1] = '1';
					result[a2] = '1';
					result[a3] = '1';
					result[a4] = '1';
					count++;
					cout << result << " 3 2 3 3 7 3 3 2 3" << endl;
					if (count == J) return 0;

				}
			}
		}
	}
    return 0;
}

