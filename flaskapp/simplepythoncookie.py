#!/usr/bin/env python3

from http import cookies

C = cookies.SimpleCookie()
C["byte"] = "academy"
C["byte"]["path"] = "/cookie"

print(C.output(header = "Cookie:"))
