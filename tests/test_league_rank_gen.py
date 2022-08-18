from unittest import TestCase
import subprocess as sb
from deepdiff import DeepDiff


class LeagueRankGenerationTest(TestCase):


    def test_sample(self):

        commands = [
            "python3 main.py -f ./tests/test_data/input_1.txt"
        ]
        process = sb.Popen(commands,stderr=sb.PIPE,stdout=sb.PIPE,shell=True)
        output, _ = process.communicate()

        with open("tests/test_data/out_1.txt") as file:
            expected = file.read()

        assert not DeepDiff(t1=output.decode("utf-8").strip("\n"), t2=expected).to_dict()

    def test_epl_201819(self):

        commands = [
            "python3 main.py -f ./tests/test_data/input_2.txt"
        ]
        process = sb.Popen(commands,stderr=sb.PIPE,stdout=sb.PIPE,shell=True)
        output, _ = process.communicate()

        with open("tests/test_data/out_2.txt") as file:
            expected = file.read()

        assert not DeepDiff(t1=output.decode("utf-8").strip("\n"), t2=expected).to_dict()