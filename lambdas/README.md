- Comandos
```
sam build MyFunctionB --template "$HOME/projects/prj_python37/lambdas/lambda-b/template.yaml" --build-dir "$HOME/projects/lambda-builds/prj-python/l-b" --use-container --debug
sam local invoke MyFunctionB --template "$HOME/projects/lambda-builds/prj-python/l-b/template.yaml" --event "$HOME/projects/prj_python37/lambdas/lambda-b/input.json"  --debug 
sam local start-lambda -p 3050 --template "$HOME/projects/lambda-builds/prj-python/l-b/template.yaml"  --debug

sam build MyFunctionA --template "$HOME/projects/prj_python37/lambdas/lambda-a/template.yaml" --build-dir "$HOME/projects/lambda-builds/prj-python/l-a" --use-container --debug
sam local invoke MyFunctionA --template "$HOME/projects/lambda-builds/prj-python/l-a/template.yaml" --event "$HOME/projects/prj_python37/lambdas/lambda-a/input.json"  --debug
```
