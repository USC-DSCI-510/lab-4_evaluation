from collections import defaultdict

import pytest

from lab4 import file_extension, generate_frequency_map, palindrome_finder


# pytest cases
@pytest.mark.parametrize(
    "base_filename, freq_map",
    [
        ("numbers_test_1.txt", [8, 7, 7, 7, 6, 6, 6, 6, 7, 8]),
        ("numbers_test_2.txt", [4, 3, 0, 1, 3, 4, 3, 0, 2, 0]),
        ("numbers_test_3.txt", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ("numbers_test_4.txt", [32, 26, 14, 18, 24, 28, 24, 12, 22, 16]),
        ("numbers_test_large_1.txt", [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]),
        ("numbers_test_large_2.txt", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ],
)
@pytest.mark.timeout(0.3)
def test_generate_frequency_map(base_filename, freq_map):
    assert generate_frequency_map(base_filename) == freq_map


@pytest.mark.timeout(0.1)
def test_generate_frequency_map_exception():
    with pytest.raises(Exception):
        generate_frequency_map("numbers_test_5.txt")


@pytest.mark.parametrize(
    "base_filename, result",
    [
        (
            "sentences_test_1.txt",
            ["did,kayak", "refer", "racecar", "", "hannah"],
        ),
        (
            "sentences_test_2.txt",
            ["", "", "", "", ""],
        ),
        (
            "sentences_test_3.txt",
            ["deified,noon", "dad,elle", "repaper", "", ""],
        ),
        ("sentences_test_4.txt", ["", "", "radar", "", ""]),
        ("sentences_test_67.txt", ["", "", "madaminedenimadam"]),
    ],
)
@pytest.mark.timeout(0.25)
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
        palindrome_finder("sentences_test_5.txt")


@pytest.mark.parametrize(
    "base_filename, result",
    [
        (
            "extensions_test_1.txt",
            {
                "txt": ["Shopping_List.txt", "Poetry_Collection.txt", "Recipe_Book.txt"],
                "doc": ["Project_Proposal.doc", "Resume_Template.doc", "Meeting_Minutes.doc"],
                "pdf": ["Report_Summary.pdf", "Vacation_Plan.pdf", "Budget_Spreadsheet.pdf"],
            },
        ),
        (
            "extensions_test_2.txt",
            {
                "txt": [],
                "doc": ["Presentation_Slides.doc", "Job_Application.doc", "Newsletter.doc"],
                "pdf": ["Business_Plan.pdf", "Research_Paper.pdf", "Travel_Itinerary.pdf"],
            },
        ),
        (
            "extensions_test_3.txt",
            {
                "txt": [
                    "Important_Notes.txt",
                    "Personal_Journal.txt",
                    "User_Manual.txt",
                    "Contact_List.txt",
                ],
                "doc": [],
                "pdf": [],
            },
        ),
        ("extensions_test_4.txt", {"pdf": [], "doc": [], "txt": []}),
        ("extensions_test_11.txt", {"pdf": [], "doc": [], "txt": []}),
        # (
        #     "extensions_test_12.txt",
        #     {"pdf": ["file2.PDF"], "doc": ["lab4.DOC"], "txt": ["file1.TXT"]},
        # ),
        (
            "extensions_test_13.txt",
            {
                "pdf": [".hidden_config.pdf"],
                "doc": ["polish-the-time.doc"],
                "txt": [".config.txt", "very_long_file_name_is_very_long.txt"],
            },
        ),
        (
            "extensions_test_15.txt",
            {"txt": ["file 3.txt"], "doc": ["file 1.doc"], "pdf": ["file 2.pdf"]},
        ),
    ],
)
@pytest.mark.timeout(0.25)
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
        file_extension("extensions_test_5.txt")
