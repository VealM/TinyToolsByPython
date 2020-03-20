import numpy as np  
import matplotlib.pyplot as plt

def BAplot(d_key, d_val,data_len):
    ''' 
        Plot  Bland-Altman figure for features in d_val in pairs
        95% limits of agreement
        input:
              d_key:  a list stores feature names
              d_val:  a list stores features corresponding to d_key 
              data_len: feature len in d_val (length of feature in d_val should be the same)
    '''

    ft_len = len(d_val)-1
    
    for k in range(ft_len,-1,-1):
        for j in range(k-1,-1,-1):

            diff = d_val[k] - d_val[j]
            mean = (d_val[k] + d_val[j])/2
            
            x_min = np.min(mean)
            x_max = np.max(mean)

            
            m_diff = np.mean(diff)
            std_diff = np.std(diff)
            up = m_diff + 1.96*std_diff
            down = m_diff - 1.96*std_diff 

            btl = d_key[k] + " and " + d_key[j]
            xtl = "Mean of " + btl 
            ytl = "Bias of " + btl

            out = (np.sum((diff > up).astype(np.int)) + np.sum((diff < down).astype(np.int)))/data_len

            print("Result for {}".format(btl))
            print("95 limits of agreement to be({:.2f},{:.2f})".format(down,up))
            print("data points over limits of agreement are {:.2%}".format(out))
            print("\n")
            plt.figure()
            plt.scatter(mean, diff, alpha=0.6)
            plt.hlines(up,x_min,x_max,colors = "b", linestyles = "dashed")
            plt.hlines(down,x_min,x_max,colors = "b", linestyles = "dashed")
            plt.xlabel(xtl)
            plt.ylabel(ytl)
            plt.savefig(btl)

if __name__ == "__main__":

    d_key = ['normal-1', 'normal-2']
    d_val = []
    data_len = 200
    d_val.append(np.random.normal(size=(1,data_len)))
    d_val.append(np.random.poisson(size=(1,data_len)))
    BAplot(d_key,d_val,data_len)    