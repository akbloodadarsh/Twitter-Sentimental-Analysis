from sklearn.ensemble import RandomTreesEmbedding
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
import numpy as np


def RandomTreesEmbeddingAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Random Trees Embedding")
    rte = RandomTreesEmbedding(n_jobs=2, random_state=0)
    rte.fit(x_train_vft, y_train)
    y_predict_class = rte.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(np.array(y_test), np.array(y_predict_class)))
    print('Accuracy Score :', accuracy_score(y_test, y_predict_class))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, y_predict_class))
    print('Average Precision Score:', average_precision_score(y_test, y_predict_class))
    if rte.predict(vec) == [1]:
        return "Positive"
    else:
        return "Negative"