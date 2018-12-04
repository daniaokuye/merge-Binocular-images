# ImageRegistration
将可见光和近红外融合在一起，对融合图像取关键点，这样两个
数据源共享一套检测点。
同时，还将关键点、框映射回原图像，继而可再分别截取图像。
像素差是少不了的，但是相比之前的像素差可以忽略
### 使用说明：
- 主函数：image_registration.py
### 代码说明（image_registration.py）：
- Line68:返回的是融合的图像，是source图融合到target上，
坐标体系是target为目标的
- Line71-75：是试验Images中27号图片，target所得到的关键
点和回归框映射回source上，具体代码可参见Line74中代码
### 变量或返回值的说明：
- 融合图：融合是为了让两幅图共享同一套关键点和回归框
- 参考系：坐标的参考系是以target图为准
- 融合方式：我这儿提供了两种，一种是均值融合；另一种是先
分别取根号，相加，再乘8，结果取值范围还是[0-255]
- 融合方式的代码：align_transform.py中的line184-185
### 相片说明（文件夹Images）
- merge.jpg:是融合后图片
- 27_vis.bmpwarp.jpg是效果图
- 试验是以nir为target，vis为source。实际中无先后顺序，
使用代码时前后照应即可
#### 参考
- 参考[链接](https://github.com/quqixun/ImageRegistration)
- [cv2 errors refers](https://blog.csdn.net/weixin_43167047/article/details/82841750)