from pkg.build.application import app
from pkg.routes.router import init_routers


init_routers()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')