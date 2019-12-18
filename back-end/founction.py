# coding=utf8
from django.http import HttpResponse
from django.shortcuts import render
import json
import os

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
