from myScripts import create_app


[app,app2,app3, app4]= create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', Debug=True)
    app2.run(host='0.0.0.0', Debug=True)

