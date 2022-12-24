try:
    f=open("demo.py")
    try:
        f.write("ABC")
    except:
        print("Erroe in file")
    finally:
        f.close()
except:
    print("hjgdfiw")