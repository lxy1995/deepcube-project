# coding=utf8
from django.http import HttpResponse
from django.shortcuts import render
import json
import os

def initF(request):
    return render(request, 'Deep Cube.html')


def stateInit(request):
    FEToState = [6, 3, 0, 7, 4, 1, 8, 5, 2, 15, 12, 9, 16, 13, 10, 17, 14, 11, 24, 21, 18, 25, 22, 19, 26, 23, 20, 33,
                 30, 27, 34, 31, 28, 35, 32, 29, 38, 41, 44, 37, 40, 43, 36, 39, 42, 51, 48, 45, 52, 49, 46, 53, 50,
                 47];
    stateToFE = [2, 5, 8, 1, 4, 7, 0, 3, 6, 11, 14, 17, 10, 13, 16, 9, 12, 15, 20, 23, 26, 19, 22, 25, 18, 21, 24,
                                      29, 32, 35, 28, 31, 34, 27, 30, 33, 42, 39, 36, 43, 40, 37, 44, 41, 38, 47, 50, 53, 46, 49, 52, 45,
                                      48, 51];
    state = [2, 5, 8, 1, 4, 7, 0, 3, 6, 11, 14, 17, 10, 13, 16, 9, 12, 15, 20, 23, 26, 19, 22, 25, 18, 21, 24, 29,
                                  32, 35, 28, 31, 34, 27, 30, 33, 42, 39, 36, 43, 40, 37, 44, 41, 38, 47, 50, 53, 46, 49, 52, 45, 48,
                                  51];
    rotateIdxs_new = {
                             "B_1": [36, 37, 38, 38, 41, 44, 44, 43, 42, 42, 39, 36, 2, 5, 8, 35, 34, 33, 15, 12, 9, 18, 19, 20],
                             "B_-1": [36, 37, 38, 38, 41, 44, 44, 43, 42, 42, 39, 36, 2, 5, 8, 35, 34, 33, 15, 12, 9, 18, 19, 20],
                             "D_1": [9, 10, 11, 11, 14, 17, 17, 16, 15, 15, 12, 9, 18, 21, 24, 36, 39, 42, 27, 30, 33, 45, 48, 51],
                             "D_-1": [9, 10, 11, 11, 14, 17, 17, 16, 15, 15, 12, 9, 18, 21, 24, 36, 39, 42, 27, 30, 33, 45, 48, 51],
                             "F_1": [45, 46, 47, 47, 50, 53, 53, 52, 51, 51, 48, 45, 0, 3, 6, 24, 25, 26, 17, 14, 11, 29, 28, 27],
                             "F_-1": [45, 46, 47, 47, 50, 53, 53, 52, 51, 51, 48, 45, 0, 3, 6, 24, 25, 26, 17, 14, 11, 29, 28, 27],
                             "L_1": [18, 19, 20, 20, 23, 26, 26, 25, 24, 24, 21, 18, 0, 1, 2, 44, 43, 42, 9, 10, 11, 45, 46, 47],
                             "L_-1": [18, 19, 20, 20, 23, 26, 26, 25, 24, 24, 21, 18, 0, 1, 2, 44, 43, 42, 9, 10, 11, 45, 46, 47],
                             "R_1": [27, 28, 29, 29, 32, 35, 35, 34, 33, 33, 30, 27, 6, 7, 8, 51, 52, 53, 15, 16, 17, 38, 37, 36],
                             "R_-1": [27, 28, 29, 29, 32, 35, 35, 34, 33, 33, 30, 27, 6, 7, 8, 51, 52, 53, 15, 16, 17, 38, 37, 36],
                             "U_1": [0, 1, 2, 2, 5, 8, 8, 7, 6, 6, 3, 0, 20, 23, 26, 47, 50, 53, 29, 32, 35, 38, 41, 44],
                             "U_-1": [0, 1, 2, 2, 5, 8, 8, 7, 6, 6, 3, 0, 20, 23, 26, 47, 50, 53, 29, 32, 35, 38, 41, 44]};
    rotateIdxs_old = {
                             "B_1": [42, 39, 36, 36, 37, 38, 38, 41, 44, 44, 43, 42, 35, 34, 33, 15, 12, 9, 18, 19, 20, 2, 5, 8],
                             "B_-1": [38, 41, 44, 44, 43, 42, 42, 39, 36, 36, 37, 38, 18, 19, 20, 2, 5, 8, 35, 34, 33, 15, 12, 9],
                             "D_1": [15, 12, 9, 9, 10, 11, 11, 14, 17, 17, 16, 15, 36, 39, 42, 27, 30, 33, 45, 48, 51, 18, 21, 24],
                             "D_-1": [11, 14, 17, 17, 16, 15, 15, 12, 9, 9, 10, 11, 45, 48, 51, 18, 21, 24, 36, 39, 42, 27, 30, 33],
                             "F_1": [51, 48, 45, 45, 46, 47, 47, 50, 53, 53, 52, 51, 24, 25, 26, 17, 14, 11, 29, 28, 27, 0, 3, 6],
                             "F_-1": [47, 50, 53, 53, 52, 51, 51, 48, 45, 45, 46, 47, 29, 28, 27, 0, 3, 6, 24, 25, 26, 17, 14, 11],
                             "L_1": [24, 21, 18, 18, 19, 20, 20, 23, 26, 26, 25, 24, 44, 43, 42, 9, 10, 11, 45, 46, 47, 0, 1, 2],
                             "L_-1": [20, 23, 26, 26, 25, 24, 24, 21, 18, 18, 19, 20, 45, 46, 47, 0, 1, 2, 44, 43, 42, 9, 10, 11],
                             "R_1": [33, 30, 27, 27, 28, 29, 29, 32, 35, 35, 34, 33, 51, 52, 53, 15, 16, 17, 38, 37, 36, 6, 7, 8],
                             "R_-1": [29, 32, 35, 35, 34, 33, 33, 30, 27, 27, 28, 29, 38, 37, 36, 6, 7, 8, 51, 52, 53, 15, 16, 17],
                             "U_1": [6, 3, 0, 0, 1, 2, 2, 5, 8, 8, 7, 6, 47, 50, 53, 29, 32, 35, 38, 41, 44, 20, 23, 26],
                             "U_-1": [2, 5, 8, 8, 7, 6, 6, 3, 0, 0, 1, 2, 38, 41, 44, 20, 23, 26, 47, 50, 53, 29, 32, 35]};
    legalMoves = ["U_-1", "U_1", "D_-1", "D_1", "L_-1", "L_1", "R_-1", "R_1", "B_-1", "B_1", "F_-1", "F_1"];

    initInfo = {
        "FEToState": FEToState,
        "stateToFE": stateToFE,
        "state": state,
        "rotateIdxs_new": rotateIdxs_new,
        "rotateIdxs_old": rotateIdxs_old,
        "legalMoves": legalMoves
    }
    if request.POST:
        initInfo = json.dumps(initInfo)
        return HttpResponse(initInfo)
    return render(request, 'Deep Cube.html')


def solveCube(request):
    if request.POST:
        path = os.path.join(os.path.dirname(os.getcwd()))
        # if os.path.exists(os.path.join(path,"output_demo.json")):
            #os.remove(os.path.join(path,"code/output_demo.json"))
        data = request.POST.getlist("state")
        data = json.loads(data[0])
        data = {"states": [data['states']]}
        with open((os.path.join(path, "input_demo.json")), "w") as file:
            json.dump(data, file)
        os.system(
            "cd " + path + "; python " + os.path.join(path, "scripts/solveStartingStates.py --input ") + os.path.join(
                path, "input_demo.json --env cube3 --methods nnet --model_loc ") + os.path.join(path,"savedModels/cube3/1/ --nnet_parallel 100 --depth_penalty 0.2"))
        # 开始调用模型
        solveMoves = []
        solveMoves_rev = []
        solution_text = []
        if os.path.exists(os.path.join(path, "output_demo.json")):
            with open(os.path.join(path, "output_demo.json"), "rb") as output:
                data = json.load(output)["nnet"][0]
                for i in data:
                    solveMoves.append(i[0] + "_" + str(i[1]))
                    solveMoves_rev.append(i[0] + "_" + str(-i[1]))
                    if i[1] == 1:
                        solution_text.append(i[0])
                    else:
                        solution_text.append(str(i[0]) + "\'")
        data = {"moves": solveMoves, "moves_rev": solveMoves_rev, "solve_text": solution_text}
        print data
        data = json.dumps(data)
        return HttpResponse(data)
    return render(request, 'Deep Cube.html')
