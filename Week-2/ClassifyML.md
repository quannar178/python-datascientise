# Bài 2: Phân nhóm các thuật toán ML

Có 2 cách phổ biến để phân nhóm các thuật toán:

**1. Phân nhóm dựa trên phương thức học.**

Supervised Learning (Học có giám sát).

  * Classification (Phân loại)
  
  * Regression (Hồi quy)
  
Unsupervised Learning (Học không giám sát).

  * Clustering (phân nhóm)
  * Association

**2. Phân nhóm dựa trên chức năng**
   
  * Regression Algorithm
  * Classification Algorithm
  * Instance-based Algorithm
  * Regularization Algorithm
  * Bayesian Algorithm
  * Clustering Algorithm
  * Artificial Neural Network Algorithm
  * Dimensionality Reduaction Algorithm
  * Ensemble Algorithms.

**1. Phân nhóm dựa trên phương thức học**

Thường chia thành 4 nhóm: Supervised learning, unsupervised learning, semi-supervised learning và Reinforcement learning.

## **Supervised learning**

Thuật toán dự đoán đầu ra (outcome) của một dữ liệu mới (new input) dựa trên các cặp (input, outcome) đã biết từ trước. Cặp này còn được gọi là (data, label).

Là nhóm phổ biến nhất trong thuật toán ML.

Một cách toán học, Supervised learning là khi chúng ta có một tập biến đầu vào X = (x1 ... xn) và tập nhãn tương ứng Y = (y1 ... yn), trong đó xi, yi là xác vector. Các cặp biết trước (xi, yi) thuộc X x Y dlg tập training data (dữ liệu huấn luyện). Từ tập này ta cần tạo một số ánh xạ mỗi phân từ X sang Y: yi = f(xi)

Mục đích là xấp xỉ f thật tốt để khi có x mới ta có thể tính được nhãn tương ứng y = f(x).

Thuật toán supervised learning còn có thể chia thành 2 loại chính:

### Classification (phân loại)

Một bài toán dlg classification nếu các label của input data được chia thành một số hữu hạn nhóm.

Ví dụ: maill có spam hay không, có phải chó hay không, ...

### Regression (Hồi quy)

Nếu *label* không được chia thành các nhóm mà là một giá trị cụ thể.

Ví dụ: dựa vào một căn nhà x m^2 có y phòng ngủ và cách trung tâm z km thì có giá bao nhiêu.

## Unsupervised Learning (Học không giám sát)

Trong thuật toán này, chúng ta không biết được *outcome* hay *nhãn* mà chỉ có dữ liệu đầu vào. Nó dựa vào cấu trúc dữ liệu để thực hiện một công việc nào đó.

Ví dụ: phân nhóm (clustering) , giảm số chiều dữ liệu (dimension reduction).

Một cách toán học, Unsupervides learning là khi chúng ta có dữ liệu X mà không biết Y tương ứng, chúng ta không biết câu trả lời chính xác cho mỗi dữ liệu đầu vào.

Các bài toán UL được chia thành 2 loại:

### Clustering (phân nhóm)

Một bài toán phân nhóm toàn bộ dữ liệu X thành các nhóm nhỏ dựa trên sự tương quan giữa các dữ liệu trong mỗi nhóm.

Ví dụ: ta có các hình tam giác, vuông, chữ nhật, ... yêu cầu trẻ phân thành tứng nhóm (mặc dù chúng ko biết mảnh nào ứng với hình nào chúng có thể phân theo hình dạng.

### Assciation

Khi chúng ta muốn khám phá một quy luật dựa trên nhiều dữ liệu cho trước.

Ví dụ: người xem phim Naruto có khả năng xem Boruto.

Dựa vào đó tạo ra một hệ thống gợi ý.

## Semi-supervised learning (học bán giám sát)

X chỉ có 1 phần được gãn nhãn.

Thực tế cho thấy nhiều bài toán ML thuộc vào nhóm này vì việc thu thập dữ liệu có nhãn tốn thời gian và chi phí. Nhiều dữ liệu chỉ chuyên gia mới gãn nhán dược ngược lại dữ liệu chưa nhãn có thể lấy ở Internet.

## Reinforcement Learning (Học Củng cố)

Bài toán giúp một hệ thống tự động xác định hành vi dựa trên hoàn cảnh để đạt được lợi ích cao nhất (maximizing the performance).

**2. Phân nhóm dựa trên chức năng.**

Regression Algorithms
  * Linear resgression
  * Logistic regression
  * Stepwise regression

Classification Algorithm
  * Linear classifier
  * Support vector machine
  * Kernel SVM
  * Sparse representation-based classification (SRC)

Instance-based algorithm
  * k-nearest neighbor (kNN)
  * Learning Vector Quantization (LVQ)

Regularization algorithm
  * Ridge regression
  * Least Absolute Shrinkage and Selection Operator (LASSO)
  * Least-Angle Regression (LARS)

Bayesian algorithm
  * Naive Bayes
  * Gaussian Naive Bayes

clustering algorithm
  * -k-means clustering
  * k-medians
  * expectation Maximization (EM)

Artificial Neural Network Algorithms
  * Perceptron
  * softmax regression
  * multi-layer perceptron
  * back-propagation

Dimensionality Recuation Algorithm
  * Principal component analysis (PCA)
  * Lenear Discrimiant Analysis (LDA)

Ensemble Algorithm
  * Boosting
  * AdaBoost
  * Random forest

