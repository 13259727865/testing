#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
from time import sleep

import pytest
import yaml


#获取用例数据
data = yaml.safe_load(open(r"F:\untitled1\testing\Advanced\cacl_data.yaml",'rb'))

#定义各用例数据变量
add_params,add_id = data['params']['add'],data['id']['addid']
sub_params,sub_id = data['params']['sub'],data['id']['subid']
mul_params,mul_id = data['params']['mul'],data['id']['mulid']
div_params,div_id = data['params']['div'],data['id']['divid']

#通过fixture参数化给加法测试
@pytest.fixture(params=add_params,ids=add_id)
def add_data(request):
	print("数据导入")
	yield request.param

#使用config.py的fixture初始化
@pytest.mark.usefixtures("frist_cla")
class TestCaclPlus:
	@pytest.mark.run(order = 1)
	@pytest.mark.usefixtures("add_data")
	#加法测试用例-使用fixture参数化
	def test_add(self,frist_cla,add_data):
		sum = frist_cla.add(add_data[0],add_data[1])
		# sleep(0.5)
		assert sum == add_data[2]



	#除法测试用例-使用parametrize参数化
	@pytest.mark.parametrize("a,b,c",div_params,ids = div_id)
	def test_div(self,frist_cla,a,b,c):
		sum = frist_cla.div(a,b)
		assert sum == c


	@pytest.mark.run(order= 2)
	#减法测试用例-使用parametrize参数化
	@pytest.mark.parametrize("a,b,c",sub_params,ids = sub_id)
	def test_sub(self,frist_cla,a,b,c):
		sum = frist_cla.sub(a,b)
		assert sum == c

	@pytest.mark.run(order=3)
	# 乘法测试用例-使用parametrize参数化
	@pytest.mark.parametrize('a,b,c',mul_params,ids = mul_id)
	def test_mul(self,frist_cla,a,b,c):
		sum = frist_cla.mul(a,b)
		assert sum == c