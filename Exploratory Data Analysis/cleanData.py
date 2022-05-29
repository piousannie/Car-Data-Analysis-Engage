import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/aulee/Downloads/Cars.csv")

#change format of alpha nuneric data to numeric form
for column in df.columns:
    try:
        if(df.dtypes[column]==np.object0):
            for i in range((len(df[column]))):
                if(pd.isnull(df.loc[i,column])):
                    df.at[i,column]=None
                    continue

                temparr=df[column][i].split(" ")
                for item in temparr:
                    item=item.replace(",","")
                    if(item.isnumeric()):
                        df.at[i,column]=int(item)
                    elif item.replace('.','',1).isdigit() and item.count('.') < 2:
                        df.at[i,column]=float(item)

    except:
        continue

#fix anomalies in make and model data
for i in range(len(df)):
    if(pd.isnull(df.loc[i,"Make"])):
        temp=df["Model"][i].split(" ")
        if(temp[0]=="Go+"):
            temp2=df["Variant"][i].split(" ")
            df.at[i,"Make"]=temp2[0]
            df.at[i,"Variant"]=" ".join(temp2[1:])
            
        else:
            df.at[i,"Make"]=temp[0]
            df.at[i,"Model"]=" ".join(temp[1: ])

#check airbags
for i in range(len(df)):
    text=df.loc[i,"Airbags"]
    try:
        df.at[i,"Airbags"]=int(len(text.split(',')))
    except:
        df.at[i,"Airbags"]=0

#convert Power
for i in range(len(df)):

    power=df.loc[i,"Power"]

    if(type(power)!=int):
        powersplit=power.split('@')
        
        #check rpm
        try:
            rpm=powersplit[1].lower()
        except:
            df.at[i,"Power"]=0
            continue

        rpm=int((rpm.replace("rpm","")).split('-')[0])

        #check energy delivered
        energy=powersplit[0].lower()
        if "ps" in energy:
            eng=float(energy.replace("ps",""))
            eng=(eng/rpm)*1000
            df.at[i,"Power"]=eng
        else:
            if "bhp" in energy:
                bhp_eng=float(energy.replace("bhp",""))
                ps_eng=float(bhp_eng*1.0137)
                ps_eng=(ps_eng/rpm)*1000
                df.at[i,"Power"]=ps_eng
                
            elif "hp" in energy:
                hp_eng=float(energy.replace("hp",""))
                ps_eng=float(hp_eng*1.014*0.99)
                ps_eng=(ps_eng/rpm)*1000
                df.at[i,"Power"]=ps_eng
            else:
                df.at[i,"Power"]=0

        # print("Power at 1000rpm for",df.loc[i,"Make"],"-",df.loc[i,"Model"],": ",df.loc[i,"Power"])      
    else:
        df.at[i,"Power"]=0

#check torque
for i in range(len(df)):

    torque=df.loc[i,"Torque"]

    if(type(torque)!=int):
      
        #check rpm
        try:
            powersplit=torque.split('@')
            rpm=powersplit[1].lower()
        except:
            df.at[i,"Torque"]=0
            continue

        rpm=int((rpm.replace("rpm","")).split('-')[0])

        #check torque delivered
        trq=powersplit[0].lower()

        if "nm" in trq:
            eng=float(trq.replace("nm",""))
            eng=(eng/rpm)*1000
            df.at[i,"Torque"]=eng
            # print("Direct from NM")
        else:
            if "kgm" in trq:
                kgm_eng=float(trq.replace("kgm",""))
                nm_eng=float(kgm_eng*9.806)
                nm_eng=(nm_eng/rpm)*1000
                df.at[i,"Torque"]=nm_eng
                # print("Converted KGM")
            else:
                df.at[i,"Torque"]=0

        # print("Torque generated at 1000rpm for",df.loc[i,"Make"],"-",df.loc[i,"Model"],": ",df.loc[i,"Torque"])


       
    else:
        df.at[i,"Torque"]=0

# replace null values
df = df.astype({"Power": float,"Airbags": float,"Torque":float})
for col in df.columns:
    if(col=="Power"):
        for i in range(len(df)):
            if(pd.isnull(df.loc[i,col])or df.loc[i,col]==0):
                df.at[i,col]=df[col].mean()
    elif(df.dtypes[col]==float):
        for i in range(len(df)):
            if(pd.isnull(df.loc[i,col]) or df.loc[i,col]==0):
                df.at[i,col]=df.mode()[col][0]
    else:
        for i in range(len(df)):
            if(pd.isnull(df.loc[i,col])):
                df.at[i,col]=df.mode()[col][0]

        

#check total null values in the file
print(df.isnull().sum(axis = 0))
#import as CSV
df.to_csv("cleanedagain6.csv")


