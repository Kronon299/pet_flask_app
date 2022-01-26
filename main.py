from app import app, api, Quote

api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True
    )
