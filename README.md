Lessc(Less Compiler)
====================

# *Less compile for Sublime Text 3* #

## **什么是 Lessc** ##
Lessc(Less Compiler)是一个在Sublime Text3下使用 `less.js` (http://lesscss.org/) 库将 `.less` 文件编译成 `.css` 文件的工具插件。

## **特性** ##
  - 利用windows自带js引擎加载 `less.js`(目前是less-1.7.5版本)库，无需任何其它额外的插件安装(*仅支持 windows*)

  - Lessc的默认设置和设置项可以从 `sublime text3\Preferences\Package Settings\Lessc\Settings` 看到和修改；
  
  - Lessc支持 **自动编译**（即时保存即时编译当前 `.less` 文件，由配置项：`auto_compile:{true|false}` 决定）、 **手动编译** 和 **全部编译**；<br>
    **手动编译** 和 **全部编译** 可以通过配置快捷键（`sublime text3\Preferences\Package Settings\Lessc\Key Bindings - Default`）进行，<br>也可以选择工具命令：`sublime text3\Tools\Lessc > CSS\Compile Current Less file | Compile All Less files` 下触发进行。

  - 可设置是否压缩 CSS：`compress:{true|false}`

  - Lessc还支持 `.sublime-project` 项目私有化配置，这样可以为不同的项目进行不同的 Lessc 的配置。<br>

    `test.sublime-project` 示例配置：
    >{<br>
    >&nbsp;&nbsp;&nbsp;"folders":[<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name":&nbsp;"test",<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"path":&nbsp;"."<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
    >&nbsp;&nbsp;&nbsp;],<br>
    >&nbsp;&nbsp;&nbsp;"settings":<br>
    >&nbsp;&nbsp;&nbsp;{<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"lessc":<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"auto_compile":&nbsp;true,<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"compress":&nbsp;false,<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encoding":&nbsp;"UTF-8",<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"less_dir":&nbsp;"D:\\workspace\\test\\src\\lessc"<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"output_dir":&nbsp;"D:\\workspace\\test\\build\\css",<br>
    >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
    >&nbsp;&nbsp;&nbsp;}<br>
    >}

## 如何使用？
  - 1.将代码下载到 "SublimeText3 安装目录\Data\Packages\lessc" 即可。

  - 2.开始编写你的 `.less` 文件，保存后相信它会自动帮你编译成 `.css` 文件，试试吧 O(∩_∩)O~


## 声明：
**此插件是修改自  https://github.com/fengdi/lessc (原插件只支持SublimeText2),尊重原作者版权！**