#!/bin/sh
# Copyright (c) 2018, The TurtleCoin Developers
# 
# Please see the included LICENSE file for more information.

rm -rf cpp csharp js objc php python java ruby
mkdir {cpp,csharp,js,objc,php,python,java,ruby}
protoc sources/*.proto --proto_path=sources/ --cpp_out=cpp/ --csharp_out=csharp/ --js_out=js/ --objc_out=objc/ --php_out=php/ --python_out=python/ --java_out=java/ --ruby_out=ruby/
