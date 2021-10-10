
class Logger:
    class __Logger:
        def __init__(self, filename):
            self.filename = filename
        def __str__(self):
            return '{0!r} {1}'.format(self, self.filename)

        def _write(self, level, msg):
            with open(self.filename, 'a') as log_file:
                log_file.write('[{0}] {1}\n'.format(level, msg))

        def critical(self, msg):
            self._write('CRITICAL', msg)

        def error(self, msg):
            self._write('ERROR', msg)

        def warn(self, msg):
            self._write('WARN', msg)

        def debug(self, msg):
            self._write('DEBUG', msg)

    instance = None

    def __new__(cls, filename):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(filename)
        return Logger.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

if __name__ == '__main__':
    log1 = Logger('test.txt')
    log1.debug("hello scy")
    print(log1)

    log2 = Logger('test.txt')
    print(log1)
    print(log2)
    log2.debug("TNP scy")
