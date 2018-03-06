from distutils.core import setup

setup(
    name='miaozhen',
    version='v2.0.1',
    packages=['libs', 'libs.db', 'libs.files', 'libs.flash', 'libs.qiniu', 'libs.flinks', 'libs.pycket', 'libs.account',
              'libs.contact', 'libs.setting', 'libs.articles', 'libs.redis_conn', 'files', 'files.image', 'utils',
              'models', 'models.accounts', 'models.Blog_model', 'models.flink_model', 'models.article_model',
              'models.contact_model', 'models.setting_model', 'static', 'static.admin', 'handlers', 'handlers.base',
              'handlers.main', 'handlers.Front', 'handlers.Front.blog', 'handlers.Front.about',
              'handlers.Front.contact', 'handlers.Front.blog_view', 'handlers.Front.project_view',
              'handlers.Admin_modules', 'handlers.Admin_modules.admin', 'handlers.Admin_modules.files',
              'handlers.Admin_modules.account', 'handlers.Admin_modules.admin_flinks',
              'handlers.Admin_modules.admin_notice', 'handlers.Admin_modules.admin_contact',
              'handlers.Admin_modules.admin_setting', 'handlers.Admin_modules.admin_articles',
              'handlers.Admin_modules.admin_category', 'handlers.Admin_modules.admin_commit_manage', 'templates',
              'templates.Admin', 'templates.Admin.admin_base', 'templates.Front'],
    url='http://www.miaozhen360.com',
    license='MIT',
    author='yanzongzhen',
    author_email='yanzongzhen127@outlook.com',
    description='IoT'
)
