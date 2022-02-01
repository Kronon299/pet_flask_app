from datetime import datetime

from flask import Flask
from flask_restful import Api, Resource, reqparse
from werkzeug.exceptions import BadRequest

from image import Image, Session, Base

app = Flask(__name__)

api = Api(app)


class Quote(Resource):
    def __init__(self):
        self.session = Session()
        Base.metadata.create_all()

    def get(self, name):
        image = self.session.query(Image).filter_by(name=name).one_or_none()
        if image is None:
            raise BadRequest(f"Invalid image name #{name}")
        image_metadata = {
            "id": image.id,
            "name": image.name,
            "added": image.added,
        }
        return image_metadata

    def post(self, ):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        params = parser.parse_args()

        image = Image(name=params["name"], added=str(datetime.now()))
        self.session.add(image)
        self.session.commit()

        return f'Image {image.name} added', 201

    def delete(self, ):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        params = parser.parse_args()
        self.session.query(Image).filter_by(name=params["name"]).delete()
        self.session.commit()
        return f'Image {params["name"]} deleted', 201
