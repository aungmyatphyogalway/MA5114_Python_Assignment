import os # set up directory variables
seq_dir ='/home/localuser/Desktop/thesis/test_dataset'
fastqc_dir ='/home/localuser/Desktop/thesis/fastqc_d'


file_list = os.listdir(seq_dir)
print ('# got list of files in: ' + seq_dir)


for seq in file_list:
    command = 'fastqc ' + seq_dir + '/' + seq 
    print(command)
    os.system(command)
    
    
command1 = 'mv ' + seq_dir + '/' + '*.html ' + fastqc_dir
print (command1)
os.system(command1)


print ('#done')       
