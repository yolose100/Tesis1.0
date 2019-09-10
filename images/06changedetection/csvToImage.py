 #!/usr/bin/python
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.signal as signal 
import sys, getopt
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 

def hacerGrafica( direc):
    
    data = pd.read_csv(direc) 


    lista1 = data.iloc[:,2] 
    
    y = signal.savgol_filter(lista1, 25, 4)
      # Declara lista1 con 8 valores
    #plt.plot(lista1)   # Dibuja el gráfico
 #   plt.plot(lista1)
    plt.plot(y)   # Dibuja el gráfico
    plt.title("IoU - Epoca")   # Establece el título del gráfico
    plt.xlabel("Epoca")   # Establece el título del eje x
    plt.ylabel("IoU")   # Establece el título del eje y
    direcGuardado = direc[:-4]
    direcGuardado = direcGuardado+".png"
    plt.savefig(direcGuardado)    

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
    #  print 'test.py -i <inputfile> -o <outputfile>'
      
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    hacerGrafica(inputfile)
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
