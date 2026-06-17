import reactpy as react

@react.component
def app():
    return react.html.h1("test")

react.run(app)