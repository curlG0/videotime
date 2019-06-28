from flask import Flask, request
from marshmallow import fields
from flask_rebar import RequestSchema, Rebar

from videotime.video_manager import manager

rebar = Rebar()
registry = rebar.create_handler_registry()


class ProcessReturnSchema(RequestSchema):
    message = fields.String(required=True)


class ProcessVideoSchema(RequestSchema):
    url = fields.String(required=True)


@registry.handles(rule="/")
def hello():
    return "VideoTime! www.videotime.me"


@registry.handles(rule="/process",
                  method='POST',
                  request_body_schema=ProcessVideoSchema(),
                  response_body_schema=ProcessReturnSchema())
def process_video():
    body = rebar.validated_body
    manager.process_video(body['url'])
    return {"message": "processing"}


app = Flask(__name__)
rebar.init_app(app)
