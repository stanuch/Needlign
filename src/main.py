import os
from fasta_read import read_fasta
from Bio import SeqIO

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, "..", "sequences") # fasta files path
    return os.path.join(seq_dir, f"{filename}.fasta")

def print_sequences(file_path, label):
    print(f"{label}:")
    for record in SeqIO.parse(file_path, "fasta"):
        print(f"ID: {record.id}")
        print(f"Seqence: {record.seq}\n")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq1_filename = input("Enter the name of sequence 1 file (without extension): ")
    seq2_filename = input("Enter the name of sequence 2 file (without extension): ")
    print("")

    seq1_path = get_file_path(base_dir, seq1_filename)
    seq2_path = get_file_path(base_dir, seq2_filename)

    print_sequences(seq1_path, seq1_filename)
    print_sequences(seq2_path, seq2_filename)

if __name__ == "__main__":
    main()
