#ecoding=utf-8
# author:herui
# time:2020/8/25 15:40
# function:测试order调整用例执行顺序

import pytest

@pytest.mark.run(order=3)
def test_01():
    print('test01')

@pytest.mark.run(order=1)
def test_02():
    print('test01')

@pytest.mark.run(order=2)
def test_06():
    print('test01')
