# flask-magic-number-app
A REST endpoint that process a number input and turns it into a magic number efficiently. 

# Coding Challenge
Look at the pseudocode below. specialMath(7) returns 79. specialMath(17) returns 10926. This question has two parts: first, implement it in Python, ensuring someone can call it through a REST endpoint (e.g. $> curl http://127.0.0.1:5000/specialmath/7); second, have the endpoint calculate for an input of 90. You can use frameworks such as Django and Flask if you like.

```
function specialMath(int n) {
	if(n==0) return 0
	else if(n==1) return 1
	else return n + specialMath(n-1) + specialMath(n-2)
}
```

# How To Test The Endpoint
Make sure flask and python is installed before running the command 

```
python -m flask run
```

# Output For Test Cases 
> 7 17 90 100

<img width="1095" alt="Screen Shot 2021-11-11 at 6 45 51 PM" src="https://user-images.githubusercontent.com/20455515/141400425-4456d769-f09d-4211-8166-d4a9d7d29541.png">
<img width="1196" alt="Screen Shot 2021-11-11 at 6 46 10 PM" src="https://user-images.githubusercontent.com/20455515/141400454-ed34df55-d956-4a1f-9e19-a054112bf361.png">
<img width="1092" alt="Screen Shot 2021-11-11 at 6 46 22 PM" src="https://user-images.githubusercontent.com/20455515/141400459-0392a8f6-4649-44a0-a5b8-11eb318cb480.png">
<img width="1079" alt="Screen Shot 2021-11-11 at 6 46 34 PM" src="https://user-images.githubusercontent.com/20455515/141400464-49604700-a332-4c43-9fbf-c28266473b3d.png">
