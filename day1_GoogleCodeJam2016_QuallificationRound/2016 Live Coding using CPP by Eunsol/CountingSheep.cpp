// CountingSheep.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{

	int T;
	int N;
	int target;
	int digit[10]{ 0 };
	int digitcount;


	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		if (N == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			digitcount = 10;
			for (int j = 0; j < 10; j++) digit[j] = 0;
			for (int j = 1; j < 100; j++) {
				target = j * N;
				while (target) {
					if (!digit[target % 10]) {
						digit[target % 10] = 1;
						digitcount--;
					}
					target /= 10;
				}
				if (!digitcount) {
					cout << j * N << endl;
					digitcount = 1000;
					break;
				}
			}
			if (digitcount != 1000) cout << "INSOMNIA" << endl;
		}

	}
    return 0;
}

