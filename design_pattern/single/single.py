# 单例模式

# 单例模式来初始化日志记录器

class Logger:
    _Instance = None
    def __new__(cls, *args, **kwargs):
        if cls._Instance is None:
           cls._Instance = super(Logger,cls).__new__(cls)
        else:
            return cls._Instance
        cls._Instance.log_file = 'log.text'
        return cls._Instance

    def set_log_config(cls,level,format):
        cls._Instance.log_config['level'] = level
        cls._Instance.log_config['format'] = format
    def log(cls,message):
        with  open(cls._Instance.log_file,'a') as f:
            f.write(message)


def main():
    pass

if __name__ == '__main__':
    main()




















