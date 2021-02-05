#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import pytest
import yaml

from Calculator.cacl import Cacl

@pytest.fixture(scope="module")
def frist_cla(request):
	print("开始计算")
	caclplus = Cacl()
	yield caclplus
	print("计算结束")

# @pytest.fixture(params=data['add'],ids=data['addid'])
