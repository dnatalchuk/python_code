#!/usr/bin/python3
import subprocess

out = open("data.out", "w");
print("Canadian weather is cool.", file=out);
out.close()
subprocess.run(["cat", "./data.out"]);
subprocess.run(["rm", "./data.out"])