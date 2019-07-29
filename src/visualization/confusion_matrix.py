from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import itertools

class ConfusionMatrix:
    '''
    Class for plotting confusion matrix
    as well as accuracy, precision, recall, and fallout.

    Args:
        y_pred (list or np array): Predicted target values.
        y_test (list or np array): Actual target values.
        model (sklearn model obj): Classifier.

    Example:
        cm = ConfusionMatrix(y_pred, y_test, model)
        cm.confusion_matrix()

    '''
    
    def __init__(self, y_pred, y_test, model):
        self.y_test = y_test
        self.y_pred = y_pred
        self.model = model
        self.cm = confusion_matrix(y_test, y_pred)
        if model.classes_[0] == 1:  #in case the labels are flipped from the usual indices
            self.cm = np.array([[self.cm[1,1], self.cm[1,0]], [self.cm[0,1], self.cm[0,0]]])


    def confusion_matrix(self, classes=['0', '1'], title_on=False, title='Confusion Matrix', cmap=plt.cm.Blues):
        '''Plots confusion matrix w/ accuracy, precision, recall, fallout.
        
        Args:
            classes (list of two str): ['0', '1'] by default, change labels as desired.
            title_on (bool, optional): Default False, set to True to print title.
            title (str): Show title, if title_on arg set to True.
            cmap: Plot color palette.

        '''

        fig, ax = plt.subplots()
        
        plt.imshow(self.cm, interpolation='nearest', cmap=cmap)
        if title_on == True:
            plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        thresh = self.cm.max() / 2.
        for i, j in itertools.product(range(self.cm.shape[0]), range(self.cm.shape[1])):
            plt.text(j, i, self.cm[i, j],
                    horizontalalignment="center",
                    color="white" if self.cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label', fontsize=14)
        ax.xaxis.tick_top()
        plt.xlabel('Predicted label', fontsize=14)
        ax.xaxis.set_label_position('top')
        plt.show()

        tp = self.cm[1,1]
        fn = self.cm[1,0]
        fp = self.cm[0,1]
        tn = self.cm[0,0]
        print('Accuracy =     {:.3f}'.format((tp+tn)/(tp+fp+tn+fn)))
        print('Precision =     {:.3f}'.format(tp/(tp+fp)))
        print('Recall (TPR) =  {:.3f}'.format(tp/(tp+fn)))
        print('Fallout (FPR) = {:.3f}'.format(fp/(fp+tn)))


    def evaluation_metrics(self, print_res=1):
        '''
        Args:
            print_res (bool, optional): default 1, set to 0 for no printing

        Example:
            acc, pr, tpr, fpr = ConfusionMatrix.show_data()
        '''
        tp = self.cm[1,1]
        fn = self.cm[1,0]
        fp = self.cm[0,1]
        tn = self.cm[0,0]
        if print_res == 1:
            print('Accuracy =     {:.3f}'.format((tp+tn)/(tp+fp+tn+fn)))
            print('Precision =     {:.3f}'.format(tp/(tp+fp)))
            print('Recall (TPR) =  {:.3f}'.format(tp/(tp+fn)))
            print('Fallout (FPR) = {:.3f}'.format(fp/(fp+tn)))
        return (tp+tn)/(tp+fp+tn+fn), tp/(tp+fp), tp/(tp+fn), fp/(fp+tn)
