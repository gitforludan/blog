from . import views
from django.urls import path, include
# 设置首页的URL地址信息
urlpatterns = [
    path('post_new', views.NewVisew, name='new'),  # 新建文章
    path(
        'post_eidtor/<int:post_id>',
        views.EidtorVisew,
        name='eidtor'),
    # 编辑文章
    path('UploadFile', views.UploadFileView, name='Upload_file'),  # 上传文件
]

urlpatterns += [
    path('chat_free', views.chatfreeView, name='chat_free'),  # 菲菲聊天机器人
    path('chat_xiaoi', views.chatxiaoiView, name='chat_xiaoi'),  # 小艾聊天机器人
    path('chat_dandan', views.chatdandanView, name='chat_dandan'),  # 小艾聊天机器人
    path('ajax_chat/', include([
        path(
            'free',
            views.ajax_chat_free,
            name='ajax_chat_free'),
        # 菲菲聊天ajax接口
        path(
            'xiaoi',
            views.ajax_chat_xiaoi,
            name='ajax_chat_xiaoi'),
        # 小艾聊天ajax接口
        path(
            'dandan',
            views.ajax_chat_dandan,
            name='ajax_chat_dandan'),
        # 蛋蛋聊天ajax接口
    ])),  # 二级路由
    path('music', views.musicView, name='music'),  # 音乐解析
    path('video', views.videoView, name='video_vip'),  # 视频解析
    path(
        'images',
        views.ImageCompressionView,
        name="ImageCompression"),
    # 图片压缩
]
