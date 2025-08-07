def filtered_age(ages,min_age=18):
  if not isinstance(ages,(list,tuple,set)):
    raise TypeError("Khong phai list, tuple hay set");
  result=[age for age in ages if age > min_age];
  return result if result else f"khong co tuoi nao lon hon 18"
filtered_age([2,3,45,6,9,100])