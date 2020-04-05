# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import *
from functions import *
import main
import unittest

class MainTest(unittest.TestCase):
    
    def setUp(self):
        self.app = main.app.test_client()

    def test_BMI_UW(self):
        feet = 5
        inches = 5
        weight = 100
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Underweight"

    def test_BMI_UW_Edge(self):
        feet = 5
        inches = 5
        weight = 108
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Underweight"

    def test_BMI_N(self):
        feet = 5
        inches = 5
        weight = 120
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Normal"

    def test_BMI_N_Edge(self):
        feet = 5
        inches = 5
        weight = 109
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Normal"

    def test_BMI_OW(self):
        feet = 5
        inches = 5
        weight = 160
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Overweight"

    def test_BMI_OW_Edge(self):
        feet = 5
        inches = 5
        weight = 170
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Overweight"

    def test_BMI_O(self):
        feet = 5
        inches = 5
        weight = 180
        bmi, category = calc_BMI(feet, inches, weight)
        assert category == "Obese"

    def test_RA_RetireAt70(self):
        age = 20
        salary = 100000
        savings = 15
        goal = 1000000
        message = calc_RA(age, salary, savings, goal)
        assert message == "You will meet your savings goal at 70"

    def test_RA_DieBeforeRetire(self):
        age = 40
        salary = 90000
        savings = 10
        goal = 1250000
        message = calc_RA(age, salary, savings, goal)
        assert message == "You will die before meeting your savings goal..."

    def test_RA_RetireEdge(self):
        age = 50
        salary = 100000
        savings = 20
        goal = 1250000
        message = calc_RA(age, salary, savings, goal)
        assert message == "You will meet your savings goal at 97"

    


if __name__ == '__main__':
    unittest.main()


