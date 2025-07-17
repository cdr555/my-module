#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一个简单的示例模块


"""

class MyModule:
    """示例类"""
    
    def __init__(self, name="默认模块"):
        self.name = name
        
    def greet(self):
        """返回问候语"""
        return f"你好，这里是{self.name}!"
    
    def process(self, data):
        """处理数据的示例方法"""
        if not data:
            return None
        return f"处理结果: {data.upper()}"

def main():
    """主函数"""
    module = MyModule("测试模块")
    print(module.greet())
    print(module.process("示例数据"))

if __name__ == "__main__":
    main() 