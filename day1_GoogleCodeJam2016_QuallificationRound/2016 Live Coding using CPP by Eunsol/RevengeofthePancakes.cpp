// RevengeofthePancakes.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int T;
	string S;
	int count;
	int end;
	int cakes[1000];
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> S;
		for (int j = 0; j < S.length(); j ++) {
			cakes[j] = S[j] == '+';
		}
		end = S.length() - 1;
		for (count = 0; count < S.length() * 3; count++) {
			for (; end >=0 && cakes[end]; end--);
			if (end == -1) break;
			if (cakes[0] == 1) {
				for (int j = 0; j < end && cakes[j]; j++) {
					cakes[j] = 0;
				}
			}
			else
			{
				for (int j = 0; j <= end; j++)
					cakes[j] = !cakes[j];
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
    return 0;
}

