#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini

import pytest
import yaml


#加法用例类
from Calculator.cacl import Cacl


class Test_cacl:
	#获取用例数据
	data = yaml.safe_load(open(r'F:\untitled1\testing\Advanced\cacl_data.yaml','rb'))
	def setup_class(self):
		self.cacl1 = Cacl()

	#参数化
	@pytest.mark.parametrize('a,b,c',data['add'],ids = data['addid'])
	#加法用例方法1
	def test_add_1(self,a,b,c):
		sum = self.cacl1.add(a,b)
		assert sum == c

	@pytest.mark.parametrize('a,b,c', data['add'],ids = data['addid'])
	#加法用例方法2
	def test_add_2(self,a,b,c):
		sum = self.cacl1.add(b,a)
		assert sum == c

	@pytest.mark.parametrize('a,b,c', data['div'], ids = data['divid'])
	def test_div(self,a,b,c):
		sum = self.cacl1.div(a,b)
		assert sum == c


