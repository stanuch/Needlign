# Enter, read and save DNA Sequence 1

seq1_filename = input("Enter the name of sequence 1 file (without file format): ")

with open(f"../sequences/{seq1_filename}.txt") as seq1:
    sequence1 = seq1.read()


# Enter, read and save DNA Sequence 2

seq2_filename = input("Enter the name of sequence 2 file (without file format): ")

with open(f"../sequences/{seq2_filename}.txt") as seq2:
    sequence2 = seq2.read()
