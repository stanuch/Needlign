# in tests/test_main.py
from src.main import similarity_percentage

def test_similarity_100_percent():
    long_seq = "ABCGACTDEF"
    short_seq = "GACT"
    assert similarity_percentage(long_seq, short_seq) == 100
    assert similarity_percentage(short_seq, long_seq) == 100

def test_similarity_no_match():
    # Test your original example that had 0%
    seq1 = "GACTGACT"
    seq2 = "ACTGACTG"
    assert similarity_percentage(seq1, seq2) == 0

def test_similarity_partial_match():
    seq1 = "SABCDEFGHI"
    seq2 = "XBCDEY" 
    assert similarity_percentage(seq1, seq2) == (4/6) * 100

def test_similarity_empty_string():
    seq1 = "ABC"
    seq2 = ""
    assert similarity_percentage(seq1, seq2) == 0.0