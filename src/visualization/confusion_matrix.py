from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import itertools

class ConfusionMatrix:
    '''
    Class for plotting confusion matrix
    as well as accuracy, precision, recall, fallout
    given the following:
    y_pred (predicted values),
    y_test (actual values),
    model (classifier)

    Usage
    --------
    1. instantiate class object, passing in
    y_pred, y_test, and model
    2. use the plot_confusion_matrix and show_data 
    methods on the class object
    '''
    
    def __init__(self, y_pred, y_test, model):
        self.y_test = y_test
        self.y_pred = y_pred
        self.model = model
        self.cm = confusion_matrix(y_test, y_pred)
        if model.classes_[0] == 1:  #in case the labels are flipped from the usual indices
            self.cm = np.array([[self.cm[1,1], self.cm[1,0]], [self.cm[0,1], self.cm[0,0]]])

    def plot_confusion_matrix(self, classes=['0', '1'],
                          normalize=False,
                          title_on=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
        '''
        This function prints and plots the confusion matrix.
        
        Args
        --------
        classes: ['0', '1'] by default, can be changed as desired (use list of 2 strings)
        title_on: set this to True to print title arg as title
        title: string to be used as plot title, if previous arg set to True
        cmap: plot color palette

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

    def show_data(self, print_res=1):
        '''
        Usage
        --------
        acc, pr, tpr, fpr = ConfusionMatrix.show_data()

        Args
        --------
        print_res: default 1, set to 0 for no printing
        '''
        tp = self.cm[1,1]
        fn = self.cm[1,0]
        fp = self.cm[0,1]
        tn = self.cm[0,0]
        if print_res == 1:
            print('Accuracy =     {:.3f}'.format((tp+tn)/(tp+fp+tn+fn)))  #my addition
            print('Precision =     {:.3f}'.format(tp/(tp+fp)))
            print('Recall (TPR) =  {:.3f}'.format(tp/(tp+fn)))
            print('Fallout (FPR) = {:.3f}'.format(fp/(fp+tn)))
        return (tp+tn)/(tp+fp+tn+fn), tp/(tp+fp), tp/(tp+fn), fp/(fp+tn)


# if __name__ == "__main__":
