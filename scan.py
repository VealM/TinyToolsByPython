'''
    Provide a simple tool for scanning document from phone photos
    Run python scan.py -h to get know how to use it
'''

import matplotlib.image as img
import numpy as np
import os
import argparse


def get_file_dict(data_dir):
    '''
        return a dict with dirs as keys and files in dirs as vals
        input: 
            data_dir: dir where img folders as its child folders
    '''

    for _, dir_name, _ in os.walk(data_dir):
        dir_name = dir_name
        break
    
    all_files = []
    for fold in dir_name:
        files = []
        for _, _, file in os.walk(os.path.join(data_dir,fold)):
            files.append(file)
        all_files.extend(files)
    folders = dict(zip(dir_name, all_files))
    return folders

def main():

    parser = argparse.ArgumentParser()

    ## Required parameters
    parser.add_argument("--data_dir",
                        default='.',
                        type=str,
                        help="The input data dir. Should contain the img folders for the scanning.")
    
    args = parser.parse_args()      
    data_dir = args.data_dir
    dir_data = get_file_dict(data_dir)
    for scan in dir_data.keys():
        print("Processing for folder {} in {}".format(scan, data_dir))
        file_list = dir_data[scan]
        dir_path = os.path.join(data_dir,scan)
    
        # mkdir for store pics after process 
        new_dir = "Scan" + scan
        new_dir = os.path.join(data_dir, new_dir)
        os.mkdir(new_dir)
    
        for file in file_list:
            pcfile = os.path.join(new_dir, file)
            file = img.imread(os.path.join(dir_path,file))
            R ,G, B = file[:,:,0], file[:,:,1], file[:,:,2]
        
            red = (R>=105).astype(int)*(R<=255).astype(int)*(G<70).astype(int)*(B<70).astype(int) # get red region
        
            R, G, B = R.copy(), G.copy(), B.copy() # R,G,B is read only, make copy for it
            idx = np.where(red == 1)
            R[idx], G[idx], B[idx] = 255, 70, 70
        
            gray=R*0.2989+G*0.587+B*0.114 # transform on gray

            white=(gray>120).astype(int)-red # reinforce white region
            widx = np.where(white == 1)
            R[widx], G[widx], B[widx] = 255, 255, 255

            black=(gray<100).astype(int) -red # reinforce black region
            bidx = np.where(black == 1)
            R[bidx], G[bidx], B[bidx] = 0, 0, 0


            res = np.zeros_like(file)
            res[:,:,0], res[:,:,1], res[:,:,2] = R, G, B
            img.imsave(pcfile,res)
        
        print("Completed for folder {} !".format(scan))              

if __name__ == "__main__":
    main()