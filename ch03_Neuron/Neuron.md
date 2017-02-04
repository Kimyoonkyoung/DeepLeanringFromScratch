# Neuron

***

### ActivationFunction
입력 신호의 총합을 출력 신호로 변환하는 비선형 함수
선형함수의 경우에는 hidden layer를 깊게 하더라도, single layer와 같은 기능을 하게 된다
* **stepFunction**
    * 0 보다 작으면 0, 0 보다 크면 1
    * 연속적이지 못한것이 하나의 단점
* **sigmoid**
    * S자 모양의 함수
    * 연속적임
* **ReLU**
    * 0 보다 작으면 0, 0 보다 크면 그 값 그대로
    
***

### OutputFunction
classfication, regrssion 의 **목적에 따라** output function을 다르게 설정한다
* **Identity Function**
    * 입력을 그대로 출력함
    * regression 에서 사용함

* **Softmax Function**
    * classification 에서 사용함
    * softmax 의 출력의 총합은 1 -> 확률
        * 즉, 인풋과 아웃풋의 대소관계가 변하지 않음 (exp(x) 가 단조증가)
        * **일반적으로 learning 할때는 softmax를 적용하지만, test 할때는 계산 낭비를 줄이기위해 적용하지 않는다**
    * 구현시 주의사항
        * exp() 의 경우, 입력값이 커지면 inf 가 나올 수 있음
        * 따라서, 입력값 중 가장 큰 값을 동일하게 빼줌
        
***

### mini batch
I/O를 통한 데이터를 읽는 것은 느리기 때문에, CPU나 GPU를 이용해서 순수 계산을 수행하는 비율을 높여줌

