from datetime import datetime
from django.db import models

# 1. 设计表结构有几个重要的点
"""
实体1 <关系> 实体2
课程 章节 视频 课程资源
"""
# 2. 实体的具体字段

# 3. 每个字段的类型，是否必填


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 表示不生成表到数据库
        abstract = True


class Device(BaseModel):
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    # degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    # fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    sn = models.CharField(verbose_name="设备编号", max_length=50)
    type = models.CharField(verbose_name="设备类型", max_length=300)
    desc = models.CharField(verbose_name="设备描述", max_length=300)
    detail = models.TextField(verbose_name="设备详情")
    online_times = models.IntegerField(default=0, verbose_name="在线时长(分钟数)")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)
    is_online = models.BooleanField(default=False, verbose_name="是否在线")

    class Meta:
        # 表的名称
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

