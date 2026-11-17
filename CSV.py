import pandas as pd
#pandas extension to write to csv

import datetime

from DM_Decode import ordered
#getting results variable from the file DM_Decode

now = datetime.datetime.now()

df = pd.DataFrame({"Decoded": [c[2] for c in ordered]})
#structures data

df.index = df.index + 1
#starts counting from 1 instead of 0 in csv file

df.to_csv("test.csv")
#saves to test.csv

#df.to_csv(now.strftime("%Y%m%d-%H%M%S.csv"))
#saves new file with date and time

if __name__ == "__main__":
    #don't import anything in this statement

    print("PANDA VERSION:", pd.__version__)
    #print pandas version number






