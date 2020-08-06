# input ที่เข้ามาหาร 3 ลงตัว ให้ return คำว่า fizz
# input ที่เข้ามาหาร 5 ลงตัว ให้ return คำว่า buzz
# input ที่เข้ามาหาร 3 ลงตัวและ 5 ลงตัว ให้ return คำว่า fizzbuzz
# ถ้าไม่ตรงเลขนั้นๆเลย ให้ return ค่านั้นๆ

#def fizzbuzz(number):
#    if number == 3:
#        return 'Fizz'
#print(fizzbuzz(3))

import unittest


def fizzbuzz(number):
    if number == 1:
    pass
    return 1


class TestFizzBuzz(unittest.TestCase):

    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

def test_input_3_should_get_1(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')

#unittest.main()