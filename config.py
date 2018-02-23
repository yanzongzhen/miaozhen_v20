#coding:utf-8

settings = dict(
    template_path = 'templates',
    static_path = 'static',
    debug = True,
    cookie_secret = 'test_mima_shishenme',
    pycket={
        'engine': 'redis',  # 设置存储器类型
        'storage': {
            'host': 'localhost',
            'port': 6379,
            'db_sessions': 6,
            'db_notifications': 11,
            'max_connections': 2 ** 31,
        },
        'cookies': {
            'expires_days': 30,  # 设置过期时间
        },
    },

)