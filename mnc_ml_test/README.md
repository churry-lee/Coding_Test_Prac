## Best Reuslt >> Test12

### Model
- input size: 6
 
        self.module = nn.Sequential(
            nn.Linear(6, 60, bias=True), nn.ELU(),
            nn.Linear(60, 60, bias=True), nn.ELU(),
            nn.Linear(60, 6, bias=True), nn.ELU(),
            nn.Linear(6, 1, bias=True)
        )
- 활성화 함수
  - ReLU, LeakyReLU, ELU 등을 사용해봤으나, ELU를 사용했을 때 가장 성능이 좋음

### Feature Engineering
- normalize: Min-Max, -1.0 ~ 1.0
- 상관계수에 따른 데이터 정제 
 
      target    1.000000
      X4        0.121294
      X3        0.044379
      X5        0.027451
      X1       -0.000290
      X2       -0.014679
      X0       -0.970127
      Name: target, dtype: float64 
- 상관계수가 가장 큰 "X0"로 모든 피처 나눠줌 
 
      target    1.000000
      X8        0.775025
      X10       0.628874
      X9        0.302194
      X4        0.121294
      X3        0.044379
      X5        0.027451
      X1       -0.000290
      X2       -0.014679
      X11      -0.285219
      X7       -0.698656
      X0       -0.970127
      X6             NaN
      Name: target, dtype: float64
- 이 후 target과 feature 간의 연관성을 크게 하기 위해 상관계수가 작은 원래 feature들을 제거, "X1", "X2", "X3", "X4", "X5"

### Loss Funtion
- MSE 손실함수 사용
- MAE 평가지표 사용
- RMSE 손실함수를 썻을 때 성능개선 없음

### Optimaizer
- ADAM, ADAMW, RADAM을 사용해봤으나, ADAMW가 가장 성능이 좋음
- SGD와 lr_scheduler을 활용하여 학습을 시켜봤으나, 크게 개선은 안됨

### batch_size
- 우선 train data set을 60:40 or 80:20으로 train:valid 셋으로 나눠 주었음
- batch_size는 16, 32를 사용
- 각각의 조합에 대해서 결과가 크게 차이 나지는 않음
- 최종 결과는 60:40, 32를 사용
