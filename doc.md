变量

举个简单的例子

@nice-blue: #5B83AD;
@light-blue: @nice-blue + #111;

#header {
  color: @light-blue;
}

编译为：

#header {
  color: #6c94be;
}
注意，由于变量只能定义一次，其本质就是“常量”。

混合（Mixin）

Mixins are a way of including ("mixing in") a bunch of properties from one rule-set into another rule-set. So say we have the following class:

.bordered {
  border-top: dotted 1px black;
  border-bottom: solid 2px black;
}
And we want to use these properties inside other rule-sets. Well, we just have to drop in the name of the class where we want the properties, like so:

#menu a {
  color: #111;
  .bordered;
}

.post a {
  color: red;
  .bordered;
}
The properties of the .bordered class will now appear in both #menu a and .post a. (Note that you can also use #ids as mixins.)

Learn more

More about mixins
Parametric Mixins
嵌套规则

Less gives you the ability to use nesting instead of, or in combination with cascading. Let's say we have the following CSS:

#header {
  color: black;
}
#header .navigation {
  font-size: 12px;
}
#header .logo {
  width: 300px;
}
In Less, we can also write it this way:

#header {
  color: black;
  .navigation {
    font-size: 12px;
  }
  .logo {
    width: 300px;
  }
}
The resulting code is more concise, and mimics the structure of your HTML.

You can also bundle pseudo-selectors with your mixins using this method. Here's the classic clearfix hack, rewritten as a mixin (& represents the current selector parent):

.clearfix {
  display: block;
  zoom: 1;

  &:after {
    content: " ";
    display: block;
    font-size: 0;
    height: 0;
    clear: both;
    visibility: hidden;
  }
}

--------------------------------------
@import 用法(http://lesscss.org/features/#import-options-less)
  @import 可以用来表示普通的 css 的 @import 行为；
  也可以用来导入一个Less文件 或 将引用的文件内容添加到被输出的less文件中。

@import statements may be treated differently by Less depending on the file extension:

  If the file has a .css extension it will be treated as CSS and the @import statement left as-is (see the inline option below).
  If it has any other extension it will be treated as Less and imported.
  If it does not have an extension, .less will be appended and it will be included as a imported Less file.

eg: @import "a.css"
    @import "a.less"

可选参数用法：
Less offers several extensions to the CSS @import CSS at-rule to provide more flexibility over what you can do with external files.

Syntax: @import (keyword) "filename";

The following import directives have been implemented:

  (reference) : use a Less file but do not output it
  (inline) : include the source file in the output but do not process it
  (less) : treat the file as a Less file, no matter what the file extension
  (css) : treat the file as a CSS file, no matter what the file extension
  (once) : only include the file once (this is default behavior)
  (multiple) : include the file multiple times
  (optional) : continue compiling when file is not found

More than one keyword per @import is allowed, you will have to use commas to separate the keywords:

Example: @import (optional, reference) "foo.less";