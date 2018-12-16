import numpy as np 

NUM_FEAT = 10
NUM_TRAIN = 100
datas = np.random.randint(low=0, high=10, size=[NUM_TRAIN, NUM_FEAT])
labels = np.random.randint(low=0, high=3, size=[NUM_TRAIN])

idx_test = int(0.7 * NUM_TRAIN)
data_train = datas[0:idx_test]
data_test = datas[idx_test:]

label_train = labels[0:idx_test]
label_test = labels[idx_test:]

def normalize_datas(datas):
    max_arr = np.max(datas)
    min_arr = np.min(datas)

    datas = (datas - min_arr) / (max_arr - min_arr)

class KNN(object):

    def __init__(self, datas, labels, K = 3):
        self.datas = datas 
        self.labels = labels 
        self.K = K 
    
    def sim_norm_2(self, vect1, vect2):
        return np.sqrt(sum((vect1-vect2)**2))

    def vote(self, test):
        
        all_sim = []

        for sample, label in zip(datas, labels):
            sim = self.sim_norm_2(test, sample)
            all_sim.append([sim, label])

        k_label = np.array(sorted(all_sim, key=lambda x: x[0]))[0:self.K][:,1]
        #print k_label 
        k_label = sorted(k_label)
        #print k_label
        
        # find most appearance neighbour 
        cur_num_appear = 1
        cur_label = k_label[0]
        voted_label = cur_label 
        voted_appear = 0

        for i in range(1, len(k_label)):
            if k_label[i] == cur_label and i != len(k_label)-1:
                cur_num_appear += 1
            else:
                if i == len(k_label) - 1: # end of iteration
                    cur_num_appear += 1
                if cur_num_appear > voted_appear:
                    voted_label = cur_label 
                    voted_appear = cur_num_appear 
                cur_num_appear = 1
                cur_label = k_label[i]
        #return class has most appearance in K-Nearest neighborhood
        return int(voted_label)

    def evaluate(self, datas, labels):
        
        len_data = len(datas) 
        c = 0

        for data, label in zip(datas, labels):
            predicted = self.vote(data)
            if predicted == label:
                c += 1 
        print "Right {} / Sum {}".format(c, len_data)
        print "Accuracy : ", c*100.0/ len_data 

if __name__ == "__main__":
    data_train = normalize_datas(data_train)
    knn = KNN(datas=data_train, labels=label_train, K=1)
    
    #print knn.vote(data_test[0])
    knn.evaluate(data_test, label_test)
