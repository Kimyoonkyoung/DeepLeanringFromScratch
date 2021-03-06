# Learning

***

### 간단한 용어 정리
* 학습
    * 훈련 데이터로부터 가중치 매개변수의 최적값을 자동으로 획득하는 것
* 오버피팅
    * 한 데이터셋에만 지나치게 최적화된 상태
* 미니배치 
    * 데이터를 일부 추려 전체의 '근사치'로 학습하는 것 (랜덤추출)
* 에폭 (epoch)
    * 미니배치 1set 을 의미함
* 하이퍼파라미터
    * learning rate, weight decay 등과 같이 신경망의 매개변수와 성질이 다른 매개변수
    * 신경망의 가중치 매개변수는 훈련 데이터와 학습 알고리즘에 의해 자동으로 획득되지만,
    * 하이퍼파라미터는 사람이 직접 설정해야함
    * 따라서 여러 후보 값 중에서 시험을 통해 가장 잘 학습하는 값을 찾는 과정이 필요함
    
****

### 손실함수 (loss function, cost function)
최적의 매개변수 값을 탐색할 수 있는 지표
* 일반적으로, 평균제곱오차(MSE) 와 교차엔트로피오차(cross entropy)를 사용함
    * 평균제곱오차 (MSE)
        * 추정값과 정답값의 차이에 대한 제곱합을 평균낸 것
    * 교차엔트로피오차 (cross entropy)
        * log에 0이 들어가지 않도록, 아주 작은값을 더해줌
        * 원-핫 인코딩으로 구현시, 정답에 해당하는 레이블 만으로 교차엔트로피를 구현할 수 있음

****

### 수치미분
아주 작은 차분으로 미분을 구하는 것을 말함
* 중심차분, 중앙차분
    * x를 중심으로 그 전후의 차분을 계산한다는 뜻
* 편미분
    * 변수가 여럿인 함수에 대한 미분
        * 변수가 하나인 함수를 정의하고 (즉, 변수하나가 상수값으로 고정된)
        
****

### 기울기 (gradient)
모든 변수의 편미분을 벡터로 정리한것을 기울기라고함
* **기울기가 가리키는 쪽은 각 장소에서 함수의 출력 값을 가장 줄이는 방향을 의미함**
* 경사법 (gradient method)
    * 현 위치에서 기울어진 방향으로 일정 거리만큼 이동하고, 이동한 곳에서 기울기를 구하고 이동하고 하면서 나아가는 방법
    * 함수의 값을 점차 줄이는 것
* 학습률 (learning rate)
    * 한번의 학습으로 얼만큼 학습해야할지, 매개변수 값을 얼마나 갱신하는지 결정

****

### SGD(stochastic gradient descent) 알고리즘
1. 전제
    * 신경망에는 적응 가능한 가중치와 편향이 있고, 이 가중치와 편향을 훈련 데이터에 적응하도록 조정하는 과정을 '학습'이라고 함
2. 미니배치
    * 훈련데이터 중 일부를 무작위로 가져옴
    * 미니배치의 손실 함수 값을 줄이는 것이 목표
3. 기울기 산출
    * 손실 함수의 값을 줄이기 위해 각 가중치 매개변수의 기울기를 구함
    * 기울기는 손실 함수의 값을 작게하는 방향을 제시함
4. 매개변수 갱신
    * 가중치 매개변수를 기울기 방향으로 아주 조금 갱신함
5. 2~4 반복

