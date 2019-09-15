class keras_checker(object):
    def __init__(self,keras_model):
        self.model=keras_model
        self.initial_weights=self.model.get_weights()
        
    def weights_checker(self,train_imgs,train_labels,no_of_epochs):
        model.fit(train_imgs,train_labels,no_of_epochs)
        final_weights=model.get_weights()
        for i in range(len(self.initial_weights)):
            print(np.array_equal(self.initial_weights[i],final_weights[i]))
        return(self.initial_weights,final_weights)
