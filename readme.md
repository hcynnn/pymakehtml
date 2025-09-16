<h5>pymakehtml可以用python来制作.html文件</h5>

函数虽然不算多，但也够用

`
import pymakehtml as ph
`

**导入pymakehtml模块**
<br>
<br>
**ct(也就是create)开头的函数可创建一个html标签**
<br>
<br>
`
ph.ct_hx("", "hello!", 5)
`
<br>

这行代码的作用是创建一个h标签
<br>

第一个参数是所有ct函数都有的--att，这代表着这个html标签的属性
<br>

第二个参数也是所有ct函数都有的--content，代表着这个标签夹着的内容


第三个参数是ph.ct_hx()函数独有的，比如说填2，就是h2标签，填5就是h5标签，默认h1标签


这段代码会被转化成：
`
<h5 >hello!</h5>
`

**再比如：**

`ph.ct_a('href="https://www.github.com"')`

会被转化成：

`<a href="https://www.baidu.com">hi</a>`

***那么怎么使用js脚本呢？***

`ph.ct_script('src="./myJs.js"')`

此脚本相当于:

`<script src="./myJs.js"></script>`

**别忘了，在最后调用ph.build(路径)才能创建.html文件！**

示例：

`
import pymakehtml as ph
ph.ct_hx("", "hello!", 5)
ph.ct_a('href="https://www.baidu.com"', "hi")
ph.ct_title("", "hey!")
ph.ct_script('src="./myJs.js"')
ph.built("./ho.html")
`
即./example.py

此脚本会被转化成：

./ho.html