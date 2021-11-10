#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import sys
import os

class CSV_Combiner:
    @staticmethod
    def file_path_check(argv):
        
        
        if len(argv) <= 1:
            print('Error: Input is not correct')
            return False
        
        args_list = argv[1:]
        
        for file_p in args_list:
            if not os.path.exists(file_p):
                print("Error: Can't Find File: " +file_p )
                return False
            return True
            
    def combiner(self, argv: list):
        
        if self.file_path_check(argv):
            files_list = argv[1:]
            
            dataframes = []
            
            for file in files_list:
                
                    
                df = pd.read_csv(file)
                df['filename'] = os.path.basename(file)
                dataframes.append(df)
                merged_df = pd.concat(dataframes)
            
            print(merged_df.to_csv(index=False,header=True))
            
        else:
            return
        
def main():
    csv_combiner = CSV_Combiner()
    csv_combiner.combiner(sys.argv)
    
    
if __name__ == '__main__':
        main()


# In[ ]:




