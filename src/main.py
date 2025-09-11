import os
from fasta_read import read_fasta
from needle import needleman_wunsch
from Bio import SeqIO

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, "..", "sequences") # fasta files path
    return os.path.join(seq_dir, f"{filename}.fasta")

def print_sequences(file_path, label):
    print(f"{label}:")
    for record in SeqIO.parse(file_path, "fasta"):
        print(f"ID: {record.id}")
        print(f"Seqence: {record.seq}\n")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq1_filename = input("Enter the name of sequence 1 file (without extension): ")
    seq2_filename = input("Enter the name of sequence 2 file (without extension): ")
    print("")

    seq1_path = get_file_path(base_dir, seq1_filename)
    seq2_path = get_file_path(base_dir, seq2_filename)

    sequences = []
    sequences.append(read_fasta(seq1_path))
    sequences.append(read_fasta(seq2_path))

    aligned1, aligned2, score = needleman_wunsch(sequences[0], sequences[1], matrix_name="BLOSUM62", gap_open=-10, gap_extend=-0.5)

    print("\nAlignment:")
    print(aligned1)
    print(aligned2)
    print(f"\nAlignment score: {score}")

if __name__ == "__main__":
    main()
