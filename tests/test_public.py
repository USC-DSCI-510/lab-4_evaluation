from collections import defaultdict

import pytest

from lab4 import file_extension, generate_frequency_map, palindrome_finder


# pytest cases
@pytest.mark.parametrize(
    "base_filename, freq_map",
    [
        ("numbers_1.txt", [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]),
        ("numbers_2.txt", [4, 7, 10, 9, 10, 7, 7, 2, 3, 0]),
        ("numbers_3.txt", [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),
        ("numbers_4.txt", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ],
)
@pytest.mark.timeout(0.2)
def test_generate_frequency_map(base_filename, freq_map):
    assert generate_frequency_map(base_filename) == freq_map


@pytest.mark.timeout(0.1)
def test_generate_frequency_map_exception():
    with pytest.raises(Exception):
        generate_frequency_map("numbers_100.txt")


@pytest.mark.parametrize(
    "base_filename, result",
    [
        (
            "sentences_1.txt",
            [
                "radar",
                "anna,kayak",
                "civic",
                "level",
                "did,deed",
                "hannah",
                "dad",
                "madam",
                "racecar",
                "",
                "rotator",
            ],
        ),
        (
            "sentences_2.txt",
            ["racecar", "", "did", "radar", "level", "refer"],
        ),
        (
            "sentences_3.txt",
            ["deified", "kayak", "redivider", "noon", "madam", "civic"],
        ),
        ("sentences_4.txt", []),
    ],
)
@pytest.mark.timeout(0.2)
def test_palindrome_finder(base_filename, result):
    palindrome_finder(base_filename)
    with open("palindrome_" + base_filename, "r") as f:
        lines = f.readlines()
    lines_s = []
    for line in lines:
        lines_s.append(line.strip())
    assert lines_s == result


@pytest.mark.timeout(0.1)
def test_palindrome_finder_exception():
    with pytest.raises(Exception):
        palindrome_finder("sentences_5.txt")


@pytest.mark.parametrize(
    "base_filename, result",
    [
        (
            "extensions_1.txt",
            {
                "txt": ["first.txt", "second.txt", "third.txt"],
                "doc": ["first.doc", "second.doc", "third.doc"],
                "pdf": ["first.pdf", "second.pdf", "third.pdf"],
            },
        ),
        (
            "extensions_2.txt",
            {
                "txt": ["first.txt"],
                "doc": ["first.doc"],
                "pdf": ["first.pdf", "second.pdf"],
            },
        ),
        (
            "extensions_3.txt",
            {
                "txt": ["second.txt", "third.txt", "first.txt"],
                "doc": ["first.doc", "third.doc", "second.doc"],
                "pdf": ["first.pdf", "second.pdf"],
            },
        ),
        ("extensions_4.txt", {"pdf": [], "doc": [], "txt": []}),
    ],
)
@pytest.mark.timeout(0.2)
def test_file_extension(base_filename, result):
    file_extension(base_filename)
    extensions = ["txt", "doc", "pdf"]
    resDir = defaultdict(list)

    for ext in extensions:
        with open(ext + "_" + base_filename, "r") as f:
            lines = f.readlines()
        lines_s = []
        for line in lines:
            lines_s.append(line.strip())
        resDir[ext] = lines_s
    assert resDir == result


@pytest.mark.timeout(0.1)
def test_file_extension_exception():
    with pytest.raises(Exception):
        file_extension("extensions_5.txt")
