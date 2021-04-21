from colorama import init, Fore, Back, Style

# Reset terminal colors after every print statement
init(autoreset=True)

class LogLevel:
  DEBUG = 0
  INFO = 1
  WARN = 2
  ERROR = 3

class log:
  LOG_LEVEL = LogLevel.DEBUG

  @classmethod
  def level(cls, level):
    if type(level) == str:
      l = LogLevel.DEBUG
      if level == 'info':
        l = LogLevel.INFO
      elif level == 'warn':
        l = LogLevel.WARN
      elif level == 'error':
        l = LogLevel.ERROR
      cls.LOG_LEVEL = l
    elif type(level) == int:
      cls.LOG_LEVEL = level

  @classmethod
  def success(cls, message: str):
    print(f'{Fore.GREEN}{Style.BRIGHT}{message}')

  @classmethod
  def debug(cls, message: str):
    if cls.LOG_LEVEL == 0:
      print(f'{Fore.BLUE}{message}')

  @classmethod
  def info(cls, message: str):
    if cls.LOG_LEVEL <= 1:
      print(f'{Fore.CYAN}{message}')

  @classmethod
  def warn(cls, message: str):
    if cls.LOG_LEVEL <= 2:
      print(f'{Fore.YELLOW}{message}')

  @classmethod
  def error(cls, message: str):
    if cls.LOG_LEVEL <= 3:
      print(f'{Fore.RED}{Style.BRIGHT}{message}')