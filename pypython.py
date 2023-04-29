import ast
import os
import sys


print('pypython 1.2 Welcome to pypython 1.2    2023.4.14  18:58')
print('Type "help", "copyright", "credits" or "license()" for more information.')
print('脚本编写:朱浩宇')

def pyt():
    while True:
        try:
            def copyright():
                print('由朱浩宇开发并维护，包括但不限于使用权，复制、修改、合并、发布、分发、再授权或出售软件的副本')
                input('按Enter键返回:')
            def credits():
                print('pypython由朱浩宇维护')
            def hp():
                print('帮组:\npypython() 获取pypython版本\nai() AI\nhp() 帮组')
            def pypython():
                print('pypython 1.1')
            def ai():
                import requests
                print('按 q 停止,请确保连网')
                print('请输入你想说的：')
                while True:
                    a = input('>>>|')
                    if a == 'q':
                        pyt()
                        print('已关闭ai')
                    elif a == '你好':
                        print('你好')
                    elif a == 'hello':
                        print("hello")
                    elif a == '你叫什么':
                        print('我叫pyAI')
                    elif a == '作者':
                        print('朱浩宇')
                    elif a == 'hello':
                            print("hello")
                    elif a == '你叫什么':
                            print('我叫pyAI')
                    elif a == '今天星期几':
                            print('作为一个人工智能，我无法获取现实世界的时间。')
                    elif a == 'hello world':
                            print('你好世界')
                    elif a == 'python':
                            print('Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆于1990年代初设计，作为一门叫做ABC语言的替代品。\nPython提供了高效的高级数据结构，还能简单有效地面向对象编程。\nPython语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的编程语言，随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、大型项目的开发。\nPython解释器易于扩展，可以使用C语言或C++（或者其他可以通过C调用的语言）扩展新的功能和数据类型。 \nPython也可用于可定制化软件中的扩展程序语言。Python丰富的标准库，提供了适用于各个主要系统平台的源码或机器码。')
                    elif a == 'c':
                            print('C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。\nC语言能以简易的方式编译、处理低级存储器。\nC语言是仅产生少量的机器语言以及不需要任何运行环境支持便能运行的高效率程序设计语言。尽管C语言提供了许多低级处理的功能，但仍然保持着跨平台的特性，以一个标准规格写出的C语言程序可在包括类似嵌入式处理器以及超级计算机等作业平台的许多计算机平台上进行编译。')
                    elif a == 'c++':
                            print('C++（c plus plus）是一种计算机高级程序设计语言，由C语言扩展升级而产生 ，最早于1979年由本贾尼·斯特劳斯特卢普在AT&T贝尔工作室研发。\nC++既可以进行C语言的过程化程序设计，又可以进行以抽象数据类型为特点的基于对象的程序设计，还可以进行以继承和多态为特点的面向对象的程序设计。\nC++擅长面向对象程序设计的同时，还可以进行基于过程的程序设计。\n C++几乎可以创建任何类型的程序：游戏、设备驱动程序、HPC、云、桌面、嵌入式和移动应用等。 甚至用于其他编程语言的库和编译器也使用C++编写。 [25] C++拥有计算机运行的实用性特征，同时还致力于提高大规模程序的编程质量与程序设计语言的问题描述能力。')
                    elif a == 'java':
                            print('Java 是一个通用术语，用于表示 Java 软件及其组件，包括“Java 运行时环境 (JRE)”、“Java 虚拟机 (JVM)”以及“插件”。\nJava具有大部分编程语言所共有的一些特征，被特意设计用于互联网的分布式环境。\nJava具有类似于C++语言的形式和感觉，但它要比C++语言更易于使用，而且在编程时彻底采用了一种以对象为导向的方式。')
                    elif a == 'php':
                            print('PHP（PHP: Hypertext Preprocessor）即“超文本预处理器”，是在服务器端执行的脚本语言，尤其适用于Web开发并可嵌入HTML中。PHP语法学习了C语言，吸纳Java和Perl多个语言的特色发展出自己的特色语法，并根据它们的长项持续改进提升自己，例如java的面向对象编程，该语言当初创建的主要目标是让开发人员快速编写出优质的web网站。PHP同时支持面向对象和面向过程的开发，使用上非常灵活。')
                    elif a != 'q' and a != '你好' and a != "hello":
                        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s%a'
                        te = requests.get(url).json()
                        data = te['data']['info']['text']
                        print(data)

            code = input('>>>|')
            tree = ast.parse(code)
            exec(compile(tree, '<string>', 'exec'))
        except SyntaxError as e:
            print(e)
        except Exception as e:
            print(e)
        except TypeError as e:
            print(e)
        except AttributeError as e:
            print(e)
        except NameError as e:
            print(e)
        except KeyError as e:
            print(e)
        except SystemExit as e:
            print(e)

while True:
    try:
        def copyright():
            print('由朱浩宇开发并维护，包括但不限于使用权，复制、修改、合并、发布、分发、再授权或出售软件的副本')
            input('按Enter键返回:')
        def credits():
            print('pypython由朱浩宇维护')
        def hp():
            print('帮组:\npypython() 获取pypython版本\nai() AI\nhp() 帮组')
        def pypython():
            print('pypython 1.1')
        def ai():
            import requests
            print('按 q 停止,请确保连网')
            print('请输入你想说的：')
            while True:
                a = input('>>>|')
                if a == 'q':
                    pyt()
                elif a == '你好':
                    print('你好')
                elif a == 'hello':
                    print("hello")
                elif a == '你叫什么':
                    print('我叫pyAI')
                elif a == 'hello':
                    print('hello')
                elif a == '今天星期几':
                    print('作为一个人工智能，我无法获取现实世界的时间。')
                elif a == 'hello world':
                    print('你好世界')
                elif a == 'python':
                    print('Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆于1990年代初设计，作为一门叫做ABC语言的替代品。\nPython提供了高效的高级数据结构，还能简单有效地面向对象编程。\nPython语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的编程语言，随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、大型项目的开发。\nPython解释器易于扩展，可以使用C语言或C++（或者其他可以通过C调用的语言）扩展新的功能和数据类型。 \nPython也可用于可定制化软件中的扩展程序语言。Python丰富的标准库，提供了适用于各个主要系统平台的源码或机器码。')
                elif a == 'c':
                    print('C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。\nC语言能以简易的方式编译、处理低级存储器。\nC语言是仅产生少量的机器语言以及不需要任何运行环境支持便能运行的高效率程序设计语言。尽管C语言提供了许多低级处理的功能，但仍然保持着跨平台的特性，以一个标准规格写出的C语言程序可在包括类似嵌入式处理器以及超级计算机等作业平台的许多计算机平台上进行编译。')
                elif a == 'c++':
                    print('C++（c plus plus）是一种计算机高级程序设计语言，由C语言扩展升级而产生 ，最早于1979年由本贾尼·斯特劳斯特卢普在AT&T贝尔工作室研发。\nC++既可以进行C语言的过程化程序设计，又可以进行以抽象数据类型为特点的基于对象的程序设计，还可以进行以继承和多态为特点的面向对象的程序设计。\nC++擅长面向对象程序设计的同时，还可以进行基于过程的程序设计。\n C++几乎可以创建任何类型的程序：游戏、设备驱动程序、HPC、云、桌面、嵌入式和移动应用等。 甚至用于其他编程语言的库和编译器也使用C++编写。 [25] C++拥有计算机运行的实用性特征，同时还致力于提高大规模程序的编程质量与程序设计语言的问题描述能力。')
                elif a == 'java':
                    print('Java 是一个通用术语，用于表示 Java 软件及其组件，包括“Java 运行时环境 (JRE)”、“Java 虚拟机 (JVM)”以及“插件”。\nJava具有大部分编程语言所共有的一些特征，被特意设计用于互联网的分布式环境。\nJava具有类似于C++语言的形式和感觉，但它要比C++语言更易于使用，而且在编程时彻底采用了一种以对象为导向的方式。')
                elif a == 'php':
                    print('PHP（PHP: Hypertext Preprocessor）即“超文本预处理器”，是在服务器端执行的脚本语言，尤其适用于Web开发并可嵌入HTML中。PHP语法学习了C语言，吸纳Java和Perl多个语言的特色发展出自己的特色语法，并根据它们的长项持续改进提升自己，例如java的面向对象编程，该语言当初创建的主要目标是让开发人员快速编写出优质的web网站。PHP同时支持面向对象和面向过程的开发，使用上非常灵活。')

                elif a != 'q' and a != '你好' and a != "hello":
                    url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s%a'
                    te = requests.get(url).json()
                    data = te['data']['info']['text']
                    print(data)

        code = input('>>>|')
        tree = ast.parse(code)
        exec(compile(tree, '<string>', 'exec'))
    except SyntaxError as e:
        print(e)
    except Exception as e:
        print(e)
    except TypeError as e:
        print(e)
    except AttributeError as e:
        print(e)
    except NameError as e:
        print(e)
    except KeyError as e:
        print(e)
    except SystemExit as e:
        print(e)
