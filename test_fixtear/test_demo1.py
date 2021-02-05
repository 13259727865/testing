#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import pytest


@pytest.fixture(params=[(1,2,3),(4,5,6)],ids=[1,2])
def login(request):
	print("登录。。")
	yield request.param
	print('断开')



@pytest.mark.driver1
@pytest.mark.vehicle1

class TestDemo1:
	@pytest.mark.usefixtures('login')
	def test_vehicle(self,login):
		print(login[0])
		print(login[1])
		print(login[2])

		print('车辆id')

	def test_driver(self):
		print(login)
		print('司机id')



class TestDemo2:

	def test_vehicle(self):
		# print(login)
		print('车辆id')

	def test_driver(self):
		print('司机id')


