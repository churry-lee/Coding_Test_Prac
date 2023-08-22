#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int solution(vector<vector<int>> board) {
	int answer = 25;

/*
	for (int i = 0; i < board.size(); i++)
		for (int j = 0; j < board[0].size(); j++)
			if (board[i][j] == 1)
			{
				if (i < board.size() && j < board[0].size())
				{
					board[i-1][j-1] == 0 ? board[i-1][j-1] = 2 : NULL;
					board[i-1][j  ] == 0 ? board[i-1][j  ] = 2 : NULL;
					board[i-1][j+1] == 0 ? board[i-1][j+1] = 2 : NULL;

					board[i][j-1] == 0 ? board[i][j-1] = 2 : NULL;
					board[i][j  ] == 0 ? board[i][j] = 2 : NULL;
					board[i][j+1] == 0 ? board[i][j+1] = 2 : NULL;

					board[i+1][j-1] == 0 ? board[i+1][j-1] = 2 : NULL;
					board[i+1][j  ] == 0 ? board[i+1][j  ] = 2 : NULL;
					board[i+1][j+1] == 0 ? board[i+1][j+1] = 2 : NULL;
				}
				else if (i == board.size() && j < board[0].size())
				{
					board[i-1][j-1] == 0 ? board[i-1][j-1] = 2 : NULL;
					board[i-1][j  ] == 0 ? board[i-1][j  ] = 2 : NULL;
					board[i-1][j+1] == 0 ? board[i-1][j+1] = 2 : NULL;

					board[i][j-1] == 0 ? board[i][j-1] = 2 : NULL;
					board[i][j  ] == 0 ? board[i][j  ] = 2 : NULL;
					board[i][j+1] == 0 ? board[i][j+1] = 2 : NULL;
				}
				else if (i < board.size() && j == board[0].size())
				{
					board[i-1][j-1] == 0 ? board[i-1][j-1] = 2 : NULL;
					board[i-1][j  ] == 0 ? board[i-1][j  ] = 2 : NULL;

					board[i][j-1] == 0 ? board[i][j-1] = 2 : NULL;
					board[i][j  ] == 0 ? board[i][j  ] = 2 : NULL;

					board[i+1][j-1] == 0 ? board[i+1][j-1] = 2 : NULL;
					board[i+1][j  ] == 0 ? board[i+1][j  ] = 2 : NULL;
				}
				else if (i == board.size() && j == board[0].size())
				{
					board[i-1][j-1] == 0 ? board[i-1][j-1] = 2 : NULL;
					board[i-1][j  ] == 0 ? board[i-1][j  ] = 2 : NULL;

					board[i][j-1] == 0 ? board[i][j-1] = 2 : NULL;
					board[i][j  ] == 0 ? board[i][j  ] = 2 : NULL;
				}
			}
*/

	for (int i = 0; i < board.size(); i++)
		for (int j = 0; j < board[0].size(); j++)
			if (board[i][j] == 1)
			{
				i == 0 ? NULL : j == 0 ? NULL : board[i-1][j-1] == 0 ? board[i-1][j-1] = 2 : NULL;
				i == 0 ? NULL : board[i-1][j  ] == 0 ? board[i-1][j  ] = 2 : NULL;
				i == 0 ? NULL : j == board[0].size()-1 ? NULL : board[i-1][j+1] == 0 ? board[i-1][j+1] = 2 : NULL;

				j == 0 ? NULL : board[i][j-1] == 0 ? board[i][j-1] = 2 : NULL;
				board[i][j  ] == 0 ? board[i][j] = 2 : NULL;
				j == board[0].size()-1 ? NULL : board[i][j+1] == 0 ? board[i][j+1] = 2 : NULL;

				i == board.size()-1 ? NULL : j == 0 ? NULL : board[i+1][j-1] == 0 ? board[i+1][j-1] = 2 : NULL;
				i == board.size()-1 ? NULL : board[i+1][j  ] == 0 ? board[i+1][j  ] = 2 : NULL;
				i == board.size()-1 ? NULL : j == board[0].size()-1 ? NULL :board[i+1][j+1] == 0 ? board[i+1][j+1] = 2 : NULL;

				answer -= 1;
			}

//	for (auto & iter : board)
//	{
//		for (auto & num : iter)
//		{
//			cout << num << " ";
//		}
//		cout << endl;
//	}
//
//	for (int i = 0; i < board.size(); i++)
//		for (int j = 0; j < board[0].size(); j++)
//			if (board[i][j] == 0)
//				answer += 1;

	return answer;
}


int main()
{
	vector<vector<int>> dots{{1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}};
	cout << solution(dots) << endl;

	return 0;
}