import pymakehtml as ph

ph.ct_hx("", "hello!", 5)
ph.ct_a('href="https://www.baidu.com"', "hi")
ph.ct_title("", "hey!")
ph.ct_script('src="./myJs.js"')
ph.build("./ho.html")