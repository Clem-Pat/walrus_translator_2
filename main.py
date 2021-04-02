import window

def main():
    app = window.App()
    while True:
        try: app.update()
        except: break

if __name__=='__main__':
    main()
