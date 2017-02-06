# Backpropagation

***

### 목적
* 수치미분은 단순하고 구현하기 쉽지만, 계산시간이 오래걸림
* 가중치 매개변수의 기울기를 효율적으로 구할 수 있음 (국소적 계산 논리)
* 연쇄법칙 (chain rule) 이용
    * 국소적 미분을 전달하는 원리
    * 합성함수의 미분은 합성함수를 구성하는 각 함수의 미분의 곱으로 나타냄
        * 그렇게 때문에, backpropagation 계산도 뒤에서 들어온 신호와 국소미분값(편미분)과 곱함
        * 책 155p 에 설명이 잘나와있음

****

### 수식 별 backpropagation
* 덧셈노드
    * 입력값을 그대로 흘려보냄
* 곱셈노드
    * 입력신호를 서로 바꾼 값을 곱해서 내보냄

****

### function 별 backpropagation
* ReLU 
    * 순전파때 0보다 작았던 layer는 0으로 함
* sigmoid
    * 순전파의 출력만으로 계산이 가능
* affine
    * 덧셈과 곱셈을 적절히 사용함
    * 편향 (bias)의 역전파는 두 데이터에 대한 미분을 데이터마다 더해서 구함
* softmax <<중요>> 
    * 예측값과 정답의 오차가 앞 계층에 전달됨
    * cross-entropy, MSE 모두 같은 backpropagation 값이 도출됨

****

### 참고
* 코드는 common.layers
* layer 들은 OrderedDict() 에 관리하면, forward() backward() 만 호출하면 유용
* gradient descent 의 정확도를 측정하기 위해서는 수치미분과 비교해봄
        
        

