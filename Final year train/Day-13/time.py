#given seconds,print it in hour,min and seconds

n=7262
h=n//3600
y=n%3600
m=y//60
s=y%60
print(h,":hr",m,":min",s,":sec")