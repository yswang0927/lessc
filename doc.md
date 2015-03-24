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