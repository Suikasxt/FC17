#include"map.h"
#include<math.h>
#include<queue>
#include<cstdio>
#include<cassert>
#include<string>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#define INF 1e90

const double Deepth = 20;
const double searchRand = 0.1;
const double WeightGreedy = 0.1;
std::string debugOutput;
double Valuation(const Map& mainGame) {
	int playerNumber = mainGame.getPlayerNumber();
	int* scoreList = new int[playerNumber];
	mainGame.calcScore(scoreList);
	double value = 1.* (scoreList[0] + 1) / (scoreList[1] + 1);
	//printf("%d %d %lf\n", scoreList[0], scoreList[1], value);
	delete[] scoreList;
	return value;
	for (int i = 0; i < mainGame.getWidth(); i++) {
		for (int j = 0; j < mainGame.getTop(i); j++) {
			if (mainGame.getCell(j, i) == 0) {
				for (int k = 0; k < ScoreRoadNumber; k++) {
					if (mainGame.validCoord(j + ScoreRoad[k][0], i + ScoreRoad[k][1]) && mainGame.getCell(j + ScoreRoad[k][0], i + ScoreRoad[k][1]) == 0) {
						value += 0.001;
					}
					if (mainGame.validCoord(j - ScoreRoad[k][0], i - ScoreRoad[k][1]) && mainGame.getCell(j - ScoreRoad[k][0], i - ScoreRoad[k][1]) == 0) {
						value += 0.001;
					}
				}
			}
		}
	}
	return value;
}
int Ai_work_Greedy(const Map& mainGame, double Rand = 0, int player = 0) {
	int playerNumber = mainGame.getPlayerNumber();
	int* operaList = new int[playerNumber];
	int* scoreList = new int[playerNumber];

	int res = -1;
	double maxScore = -INF;
	int* preScoreList = new int[playerNumber];
	mainGame.calcScore(preScoreList);
	//枚举所有合法操作，判断在哪个位置落子能够最大化自己的收益
	for (int i = 0; i < mainGame.getWidth(); i++) {
		if (mainGame.judgeValidity(player, i)) {
			Map tmpGame(mainGame);
			for (int j = 0; j < playerNumber; j++) {
				operaList[j] = -1;
			}
			operaList[player] = i;
			tmpGame.doOpeartor(operaList);
			tmpGame.calcScore(scoreList);
			double score = scoreList[player] - preScoreList[player];
			score *= 1 + (1.* rand() / RAND_MAX - 0.5) * Rand;

			if ( score > maxScore) {
				res = i;
				maxScore = score;
			}
		}
	}
	for (int i = 0; i < mainGame.getWidth(); i++) {
		if (mainGame.judgeValidity(player, i)) {
			Map tmpGame(mainGame);
			for (int j = 0; j < playerNumber; j++) {
				operaList[j] = -1;
			}
			operaList[player ^ 1] = i;
			tmpGame.doOpeartor(operaList);
			tmpGame.calcScore(scoreList);
			double score = scoreList[player ^ 1] - preScoreList[player ^ 1];
			score *= 1 + (1.* rand() / RAND_MAX - 0.5) * Rand;

			if (score > maxScore) {
				res = i;
				maxScore = score;
			}
		}
	}
	delete[] operaList;
	delete[] scoreList;
	delete[] preScoreList;
	return res;
}
double search(const Map& mainGame, int firstOpera) {
	int playerNumber = mainGame.getPlayerNumber();
	int* operaList = new int[playerNumber];
	Map tmpGame(mainGame);
	for (int i = 0; i < Deepth && !tmpGame.getOver(); i++) {
		if (i == 0) {
			operaList[0] = firstOpera;
		}
		else {
			operaList[0] = Ai_work_Greedy(tmpGame, searchRand);
		}
		operaList[1] = Ai_work_Greedy(tmpGame, searchRand, 1);
		//printf("%d %d %d\n", tmpGame.getRoundId(), operaList[0], operaList[1]);
		tmpGame.doOpeartor(operaList);
	}
	delete[] operaList;
	return Valuation(tmpGame);
}
int Ai_work(const Map& mainGame) {
	int startTime = clock();
	debugOutput = "";
	int playerNumber = mainGame.getPlayerNumber();
	double* valueList = new double[mainGame.getWidth()];

	int res = -1;
	for (int i = 0; i < mainGame.getWidth(); i++) valueList[i] = 0;
	while(1.*(clock()-startTime)/CLOCKS_PER_SEC < 0.65) {
		for (int i = 0; i < mainGame.getWidth(); i++) {
			if (mainGame.judgeValidity(0, i)) {
				valueList[i] += search(mainGame, i);
			}
		}
	}
	int GreedyOpera = Ai_work_Greedy(mainGame);
	valueList[GreedyOpera] += fabs(valueList[GreedyOpera]) * WeightGreedy;
	for (int i = 0; i < mainGame.getWidth(); i++) {
		if (mainGame.judgeValidity(0, i)) {
			if (res == -1 || valueList[res] < valueList[i]) {
				res = i;
			}
		}
	}

	delete[] valueList;
	return res;
}

int main() {
	int height, width, playerNumber, blockNumber, range;
	scanf("%d%d%d%d%d", &height, &width, &playerNumber, &blockNumber, &range);
	Map mainGame(height, width, playerNumber, range);
	for (int i = 0; i < blockNumber; i++) {
		int column, row;
		scanf("%d%d", &column, &row);
		mainGame.setBlock(column, row);
	}
	int* operaList = new int[playerNumber];

	while (!mainGame.getOver()) {
		operaList[0] = Ai_work(mainGame);
		printf("%d\n", operaList[0]);
		std::cout << debugOutput << std::endl;
		fflush(stdout);
		for (int i = 1; i < playerNumber; i++) {
			scanf("%d", operaList + i);
		}
		if (mainGame.doOpeartor(operaList) == 0) {
			mainGame.setOver();
		}
	}
	delete[] operaList;
}
