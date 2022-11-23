import os
# set up directory variables
seq_dir = 'test_dataset'
fastqc_dir = 'trimmed_out'
# create output directory
isExist = os.path.exists(fastqc_dir)
if not isExist:
	os.mkdir(fastqc_dir)
print('created subdir: ' + fastqc_dir)
# get list of FASTQ files
test_datset = os.listdir(seq_dir)
print('got list of files in: ' + seq_dir)
# create the command string for each sequence
# & implement it
for seq in test_datset:
	output_name= " trimmed_out/out_trim"+seq
	input_name= " test_dataset/" + seq
	command = 'trimmomatic SE' + input_name + output_name + " ILLUMINACLIP:TruSeq3-SE:2:30:10"
	print(command)
	os.system(command)
# mv html & zip files out of sequence directory
# into FASTQC directory

print('done')
