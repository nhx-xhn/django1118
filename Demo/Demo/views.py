from django.http import HttpResponse
import time

# def index1(request):
#     """
#     视图：作用
#     :param request:  形参 包含请求信息的请求对象
#     :return:  HttpResponse 响应对象
#     """
#     te=time.time()
#     ret=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#     return HttpResponse(ret)
#
# def about1(request):
#     return HttpResponse("我是about页面")
#
# def retest(request,id):
#     print(id)
#     return HttpResponse("retest视图")
#
# def testdemo(request,city,year):
#     rul="我%s年在%s"%(year,city)
#     return HttpResponse(rul)
# from django.template import Template,Context
# def indexhtml(request,age):
#     """
#
#     :param request:
#     :return:
#     """
#     html="""
#     <html>
#         <head></head>
#         <body>
#             <h1>我是index页面</h1>
#             <img src="https://i01piccdn.sogoucdn.com/820aa01431b8be1c">
#         </body>
#         姓名:{{name}}
#         年龄:{{age}}
#     </html>
#      """
#     ## 返回响应对象
#     # return HttpResponse(html)
#     ## 渲染动态数据
#     #1创建模板
#     template_obj=Template(html)
#     #2构建动态数据
#     parmas={"name":"古天乐","age":age}  ##字典
#     content_obj=Context(parmas)
#     #3构建动态页面  将动态数据渲染到静态页面
#     result=template_obj.render(content_obj)
#     return HttpResponse(result)
#
#
#
# ###调用模板
# from django.template.loader import get_template
# def getindex1(request):
#     ##第一种方式
#     ##返回templates中的index.htmel 页面
#     ##创建一个模板对象
#     template_obj=get_template("index.html")
#     ##创建返回对象
#     ##完成动态数据的渲染
#     params={"name":"houxian","age":21}
#     result=template_obj.render(params)
#     return HttpResponse(result)
#
#
# from django.shortcuts import render_to_response
# def getindex2(request):
#     ##第二种调用方法
#     ##返回index页面
#     ##返回动态数据
#     params={"name":'jinxinyan',"age":22}
#     #render_to_response(要返回的页面，动态数据)
#     return render_to_response("index.html",params)
#
#
# from django.shortcuts import render
# def getindex(request):
#     ##第三种
#     ##返回的是index.html
#     ##渲染的数据  name  age
#     ##render(request,要返回的页面，动态数据)
#     params={"name":'liuruxia',"age":20}
#     return render(request,'index.html',params)
#
#
#
# ##模板语法
#
# def templatest(request):
#     name="zhengfei"
#     age=21
#     hobby=["唱歌","跳舞","学习"]
#     score={"asdg":123,"etgx":345}
#     ##返回数据的方式
#     #第一种
#     # return render_to_response("templatest.html",{"name":name,"age":age,"hobby":hobby})
#     #第二种
#     # params={"name":"aklgd","age":age}
#     # return render(request,"index.html",params)
#     #第三种
#     #locals()  会将所有变量作为字典返回
#     return render_to_response("templatest.html",locals())
#
# import datetime
#
# myjs="""
#     <script>
#     alert('myjs'):
#     </script>
#     """
#
#
# from django.shortcuts import render
# def about(request):
#     return render(request,'about.html')
#
#
# def index(request):
#     return render(request,'index.html')
#
#
# def listpic(request):
#     return render(request,'listpic.html')
#
#
# from django.shortcuts import render
# def newslistpic1(request):
#     return render_to_response(request,'newslistpic.html')
#
# def base(request):
#     return render_to_response("base.html")
#
#
# def demo01(request):
#     return render_to_response("demo01.html")

