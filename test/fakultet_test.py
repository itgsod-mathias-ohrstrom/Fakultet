#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')

from fakultet import fakultet




@raises(TypeError)
def test_fakultet_takes_a_tal_as_argument():
    fakultet()


def test_fakultet_5_should_give_120():

    assert_equal(fakultet(5), 120)

def test_fakultet_12_should_give_479001600():

    assert_equal(fakultet(12), 479001600)

def test_fakultet_0_should_give_1():

    assert_equal(fakultet(12), 479001600)