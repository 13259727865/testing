#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import yaml


class Cacl:
	#加法
	def add(self,a,b):
		if isinstance(a,int) or isinstance(a,float):
			if isinstance(b,int) or isinstance(b,float):
				if a >= -100 and a <= 100:
					if b >= -100 and b <= 100:
						return a + b
					elif b < -100 or b > 100:
						return "请填写-100——100数字"
				elif a < -100 or a > 100:
					return "请填写-100——100数字"
			else:
				return "请填写数字"
		else:
			return "请填写数字"



	#减法
	def sub(self,a,b):
		if isinstance(a,int) or isinstance(a,float):
			if isinstance(b,int) or isinstance(b,float):
				if a >= -100 and a <= 100:
					if b >= -100 and b <= 100:
						return a - b
					elif b < -100 or b > 100:
						return "请填写-100——100数字"
				elif a < -100 or a > 100:
					return "请填写-100——100数字"
			else:
				return "请填写数字"
		else:
			return "请填写数字"


	#乘法
	def mul(self,a,b):
		if isinstance(a,int) or isinstance(a,float):
			if isinstance(b,int) or isinstance(b,float):
				if a >= -100 and a <= 100:
					if b >= -100 and b <= 100:
						return a * b
					elif b < -100 or b > 100:
						return "请填写-100——100数字"
				elif a < -100 or a > 100:
					return "请填写-100——100数字"
			else:
				return "请填写数字"
		else:
			return "请填写数字"

	#除法
	def div(self,a,b):
		if isinstance(a,int) or isinstance(a,float):
			if isinstance(b,int) or isinstance(b,float):
				if b ==0:
					return "除数不能为0"
				elif a >= -100 and a <= 100:
					if b >= -100 and b <= 100:
						return a / b
					elif b < -100 or b > 100:
						return "请填写-100——100数字"
				elif a < -100 or a > 100:
					return "请填写-100——100数字"
			else:
				return "请填写数字"
		else:
			return "请填写数字"


a = yaml.safe_load(open(r'F:\untitled1\testing\Advanced\cacl_data.yaml','rb'))
print(a)

print(-100 / -4)
